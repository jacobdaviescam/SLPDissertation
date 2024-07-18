def strip_comments_from_file(filename):
    """Strip lines starting with '#' from the given file."""
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    with open(f'{filename}_stripped', 'w', encoding='utf-8') as file:
        for line in lines:
            if not line.startswith('#'):
                file.write(line)

def main():
    files_to_strip = ['UD_SLOG/slog-ud-test.conllu', 'output/test_set/out.conllu']
    for filename in files_to_strip:
        strip_comments_from_file(filename)
        print(f"Comments stripped from {filename}")

if __name__ == "__main__":
    main()