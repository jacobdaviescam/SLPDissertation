import pandas as pd

def read_conllu(file_path):
    """Reads a CoNLL-U file and returns a list of sentences, where each sentence is a DataFrame."""
    sentences = []
    current_sentence = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip() == "":
                if current_sentence:
                    sentences.append(pd.DataFrame(current_sentence))
                    current_sentence = []
            elif line.startswith("#"):
                continue
            else:
                columns = line.strip().split("\t")
                if "-" not in columns[0]:  # Skip multiword tokens
                    current_sentence.append(columns)
        # Add the last sentence if the file doesn't end with a newline
        if current_sentence:
            sentences.append(pd.DataFrame(current_sentence))
    return sentences

def compare_heads(file1, file2):
    """Compares the 'HEAD' column of sentences in two CoNLL-U files."""
    sentences1 = read_conllu(file1)
    sentences2 = read_conllu(file2)

    with open('analysis_heads.txt', 'w') as f:
    
        for i, (sent1, sent2) in enumerate(zip(sentences1, sentences2)):
            # Assuming column 6 is 'HEAD'. Adjust index if necessary.
            if not sent1[6].equals(sent2[6]):


                    f.write(f"Sentence {i+1} differs.\n")
                    f.write(f"File 1 Sentence {i+1} HEADs: {sent1[6].tolist()}\n")
                    f.write(f"File 2 Sentence {i+1} HEADs: {sent2[6].tolist()}\n\n")

    # with open('analysis_dist.txt', 'w') as f:

    #     for i, (sent1, sent2) in enumerate(zip(sentences1, sentences2)):
    #         # Assuming column 6 is 'HEAD'. Adjust index if necessary.
    #         if not sent1[6].equals(sent2[6]):
    #             f.write(f"{i+1}\n")

# Paths to the CoNLL-U files
file1 = 'output/subset_debug/out.conllu'
file2 = 'UD_SLOG/slog-subset-ud-test.conllu'

# Compare the 'HEAD' columns
compare_heads(file1, file2)

