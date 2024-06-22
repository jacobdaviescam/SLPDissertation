import csv

with open('/Users/jacobdavies/Dissertation/SLOG/data/cogs_LF/train.tsv', 'r') as file:
    lines = file.readlines()
    values = [line.split('\t')[2].strip() for line in lines]
    print(set(values))
