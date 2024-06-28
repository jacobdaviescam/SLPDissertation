import unittest
import csv
import pandas as pd

from conversion import DissertationModule  # Replace "YourClass" with the actual class name from attempt.py

class TestYourClass(unittest.TestCase):

    def __init__(self):

        with open('train.tsv', 'r') as tsvfile:
            reader = csv.reader(tsvfile, delimiter='\t')
            self.train = {}
            sentence_id = 1
            for row in reader:
                if row:
                    sentence = row[0]
                    semantics = row[1]
                    distribution = row[2]
                    self.train[sentence_id] = {'sentence': sentence, 'semantics': semantics, 'distribution': distribution}
                    sentence_id += 1

        with open('gen_cogsLF.tsv', 'r') as tsvfile:
            reader = csv.reader(tsvfile, delimiter='\t')
            self.gen = {}
            sentence_id = 1
            for row in reader:
                if row:
                    sentence = row[0]
                    semantics = row[1]
                    distribution = row[2]
                    self.gen[sentence_id] = {'sentence': sentence, 'semantics': semantics, 'distribution': distribution}
                    sentence_id += 1

    def test_in_distribution(self):
        
        input_data = self.train[1]  

        # sentence = A cake was cooked by the scientist .

        conversion = {'form': ['a', 'cake', 'was', 'cooked', 'by', 'the', 'scientist', '.'], 'lemma': ['a', 'cake', 'be', 'cook', 'by', 'the', 'scientist', '.'], 'pos':['DET', 'NOUN', 'AUX', 'VERB', 'ADP', 'DET', 'NOUN', 'PUNCT'], 'head':[1, 3, 3, 0, 6, 6, 3, 3], 'deprel': ['det', 'nsubj:pass', 'aux:pass', 'root', 'case', 'det', 'obl:agent', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        test_instance = DissertationModule()

        actual_output = test_instance.process_sentence(input_data) 

        self.assertEqual(actual_output, expected_output)

    def test_exposure_example_obj_omitted_transitive(self):
        
        input_data = self.train[971]  

        # sentence = The goose baked .

        conversion = {'form': ['the', 'goose', 'baked', '.'], 'lemma': ['the', 'goose', 'bake', '.'], 'pos':['DET', 'NOUN', 'VERB', 'PUNCT'], 'head':[1, 2, 0, 2], 'deprel': ['det', 'nsubj', 'root', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        test_instance = DissertationModule()

        actual_output = test_instance.process_sentence(input_data) 

        self.assertEqual(actual_output, expected_output)

    def test_exposure_example_pp_dative(self):
        
        input_data = self.train[3346]  

        # sentence = The girl shipped a cookie in a container to Scarlett .

        conversion = {'form': ['the', 'girl', 'shipped', 'a', 'cookie', 'in', 'a', 'container', 'to', 'Scarlett', '.'], 'lemma': ['the', 'girl', 'ship', 'a', 'cookie', 'in', 'a', 'container', 'to', 'Scarlett', '.'], 'pos':['DET', 'NOUN', 'VERB', 'DET', 'NOUN', 'ADP', 'DET', 'NOUN', 'ADP', 'PROPN', 'PUNCT'], 'head':[1, 2, 0, 4, 2, 7, 7, 4, 9, 2, 2], 'deprel': ['det', 'nsubj', 'root', 'det', 'obj', 'case', 'det', 'nmod:in', 'case', 'obl:to', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        test_instance = DissertationModule()

        actual_output = test_instance.process_sentence(input_data) 

        self.assertEqual(actual_output, expected_output)

    def test_exposure_example_do_dative(self):
        
        input_data = self.train[5732]  

        # sentence = The girl teleported Liam the cookie .

        conversion = {'form': ['the', 'girl', 'teleported', 'Liam', 'the', 'cookie', '.'], 'lemma': ['the', 'girl', 'teleport', 'Liam', 'the', 'cookie', '.'], 'pos':['DET', 'NOUN', 'VERB', 'PROPN', 'DET', 'NOUN', 'PUNCT'], 'head':[1, 2, 0, 2, 5, 2, 2], 'deprel': ['det', 'nsubj', 'root', 'iobj', 'det', 'obj', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        test_instance = DissertationModule()

        actual_output = test_instance.process_sentence(input_data) 

        self.assertEqual(actual_output, expected_output)

    def test_exposure_example_passive(self):
        
        input_data = self.train[7912]  

        # sentence = The book was squeezed .

        conversion = {'form': ['the', 'book', 'was', 'squeezed', '.'], 'lemma': ['the', 'book', 'be', 'squeeze', '.'], 'pos':['DET', 'NOUN', 'AUX', 'VERB', 'PUNCT'], 'head':[1, 3, 3, 0, 3], 'deprel': ['det', 'nsubj', 'aux:pass', 'root', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        test_instance = DissertationModule()

        actual_output = test_instance.process_sentence(input_data) 

        self.assertEqual(actual_output, expected_output)

    def test_object_modifying_RC(self):
        
        input_data = self.train[10795]  

        # sentence = Emma adored a drink that Noah liked .

        conversion = {'form': ['Emma', 'adored', 'a', 'drink', 'that', 'Noah', 'liked', '.'], 'lemma': ['Emma', 'adore', 'a', 'drink', 'that', 'Noah', 'like', '.'], 'pos':['PROPN', 'VERB', 'DET', 'NOUN', 'SCONJ', 'PROPN', 'VERB', 'PUNCT'], 'head':[1, 0, 3, 1, 6, 6, 1, 1], 'deprel': ['nsubj', 'root', 'det', 'obj', 'mark', 'nsubj', 'acl:relcl', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        test_instance = DissertationModule()

        actual_output = test_instance.process_sentence(input_data) 

        self.assertEqual(actual_output, expected_output)

    def test_exposure_example_transitive_subj(self):
        
        input_data = self.train[12920]  

        # sentence = A cobra helped a cake in the house .

        conversion = {'form': ['a', 'cobra', 'helped', 'a', 'cake', 'in', 'the', 'house', '.'], 'lemma': ['a', 'cobra', 'help', 'a', 'cake', 'in', 'the', 'house', '.'], 'pos':['DET', 'NOUN', 'VERB', 'DET', 'NOUN', 'ADP', 'DET', 'NOUN', 'PUNCT'], 'head':[1, 2, 0, 4, 2, 7, 7, 4, 2], 'deprel': ['det', 'nsubj', 'root', 'det', 'obj', 'case', 'det', 'nmod:in', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        test_instance = DissertationModule()

        actual_output = test_instance.process_sentence(input_data) 

        self.assertEqual(actual_output, expected_output)

    def test_exposure_example_unacc_subj(self):
        
        input_data = self.train[13564]  

        # sentence = A landlord hoped that the hippo decomposed .

        conversion = {'form': ['a', 'landlord', 'hoped', 'that', 'the', 'hippo', 'decomposed', '.'], 'lemma': ['a', 'landlord', 'hope', 'that', 'the', 'hippo', 'decompose', '.'], 'pos':['DET', 'NOUN', 'VERB', 'SCONJ', 'DET', 'NOUN', 'VERB', 'PUNCT'], 'head':[1, 2, 0, 6, 5, 6, 2, 2], 'deprel': ['det', 'nsubj', 'root', 'mark', 'det', 'nsubj', 'ccomp', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        test_instance = DissertationModule()

        actual_output = test_instance.process_sentence(input_data) 

        self.assertEqual(actual_output, expected_output)

    def test_exposure_example_unacc(self):
        
        input_data = self.train[15694]  

        # sentence = Julian shattered .

        conversion = {'form': ['Julian', 'shattered', '.'], 'lemma': ['Julian', 'shatter', '.'], 'pos':['PROPN', 'VERB', 'PUNCT'], 'head':[1, 0, 1], 'deprel': ['nsubj', 'root', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        test_instance = DissertationModule()

        actual_output = test_instance.process_sentence(input_data) 

        self.assertEqual(actual_output, expected_output)

    def test_center_embed_2(self):
        
        input_data = self.train[15876]  

        # sentence = A boy helped the cat that the girl that Emma changed rolled .

        conversion = {'form': ['a', 'boy', 'helped', 'the', 'cat', 'that', 'the', 'girl', 'that', 'Emma', 'changed', 'rolled', '.'], 'lemma': ['a', 'boy', 'help', 'the', 'cat', 'that', 'the', 'girl', 'that', 'Emma', 'change', 'roll', '.'], 'pos':['DET', 'NOUN', 'VERB', 'DET', 'NOUN', 'SCONJ', 'DET', 'NOUN', 'SCONJ', 'PROPN', 'VERB', 'VERB', 'PUNCT'], 'head':[1, 2, 0, 4, 2, 11, 7, 11, 10, 10, 11, 7, 4], 'deprel': ['det', 'nsubj', 'root', 'det', 'obj', 'mark', 'det', 'nsubj', 'mark', 'nsubj', 'acl:relcl', 'acl:relcl', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        test_instance = DissertationModule()

        actual_output = test_instance.process_sentence(input_data) 

        self.assertEqual(actual_output, expected_output)

    def test_center_embed_4(self):
        
        input_data = self.train[15881]  

        # sentence = Charlotte burned a penny that the president that the girl that a boy that Ava enlarged ate crumpled tolerated .

        conversion = {'form': ['Charlotte', 'burned', 'a', 'penny', 'that', 'the', 'president', 'that', 'the', 'girl', 'that', 'a', 'boy', 'that', 'Ava', 'enlarged', 'ate', 'crumpled', 'tolerated', '.'], 'lemma': ['Charlotte', 'burn', 'a', 'penny', 'that', 'the', 'president', 'that', 'the', 'girl', 'that', 'a', 'boy', 'that', 'Ava', 'enlarge', 'eat', 'crumple', 'tolerate', '.'], 'pos':['PROPN', 'VERB', 'DET', 'NOUN', 'SCONJ', 'DET', 'NOUN', 'SCONJ', 'DET', 'NOUN', 'SCONJ', 'DET', 'NOUN', 'SCONJ', 'PROPN', 'VERB', 'VERB', 'VERB', 'VERB',  'PUNCT'], 'head':[1, 0, 3, 1, 18, 6, 18, 17, 9, 17, 16, 12, 16, 15, 15, 12, 9, 6, 3, 1], 'deprel': ['nsubj', 'root', 'det', 'obj', 'mark', 'det', 'nsubj', 'mark', 'det', 'nsubj', 'mark', 'det', 'nsubj', 'mark', 'nsubj', 'acl:relcl', 'acl:relcl', 'acl:relcl', 'acl:relcl', 'punct' ]}


        expected_output = pd.DataFrame(conversion)  

        test_instance = DissertationModule()

        actual_output = test_instance.process_sentence(input_data) 

        self.assertEqual(actual_output, expected_output)

    def test_cp_4(self):
        
        input_data = self.train[16220]  

        # sentence = A baby respected that the host confessed that Emma admired that a girl liked that a bunny was offered a block on the tabletop .

        conversion = {'form': ['a', 'baby', 'respected', 'that', 'the', 'host', 'confessed', 'that', 'Emma', 'admired', 'that', 'a', 'girl', 'liked', 'that', 'a', 'bunny', 'was', 'offered', 'a', 'block', 'on', 'the', 'tabletop', '.'], 'lemma': ['a', 'baby', 'respect', 'that', 'the', 'host', 'confess', 'that', 'Emma', 'admire', 'that', 'a', 'girl', 'like', 'that', 'a', 'bunny', 'be', 'offer', 'a', 'block', 'on', 'the', 'tabletop', '.'], 'pos':['DET', 'NOUN', 'VERB', 'SCONJ', 'DET', 'NOUN', 'VERB', 'SCONJ', 'PROPN', 'VERB', 'SCONJ', 'DET', 'NOUN', 'VERB', 'SCONJ', 'DET', 'NOUN', 'AUX', 'VERB', 'DET', 'NOUN', 'ADP', 'DET', 'NOUN', 'PUNCT'], 'head':[1, 2, 0, 6, 5, 6, 2, 9, 9, 2, 13, 12, 13, 2, 18, 16, 18, 18, 2, 20, 18, 23, 23, 20, 2], 'deprel': ['det', 'nsubj', 'root', 'mark', 'det', 'nsubj', 'ccomp', 'mark', 'nsubj', 'ccomp', 'mark', 'det', 'nsubj', 'ccomp', 'mark', 'det', 'nsubj', 'aux:pass', 'ccomp', 'det', 'obj', 'case', 'det', 'nmod:on', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        test_instance = DissertationModule()

        actual_output = test_instance.process_sentence(input_data) 

        self.assertEqual(actual_output, expected_output)

    def test_pp_4(self):
        
        input_data = self.train[16377]  

        # sentence = Emma juggled a cake on a stage in a garden on a table beside the whale .

        conversion = {'form': ['Emma', 'juggled', 'a', 'cake', 'on', 'a', 'stage', 'in', 'a', 'garden', 'on', 'a', 'table', 'beside', 'the', 'whale', '.'], 'lemma': ['Emma', 'juggle', 'a', 'cake', 'on', 'a', 'stage', 'in', 'a', 'garden', 'on', 'a', 'table', 'beside', 'the', 'whale', '.'], 'pos':['PROPN', 'VERB', 'DET', 'NOUN', 'ADP', 'DET', 'NOUN', 'ADP', 'DET', 'NOUN', 'ADP', 'DET', 'NOUN', 'ADP', 'DET', 'NOUN', 'PUNCT'], 'head':[1, 0, 3, 1, 6, 6, 3, 9, 9, 6, 12, 12, 9, 15, 15, 12, 1], 'deprel': ['nsubj', 'root', 'det', 'obj', 'case', 'det', 'nmod:on', 'case', 'det', 'nmod:in', 'case', 'det', 'nmod:on', 'case', 'det', 'nmod:beside', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        test_instance = DissertationModule()

        actual_output = test_instance.process_sentence(input_data) 

        self.assertEqual(actual_output, expected_output)

    def test_wh_Q_simple_trans(self):
        
        input_data = self.train[16828]  

        # sentence = What did Liam tolerate ?

        conversion = {'form': ['what', 'did', 'Liam', 'tolerate', '?'], 'lemma': ['what', 'do', 'Liam', 'tolerate', '?'], 'pos':['PRON', 'AUX', 'PROPN', 'VERB', 'PUNCT'], 'head':[3, 3, 3, 0, 3], 'deprel': ['obj', 'aux', 'nsubj', 'root', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        test_instance = DissertationModule()

        actual_output = test_instance.process_sentence(input_data) 

        self.assertEqual(actual_output, expected_output)

    def test_exposure_example_active(self):
        
        input_data = self.train[18849]  

        # sentence = A crocodile blessed William .

        conversion = {'form': ['a', 'crocodile', 'blessed', 'William', '.'], 'lemma': ['a', 'crocodile', 'bless', 'William', '.'], 'pos':['DET', 'NOUN', 'VERB', 'PROPN', 'PUNCT'], 'head':[1, 2, 0, 2, 2], 'deprel': ['det', 'nsubj', 'root', 'obj', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        test_instance = DissertationModule()

        actual_output = test_instance.process_sentence(input_data) 

        self.assertEqual(actual_output, expected_output)

    def test_standalone_NP_PP(self):
        
        input_data = self.train[19194]  

        # sentence = a cat beside the bed

        conversion = {'form': ['a', 'cat', 'beside', 'the', 'bed'], 'lemma': ['a', 'cat', 'beside', 'the', 'bed'], 'pos':['DET', 'NOUN', 'ADP', 'DET', 'NOUN'], 'head':[1, 0, 4, 4, 1], 'deprel': ['det', 'root', 'case', 'det', 'nmod:beside']}


        expected_output = pd.DataFrame(conversion)  

        test_instance = DissertationModule()

        actual_output = test_instance.process_sentence(input_data) 

        self.assertEqual(actual_output, expected_output)

    def test_standalone_NP_RC(self):
        
        input_data = self.train[19295]  

        # sentence = the girl that Mia liked

        conversion = {'form': ['the', 'girl', 'that', 'Mia', 'liked'], 'lemma': ['the', 'girl', 'that', 'Mia', 'like'], 'pos':['DET', 'NOUN', 'SCONJ', 'PROPN', 'VERB'], 'head':[1, 0, 4, 4, 1], 'deprel': ['det', 'root', 'mark', 'nsubj', 'acl:relcl']}


        expected_output = pd.DataFrame(conversion)  

        test_instance = DissertationModule()

        actual_output = test_instance.process_sentence(input_data) 

        self.assertEqual(actual_output, expected_output)

    def test_exposure_example_obj_common(self):
        
        input_data = self.train[20422]  

        # sentence = Henry liked a cockroach in a box .

        conversion = {'form': ['Henry', 'liked', 'a' 'cockroach', 'in', 'a', 'box', '.'], 'lemma': ['Henry', 'like', 'a', 'cockroach', 'in', 'a', 'box', '.'], 'pos':['PROPN', 'VERB', 'DET', 'NOUN', 'ADP', 'DET', 'NOUN', 'PUNCT'], 'head':[1, 0, 3, 1, 6, 6, 3, 1], 'deprel': ['nsubj', 'root', 'det', 'obj', 'case', 'det', 'nmod:in', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        test_instance = DissertationModule()

        actual_output = test_instance.process_sentence(input_data) 

        self.assertEqual(actual_output, expected_output)

    def test_exposure_example_subj_common(self):
        
        input_data = self.train[28501]  

        # sentence = A hedgehog ate the cake on the bed .

        conversion = {'form': ['a', 'hedgehog', 'ate', 'the', 'cake', 'on', 'the', 'bed', '.'], 'lemma': ['a', 'hedgehog', 'eat', 'the', 'cake', 'on', 'the', 'bed', '.'], 'pos':['DET', 'NOUN', 'VERB', 'DET', 'NOUN', 'ADP', 'DET', 'NOUN', 'PUNCT'], 'head':[1, 2, 0, 4, 2, 7, 7, 4, 2], 'deprel': ['det', 'nsubj', 'root', 'det', 'obj', 'case', 'det', 'nmod:on', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        test_instance = DissertationModule()

        actual_output = test_instance.process_sentence(input_data) 

        self.assertEqual(actual_output, expected_output)

    def test_exposure_example_obj_proper(self):
        
        input_data = self.train[29495]  

        # sentence = The creature grew Charlie .

        conversion = {'form': ['the', 'creature', 'grew', 'Charlie', '.'], 'lemma': ['the', 'creature', 'grow', 'Charlie', '.'], 'pos':['DET', 'NOUN', 'VERB', 'PROPN', 'PUNCT'], 'head':[1, 2, 0, 2, 2], 'deprel': ['det', 'nsubj', 'root', 'obj', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        test_instance = DissertationModule()

        actual_output = test_instance.process_sentence(input_data) 

        self.assertEqual(actual_output, expected_output)

    def test_exposure_example_subj_proper(self):
        
        input_data = self.train[29541]  

        # sentence = Lina gave the cake beside a stage to Olivia .

        conversion = {'form': ['Lina', 'gave', 'the', 'cake', 'beside', 'a', 'stage', 'to', 'Olivia', '.'], 'lemma': ['Lina', 'give', 'the', 'cake', 'beside', 'a', 'stage', 'to', 'Olivia', '.'], 'pos':['PROPN', 'VERB', 'DET', 'NOUN', 'ADP', 'DET', 'NOUN', 'ADP', 'PROPN', 'PUNCT'], 'head':[1, 0, 3, 1, 6, 6, 3, 8, 1, 1], 'deprel': ['nsubj', 'root', 'det', 'obj', 'case', 'det', 'nmod:beside', 'case', 'iobj', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        test_instance = DissertationModule()

        actual_output = test_instance.process_sentence(input_data) 

        self.assertEqual(actual_output, expected_output)

        # --------- The next set of tests are from the generalisation dataset -------- #

    def test_PP_modif_subj(self):
        
        input_data = self.gen[6001]  

        # sentence = The baby beside the seat helped a cake in a house .

        conversion = {'form': ['the', 'baby', 'beside', 'the', 'seat', 'helped', 'a', 'cake', 'in', 'a', 'house' '.'], 'lemma': ['the', 'baby', 'beside', 'the', 'seat', 'help', 'a', 'cake', 'in', 'a', 'house', '.'], 'pos':['DET', 'NOUN', 'ADP', 'DET', 'NOUN', 'VERB', 'DET', 'NOUN', 'ADP', 'DET', 'NOUN', 'PUNCT'], 'head':[1, 5, 4, 4, 1, 0, 7, 5, 10, 10, 7, 5], 'deprel': ['det', 'nsubj', 'case', 'det', 'nmod:beside', 'root', 'det', 'obj', 'case', 'det', 'nmod:in', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        test_instance = DissertationModule()

        actual_output = test_instance.process_sentence(input_data) 

        self.assertEqual(actual_output, expected_output)

    def test_PP_modif_iobj(self):
        
        input_data = self.gen[7001]  

        # sentence = A cake was passed to a passenger beside a tree by the boy .

        conversion = {'form': ['a', 'cake', 'was', 'passed', 'to', 'a', 'passenger', 'beside', 'a', 'tree', 'by', 'the', 'boy', '.'], 'lemma': ['a', 'cake', 'be', 'pass', 'to', 'a', 'passenger', 'beside', 'a', 'tree', '.'], 'pos':['DET', 'NOUN', 'AUX', 'VERB', 'ADP', 'DET', 'NOUN', 'ADP', 'DET', 'NOUN', 'ADP', 'DET', 'NOUN', 'PUNCT'], 'head':[1, 3, 3, 0, 6, 6, 3, 9, 9, 6, 12, 12, 3, 3], 'deprel': ['det', 'nsubj', 'aux:pass', 'root', 'case', 'det', 'iobj', 'case', 'det', 'nmod:beside', 'case', 'det', 'obl:agent', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        test_instance = DissertationModule()

        actual_output = test_instance.process_sentence(input_data) 

        self.assertEqual(actual_output, expected_output)

    def test_RC_modif_subj(self):
        
        input_data = self.gen[8001]  

        # sentence = A cake that Liam found was investigated by the cat .

        conversion = {'form': ['a', 'cake', 'that', 'Liam', 'found', 'was', 'investigated', 'by', 'the', 'cat', '.'], 'lemma': ['a', 'cake', 'that', 'Liam', 'find', 'be', 'investigate', 'by', 'the', 'cat', '.'], 'pos':['DET', 'NOUN', 'SCONJ', 'PROPN', 'VERB', 'AUX', 'VERB', 'ADP', 'DET', 'NOUN', 'PUNCT'], 'head':[1, 6, 4, 4, 1, 6, 0, 9, 9, 6, 6], 'deprel': ['det', 'nsubj', 'mark', 'nsubj', 'acl:relcl', 'aux:pass', 'root', 'case', 'det', 'obl:agent', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        test_instance = DissertationModule()

        actual_output = test_instance.process_sentence(input_data) 

        self.assertEqual(actual_output, expected_output)

    def test_RC_modif_iobj(self):
        
        input_data = self.gen[9001]  

        # sentence = Emma gave a bird that was lent the cookie a cake .

        conversion = {'form': ['Emma', 'gave', 'a', 'bird', 'that', 'was', 'lent', 'the', 'cookie', 'a', 'cake', '.'], 'lemma': ['Emma', 'give', 'a', 'bird', 'that', 'be', 'lend', 'the', 'cookie', 'a', 'cake', '.'], 'pos':['PROPN', 'VERB', 'DET', 'NOUN', 'SCONJ', 'AUX', 'VERB', 'DET', 'NOUN', 'DET', 'NOUN', 'PUNCT'], 'head':[1, 0, 3, 1, 6, 6, 3, 8, 6, 10, 1, 1], 'deprel': ['nsubj', 'root', 'det', 'iobj', 'mark', 'aux:pass', 'acl:relcl', 'det', 'obj', 'det', 'obj', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        test_instance = DissertationModule()

        actual_output = test_instance.process_sentence(input_data) 

        self.assertEqual(actual_output, expected_output)

    def test_RC_iobj_extracted(self):
        
        input_data = self.gen[10001]  

        # sentence = Ella cooked the servant that Emma gave a tool to .

        conversion = {'form': ['Ella', 'cooked', 'the', 'servant', 'that', 'Emma', 'gave', 'a', 'tool', 'to', '.'], 'lemma': ['Ella', 'cook', 'the', 'servant', 'that', 'Emma', 'give', 'a', 'tool', 'to', '.'], 'pos':['PROPN', 'VERB', 'DET', 'NOUN', 'SCONJ', 'PROPN', 'VERB', 'DET', 'NOUN', 'ADP', 'PUNCT'], 'head':[1, 0, 3, 1, 6, 6, 3, 8, 6, 3, 1], 'deprel': ['nsubj', 'root', 'det', 'obj', 'mark', 'nsubj', 'acl:relcl', 'det', 'obj', 'case', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        test_instance = DissertationModule()

        actual_output = test_instance.process_sentence(input_data) 

        self.assertEqual(actual_output, expected_output)

    def test_Q_subj_active(self):
        
        input_data = self.gen[11001]  

        # sentence = Who hated to dust ?

        conversion = {'form': ['who', 'hated', 'to', 'dust', '?'], 'lemma': ['who', 'hate', 'to', 'dust', '?'], 'pos':['PRON', 'VERB', 'PART', 'VERB', 'PUNCT'], 'head':[1, 0, 3, 1, 1], 'deprel': ['nsubj', 'root', 'mark', 'xcomp', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        test_instance = DissertationModule()

        actual_output = test_instance.process_sentence(input_data) 

        self.assertEqual(actual_output, expected_output)

    def test_Q_subj_passive(self):
        
        input_data = self.gen[12001]  

        # sentence = What was admired by Liam ?

        conversion = {'form': ['what', 'was', 'admired', 'by', 'Liam', '?'], 'lemma': ['what', 'be', 'admire', 'by', 'Liam', '?'], 'pos':['PRON', 'AUX', 'VERB', 'ADP', 'PROPN', 'PUNCT'], 'head':[2, 2, 0, 4, 2, 2], 'deprel': ['nsubj', 'aux:pass', 'root', 'case', 'obl:agent', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        test_instance = DissertationModule()

        actual_output = test_instance.process_sentence(input_data) 

        self.assertEqual(actual_output, expected_output)

    def test_Q_dobj_ditransV(self):
        
        input_data = self.gen[13001]  

        # sentence = What did Liam give Owen ?

        conversion = {'form': ['what', 'did', 'Liam', 'give', 'Owen', '?'], 'lemma': ['what', 'do', 'Liam', 'give', 'Owen', '?'], 'pos':['PRON', 'AUX', 'PROPN', 'VERB', 'PROPN', 'PUNCT'], 'head':[3, 3, 3, 0, 3, 3], 'deprel': ['obj', 'aux', 'nsubj', 'root', 'iobj', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        test_instance = DissertationModule()

        actual_output = test_instance.process_sentence(input_data) 

        self.assertEqual(actual_output, expected_output)

    def test_Q_iobj_ditransV(self):
        
        input_data = self.gen[14001]  

        # sentence = Who did Emma give the cake to ?

        conversion = {'form': ['who', 'did', 'Emma', 'give', 'the', 'cake', 'to', '?'], 'lemma': ['who', 'do', 'Emma', 'give', 'the', 'cake', 'to', '?'], 'pos':['PRON', 'AUX', 'PROPN', 'VERB', 'DET', 'NOUN', 'ADP', 'PUNCT'], 'head':[3, 3, 3, 0, 5, 3, 0, 3], 'deprel': ['iobj', 'aux', 'nsubj', 'root', 'det', 'obj', 'case', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        test_instance = DissertationModule()

        actual_output = test_instance.process_sentence(input_data) 

        self.assertEqual(actual_output, expected_output)

    def test_Q_modified_NPs(self):
        
        input_data = self.gen[15001]  

        # sentence = Who cleaned a cake beside a car ?

        conversion = {'form': ['who', 'cleaned', 'a', 'cake', 'beside', 'a', 'car', '?'], 'lemma': ['who', 'cleaned', 'a', 'cake', 'beside', 'a', 'car', '?'], 'pos':['PRON', 'VERB', 'DET', 'NOUN', 'ADP', 'DET', 'NOUN', 'PUNCT'], 'head':[1, 0, 3, 1, 6, 6, 3, 3], 'deprel': ['nsubj', 'root', 'det', 'obj', 'case', 'det', 'nmod:beside', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        test_instance = DissertationModule()

        actual_output = test_instance.process_sentence(input_data) 

        self.assertEqual(actual_output, expected_output)

    def test_Q_long_mv(self):
        
        input_data = self.gen[16001]  

        # sentence = Who did a governor hope that William froze ?

        conversion = {'form': ['who', 'did', 'a', 'governor', 'hope', 'that', 'William', 'froze', '?'], 'lemma': ['who', 'do', 'a', 'governor', 'hope', 'that', 'William', 'freeze', '?'], 'pos':['PRON', 'AUX', 'DET', 'NOUN', 'VERB', 'SCONJ', 'PROPN', 'VERB', 'PUNCT'], 'head':[7, 4, 3, 4, 0, 7, 7, 4, 4], 'deprel': ['obj', 'aux', 'det', 'nsubj', 'root', 'mark', 'nsubj', 'ccomp', 'punct']}


        expected_output = pd.DataFrame(conversion)  

        test_instance = DissertationModule()

        actual_output = test_instance.process_sentence(input_data) 

        self.assertEqual(actual_output, expected_output)


# Run the tests
if __name__ == '__main__':
    unittest.main()