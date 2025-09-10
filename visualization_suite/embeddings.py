import csv
import re
import pandas as pd

# Define the input file paths
train_file = 'train.tsv'
dev_file = 'dev.tsv'
test_file = 'test.tsv'
gen_cogsLF_file = 'gen_cogsLF.tsv'

# Define the output file path
output_file = 'allfiles.tsv'

# Define a function to load data from a file and return a dictionary
def load_data(infile):
    data = {}
    with open(infile, 'r') as tsvfile:
        filename = infile.split('/')[-1].split('.')[0]
        reader = csv.reader(tsvfile, delimiter='\t')
        sentence_id = 1
        for row in reader:
            if row:
                sentence = row[0]
                # semantics = row[1]
                # distribution = row[2]
                data[f'{filename}_{sentence_id}'] = {'sentence': sentence}
                sentence_id += 1
    return data

# Load data from each input file
train_data = load_data(train_file)
dev_data = load_data(dev_file)
test_data = load_data(test_file)
gen_cogsLF_data = load_data(gen_cogsLF_file)

# Combine all the data into one dictionary
output = {**train_data, **dev_data, **test_data, **gen_cogsLF_data}

# Write the combined data to the output file
with open(output_file, 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    for sentence_id, sentence_data in output.items():
        sentence = sentence_data['sentence']
        # semantics = sentence_data['semantics']
        # distribution = sentence_data['distribution']
        writer.writerow([sentence_id, sentence])


# output = {}

# def load_data(infile1, infile2, outfile):
#         with open(infile1, 'r') as tsvfile:
#             reader = csv.reader(tsvfile, delimiter='\t')
#             sentence_id = 1
#             for row in reader:
#                 if row:
#                     sentence = row[0]
#                     semantics = row[1]
#                     distribution = row[2]
#                     output[sentence_id] = {'sentence': sentence, 'semantics': semantics, 'distribution': distribution}
#                     sentence_id += 1

#         with open(infile2, 'r') as tsvfile:
#             reader = csv.reader(tsvfile, delimiter='\t')
#             for row in reader:
#                 if row:
#                     sentence = row[0]
#                     semantics = row[1]
#                     distribution = row[2]
#                     output[sentence_id]['sentence'] = sentence
#                     output[sentence_id]['semantics'] = semantics
#                     output[sentence_id]['distribution'] = distribution
#                     sentence_id += 1


#         with open(outfile, 'w') as f:
             