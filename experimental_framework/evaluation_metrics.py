"""
Evaluation Metrics for Dependency Parsing

This module provides comprehensive evaluation metrics specifically designed 
for dependency parsing tasks, including analysis by linguistic phenomena.

Features:
- Standard dependency parsing metrics (UAS, LAS)
- Linguistic phenomenon-specific analysis
- Statistical significance testing
- Error categorization and analysis

Author: Jacob Davies
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, field
from collections import defaultdict, Counter
try:
    from scipy import stats
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False


@dataclass
class ParseResult:
    """Represents a single dependency parse result."""
    tokens: List[str]
    predicted_heads: List[int]
    predicted_labels: List[str]
    gold_heads: List[int]
    gold_labels: List[str]
    sentence_id: str = ""
    
    def __post_init__(self):
        """Validate consistency of parse result."""
        lengths = [len(self.tokens), len(self.predicted_heads), 
                   len(self.predicted_labels), len(self.gold_heads), 
                   len(self.gold_labels)]
        
        if not all(length == lengths[0] for length in lengths):
            raise ValueError("All parse components must have same length")


@dataclass
class EvaluationMetrics:
    """Container for evaluation metrics."""
    uas: float = 0.0  # Unlabeled Attachment Score
    las: float = 0.0  # Labeled Attachment Score
    label_accuracy: float = 0.0
    root_accuracy: float = 0.0
    complete_match: float = 0.0
    
    # Detailed breakdown
    total_tokens: int = 0
    correct_heads: int = 0
    correct_labels: int = 0
    correct_both: int = 0
    correct_roots: int = 0
    complete_sentences: int = 0
    total_sentences: int = 0
    
    # Error analysis
    error_breakdown: Dict[str, int] = field(default_factory=dict)
    confusion_matrix: Dict[Tuple[str, str], int] = field(default_factory=dict)


class DependencyEvaluator:
    """
    Comprehensive evaluation framework for dependency parsing.
    
    This class provides methods for calculating standard dependency parsing
    metrics and performing detailed error analysis.
    """
    
    def __init__(self):
        """Initialize the evaluator."""
        self.parse_results: List[ParseResult] = []
        self.metrics_cache: Optional[EvaluationMetrics] = None
        
    def add_parse_result(self, result: ParseResult) -> None:
        """
        Add a parse result for evaluation.
        
        Args:
            result: ParseResult object containing predictions and gold standard
        """
        self.parse_results.append(result)
        self.metrics_cache = None  # Invalidate cache
    
    def add_conllu_results(self, gold_file: str, predicted_file: str) -> None:
        """
        Load parse results from CoNLL-U format files.
        
        Args:
            gold_file: Path to gold standard file
            predicted_file: Path to predicted output file
        """
        gold_sentences = self._parse_conllu_file(gold_file)
        pred_sentences = self._parse_conllu_file(predicted_file)
        
        if len(gold_sentences) != len(pred_sentences):
            raise ValueError("Gold and predicted files have different number of sentences")
        
        for i, (gold, pred) in enumerate(zip(gold_sentences, pred_sentences)):
            if len(gold['tokens']) != len(pred['tokens']):
                raise ValueError(f"Sentence {i}: token count mismatch")
            
            result = ParseResult(
                tokens=gold['tokens'],
                predicted_heads=pred['heads'],
                predicted_labels=pred['labels'],
                gold_heads=gold['heads'],
                gold_labels=gold['labels'],
                sentence_id=f"sent_{i}"
            )
            
            self.add_parse_result(result)
    
    def _parse_conllu_file(self, file_path: str) -> List[Dict]:
        """Parse a CoNLL-U format file."""
        sentences = []
        current_sentence = {'tokens': [], 'heads': [], 'labels': []}
        
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                
                if not line:  # Empty line marks sentence boundary
                    if current_sentence['tokens']:
                        sentences.append(current_sentence)
                        current_sentence = {'tokens': [], 'heads': [], 'labels': []}
                
                elif not line.startswith('#'):  # Skip comments
                    parts = line.split('\t')
                    
                    if len(parts) >= 8 and '-' not in parts[0]:  # Valid token line
                        token = parts[1]
                        head = int(parts[6]) if parts[6] != '_' else 0
                        label = parts[7] if parts[7] != '_' else 'root'
                        
                        current_sentence['tokens'].append(token)
                        current_sentence['heads'].append(head)
                        current_sentence['labels'].append(label)
        
        # Add final sentence if exists
        if current_sentence['tokens']:
            sentences.append(current_sentence)
        
        return sentences
    
    def calculate_metrics(self) -> EvaluationMetrics:
        """
        Calculate comprehensive evaluation metrics.
        
        Returns:
            EvaluationMetrics object with all computed metrics
        """
        if self.metrics_cache is not None:
            return self.metrics_cache
        
        metrics = EvaluationMetrics()
        
        correct_heads = 0
        correct_labels = 0 
        correct_both = 0
        correct_roots = 0
        complete_sentences = 0
        total_tokens = 0
        
        error_breakdown = Counter()
        confusion_matrix = Counter()
        
        for result in self.parse_results:
            sentence_correct = True
            
            for i, (token, pred_head, pred_label, gold_head, gold_label) in enumerate(
                zip(result.tokens, result.predicted_heads, result.predicted_labels,
                    result.gold_heads, result.gold_labels)
            ):
                total_tokens += 1
                
                # Check head correctness
                head_correct = pred_head == gold_head
                if head_correct:
                    correct_heads += 1
                
                # Check label correctness
                label_correct = pred_label == gold_label
                if label_correct:
                    correct_labels += 1
                
                # Check both head and label
                if head_correct and label_correct:
                    correct_both += 1
                else:
                    sentence_correct = False
                
                # Check root accuracy
                if gold_head == 0:  # Root token
                    if pred_head == 0:
                        correct_roots += 1
                
                # Error analysis
                if not head_correct:
                    error_type = self._categorize_head_error(
                        i + 1, pred_head, gold_head, len(result.tokens)
                    )
                    error_breakdown[error_type] += 1
                
                # Confusion matrix for labels
                confusion_matrix[(gold_label, pred_label)] += 1
            
            if sentence_correct:
                complete_sentences += 1
        
        # Calculate percentages
        metrics.total_tokens = total_tokens
        metrics.correct_heads = correct_heads
        metrics.correct_labels = correct_labels
        metrics.correct_both = correct_both
        metrics.correct_roots = correct_roots
        metrics.complete_sentences = complete_sentences
        metrics.total_sentences = len(self.parse_results)
        
        metrics.uas = (correct_heads / total_tokens * 100) if total_tokens > 0 else 0
        metrics.las = (correct_both / total_tokens * 100) if total_tokens > 0 else 0
        metrics.label_accuracy = (correct_labels / total_tokens * 100) if total_tokens > 0 else 0
        metrics.root_accuracy = (correct_roots / self._count_roots() * 100) if self._count_roots() > 0 else 0
        metrics.complete_match = (complete_sentences / len(self.parse_results) * 100) if self.parse_results else 0
        
        metrics.error_breakdown = dict(error_breakdown)
        metrics.confusion_matrix = dict(confusion_matrix)
        
        self.metrics_cache = metrics
        return metrics
    
    def _categorize_head_error(self, token_pos: int, pred_head: int, 
                              gold_head: int, sentence_length: int) -> str:
        """Categorize the type of head attachment error."""
        
        if gold_head == 0:
            return "root_error"
        elif pred_head == 0:
            return "false_root"
        elif abs(pred_head - token_pos) < abs(gold_head - token_pos):
            return "attachment_too_close"
        elif abs(pred_head - token_pos) > abs(gold_head - token_pos):
            return "attachment_too_far"
        elif pred_head < token_pos and gold_head > token_pos:
            return "direction_left_to_right"
        elif pred_head > token_pos and gold_head < token_pos:
            return "direction_right_to_left"
        else:
            return "other_error"
    
    def _count_roots(self) -> int:
        """Count total number of root tokens across all sentences."""
        count = 0
        for result in self.parse_results:
            count += sum(1 for head in result.gold_heads if head == 0)
        return count
    
    def analyze_by_pos_tags(self, pos_file: str) -> Dict[str, EvaluationMetrics]:
        """
        Analyze performance by part-of-speech tags.
        
        Args:
            pos_file: Path to file with POS tags in CoNLL-U format
            
        Returns:
            Dictionary mapping POS tags to their metrics
        """
        pos_data = self._parse_pos_file(pos_file)
        pos_metrics = defaultdict(lambda: {'correct': 0, 'total': 0})
        
        for i, result in enumerate(self.parse_results):
            if i >= len(pos_data):
                break
                
            pos_tags = pos_data[i]
            
            for j, (pred_head, gold_head, pos_tag) in enumerate(
                zip(result.predicted_heads, result.gold_heads, pos_tags)
            ):
                pos_metrics[pos_tag]['total'] += 1
                if pred_head == gold_head:
                    pos_metrics[pos_tag]['correct'] += 1
        
        # Convert to EvaluationMetrics objects
        result_metrics = {}
        for pos_tag, data in pos_metrics.items():
            metrics = EvaluationMetrics()
            metrics.total_tokens = data['total']
            metrics.correct_heads = data['correct']
            metrics.uas = (data['correct'] / data['total'] * 100) if data['total'] > 0 else 0
            result_metrics[pos_tag] = metrics
        
        return result_metrics
    
    def _parse_pos_file(self, pos_file: str) -> List[List[str]]:
        """Parse POS tags from CoNLL-U file."""
        sentences = []
        current_sentence = []
        
        with open(pos_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                
                if not line:
                    if current_sentence:
                        sentences.append(current_sentence)
                        current_sentence = []
                
                elif not line.startswith('#'):
                    parts = line.split('\t')
                    if len(parts) >= 4 and '-' not in parts[0]:
                        pos_tag = parts[3]  # POS tag is in column 4
                        current_sentence.append(pos_tag)
        
        if current_sentence:
            sentences.append(current_sentence)
        
        return sentences
    
    def analyze_by_dependency_length(self) -> Dict[str, EvaluationMetrics]:
        """
        Analyze performance by dependency arc length.
        
        Returns:
            Dictionary mapping length categories to metrics
        """
        length_categories = {
            'short': (1, 2),
            'medium': (3, 5),
            'long': (6, 10),
            'very_long': (11, float('inf'))
        }
        
        length_metrics = defaultdict(lambda: {'correct': 0, 'total': 0})
        
        for result in self.parse_results:
            for i, (pred_head, gold_head) in enumerate(
                zip(result.predicted_heads, result.gold_heads)
            ):
                if gold_head == 0:  # Skip root
                    continue
                
                arc_length = abs(gold_head - (i + 1))
                
                for category, (min_len, max_len) in length_categories.items():
                    if min_len <= arc_length <= max_len:
                        length_metrics[category]['total'] += 1
                        if pred_head == gold_head:
                            length_metrics[category]['correct'] += 1
                        break
        
        # Convert to EvaluationMetrics
        result_metrics = {}
        for category, data in length_metrics.items():
            metrics = EvaluationMetrics()
            metrics.total_tokens = data['total']
            metrics.correct_heads = data['correct']
            metrics.uas = (data['correct'] / data['total'] * 100) if data['total'] > 0 else 0
            result_metrics[category] = metrics
        
        return result_metrics
    
    def statistical_significance_test(self, other_evaluator: 'DependencyEvaluator', 
                                    metric: str = 'uas') -> Dict[str, float]:
        """
        Perform statistical significance test between two evaluators.
        
        Args:
            other_evaluator: Another DependencyEvaluator to compare against
            metric: Metric to compare ('uas', 'las', 'label_accuracy')
            
        Returns:
            Dictionary with test statistics
        """
        if not SCIPY_AVAILABLE:
            raise ImportError("scipy is required for statistical significance testing")
        
        self_scores = self._get_sentence_scores(metric)
        other_scores = other_evaluator._get_sentence_scores(metric)
        
        if len(self_scores) != len(other_scores):
            raise ValueError("Evaluators must have same number of sentences")
        
        # Paired t-test
        t_stat, p_value = stats.ttest_rel(self_scores, other_scores)
        
        # Effect size (Cohen's d)
        diff = np.array(self_scores) - np.array(other_scores)
        cohen_d = np.mean(diff) / np.std(diff)
        
        return {
            't_statistic': t_stat,
            'p_value': p_value,
            'cohen_d': cohen_d,
            'mean_difference': np.mean(diff),
            'significant': p_value < 0.05
        }
    
    def _get_sentence_scores(self, metric: str) -> List[float]:
        """Get per-sentence scores for a specific metric."""
        scores = []
        
        for result in self.parse_results:
            if metric == 'uas':
                correct = sum(1 for pred, gold in zip(result.predicted_heads, result.gold_heads) 
                             if pred == gold)
                score = correct / len(result.tokens) * 100
            
            elif metric == 'las':
                correct = sum(1 for pred_h, pred_l, gold_h, gold_l in 
                             zip(result.predicted_heads, result.predicted_labels,
                                 result.gold_heads, result.gold_labels)
                             if pred_h == gold_h and pred_l == gold_l)
                score = correct / len(result.tokens) * 100
            
            elif metric == 'label_accuracy':
                correct = sum(1 for pred, gold in zip(result.predicted_labels, result.gold_labels)
                             if pred == gold)
                score = correct / len(result.tokens) * 100
            
            else:
                raise ValueError(f"Unknown metric: {metric}")
            
            scores.append(score)
        
        return scores
    
    def generate_detailed_report(self) -> str:
        """
        Generate a comprehensive evaluation report.
        
        Returns:
            Formatted string report
        """
        metrics = self.calculate_metrics()
        
        report = []
        report.append("=" * 60)
        report.append("DEPENDENCY PARSING EVALUATION REPORT")
        report.append("=" * 60)
        report.append("")
        
        # Overall metrics
        report.append("OVERALL PERFORMANCE:")
        report.append(f"  Unlabeled Attachment Score (UAS): {metrics.uas:.2f}%")
        report.append(f"  Labeled Attachment Score (LAS):   {metrics.las:.2f}%")
        report.append(f"  Label Accuracy:                   {metrics.label_accuracy:.2f}%")
        report.append(f"  Root Accuracy:                    {metrics.root_accuracy:.2f}%")
        report.append(f"  Complete Match:                   {metrics.complete_match:.2f}%")
        report.append("")
        
        # Count statistics
        report.append("COUNT STATISTICS:")
        report.append(f"  Total Tokens:      {metrics.total_tokens}")
        report.append(f"  Total Sentences:   {metrics.total_sentences}")
        report.append(f"  Correct Heads:     {metrics.correct_heads}")
        report.append(f"  Correct Labels:    {metrics.correct_labels}")
        report.append(f"  Correct Both:      {metrics.correct_both}")
        report.append("")
        
        # Error breakdown
        report.append("ERROR ANALYSIS:")
        if metrics.error_breakdown:
            for error_type, count in sorted(metrics.error_breakdown.items(), 
                                          key=lambda x: x[1], reverse=True):
                percentage = count / (metrics.total_tokens - metrics.correct_heads) * 100
                report.append(f"  {error_type:<25}: {count:>5} ({percentage:>5.1f}%)")
        else:
            report.append("  No errors found")
        
        return "\n".join(report)


def compare_parsers(evaluator1: DependencyEvaluator, evaluator2: DependencyEvaluator,
                   names: Tuple[str, str] = ("Parser 1", "Parser 2")) -> pd.DataFrame:
    """
    Compare two parsers side by side.
    
    Args:
        evaluator1: First parser evaluator
        evaluator2: Second parser evaluator
        names: Names for the parsers
        
    Returns:
        Comparison DataFrame
    """
    metrics1 = evaluator1.calculate_metrics()
    metrics2 = evaluator2.calculate_metrics()
    
    comparison = pd.DataFrame({
        'Metric': ['UAS', 'LAS', 'Label Accuracy', 'Root Accuracy', 'Complete Match'],
        names[0]: [metrics1.uas, metrics1.las, metrics1.label_accuracy, 
                   metrics1.root_accuracy, metrics1.complete_match],
        names[1]: [metrics2.uas, metrics2.las, metrics2.label_accuracy,
                   metrics2.root_accuracy, metrics2.complete_match]
    })
    
    # Add difference column
    comparison['Difference'] = comparison[names[1]] - comparison[names[0]]
    
    return comparison


if __name__ == "__main__":
    # Example usage
    evaluator = DependencyEvaluator()
    
    # Add sample results (would normally load from files)
    sample_result = ParseResult(
        tokens=["The", "cat", "sat", "on", "the", "mat"],
        predicted_heads=[2, 3, 0, 3, 6, 4],
        predicted_labels=["det", "nsubj", "root", "case", "det", "nmod"],
        gold_heads=[2, 3, 0, 3, 6, 4],
        gold_labels=["det", "nsubj", "root", "case", "det", "nmod"]
    )
    
    evaluator.add_parse_result(sample_result)
    metrics = evaluator.calculate_metrics()
    
    print(evaluator.generate_detailed_report())
