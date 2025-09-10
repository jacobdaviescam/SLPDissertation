#!/usr/bin/env python3
"""
Experiment Runner for Dependency Parsing Evaluation

This script orchestrates the complete experimental pipeline for evaluating
multiple dependency parsing architectures on various linguistic test sets.

Usage:
    python run_experiments.py --config experiments.json
    python run_experiments.py --quick-demo

Author: Jacob Davies
"""

import sys
sys.path.append('.')

import argparse
import json
import time
from pathlib import Path
from typing import Dict, Any

from experimental_framework.parser_evaluation import ParserEvaluationFramework, ParserConfig
from visualization_suite.publication_plots import PublicationPlotter


def load_experiment_config(config_file: str) -> Dict[str, Any]:
    """Load experiment configuration from JSON file."""
    with open(config_file, 'r') as f:
        return json.load(f)


def setup_parsers(config: Dict[str, Any]) -> ParserEvaluationFramework:
    """Set up the parser evaluation framework with configured parsers."""
    framework = ParserEvaluationFramework(config.get('output_dir', 'model_outputs'))
    
    for parser_config in config['parsers']:
        parser = ParserConfig(
            name=parser_config['name'],
            model_path=parser_config['model_path'],
            parser_type=parser_config['type'],
            embedding_type=parser_config.get('embedding_type'),
            additional_params=parser_config.get('additional_params')
        )
        framework.register_parser(parser)
    
    return framework


def setup_test_sets(framework: ParserEvaluationFramework, config: Dict[str, Any]) -> None:
    """Register test sets with the evaluation framework."""
    for test_config in config['test_sets']:
        if Path(test_config['path']).exists():
            framework.register_test_set(test_config['name'], test_config['path'])
            print(f"Registered test set: {test_config['name']}")
        else:
            print(f"Warning: Test set file not found: {test_config['path']}")


def run_full_evaluation(config_file: str) -> None:
    """Run the complete evaluation pipeline."""
    print("Loading experiment configuration...")
    config = load_experiment_config(config_file)
    
    print("Setting up parser evaluation framework...")
    framework = setup_parsers(config)
    
    print("Registering test sets...")
    setup_test_sets(framework, config)
    
    print("Running comprehensive evaluation...")
    start_time = time.time()
    results = framework.run_comprehensive_evaluation()
    evaluation_time = time.time() - start_time
    
    print(f"Evaluation completed in {evaluation_time:.2f} seconds")
    print(f"Generated {len(results)} evaluation results")
    
    # Save results
    results_file = config.get('results_file', 'evaluation_results.csv')
    framework.save_results(results_file)
    print(f"Results saved to {results_file}")
    
    # Generate visualizations
    if config.get('generate_plots', True):
        print("Generating visualization report...")
        results_df = framework.generate_comparative_report()
        
        plot_config = config.get('visualization', {})
        output_dir = plot_config.get('output_dir', 'visualization_suite/figures')
        
        plotter = PublicationPlotter(output_dir)
        plotter.create_comprehensive_report(results_df)
        print(f"Visualizations saved to {output_dir}")


def run_quick_demo() -> None:
    """Run a quick demonstration with synthetic data."""
    print("Running quick demonstration...")
    
    # Create demo directory and files
    demo_dir = Path("demo")
    demo_dir.mkdir(exist_ok=True)
    
    # Create a simple demo test file
    demo_test_content = """# sent_id = 1
# text = The cat sat.
1	The	the	DET	DT	_	2	det	_	_
2	cat	cat	NOUN	NN	_	3	nsubj	_	_
3	sat	sit	VERB	VBD	_	0	root	_	_

# sent_id = 2  
# text = Dogs bark loudly.
1	Dogs	dog	NOUN	NNS	_	2	nsubj	_	_
2	bark	bark	VERB	VBP	_	0	root	_	_
3	loudly	loudly	ADV	RB	_	2	advmod	_	_

"""
    
    with open(demo_dir / "test.conllu", 'w') as f:
        f.write(demo_test_content)
    
    # Create demo model placeholders
    (demo_dir / "graph_model.pkl").touch()
    (demo_dir / "transition_model.pkl").touch()
    
    print("Demo setup complete.")
    print("Note: This is a demonstration with placeholder files.")
    print("For real evaluation, provide actual model files and test sets.")
    
    # Generate sample visualizations
    from visualization_suite.publication_plots import generate_sample_plots
    generate_sample_plots()
    
    print("Demo visualization complete!")


def create_sample_config() -> None:
    """Create a sample configuration file."""
    sample_config = {
        "description": "Sample configuration for dependency parsing evaluation",
        "parsers": [
            {
                "name": "graph_baseline",
                "model_path": "model_outputs/parser/graph_model.pkl",
                "type": "graph"
            },
            {
                "name": "transition_baseline",
                "model_path": "model_outputs/parser/transition_model.pkl", 
                "type": "transition"
            },
            {
                "name": "bert_graph",
                "model_path": "model_outputs/parser/bert_graph_model.pkl",
                "type": "bert",
                "embedding_type": "bert"
            },
            {
                "name": "bert_transition",
                "model_path": "model_outputs/parser/bert_transition_model.pkl",
                "type": "bert",
                "embedding_type": "bert"
            }
        ],
        "test_sets": [
            {
                "name": "CP_3",
                "path": "datasets/generalisation_sets/stripped/CP_3_stripped.conllu",
                "description": "Center embedding depth 3"
            },
            {
                "name": "CP_5-12", 
                "path": "datasets/generalisation_sets/stripped/CP_5-12_stripped.conllu",
                "description": "Center embedding depth 5-12"
            },
            {
                "name": "PP_3",
                "path": "datasets/generalisation_sets/stripped/PP_3_stripped.conllu",
                "description": "PP attachment depth 3"
            },
            {
                "name": "PP_5-12",
                "path": "datasets/generalisation_sets/stripped/PP_5-12_stripped.conllu", 
                "description": "PP attachment depth 5-12"
            }
        ],
        "output_dir": "model_outputs",
        "results_file": "evaluation_results.csv",
        "generate_plots": True,
        "visualization": {
            "output_dir": "visualization_suite/figures",
            "formats": ["pdf", "png"]
        }
    }
    
    with open("experiments.json", 'w') as f:
        json.dump(sample_config, f, indent=2)
    
    print("Sample configuration saved to experiments.json")


def main():
    """Main entry point for the experiment runner."""
    parser = argparse.ArgumentParser(
        description="Run dependency parsing evaluation experiments"
    )
    
    parser.add_argument(
        '--config', 
        type=str,
        help='Path to experiment configuration file'
    )
    
    parser.add_argument(
        '--quick-demo',
        action='store_true',
        help='Run a quick demonstration with sample data'
    )
    
    parser.add_argument(
        '--create-config',
        action='store_true', 
        help='Create a sample configuration file'
    )
    
    args = parser.parse_args()
    
    if args.create_config:
        create_sample_config()
    elif args.quick_demo:
        run_quick_demo()
    elif args.config:
        run_full_evaluation(args.config)
    else:
        parser.print_help()
        print("\nTo get started, try:")
        print("  python run_experiments.py --create-config")
        print("  python run_experiments.py --quick-demo")


if __name__ == "__main__":
    main()
