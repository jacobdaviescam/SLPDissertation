import csv
import re
import pandas as pd

def load_data(filename):
    with open(filename, 'r') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        check = re.compile(r' to .')
        ditransitives = re.compile(r'recipient')
        sentence_id = 1
        for row in reader:
            if row:
                sentence = row[0]
                semantics = row[1]
                if check.search(sentence):
                    if len(ditransitives.findall(semantics)) > 1:
                        with open('to_sentences.txt', 'w') as writefile:
                            writefile.write(f'{sentence_id}')
                            writefile.write(sentence)
                            writefile.write('\n')

            sentence_id += 1
                            
load_data('gen_cogsLF.tsv')

