import sys
import unittest
import csv
import pandas as pd
from pandas.util.testing import assert_frame_equal
sys.path.append('/Users/jacobdavies/SLPDissertation')
from conversion import DissertationModule

class TestConversion(unittest.TestCase):

    def __init__(self, *args, **kwargs) -> None:
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.test_instance = DissertationModule()
        self.test_instance.load_data('gen_cogsLF.tsv') 

    def test_PP_modif_subj(self):
        
        input_data = 6001  

        # sentence = The baby beside the seat helped a cake in a house .

        conversion = {'form': ['the', 'baby', 'beside', 'the', 'seat', 'helped', 'a', 'cake', 'in', 'a', 'house', '.'], 'lemma': ['the', 'baby', 'beside', 'the', 'seat', 'help', 'a', 'cake', 'in', 'a', 'house', '.'], 'pos':['DET', 'NOUN', 'ADP', 'DET', 'NOUN', 'VERB', 'DET', 'NOUN', 'ADP', 'DET', 'NOUN', 'PUNCT'], 'head':[1, 5, 4, 4, 1, 0, 7, 5, 10, 10, 7, 5], 'deprel': ['det', 'nsubj', 'case', 'det', 'nmod:beside', 'root', 'det', 'obj', 'case', 'det', 'nmod:in', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        

        actual_output = self.test_instance.process_sentence(input_data) 

        assert_frame_equal(actual_output, expected_output)

    def test_PP_modif_iobj(self):
        
        input_data = 7001  

        # sentence = A cake was passed to a passenger beside a tree by the boy .

        conversion = {'form': ['a', 'cake', 'was', 'passed', 'to', 'a', 'passenger', 'beside', 'a', 'tree', 'by', 'the', 'boy', '.'], 'lemma': ['a', 'cake', 'be', 'pass', 'to', 'a', 'passenger', 'beside', 'a', 'tree', 'by', 'the', 'boy', '.'], 'pos':['DET', 'NOUN', 'AUX', 'VERB', 'ADP', 'DET', 'NOUN', 'ADP', 'DET', 'NOUN', 'ADP', 'DET', 'NOUN', 'PUNCT'], 'head':[1, 3, 3, 0, 6, 6, 3, 9, 9, 6, 12, 12, 3, 3], 'deprel': ['det', 'nsubj:pass', 'aux:pass', 'root', 'case', 'det', 'obl:to', 'case', 'det', 'nmod:beside', 'case', 'det', 'obl:agent', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        

        actual_output = self.test_instance.process_sentence(input_data) 

        assert_frame_equal(actual_output, expected_output)

    def test_RC_modif_subj(self):
        
        input_data = 8001  

        # sentence = A cake that Liam found was investigated by the cat .

        conversion = {'form': ['a', 'cake', 'that', 'Liam', 'found', 'was', 'investigated', 'by', 'the', 'cat', '.'], 'lemma': ['a', 'cake', 'that', 'Liam', 'find', 'be', 'investigate', 'by', 'the', 'cat', '.'], 'pos':['DET', 'NOUN', 'SCONJ', 'PROPN', 'VERB', 'AUX', 'VERB', 'ADP', 'DET', 'NOUN', 'PUNCT'], 'head':[1, 6, 4, 4, 1, 6, 0, 9, 9, 6, 6], 'deprel': ['det', 'nsubj:pass', 'mark', 'nsubj', 'acl:relcl', 'aux:pass', 'root', 'case', 'det', 'obl:agent', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        

        actual_output = self.test_instance.process_sentence(input_data) 

        assert_frame_equal(actual_output, expected_output)

    def test_RC_modif_iobj(self):
        
        input_data = 9001  

        # sentence = Emma gave a bird that was lent the cookie a cake .

        conversion = {'form': ['Emma', 'gave', 'a', 'bird', 'that', 'was', 'lent', 'the', 'cookie', 'a', 'cake', '.'], 'lemma': ['Emma', 'give', 'a', 'bird', 'that', 'be', 'lend', 'the', 'cookie', 'a', 'cake', '.'], 'pos':['PROPN', 'VERB', 'DET', 'NOUN', 'SCONJ', 'AUX', 'VERB', 'DET', 'NOUN', 'DET', 'NOUN', 'PUNCT'], 'head':[1, 0, 3, 1, 6, 6, 3, 8, 6, 10, 1, 1], 'deprel': ['nsubj', 'root', 'det', 'iobj', 'mark', 'aux:pass', 'acl:relcl', 'det', 'obj', 'det', 'obj', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        

        actual_output = self.test_instance.process_sentence(input_data) 

        assert_frame_equal(actual_output, expected_output)

    def test_RC_iobj_extracted(self):
        
        input_data = 10001  

        # sentence = Ella cooked the servant that Emma gave a tool to .

        conversion = {'form': ['Ella', 'cooked', 'the', 'servant', 'that', 'Emma', 'gave', 'a', 'tool', 'to', '.'], 'lemma': ['Ella', 'cook', 'the', 'servant', 'that', 'Emma', 'give', 'a', 'tool', 'to', '.'], 'pos':['PROPN', 'VERB', 'DET', 'NOUN', 'SCONJ', 'PROPN', 'VERB', 'DET', 'NOUN', 'ADP', 'PUNCT'], 'head':[1, 0, 3, 1, 6, 6, 3, 8, 6, 3, 1], 'deprel': ['nsubj', 'root', 'det', 'obj', 'mark', 'nsubj', 'acl:relcl', 'det', 'obj', 'case', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        

        actual_output = self.test_instance.process_sentence(input_data) 

        assert_frame_equal(actual_output, expected_output)

    def test_Q_subj_active(self):
        
        input_data = 11001  

        # sentence = Who hated to dust ?

        conversion = {'form': ['who', 'hated', 'to', 'dust', '?'], 'lemma': ['who', 'hate', 'to', 'dust', '?'], 'pos':['PRON', 'VERB', 'PART', 'VERB', 'PUNCT'], 'head':[1, 0, 3, 1, 1], 'deprel': ['nsubj', 'root', 'mark', 'xcomp', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        

        actual_output = self.test_instance.process_sentence(input_data) 

        assert_frame_equal(actual_output, expected_output)

    def test_Q_subj_passive(self):
        
        input_data = 12001  

        # sentence = What was admired by Liam ?

        conversion = {'form': ['what', 'was', 'admired', 'by', 'Liam', '?'], 'lemma': ['what', 'be', 'admire', 'by', 'Liam', '?'], 'pos':['PRON', 'AUX', 'VERB', 'ADP', 'PROPN', 'PUNCT'], 'head':[2, 2, 0, 4, 2, 2], 'deprel': ['nsubj:pass', 'aux:pass', 'root', 'case', 'obl:agent', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        

        actual_output = self.test_instance.process_sentence(input_data) 

        assert_frame_equal(actual_output, expected_output)

    def test_Q_dobj_ditransV(self):
        
        input_data = 13001  

        # sentence = What did Liam give Owen ?

        conversion = {'form': ['what', 'did', 'Liam', 'give', 'Owen', '?'], 'lemma': ['what', 'do', 'Liam', 'give', 'Owen', '?'], 'pos':['PRON', 'AUX', 'PROPN', 'VERB', 'PROPN', 'PUNCT'], 'head':[3, 3, 3, 0, 3, 3], 'deprel': ['obj', 'aux', 'nsubj', 'root', 'iobj', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        

        actual_output = self.test_instance.process_sentence(input_data) 

        assert_frame_equal(actual_output, expected_output)

    def test_Q_iobj_ditransV(self):
        
        input_data = 14001  

        # sentence = Who did Emma give the cake to ?

        conversion = {'form': ['who', 'did', 'Emma', 'give', 'the', 'cake', 'to', '?'], 'lemma': ['who', 'do', 'Emma', 'give', 'the', 'cake', 'to', '?'], 'pos':['PRON', 'AUX', 'PROPN', 'VERB', 'DET', 'NOUN', 'ADP', 'PUNCT'], 'head':[3, 3, 3, 0, 5, 3, 0, 3], 'deprel': ['obl:to', 'aux', 'nsubj', 'root', 'det', 'obj', 'case', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        

        actual_output = self.test_instance.process_sentence(input_data) 

        assert_frame_equal(actual_output, expected_output)

    def test_Q_modified_NPs(self):
        
        input_data = 15001  

        # sentence = Who cleaned a cake beside a car ?

        conversion = {'form': ['who', 'cleaned', 'a', 'cake', 'beside', 'a', 'car', '?'], 'lemma': ['who', 'clean', 'a', 'cake', 'beside', 'a', 'car', '?'], 'pos':['PRON', 'VERB', 'DET', 'NOUN', 'ADP', 'DET', 'NOUN', 'PUNCT'], 'head':[1, 0, 3, 1, 6, 6, 3, 1], 'deprel': ['nsubj', 'root', 'det', 'obj', 'case', 'det', 'nmod:beside', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        

        actual_output = self.test_instance.process_sentence(input_data) 

        assert_frame_equal(actual_output, expected_output)

    def test_Q_long_mv(self):
        
        input_data = 16001  

        # sentence = Who did a governor hope that William froze ?

        conversion = {'form': ['who', 'did', 'a', 'governor', 'hope', 'that', 'William', 'froze', '?'], 'lemma': ['who', 'do', 'a', 'governor', 'hope', 'that', 'William', 'freeze', '?'], 'pos':['PRON', 'AUX', 'DET', 'NOUN', 'VERB', 'SCONJ', 'PROPN', 'VERB', 'PUNCT'], 'head':[7, 4, 3, 4, 0, 7, 7, 4, 7], 'deprel': ['obj', 'aux', 'det', 'nsubj', 'root', 'mark', 'nsubj', 'ccomp', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        actual_output = self.test_instance.process_sentence(input_data) 

        assert_frame_equal(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()