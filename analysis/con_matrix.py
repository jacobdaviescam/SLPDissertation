import matplotlib.pyplot as plt
import seaborn as sn
import pandas as pd

# Your confusion matrix data
confusion_matrix = [
    ["-", 0, 134, 0, 209, 0, 2, 0, 0, 0, 0, 105, 142, 0, 0, 0, 0, 0, 0, "acl:relcl"],
    [141, "-", 0, 16, 0, 92, 0, 0, 0, 0, 7, 95, 0, 0, 0, 0, 0, 0, 0, "aux"],
    [0, 0, "-", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "aux:pass"],
    [0, 15, 9, "-", 0, 0, 737, 576, 0, 0, 0, 0, 1, 8, 1038, 0, 0, 0, 0, "case"],
    [61, 0, 1, 14, "-", 0, 3, 0, 3, 0, 3, 2, 0, 3, 1, 0, 0, 6, 0, "ccomp"],
    [0, 0, 0, 0, 0, "-", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "det"],
    [0, 0, 0, 0, 0, 0, "-", 0, 0, 0, 0, 0, 21, 1167, 0, 1, 0, 8, 0, "iobj"],
    [0, 0, 0, 3, 0, 0, 0, "-", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "mark"],
    [0, 0, 0, 88, 0, 0, 2, 0, "-", 17, 231, 163, 145, 13, 37, 8, 0, 0, 0, "nmod:beside"],
    [0, 0, 0, 24, 0, 0, 0, 0, 153, "-", 143, 273, 151, 0, 36, 0, 0, 0, 0, "nmod:in"],
    [0, 0, 0, 55, 0, 0, 10, 0, 43, 0, "-", 277, 162, 22, 28, 22, 0, 0, 0, "nmod:on"],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, "-", 182, 7, 0, 6, 0, 1261, 0, "nsubj"],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 3, 23, "-", 17, 0, 1, 0, 825, 0, "nsubj:pass"],
[109, 3, 0, 1, 0, 0, 219, 0, 167, 82, 165, 254, 65, "-", 16, 250, 0, 0, 0, "obj"],
[0, 0, 0, 15, 0, 3, 0, 0, 0, 15, 0, 5, 6, 0, "-", 0, 0, 0, 0, "obl:agent"],
[49, 0, 0, 4, 0, 2, 36, 0, 2, 0, 22, 146, 87, 1154, 2, "-", 0, 0, 413, "obl:to"],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "-", 0, 0, "punct"],
[1181, 0, 8, 101, 194, 0, 150, 0, 179, 2, 61, 1, 0, 107, 85, 6, "-", 19, "root"],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 22, 2, 0, 1, 9, 0, 0, 0, "-", "xcomp"]]

# Extract the labels and values from the confusion matrix
labels = [row[-1] for row in confusion_matrix]
values = [[float(val) if val != "-" else 0.0 for val in row[0:-1]] for row in confusion_matrix]

df_cm = pd.DataFrame(values, labels, labels)
plt.figure(figsize=(10,7))
sn.heatmap(df_cm, annot=True, fmt='g')

plt.show()

# Create a figure and axis
# fig, ax = plt.subplots()

# # Plot the confusion matrix
# im = ax.imshow(values, cmap="Blues")

# # Add colorbar
# cbar = ax.figure.colorbar(im, ax=ax)

# # Set the tick labels and positions
# ax.set_xticks(range(len(labels)))
# ax.set_yticks(range(len(labels)))
# ax.set_xticklabels(labels, rotation=90)
# ax.set_yticklabels(labels)

# # Loop over data dimensions and create text annotations
# for i in range(len(labels)):
#     for j in range(len(labels)):
#         text = ax.text(j, i, values[i][j], ha="center", va="center", color="w")

# # Set the title and show the plot
# ax.set_title("Confusion Matrix")
# plt.show()