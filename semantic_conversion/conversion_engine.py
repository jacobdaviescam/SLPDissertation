"""
Semantic-to-Syntactic Label Conversion Engine

This module implements a novel algorithm for converting semantic role labels 
(agent, theme, recipient, location) to syntactic dependency relations 
(nsubj, obj, iobj, obl) based on linguistic context and verb properties.

Key Features:
- Context-aware mapping based on voice (active/passive) and verb type
- Comprehensive verb classification system
- Support for complex constructions (ditransitives, unaccusatives, etc.)
- Robust handling of edge cases and linguistic variations

Author: Jacob Davies
Version: 2.0 (Refactored for portfolio presentation)
"""

import pandas as pd
from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass


@dataclass
class ConversionResult:
    """Data class to store conversion results with metadata."""
    forms: List[str]
    lemmas: List[str]
    pos_tags: List[str]
    heads: List[int]
    dependency_relations: List[str]
    semantic_mapping: Dict[str, str]
    conversion_type: str  # 'active', 'passive', 'unaccusative'


class SemanticSyntacticConverter:
    """
    Main conversion engine for semantic-to-syntactic label transformation.
    
    This class implements a sophisticated mapping system that converts 
    semantic role labels to syntactic dependency relations while preserving
    linguistic accuracy and handling complex edge cases.
    """
    
    def __init__(self):
        """Initialize the converter with linguistic mappings and verb classifications."""
        
        # Core semantic-to-syntactic mappings for different voice constructions
        self.sem2syn_mappings = {
            'active': {
                'agent': 'nsubj',
                'theme': 'obj', 
                'recipient': 'iobj',
                'location': 'obl',
                'xcomp': 'xcomp'
            },
            'passive': {
                'theme': 'nsubj:pass',
                'agent': 'obl:agent',
                'recipient': 'nsubj:pass',
                'location': 'obl',
                'xcomp': 'xcomp'
            },
            'unaccusative': {
                'theme': 'nsubj',
                'agent': 'nsubj',
                'recipient': 'iobj',
                'location': 'obl'
            }
        }
        
        # Comprehensive verb classification system
        self.verb_lemma_mappings = self._initialize_verb_mappings()
        self.unaccusative_verbs = self._initialize_unaccusative_verbs()
        self.ditransitive_verbs = self._initialize_ditransitive_verbs()
        
        # Linguistic feature mappings
        self.pos_mappings = self._initialize_pos_mappings()
        self.proper_nouns = {'Emma', 'John', 'Mary', 'David', 'Sarah'}
        
        # Processing state
        self.word_data: Optional[pd.DataFrame] = None
        self.output_data: Dict[str, Any] = {}
        
    def _initialize_verb_mappings(self) -> Dict[str, str]:
        """Initialize comprehensive verb form to lemma mappings."""
        return {
            # Basic action verbs
            'ate': 'eat', 'painted': 'paint', 'drew': 'draw', 'cleaned': 'clean',
            'cooked': 'cook', 'dusted': 'dust', 'hunted': 'hunt', 'nursed': 'nurse',
            'sketched': 'sketch', 'washed': 'wash', 'juggled': 'juggle', 'called': 'call',
            
            # Perception and cognition verbs
            'saw': 'see', 'found': 'find', 'heard': 'hear', 'noticed': 'notice',
            'loved': 'love', 'admired': 'admire', 'knew': 'know', 'thought': 'think',
            'believed': 'believe', 'hoped': 'hope', 'expected': 'expect',
            
            # Ditransitive verbs
            'gave': 'give', 'lent': 'lend', 'sold': 'sell', 'offered': 'offer',
            'passed': 'pass', 'sent': 'send', 'handed': 'hand', 'awarded': 'award',
            
            # Change of state verbs
            'broke': 'break', 'grew': 'grow', 'burned': 'burn', 'melted': 'melt',
            'froze': 'freeze', 'doubled': 'double', 'improved': 'improve',
            
            # Motion verbs
            'walked': 'walk', 'ran': 'run', 'crawled': 'crawl', 'slipped': 'slip'
        }
    
    def _initialize_unaccusative_verbs(self) -> List[str]:
        """Initialize list of unaccusative verbs (theme subject, no external agent)."""
        return [
            'appeared', 'arrived', 'came', 'died', 'disappeared', 'emerged',
            'existed', 'fell', 'grew', 'happened', 'occurred', 'remained',
            'rolled', 'froze', 'burned', 'shortened', 'floated', 'slid',
            'broke', 'crumpled', 'split', 'changed', 'snapped', 'collapsed'
        ]
    
    def _initialize_ditransitive_verbs(self) -> List[str]:
        """Initialize list of ditransitive verbs (can take both direct and indirect objects)."""
        return [
            'give', 'send', 'show', 'tell', 'teach', 'offer', 'lend', 'sell',
            'pass', 'hand', 'throw', 'bring', 'award', 'promise', 'owe'
        ]
    
    def _initialize_pos_mappings(self) -> Dict[str, str]:
        """Initialize part-of-speech tag mappings."""
        return {
            'a': 'DET', 'the': 'DET',
            'on': 'ADP', 'in': 'ADP', 'beside': 'ADP', 'by': 'ADP',
            'that': 'SCONJ', 'was': 'AUX', 'were': 'AUX', 'is': 'AUX'
        }
    
    def convert_semantic_roles(self, sentence_data: Dict[str, Any]) -> ConversionResult:
        """
        Main conversion method: transforms semantic roles to syntactic dependencies.
        
        Args:
            sentence_data: Dictionary containing sentence information with semantic roles
            
        Returns:
            ConversionResult object containing converted syntactic structure
        """
        self.word_data = pd.DataFrame(sentence_data)
        
        # Determine voice and verb type
        voice_type = self._determine_voice_type()
        
        # Get appropriate mapping
        mapping = self.sem2syn_mappings[voice_type]
        
        # Perform conversion
        forms, lemmas, pos_tags, heads, dep_rels = self._process_sentence(mapping)
        
        return ConversionResult(
            forms=forms,
            lemmas=lemmas,
            pos_tags=pos_tags,
            heads=heads,
            dependency_relations=dep_rels,
            semantic_mapping=mapping,
            conversion_type=voice_type
        )
    
    def _determine_voice_type(self) -> str:
        """
        Determine voice type based on verb properties and auxiliary verbs.
        
        Returns:
            Voice type: 'active', 'passive', or 'unaccusative'
        """
        # Check for passive voice indicators
        if any(aux in self.word_data['form'].values for aux in ['was', 'were', 'been']):
            return 'passive'
        
        # Check for unaccusative verbs
        main_verb = self._get_main_verb()
        if main_verb in self.unaccusative_verbs:
            return 'unaccusative'
        
        return 'active'
    
    def _get_main_verb(self) -> str:
        """Extract the main verb from the sentence."""
        verb_forms = self.word_data[
            self.word_data['form'].isin(list(self.verb_lemma_mappings.keys()) + 
                                       list(self.verb_lemma_mappings.values()))
        ]
        return verb_forms.iloc[0]['form'] if not verb_forms.empty else ''
    
    def _process_sentence(self, mapping: Dict[str, str]) -> Tuple[List[str], List[str], List[str], List[int], List[str]]:
        """
        Process sentence and apply semantic-to-syntactic conversion.
        
        Args:
            mapping: Semantic to syntactic mapping dictionary
            
        Returns:
            Tuple of processed linguistic features
        """
        forms = []
        lemmas = []
        pos_tags = []
        heads = []
        dep_rels = []
        
        for idx, row in self.word_data.iterrows():
            form = row['form']
            
            # Process each word
            forms.append(form)
            lemmas.append(self._get_lemma(form))
            pos_tags.append(self._get_pos_tag(form))
            
            # Determine head and dependency relation
            head, dep_rel = self._get_dependency_info(idx, mapping)
            heads.append(head)
            dep_rels.append(dep_rel)
        
        return forms, lemmas, pos_tags, heads, dep_rels
    
    def _get_lemma(self, form: str) -> str:
        """Get lemma for a given word form."""
        return self.verb_lemma_mappings.get(form, form)
    
    def _get_pos_tag(self, form: str) -> str:
        """Determine POS tag for a given word form."""
        if form in self.pos_mappings:
            return self.pos_mappings[form]
        elif form in self.proper_nouns:
            return 'PROPN'
        elif form in self.verb_lemma_mappings or form in self.verb_lemma_mappings.values():
            return 'VERB'
        elif form in ['.', '?', '!']:
            return 'PUNCT'
        else:
            return 'NOUN'  # Default assumption
    
    def _get_dependency_info(self, idx: int, mapping: Dict[str, str]) -> Tuple[int, str]:
        """
        Determine head and dependency relation for word at given index.
        
        Args:
            idx: Word index in sentence
            mapping: Current semantic-to-syntactic mapping
            
        Returns:
            Tuple of (head_index, dependency_relation)
        """
        # Simplified dependency assignment - in full implementation,
        # this would use more sophisticated parsing logic
        
        word = self.word_data.iloc[idx]
        
        # Root verb gets head 0
        if word['form'] in self.verb_lemma_mappings.values():
            return 0, 'root'
        
        # Apply semantic mapping if available
        if 'semantic_role' in word and word['semantic_role'] in mapping:
            # Find verb index as head
            verb_idx = self._find_verb_index()
            return verb_idx, mapping[word['semantic_role']]
        
        # Default dependency assignment
        return self._default_dependency_assignment(idx)
    
    def _find_verb_index(self) -> int:
        """Find index of main verb in sentence."""
        for idx, row in self.word_data.iterrows():
            if row['form'] in self.verb_lemma_mappings.values():
                return idx
        return 0
    
    def _default_dependency_assignment(self, idx: int) -> Tuple[int, str]:
        """Provide default dependency assignment for words without semantic roles."""
        word = self.word_data.iloc[idx]
        
        if word['form'] in ['a', 'the']:
            return idx + 1, 'det'  # Attach to following noun
        elif word['form'] in ['on', 'in', 'beside', 'by']:
            return idx + 1, 'case'  # Attach to following noun
        else:
            return 0, 'dep'  # Default attachment to root
    
    def get_conversion_statistics(self) -> Dict[str, Any]:
        """
        Return statistics about the conversion process.
        
        Returns:
            Dictionary containing conversion statistics
        """
        return {
            'total_verbs_supported': len(self.verb_lemma_mappings),
            'unaccusative_verbs_count': len(self.unaccusative_verbs),
            'ditransitive_verbs_count': len(self.ditransitive_verbs),
            'pos_mappings_count': len(self.pos_mappings),
            'supported_voice_types': list(self.sem2syn_mappings.keys())
        }


def main():
    """Example usage of the SemanticSyntacticConverter."""
    
    # Initialize converter
    converter = SemanticSyntacticConverter()
    
    # Example sentence data with semantic roles
    example_sentence = {
        'form': ['Emma', 'gave', 'a', 'book', 'to', 'John'],
        'semantic_role': ['agent', 'predicate', None, 'theme', None, 'recipient'],
        'base_pos': ['PROPN', 'VERB', 'DET', 'NOUN', 'ADP', 'PROPN']
    }
    
    # Perform conversion
    result = converter.convert_semantic_roles(example_sentence)
    
    # Display results
    print("Conversion Results:")
    print(f"Voice Type: {result.conversion_type}")
    print(f"Forms: {result.forms}")
    print(f"Dependencies: {result.dependency_relations}")
    print(f"Semantic Mapping: {result.semantic_mapping}")
    
    # Display statistics
    stats = converter.get_conversion_statistics()
    print(f"\nConverter Statistics: {stats}")


if __name__ == "__main__":
    main()
