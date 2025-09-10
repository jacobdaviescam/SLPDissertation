# Dependency Parsing Research

A comprehensive showcase of advanced Python development, experimental methodology, and data visualization skills applied to natural language processing research.

## Overview

This repository demonstrates three core competencies through a complete dependency parsing research pipeline:

1. **Python Algorithm Development**: Novel semantic-to-syntactic conversion algorithms with advanced linguistic rule systems
2. **Experimental Design & Evaluation**: Systematic evaluation framework for multiple neural parser architectures
3. **Data Visualization**: Publication-ready analysis and plotting capabilities for research presentation

## Repository Structure

```
├── semantic_conversion/          # Core Algorithm Development
│   ├── conversion_engine.py     # Main semantic-syntactic converter
│   ├── linguistic_rules.py      # Advanced linguistic rule system
│   └── test_suite/             # Comprehensive test framework
├── experimental_framework/       # Systematic Evaluation Pipeline
│   ├── parser_evaluation.py    # Multi-parser evaluation framework
│   └── evaluation_metrics.py   # Advanced metrics & statistical analysis
├── visualization_suite/         # Publication-Quality Visualizations
│   ├── publication_plots.py    # Professional plotting framework
│   └── figures/                # Generated research figures
├── datasets/                    # Linguistic Datasets
│   ├── generalisation_sets/    # Syntactic complexity test sets
│   └── stripped_full/          # Processed training data
├── model_outputs/               # Parser Results & Artifacts
├── results_analysis/           # Performance Analysis Data
└── run_experiments.py          # Complete Pipeline Orchestration
```

## Core Technical Achievements

### 1. Python Algorithm Development (`semantic_conversion/`)

**Novel Semantic-to-Syntactic Conversion Engine**
- **Advanced NLP Processing**: Context-aware voice detection and argument structure mapping
- **Object-Oriented Design**: Modular `SemanticSyntacticConverter` class with extensible rule system
- **Linguistic Innovation**: Novel mapping algorithms for complex constructions (passives, causatives, control structures)
- **Comprehensive Testing**: Full unittest suite with edge case coverage

**Key Features:**
```python
# Advanced voice detection with context analysis
def detect_voice_context(self, tokens: List[str], semantic_roles: List[str]) -> VoiceType

# Complex construction handling
def handle_passive_construction(self, conversion_context: ConversionContext) -> ConversionResult

# Extensible rule engine integration
def apply_linguistic_rules(self, rule_engine: LinguisticRuleEngine) -> ConversionResult
```
### 2. Experimental Framework (`experimental_framework/`)

**Multi-Architecture Parser Evaluation System**
- **Systematic Evaluation**: Automated testing across BERT, Graph-based, and Transition-based parsers
- **Advanced Metrics**: UAS, LAS, statistical significance testing, linguistic phenomenon analysis
- **Scalable Design**: Configurable framework supporting multiple parser types and test sets
- **Performance Analysis**: Detailed breakdown by dependency length, POS tags, and sentence complexity

**Evaluation Capabilities:**
- Comparative analysis across 4+ parser architectures
- 6 specialized linguistic test sets (center embedding, PP attachment, etc.)
- Statistical significance testing with effect size calculation
- Automated report generation with detailed error analysis

### 3. Data Visualization (`visualization_suite/`)

**Publication-Ready Research Visualization**
- **Professional Quality**: Publication-standard figures with configurable styling
- **Comprehensive Coverage**: Performance comparisons, error analysis, linguistic phenomenon breakdown
- **Interactive Analysis**: Automated report generation with multiple visualization types
- **Research Integration**: Direct integration with experimental results for seamless analysis

**Visualization Types:**
- Parser performance comparisons with statistical annotations
- Error analysis heatmaps and confusion matrices
- Linguistic complexity analysis (dependency length, sentence depth)
- Learning curves and training progression visualization

## Quick Start

### Run Complete Experimental Pipeline
```bash
# Generate sample configuration
python run_experiments.py --create-config

# Run full evaluation with custom config
python run_experiments.py --config experiments.json

# Quick demonstration
python run_experiments.py --quick-demo
```

### Use Individual Components
```python
# Semantic conversion
from semantic_conversion.conversion_engine import SemanticSyntacticConverter
converter = SemanticSyntacticConverter()
result = converter.convert_semantic_to_syntactic(tokens, semantic_roles)

# Parser evaluation
from experimental_framework.parser_evaluation import ParserEvaluationFramework
framework = ParserEvaluationFramework()
results = framework.run_comprehensive_evaluation()

# Visualization
from visualization_suite.publication_plots import PublicationPlotter
plotter = PublicationPlotter()
plotter.create_comprehensive_report(results_df)
```

## Technical Specifications

### Dependencies
- **Core**: Python 3.7+, NumPy, Pandas
- **NLP**: Advanced linguistic processing capabilities
- **Visualization**: Matplotlib, Seaborn (publication-quality output)
- **Evaluation**: Statistical analysis (scipy for significance testing)
- **Neural Parsers**: PyTorch integration for BERT-based models

### Dataset Support
- **CoNLL-U Format**: Universal Dependencies standard
- **Linguistic Annotations**: POS tags, dependency relations, semantic roles
- **Test Sets**: Specialized complexity-graded evaluation sets
- **Git LFS**: Efficient handling of large linguistic datasets (425MB total)

### Performance Metrics
- **Unlabeled Attachment Score (UAS)**: Head attachment accuracy
- **Labeled Attachment Score (LAS)**: Complete dependency accuracy  
- **Statistical Analysis**: Paired t-tests, effect size calculation
- **Linguistic Analysis**: Performance by grammatical complexity

## Research Applications

This framework has been successfully applied to:

1. **Neural Parser Comparison**: Systematic evaluation of BERT vs. traditional approaches
2. **Linguistic Generalization**: Analysis of parser performance on complex syntactic structures
3. **Error Analysis**: Detailed categorization of parsing failures by linguistic phenomena
4. **Performance Optimization**: Identification of architecture-specific strengths and weaknesses
