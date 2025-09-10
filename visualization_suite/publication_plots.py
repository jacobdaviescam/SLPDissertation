"""
Publication-Ready Visualization Suite for Dependency Parsing Results

This module provides professional data visualization capabilities for 
dependency parsing research, creating publication-quality plots and figures.

Features:
- Performance comparison charts
- Error analysis visualizations  
- Linguistic phenomenon analysis plots
- Statistical significance visualization
- Publication-ready styling

Author: Jacob Davies
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional
from pathlib import Path
import warnings

# Set publication-ready style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")
warnings.filterwarnings('ignore')

# Publication settings
PUBLICATION_FIGSIZE = (10, 6)
PUBLICATION_DPI = 300
FONT_SIZE = 12
TITLE_SIZE = 14
LEGEND_SIZE = 10


class PublicationPlotter:
    """
    Main plotting class for creating publication-ready visualizations.
    
    This class provides methods for creating various types of plots commonly
    used in dependency parsing research papers.
    """
    
    def __init__(self, output_dir: str = "visualization_suite/figures"):
        """
        Initialize the plotter.
        
        Args:
            output_dir: Directory to save generated figures
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Set matplotlib parameters for publication quality
        plt.rcParams['font.size'] = FONT_SIZE
        plt.rcParams['axes.titlesize'] = TITLE_SIZE
        plt.rcParams['axes.labelsize'] = FONT_SIZE
        plt.rcParams['xtick.labelsize'] = FONT_SIZE - 1
        plt.rcParams['ytick.labelsize'] = FONT_SIZE - 1
        plt.rcParams['legend.fontsize'] = LEGEND_SIZE
        plt.rcParams['figure.dpi'] = PUBLICATION_DPI
        plt.rcParams['savefig.dpi'] = PUBLICATION_DPI
        plt.rcParams['figure.figsize'] = PUBLICATION_FIGSIZE
    
    def plot_parser_comparison(self, results_df: pd.DataFrame, 
                              metric: str = 'UAS',
                              title: Optional[str] = None,
                              filename: str = "parser_comparison.pdf") -> None:
        """
        Create a bar chart comparing different parsers.
        
        Args:
            results_df: DataFrame with parser results
            metric: Metric to plot ('UAS', 'LAS', etc.)
            title: Custom title for the plot
            filename: Output filename
        """
        fig, ax = plt.subplots(figsize=PUBLICATION_FIGSIZE)
        
        # Group by parser and calculate mean scores
        parser_scores = results_df.groupby('Parser')[metric].mean().sort_values(ascending=False)
        
        # Create bar plot
        bars = ax.bar(range(len(parser_scores)), parser_scores.values, 
                     color=sns.color_palette("husl", len(parser_scores)))
        
        # Customize the plot
        ax.set_xlabel('Parser Architecture')
        ax.set_ylabel(f'{metric} Score (%)')
        ax.set_title(title or f'{metric} Performance Comparison')
        ax.set_xticks(range(len(parser_scores)))
        ax.set_xticklabels(parser_scores.index, rotation=45, ha='right')
        
        # Add value labels on bars
        for i, (bar, value) in enumerate(zip(bars, parser_scores.values)):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                   f'{value:.1f}%', ha='center', va='bottom', fontweight='bold')
        
        # Set y-axis limits for better visibility
        ax.set_ylim(0, max(parser_scores.values) * 1.1)
        
        # Add grid for better readability
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(self.output_dir / filename, bbox_inches='tight', dpi=PUBLICATION_DPI)
        plt.close()
    
    def plot_performance_by_test_set(self, results_df: pd.DataFrame,
                                   metric: str = 'UAS',
                                   title: Optional[str] = None,
                                   filename: str = "performance_by_test_set.pdf") -> None:
        """
        Create a grouped bar chart showing performance across test sets.
        
        Args:
            results_df: DataFrame with results
            metric: Metric to plot
            title: Custom title
            filename: Output filename
        """
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Pivot the data for grouped bar chart
        pivot_df = results_df.pivot(index='Test Set', columns='Parser', values=metric)
        
        # Create grouped bar chart
        pivot_df.plot(kind='bar', ax=ax, width=0.8)
        
        ax.set_xlabel('Test Set')
        ax.set_ylabel(f'{metric} Score (%)')
        ax.set_title(title or f'{metric} Performance by Test Set')
        ax.legend(title='Parser', bbox_to_anchor=(1.05, 1), loc='upper left')
        ax.grid(True, alpha=0.3)
        
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(self.output_dir / filename, bbox_inches='tight', dpi=PUBLICATION_DPI)
        plt.close()
    
    def plot_error_analysis_heatmap(self, confusion_data: Dict[Tuple[str, str], int],
                                  title: str = "Label Confusion Matrix",
                                  filename: str = "confusion_matrix.pdf") -> None:
        """
        Create a heatmap showing label confusion matrix.
        
        Args:
            confusion_data: Dictionary mapping (gold, predicted) to counts
            title: Plot title
            filename: Output filename
        """
        # Convert confusion data to matrix format
        all_labels = sorted(set([label for gold, pred in confusion_data.keys() 
                               for label in [gold, pred]]))
        
        matrix = np.zeros((len(all_labels), len(all_labels)))
        
        for (gold, pred), count in confusion_data.items():
            if gold in all_labels and pred in all_labels:
                gold_idx = all_labels.index(gold)
                pred_idx = all_labels.index(pred)
                matrix[gold_idx][pred_idx] = count
        
        # Create heatmap
        fig, ax = plt.subplots(figsize=(10, 8))
        
        sns.heatmap(matrix, 
                   xticklabels=all_labels,
                   yticklabels=all_labels,
                   annot=True, 
                   fmt='g',
                   cmap='Blues',
                   ax=ax)
        
        ax.set_xlabel('Predicted Label')
        ax.set_ylabel('Gold Label')
        ax.set_title(title)
        
        plt.xticks(rotation=45, ha='right')
        plt.yticks(rotation=0)
        plt.tight_layout()
        plt.savefig(self.output_dir / filename, bbox_inches='tight', dpi=PUBLICATION_DPI)
        plt.close()
    
    def plot_sentence_length_analysis(self, results_by_length: Dict[str, List[float]],
                                     title: str = "Performance by Sentence Length",
                                     filename: str = "sentence_length_analysis.pdf") -> None:
        """
        Plot performance analysis by sentence length.
        
        Args:
            results_by_length: Dictionary mapping length categories to scores
            title: Plot title
            filename: Output filename
        """
        fig, ax = plt.subplots(figsize=PUBLICATION_FIGSIZE)
        
        # Prepare data
        categories = list(results_by_length.keys())
        box_data = [results_by_length[cat] for cat in categories]
        
        # Create box plot
        bp = ax.boxplot(box_data, labels=categories, patch_artist=True)
        
        # Color the boxes
        colors = sns.color_palette("husl", len(categories))
        for patch, color in zip(bp['boxes'], colors):
            patch.set_facecolor(color)
            patch.set_alpha(0.7)
        
        ax.set_xlabel('Sentence Length Category')
        ax.set_ylabel('Accuracy (%)')
        ax.set_title(title)
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(self.output_dir / filename, bbox_inches='tight', dpi=PUBLICATION_DPI)
        plt.close()
    
    def plot_dependency_length_analysis(self, length_results: Dict[str, float],
                                      title: str = "Performance by Dependency Arc Length",
                                      filename: str = "dependency_length_analysis.pdf") -> None:
        """
        Plot performance by dependency arc length.
        
        Args:
            length_results: Dictionary mapping length categories to accuracy
            title: Plot title
            filename: Output filename
        """
        fig, ax = plt.subplots(figsize=PUBLICATION_FIGSIZE)
        
        categories = list(length_results.keys())
        accuracies = list(length_results.values())
        
        # Create line plot with markers
        ax.plot(categories, accuracies, marker='o', linewidth=2, markersize=8)
        
        # Add value labels
        for i, (cat, acc) in enumerate(zip(categories, accuracies)):
            ax.annotate(f'{acc:.1f}%', (i, acc), textcoords="offset points",
                       xytext=(0,10), ha='center', fontweight='bold')
        
        ax.set_xlabel('Dependency Arc Length Category')
        ax.set_ylabel('UAS (%)')
        ax.set_title(title)
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(self.output_dir / filename, bbox_inches='tight', dpi=PUBLICATION_DPI)
        plt.close()
    
    def plot_pos_tag_analysis(self, pos_results: Dict[str, float],
                            title: str = "Performance by Part-of-Speech Tag",
                            filename: str = "pos_tag_analysis.pdf") -> None:
        """
        Plot performance breakdown by POS tags.
        
        Args:
            pos_results: Dictionary mapping POS tags to accuracy
            title: Plot title
            filename: Output filename
        """
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Sort by accuracy for better visualization
        sorted_results = sorted(pos_results.items(), key=lambda x: x[1], reverse=True)
        pos_tags, accuracies = zip(*sorted_results)
        
        # Create horizontal bar chart
        bars = ax.barh(range(len(pos_tags)), accuracies, 
                      color=sns.color_palette("viridis", len(pos_tags)))
        
        ax.set_yticks(range(len(pos_tags)))
        ax.set_yticklabels(pos_tags)
        ax.set_xlabel('UAS (%)')
        ax.set_title(title)
        
        # Add value labels
        for i, (bar, acc) in enumerate(zip(bars, accuracies)):
            ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
                   f'{acc:.1f}%', va='center', fontweight='bold')
        
        ax.grid(True, alpha=0.3, axis='x')
        
        plt.tight_layout()
        plt.savefig(self.output_dir / filename, bbox_inches='tight', dpi=PUBLICATION_DPI)
        plt.close()
    
    def plot_learning_curves(self, training_data: Dict[str, List[float]],
                           title: str = "Training Learning Curves",
                           filename: str = "learning_curves.pdf") -> None:
        """
        Plot training learning curves for different parsers.
        
        Args:
            training_data: Dictionary mapping parser names to accuracy lists
            title: Plot title
            filename: Output filename
        """
        fig, ax = plt.subplots(figsize=PUBLICATION_FIGSIZE)
        
        for parser_name, accuracies in training_data.items():
            epochs = range(1, len(accuracies) + 1)
            ax.plot(epochs, accuracies, marker='o', label=parser_name, linewidth=2)
        
        ax.set_xlabel('Training Epoch')
        ax.set_ylabel('Validation Accuracy (%)')
        ax.set_title(title)
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(self.output_dir / filename, bbox_inches='tight', dpi=PUBLICATION_DPI)
        plt.close()
    
    def plot_error_distribution(self, error_data: Dict[str, int],
                              title: str = "Error Type Distribution",
                              filename: str = "error_distribution.pdf") -> None:
        """
        Create a pie chart showing distribution of error types.
        
        Args:
            error_data: Dictionary mapping error types to counts
            title: Plot title
            filename: Output filename
        """
        fig, ax = plt.subplots(figsize=(8, 8))
        
        # Sort by count for better visualization
        sorted_errors = sorted(error_data.items(), key=lambda x: x[1], reverse=True)
        error_types, counts = zip(*sorted_errors)
        
        # Create pie chart
        colors = sns.color_palette("Set3", len(error_types))
        wedges, texts, autotexts = ax.pie(counts, labels=error_types, autopct='%1.1f%%',
                                         colors=colors, startangle=90)
        
        # Improve text readability
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
        
        ax.set_title(title)
        
        plt.tight_layout()
        plt.savefig(self.output_dir / filename, bbox_inches='tight', dpi=PUBLICATION_DPI)
        plt.close()
    
    def create_comprehensive_report(self, results_df: pd.DataFrame,
                                  confusion_data: Optional[Dict] = None,
                                  error_data: Optional[Dict] = None) -> None:
        """
        Create a comprehensive visualization report.
        
        Args:
            results_df: Main results DataFrame
            confusion_data: Label confusion matrix data
            error_data: Error breakdown data
        """
        print("Generating comprehensive visualization report...")
        
        # Main performance comparison
        self.plot_parser_comparison(results_df, 'UAS', 
                                  "Unlabeled Attachment Score Comparison",
                                  "uas_comparison.pdf")
        
        self.plot_parser_comparison(results_df, 'LAS',
                                  "Labeled Attachment Score Comparison", 
                                  "las_comparison.pdf")
        
        # Performance by test set
        self.plot_performance_by_test_set(results_df, 'UAS',
                                        "UAS Performance by Test Set",
                                        "uas_by_test_set.pdf")
        
        # Additional plots if data is available
        if confusion_data:
            self.plot_error_analysis_heatmap(confusion_data)
        
        if error_data:
            self.plot_error_distribution(error_data)
        
        print(f"Report generated in {self.output_dir}")


def load_results_from_csv(csv_file: str) -> pd.DataFrame:
    """
    Load results from CSV file for plotting.
    
    Args:
        csv_file: Path to CSV file with results
        
    Returns:
        DataFrame with results
    """
    return pd.read_csv(csv_file)


def generate_sample_plots():
    """Generate sample plots with synthetic data for demonstration."""
    
    plotter = PublicationPlotter()
    
    # Sample data
    sample_results = pd.DataFrame({
        'Parser': ['Graph-BERT', 'Transition-BERT', 'Graph-Baseline', 'Transition-Baseline'] * 3,
        'Test Set': ['CP_3', 'CP_3', 'CP_3', 'CP_3', 'PP_5-12', 'PP_5-12', 'PP_5-12', 'PP_5-12',
                    'Center_Embed', 'Center_Embed', 'Center_Embed', 'Center_Embed'],
        'UAS': [92.5, 91.8, 89.2, 88.7, 88.9, 87.2, 85.1, 84.8, 85.2, 83.7, 81.3, 80.9],
        'LAS': [89.1, 88.4, 85.8, 85.2, 85.3, 83.9, 81.2, 80.8, 81.7, 80.1, 77.5, 77.1]
    })
    
    # Generate plots
    plotter.create_comprehensive_report(sample_results)
    
    print("Sample plots generated successfully!")


if __name__ == "__main__":
    generate_sample_plots()
