import random

# Path to the original file
original_file = '/Users/jacobdavies/SLPDissertation/UD_English-GUM/en_gum-ud-test.conllu'

# Path to the subset file
subset_file = '/Users/jacobdavies/SLPDissertation/UD_English-GUM/en_gum-ud-test-subset.conllu'

# Percentage of data to include in the subset (e.g., 50%)
subset_percentage = 5

# Read the original file
with open(original_file, 'r') as f:
    lines = f.readlines()

# Calculate the number of lines to include in the subset
num_lines = int(len(lines) * (subset_percentage / 100))

# Randomly select lines for the subset
subset_lines = lines[:num_lines]

# Write the subset to the subset file
with open(subset_file, 'w') as f:
    f.writelines(subset_lines)

print(f'Subset created with {num_lines} lines in {subset_file}')