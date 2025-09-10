"""
Linguistic Rules Module

This module contains specialized linguistic rules and transformations 
for handling complex syntactic constructions in the semantic-to-syntactic 
conversion process.

Features:
- Passive voice transformation rules
- Unaccusative verb handling
- Complex predicate structures
- Multi-argument constructions

Author: Jacob Davies
"""

from typing import Dict, List, Tuple
from enum import Enum


class VoiceType(Enum):
    """Enumeration of voice types for linguistic constructions."""
    ACTIVE = "active"
    PASSIVE = "passive"
    UNACCUSATIVE = "unaccusative"
    MIDDLE = "middle"


class ConstructionType(Enum):
    """Enumeration of syntactic construction types."""
    SIMPLE_TRANSITIVE = "simple_transitive"
    DITRANSITIVE = "ditransitive"
    PREPOSITIONAL_PHRASE = "prepositional_phrase"
    RELATIVE_CLAUSE = "relative_clause"
    CENTER_EMBEDDING = "center_embedding"
    QUESTION_FORMATION = "question_formation"


class LinguisticRuleEngine:
    """
    Engine for applying linguistic transformation rules.
    
    This class handles complex linguistic phenomena that require
    specialized rules beyond simple semantic-to-syntactic mappings.
    """
    
    def __init__(self):
        """Initialize the rule engine with linguistic patterns."""
        self.passive_patterns = self._initialize_passive_patterns()
        self.unaccusative_patterns = self._initialize_unaccusative_patterns()
        self.complex_predicate_rules = self._initialize_complex_predicate_rules()
        
    def _initialize_passive_patterns(self) -> Dict[str, Dict[str, str]]:
        """
        Initialize patterns for passive voice transformations.
        
        Returns:
            Dictionary mapping semantic roles to syntactic relations in passive voice
        """
        return {
            'canonical_passive': {
                'theme': 'nsubj:pass',
                'agent': 'obl:agent', 
                'recipient': 'iobj',
                'location': 'obl',
                'instrument': 'obl:with'
            },
            'get_passive': {
                'theme': 'nsubj:pass',
                'agent': 'obl:by',
                'recipient': 'iobj'
            },
            'adjectival_passive': {
                'theme': 'nsubj',
                'agent': 'obl:by',
                'location': 'obl'
            }
        }
    
    def _initialize_unaccusative_patterns(self) -> Dict[str, Dict[str, str]]:
        """
        Initialize patterns for unaccusative verb constructions.
        
        Returns:
            Dictionary mapping semantic roles for unaccusative constructions
        """
        return {
            'motion_unaccusative': {
                'theme': 'nsubj',
                'location': 'obl',
                'direction': 'obl:to'
            },
            'change_of_state': {
                'theme': 'nsubj',
                'result': 'xcomp',
                'cause': 'obl:due_to'
            },
            'existence_appearance': {
                'theme': 'nsubj',
                'location': 'obl:in',
                'time': 'obl:tmod'
            }
        }
    
    def _initialize_complex_predicate_rules(self) -> Dict[str, List[str]]:
        """
        Initialize rules for complex predicate constructions.
        
        Returns:
            Dictionary mapping construction types to processing rules
        """
        return {
            'ditransitive_dative': [
                'identify_recipient',
                'assign_iobj_to_recipient', 
                'assign_obj_to_theme',
                'handle_dative_alternation'
            ],
            'prepositional_dative': [
                'identify_prepositional_phrase',
                'assign_obl_to_recipient',
                'assign_obj_to_theme'
            ],
            'relative_clause': [
                'identify_relativizer',
                'establish_gap_site',
                'assign_appropriate_function',
                'handle_extraction'
            ],
            'wh_question': [
                'identify_wh_word',
                'determine_extraction_site',
                'assign_question_function',
                'handle_long_distance_dependency'
            ]
        }
    
    def apply_passive_transformation(self, 
                                   semantic_roles: Dict[str, str], 
                                   passive_type: str = 'canonical_passive') -> Dict[str, str]:
        """
        Apply passive voice transformation rules.
        
        Args:
            semantic_roles: Original semantic role assignments
            passive_type: Type of passive construction
            
        Returns:
            Transformed syntactic dependency assignments
        """
        if passive_type not in self.passive_patterns:
            raise ValueError(f"Unknown passive type: {passive_type}")
        
        transformation_rules = self.passive_patterns[passive_type]
        syntactic_deps = {}
        
        for semantic_role, entity in semantic_roles.items():
            if semantic_role in transformation_rules:
                syntactic_dep = transformation_rules[semantic_role]
                syntactic_deps[entity] = syntactic_dep
            else:
                # Default handling for unmapped roles
                syntactic_deps[entity] = 'obl'
        
        return syntactic_deps
    
    def apply_unaccusative_transformation(self, 
                                        semantic_roles: Dict[str, str],
                                        unaccusative_type: str = 'motion_unaccusative') -> Dict[str, str]:
        """
        Apply unaccusative verb transformation rules.
        
        Args:
            semantic_roles: Original semantic role assignments
            unaccusative_type: Type of unaccusative construction
            
        Returns:
            Transformed syntactic dependency assignments
        """
        if unaccusative_type not in self.unaccusative_patterns:
            raise ValueError(f"Unknown unaccusative type: {unaccusative_type}")
        
        transformation_rules = self.unaccusative_patterns[unaccusative_type]
        syntactic_deps = {}
        
        for semantic_role, entity in semantic_roles.items():
            if semantic_role in transformation_rules:
                syntactic_dep = transformation_rules[semantic_role]
                syntactic_deps[entity] = syntactic_dep
        
        return syntactic_deps
    
    def handle_complex_predicate(self, 
                                construction_type: ConstructionType,
                                sentence_structure: Dict[str, any]) -> Dict[str, str]:
        """
        Handle complex predicate constructions with specialized rules.
        
        Args:
            construction_type: Type of complex construction
            sentence_structure: Detailed sentence structure information
            
        Returns:
            Appropriate syntactic dependency assignments
        """
        construction_name = construction_type.value
        
        if construction_name not in self.complex_predicate_rules:
            return self._default_complex_handling(sentence_structure)
        
        rules = self.complex_predicate_rules[construction_name]
        result = {}
        
        for rule in rules:
            if rule == 'identify_recipient':
                result.update(self._identify_recipient(sentence_structure))
            elif rule == 'assign_iobj_to_recipient':
                result.update(self._assign_iobj_to_recipient(sentence_structure))
            elif rule == 'handle_dative_alternation':
                result.update(self._handle_dative_alternation(sentence_structure))
            elif rule == 'identify_wh_word':
                result.update(self._identify_wh_word(sentence_structure))
            # Add more rule handlers as needed
        
        return result
    
    def _identify_recipient(self, sentence_structure: Dict[str, any]) -> Dict[str, str]:
        """Identify recipient entities in ditransitive constructions."""
        recipients = {}
        # Implementation logic for recipient identification
        return recipients
    
    def _assign_iobj_to_recipient(self, sentence_structure: Dict[str, any]) -> Dict[str, str]:
        """Assign indirect object relation to identified recipients."""
        assignments = {}
        # Implementation logic for iobj assignment
        return assignments
    
    def _handle_dative_alternation(self, sentence_structure: Dict[str, any]) -> Dict[str, str]:
        """Handle dative alternation patterns."""
        alternations = {}
        # Implementation logic for dative alternation
        return alternations
    
    def _identify_wh_word(self, sentence_structure: Dict[str, any]) -> Dict[str, str]:
        """Identify wh-words in question constructions."""
        wh_assignments = {}
        # Implementation logic for wh-word identification
        return wh_assignments
    
    def _default_complex_handling(self, sentence_structure: Dict[str, any]) -> Dict[str, str]:
        """Provide default handling for unrecognized complex constructions."""
        return {'default': 'dep'}
    
    def detect_construction_type(self, sentence_tokens: List[str]) -> ConstructionType:
        """
        Automatically detect the type of syntactic construction.
        
        Args:
            sentence_tokens: List of tokens in the sentence
            
        Returns:
            Detected construction type
        """
        # Check for question formation
        if any(token.lower() in ['what', 'who', 'where', 'when', 'why', 'how'] 
               for token in sentence_tokens):
            return ConstructionType.QUESTION_FORMATION
        
        # Check for relative clauses
        if any(token.lower() in ['that', 'which', 'who', 'whom', 'whose'] 
               for token in sentence_tokens):
            return ConstructionType.RELATIVE_CLAUSE
        
        # Check for prepositional phrases
        if any(token.lower() in ['to', 'for', 'with', 'by', 'in', 'on', 'at'] 
               for token in sentence_tokens):
            return ConstructionType.PREPOSITIONAL_PHRASE
        
        # Default to simple transitive
        return ConstructionType.SIMPLE_TRANSITIVE
    
    def get_transformation_rules(self, voice_type: VoiceType) -> Dict[str, str]:
        """
        Get transformation rules for a specific voice type.
        
        Args:
            voice_type: Type of voice construction
            
        Returns:
            Dictionary of transformation rules
        """
        if voice_type == VoiceType.PASSIVE:
            return self.passive_patterns['canonical_passive']
        elif voice_type == VoiceType.UNACCUSATIVE:
            return self.unaccusative_patterns['motion_unaccusative']
        else:
            # Active voice - direct mapping
            return {
                'agent': 'nsubj',
                'theme': 'obj',
                'recipient': 'iobj',
                'location': 'obl'
            }


class ConstraintChecker:
    """
    Linguistic constraint checker for validating transformations.
    
    This class ensures that generated syntactic structures conform
    to linguistic well-formedness constraints.
    """
    
    def __init__(self):
        """Initialize constraint checker with linguistic constraints."""
        self.obligatory_arguments = {
            'transitive': ['nsubj', 'obj'],
            'ditransitive': ['nsubj', 'obj', 'iobj'],
            'intransitive': ['nsubj'],
            'unaccusative': ['nsubj']
        }
    
    def validate_structure(self, 
                         verb_type: str, 
                         dependencies: Dict[str, str]) -> Tuple[bool, List[str]]:
        """
        Validate syntactic structure against linguistic constraints.
        
        Args:
            verb_type: Type of verb construction
            dependencies: Generated dependency relations
            
        Returns:
            Tuple of (is_valid, list_of_violations)
        """
        violations = []
        
        if verb_type in self.obligatory_arguments:
            required_deps = self.obligatory_arguments[verb_type]
            present_deps = list(dependencies.values())
            
            for required_dep in required_deps:
                if required_dep not in present_deps:
                    violations.append(f"Missing obligatory argument: {required_dep}")
        
        # Check for conflicting assignments
        if 'nsubj' in dependencies.values() and 'nsubj:pass' in dependencies.values():
            violations.append("Conflicting subject assignments: nsubj and nsubj:pass")
        
        is_valid = len(violations) == 0
        return is_valid, violations
