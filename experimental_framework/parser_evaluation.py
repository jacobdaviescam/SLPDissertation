"""
Parser Evaluation Framework

This module provides a comprehensive framework for evaluating different 
neural dependency parsers across multiple metrics and linguistic phenomena.

Features:
- Multi-parser evaluation (BERT, Graph-based, Transition-based)
- Automated test set generation
- Comprehensive metric calculation (UAS, LAS, Accuracy)
- Comparative analysis across architectures

Author: Jacob Davies
"""

import os
import subprocess
import pandas as pd
from typing import Dict, List, Any, Optional
from pathlib import Path
import json
from dataclasses import dataclass


@dataclass
class EvaluationResult:
    """Data class for storing evaluation results."""
    parser_name: str
    test_set: str
    uas_score: float
    las_score: float
    accuracy: float
    sentence_count: int
    evaluation_time: float
    

@dataclass
class ParserConfig:
    """Configuration for a specific parser."""
    name: str
    model_path: str
    parser_type: str  # 'graph', 'transition', 'bert'
    embedding_type: Optional[str] = None
    additional_params: Optional[Dict[str, Any]] = None


class ParserEvaluationFramework:
    """
    Main framework for systematic parser evaluation.
    
    This class coordinates the evaluation of multiple parser architectures
    across different test sets and linguistic phenomena.
    """
    
    def __init__(self, base_output_dir: str = "model_outputs"):
        """
        Initialize the evaluation framework.
        
        Args:
            base_output_dir: Base directory for storing evaluation outputs
        """
        self.base_output_dir = Path(base_output_dir)
        self.base_output_dir.mkdir(exist_ok=True)
        
        self.parsers: Dict[str, ParserConfig] = {}
        self.test_sets: Dict[str, str] = {}
        self.evaluation_results: List[EvaluationResult] = []
        
        self.evaluation_script = self._locate_evaluation_script()
        
    def _locate_evaluation_script(self) -> str:
        """Locate the CoNLL evaluation script."""
        possible_paths = [
            "MaltEval/dist-20141005/lib/MaltEval.jar",
            "uuparser/uuparser/utils/evaluation_script/conll17_ud_eval.py",
            "/usr/local/bin/eval.pl"
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                return path
        
        raise FileNotFoundError("Could not locate evaluation script")
    
    def register_parser(self, config: ParserConfig) -> None:
        """
        Register a parser for evaluation.
        
        Args:
            config: Parser configuration object
        """
        self.parsers[config.name] = config
        
        # Create output directory for this parser
        parser_dir = self.base_output_dir / config.parser_type / config.name
        parser_dir.mkdir(parents=True, exist_ok=True)
    
    def register_test_set(self, name: str, file_path: str) -> None:
        """
        Register a test set for evaluation.
        
        Args:
            name: Name identifier for the test set
            file_path: Path to the test file
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Test set file not found: {file_path}")
        
        self.test_sets[name] = file_path
    
    def run_parser(self, parser_name: str, input_file: str, output_file: str) -> bool:
        """
        Run a specific parser on an input file.
        
        Args:
            parser_name: Name of the registered parser
            input_file: Path to input file
            output_file: Path to save output
            
        Returns:
            Success status
        """
        if parser_name not in self.parsers:
            raise ValueError(f"Parser {parser_name} not registered")
        
        parser_config = self.parsers[parser_name]
        
        try:
            if parser_config.parser_type == 'graph':
                return self._run_graph_parser(parser_config, input_file, output_file)
            elif parser_config.parser_type == 'transition':
                return self._run_transition_parser(parser_config, input_file, output_file)
            elif parser_config.parser_type == 'bert':
                return self._run_bert_parser(parser_config, input_file, output_file)
            else:
                raise ValueError(f"Unknown parser type: {parser_config.parser_type}")
        
        except Exception as e:
            print(f"Error running parser {parser_name}: {e}")
            return False
    
    def _run_graph_parser(self, config: ParserConfig, input_file: str, output_file: str) -> bool:
        """Run graph-based parser."""
        cmd = [
            'python', 'uuparser/uuparser/parser.py',
            '--predict',
            '--model', config.model_path,
            '--test', input_file,
            '--output', output_file,
            '--graph_based'
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.returncode == 0
    
    def _run_transition_parser(self, config: ParserConfig, input_file: str, output_file: str) -> bool:
        """Run transition-based parser."""
        cmd = [
            'python', 'uuparser/uuparser/parser.py',
            '--predict',
            '--model', config.model_path,
            '--test', input_file,
            '--output', output_file
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.returncode == 0
    
    def _run_bert_parser(self, config: ParserConfig, input_file: str, output_file: str) -> bool:
        """Run BERT-enhanced parser."""
        cmd = [
            'python', 'uuparser/uuparser/parser.py',
            '--predict',
            '--model', config.model_path,
            '--test', input_file,
            '--output', output_file,
            '--embedding_type', config.embedding_type or 'bert'
        ]
        
        if config.additional_params:
            for param, value in config.additional_params.items():
                cmd.extend([f'--{param}', str(value)])
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.returncode == 0
    
    def evaluate_output(self, gold_file: str, predicted_file: str) -> Dict[str, float]:
        """
        Evaluate parser output against gold standard.
        
        Args:
            gold_file: Path to gold standard file
            predicted_file: Path to predicted output file
            
        Returns:
            Dictionary of evaluation metrics
        """
        cmd = [
            'python', self.evaluation_script,
            gold_file, predicted_file
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode != 0:
            raise RuntimeError(f"Evaluation failed: {result.stderr}")
        
        return self._parse_evaluation_output(result.stdout)
    
    def _parse_evaluation_output(self, eval_output: str) -> Dict[str, float]:
        """Parse evaluation script output to extract metrics."""
        metrics = {}
        
        lines = eval_output.strip().split('\n')
        for line in lines:
            if 'UAS' in line:
                # Extract UAS score
                parts = line.split()
                for i, part in enumerate(parts):
                    if part == 'UAS' and i + 1 < len(parts):
                        try:
                            metrics['uas'] = float(parts[i + 1])
                        except ValueError:
                            pass
            
            elif 'LAS' in line:
                # Extract LAS score
                parts = line.split()
                for i, part in enumerate(parts):
                    if part == 'LAS' and i + 1 < len(parts):
                        try:
                            metrics['las'] = float(parts[i + 1])
                        except ValueError:
                            pass
        
        return metrics
    
    def run_comprehensive_evaluation(self) -> List[EvaluationResult]:
        """
        Run comprehensive evaluation across all registered parsers and test sets.
        
        Returns:
            List of evaluation results
        """
        results = []
        
        for parser_name, parser_config in self.parsers.items():
            for test_name, test_path in self.test_sets.items():
                
                # Generate output file path
                output_dir = self.base_output_dir / parser_config.parser_type / parser_name
                output_file = output_dir / f"{test_name}_output.conllu"
                
                # Run parser
                success = self.run_parser(parser_name, test_path, str(output_file))
                
                if success:
                    # Evaluate results
                    metrics = self.evaluate_output(test_path, str(output_file))
                    
                    result = EvaluationResult(
                        parser_name=parser_name,
                        test_set=test_name,
                        uas_score=metrics.get('uas', 0.0),
                        las_score=metrics.get('las', 0.0),
                        accuracy=metrics.get('accuracy', 0.0),
                        sentence_count=self._count_sentences(test_path),
                        evaluation_time=0.0  # Could be measured if needed
                    )
                    
                    results.append(result)
                    self.evaluation_results.append(result)
        
        return results
    
    def _count_sentences(self, file_path: str) -> int:
        """Count sentences in a CoNLL-U file."""
        count = 0
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip() == '':
                    count += 1
        return count
    
    def generate_comparative_report(self) -> pd.DataFrame:
        """
        Generate a comparative report of all evaluation results.
        
        Returns:
            Pandas DataFrame with comparative results
        """
        data = []
        for result in self.evaluation_results:
            data.append({
                'Parser': result.parser_name,
                'Test Set': result.test_set,
                'UAS': result.uas_score,
                'LAS': result.las_score,
                'Accuracy': result.accuracy,
                'Sentences': result.sentence_count
            })
        
        df = pd.DataFrame(data)
        
        # Add parser type information
        df['Parser Type'] = df['Parser'].map(
            lambda x: self.parsers[x].parser_type if x in self.parsers else 'unknown'
        )
        
        return df
    
    def save_results(self, output_file: str) -> None:
        """
        Save evaluation results to file.
        
        Args:
            output_file: Path to save results
        """
        df = self.generate_comparative_report()
        df.to_csv(output_file, index=False)
        
        # Also save as JSON for programmatic access
        json_file = output_file.replace('.csv', '.json')
        results_dict = [
            {
                'parser_name': r.parser_name,
                'test_set': r.test_set,
                'uas_score': r.uas_score,
                'las_score': r.las_score,
                'accuracy': r.accuracy,
                'sentence_count': r.sentence_count
            }
            for r in self.evaluation_results
        ]
        
        with open(json_file, 'w') as f:
            json.dump(results_dict, f, indent=2)


def setup_standard_evaluation():
    """Set up a standard evaluation configuration."""
    
    framework = ParserEvaluationFramework()
    
    # Register parsers
    parsers = [
        ParserConfig(
            name="graph_baseline",
            model_path="output/parser/graph_model.pkl",
            parser_type="graph"
        ),
        ParserConfig(
            name="transition_baseline", 
            model_path="output/parser/transition_model.pkl",
            parser_type="transition"
        ),
        ParserConfig(
            name="bert_graph",
            model_path="output/parser/bert_graph_model.pkl",
            parser_type="bert",
            embedding_type="bert"
        ),
        ParserConfig(
            name="bert_transition",
            model_path="output/parser/bert_transition_model.pkl", 
            parser_type="bert",
            embedding_type="bert"
        )
    ]
    
    for parser in parsers:
        framework.register_parser(parser)
    
    # Register test sets
    test_sets = {
        "CP_3": "UD_SLOG/generalisation_sets/stripped/CP_3_stripped.conllu",
        "CP_5-12": "UD_SLOG/generalisation_sets/stripped/CP_5-12_stripped.conllu",
        "PP_3": "UD_SLOG/generalisation_sets/stripped/PP_3_stripped.conllu",
        "PP_5-12": "UD_SLOG/generalisation_sets/stripped/PP_5-12_stripped.conllu",
        "center_embed_3": "UD_SLOG/generalisation_sets/stripped/center_embed_3_stripped.conllu",
        "center_embed_5-12": "UD_SLOG/generalisation_sets/stripped/center_embed_5-12_stripped.conllu"
    }
    
    for name, path in test_sets.items():
        if os.path.exists(path):
            framework.register_test_set(name, path)
    
    return framework


if __name__ == "__main__":
    # Example usage
    framework = setup_standard_evaluation()
    results = framework.run_comprehensive_evaluation()
    framework.save_results("evaluation_results.csv")
    print(f"Completed evaluation with {len(results)} results")
