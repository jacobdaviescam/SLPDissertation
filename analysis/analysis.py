import conllu
from conllu import parse

def subset_generalisation(filename):

    with open(filename, 'r') as f:
        data = f.read()
        sentences = parse(data)
        distributions = {}
        for sentence in sentences:
            distribution = sentence.metadata['distribution']
            if distribution not in distributions:
                distributions[distribution] = [sentence]
            else:
                distributions[distribution].append(sentence)

    for distribution in distributions:
        with open(f'{distribution}.conllu', 'w') as f:
            for sentence in distributions[distribution]:
                f.write(sentence.serialize())

def main():
    subset_generalisation('output/generalisation/out.conllu')

if __name__ == "__main__":
    main()

