import csv

phenomena = {}

with open('/Users/jacobdavies/Dissertation/SLOG/data/cogs_LF/train.tsv', 'r') as file:
    lines = file.readlines()

    for line in lines:
        sentence, semantics, distribution = line.split('\t')
        if distribution not in phenomena:
            phenomena[distribution] = [sentence, semantics]


with open('/Users/jacobdavies/SLPDissertation/gen_cogsLF.tsv', 'r') as file:
    lines = file.readlines()
    for line in lines:
        sentence, semantics, distribution = line.split('\t')
        if distribution not in phenomena:
            phenomena[distribution] = [sentence, semantics]
    for distribution, data in phenomena.items():
        with open('/Users/jacobdavies/SLPDissertation/unit-tests.txt', 'w') as file:
            for distribution, data in phenomena.items():
                file.write(f"{distribution}\n")
                file.write(f"{data[0]}\n")
                file.write(f"{data[1]}\n")
                file.write("\n")
