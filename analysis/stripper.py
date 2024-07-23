import os

def strip_comments_from_file(filename):
    """Strip lines starting with '#' from the given file."""
    infile = filename.split('/')[-1].split('.')[0]
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    with open(f'{infile}_stripped.conllu', 'w', encoding='utf-8') as file:
        for line in lines:
            if not line.startswith('#'):
                file.write(line)

def main():
    # Get the list of files in the output/generalisation_sets directory
    directory = '/Users/jacobdavies/SLPDissertation/output/parser/transition_generalisation_sets/randinit2'
    files_to_strip = [os.path.join(directory, filename) for filename in os.listdir(directory)]

    # Call the strip_comments_from_file function for each file
    for filename in files_to_strip:
        strip_comments_from_file(filename)
        print(f"Comments stripped from {filename}")


if __name__ == "__main__":
    main()