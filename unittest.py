import unittest
import csv
import pandas as pd

from conversion import DissertationModule  # Replace "YourClass" with the actual class name from attempt.py

class TestYourClass(unittest.TestCase):

    def __init__(self):

        with open('SLOG/data/cogs_LF/train.tsv', 'r') as tsvfile:
            reader = csv.reader(tsvfile, delimiter='\t')
            self.output = {}
            sentence_id = 1
            for row in reader:
                if row:
                    sentence = row[0]
                    semantics = row[1]
                    distribution = row[2]
                    self.output[sentence_id] = {'sentence': sentence, 'semantics': semantics, 'distribution': distribution}
                    sentence_id += 1

    def test_case_1(self):
        # Test case 1
        # Define the input for the test case
        input_data = self.output[9]  # Replace "input_data" with the actual input data for the test case

        # Define the expected output for the test case

        conversion = {'form': ['a', 'boy', 'painted', 'a', 'child', '.'], 'lemma': ['a', 'boy', 'paint', 'a', 'child', '.'], 'head':[1, 2, 0, 4, 2, 2], 'deprel': ['det', 'nsubj', 'root', 'det', 'obj', 'punct']}


        expected_output = pd.DataFrame(conversion)  # Replace "expected_output" with the actual expected output for the test case

        # Create an instance of YourClass
        test_instance = DissertationModule()

        # Call the method or function to be tested
        actual_output = test_instance.process_sentence(input_data) # Replace "your_method" with the actual method or function to be tested

        # Assert that the actual output matches the expected output
        self.assertEqual(actual_output, expected_output)

    # def test_case_2(self):
    #     # Test case 2
    #     # Define the input for the test case
    #     input_data = "input_data"  # Replace "input_data" with the actual input data for the test case

    #     # Define the expected output for the test case
    #     expected_output = "expected_output"  # Replace "expected_output" with the actual expected output for the test case

    #     # Create an instance of YourClass
    #     your_instance = YourClass()

    #     # Call the method or function to be tested
    #     actual_output = your_instance.your_method(input_data)  # Replace "your_method" with the actual method or function to be tested

    #     # Assert that the actual output matches the expected output
    #     self.assertEqual(actual_output, expected_output)

# Run the tests
if __name__ == '__main__':
    unittest.main()