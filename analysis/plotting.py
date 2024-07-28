import pandas as pd
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------- #
#                              ArcDepth Precision                              #
# ---------------------------------------------------------------------------- #

# data = {
#     'Transition': [0.868, 0.921, 0.895, 0.868, 0.867, 0.917, 0.96, 0.99, 0.997, 0.998, 0.999],
#     'Graph':[0.877, 0.902, 0.836, 0.791, 0.78, 0.611, 0.458, 0.429, 0.352, 0.26, 0.228, ],
#     'ArcDepth': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# }
# df = pd.DataFrame(data)

# plt.plot(df['ArcDepth'], df['Transition'], label='Transition-Based Parser')
# plt.plot(df['ArcDepth'], df['Graph'], label='Graph-Based Parser')

# plt.xlabel('Arc Depth')
# plt.ylabel('Precision')
# plt.title('Precision vs Arc Depth')

# plt.legend()
# plt.savefig('analysis/figures/precision.pdf')

# ----------  parsercount for different arcdepths ---------- #
# graphparsercount = [16999, 60464, 49641, 35088, 25365, 21362, 18575, 13279, 8839, 6468, 4351, 3050, 1419, 878, 67, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# transitionparsercount = [16999, 61208, 47835, 34172, 24151, 15943, 11493, 10324, 7934, 6570, 5789, 4952, 3949, 3080, 2080, 1596, 1306, 1250, 1045, 1000, 794, 750, 551, 500, 291, 250, 33]
# ArcDepth = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

# plt.figure()
# plt.plot(ArcDepth, transitionparsercount, label='Transition-Based Parser')
# plt.plot(ArcDepth, graphparsercount, label='Graph-Based Parser')


# plt.xlabel('Arc Depth')
# plt.ylabel('Parser Count')
# plt.title('Parser Count vs Arc Depth')

# plt.legend()
# plt.savefig('analysis/figures/parsercount.pdf')

# ---------------------------------------------------------------------------- #
#                                ArcDepth Recall                               #
# ---------------------------------------------------------------------------- #
# transitionrecall = [0.868, 0.905, 0.843, 0.868, 0.954, 0.994, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# graphrecall = [0.877, 0.875, 0.817, 0.813, 0.902, 0.888, 0.771, 0.558, 0.394, 0.257, 0.172, 0.115, 0.033, 0.005, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ArcDepth = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

# plt.figure()
# plt.plot(ArcDepth, transitionrecall, label='Transition-Based Parser')
# plt.plot(ArcDepth, graphrecall, label='Graph-Based Parser')


# plt.xlabel('Arc Depth')
# plt.ylabel('Recall')
# plt.title('Recall vs Arc Depth')

# plt.legend()
# plt.savefig('analysis/figures/recall.pdf')


# data = {
#     'Accuracy': [1, 1, 1, 0.999, 0.95, 0.836, 0.742, 0.767, 0.86, 0.945, 0.987, 0.996, 1, 1],
#     'Precision':[1, 1, 1, 0.999, 0.949, 0.796, 0.622, 0.557, 0.513, 0.453, 0.375, 0.317, 0.289, 0.25],
#     'ArcDepth': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# }
# df = pd.DataFrame(data)

# plt.plot(df['ArcDepth'], df['Accuracy'], label='Parser Accuracy')
# plt.plot(df['ArcDepth'], df['Precision'], label='Treebank Accuracy')

# plt.xlabel('Arc Depth')
# plt.ylabel('Accuracy')
# plt.title('Accuracy vs Arc Depth')

# plt.legend()
# plt.show()

# ---------------------------------------------------------------------------- #
#                  PP deeper generalisation ArcDepth accuracy                  #
# ---------------------------------------------------------------------------- #

PP_UAS = [100, 100, 100, 99.9, 95.0, 83.6, 74.2, 76.7, 86.0, 94.5, 98.7, 99.6, 100, 100]
CP_UAS = [1, 1, 0.957, 0.668, 0.481, 0.595, 0.809, 0.992, 1, 1, 1, 1, 1, 1]
CE_UAS = [1, 1, 1, 0.981, 0.983, 0.359, 0.412, 0.176, 0.955, 0.981, 1, 1, 1, 1]
ArcDepth = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

CP_UAS = [x *100 for x in CP_UAS if x is not None]
CE_UAS = [x * 100 for x in CE_UAS]

plt.plot(ArcDepth, PP_UAS, label='PP')
plt.plot(ArcDepth, CP_UAS, label='CP')
plt.plot(ArcDepth, CE_UAS, label='CE')


plt.xlabel('Arc Depth')
plt.ylabel('Accuracy')
plt.title('Accuracy vs Arc Depth')

plt.legend()
plt.show()
# plt.savefig('analysis/figures/graph_accuracy_arcdepth_pp_5-12.pdf')

# ---------------------------------------------------------------------------- #
#                                Sentence Length                               #
# ---------------------------------------------------------------------------- #

# transition = [1, 1, 1, 0.943, 0.847, 0.828, 0.803, 0.825, 0.873, 0.876, 0.874, 0.924, 0.962, 0.949, 0.975, 0.99, 0.921, 0.978, 0.959, 0.96, 0.977, 0.996]

# sentence_length = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

# ---------------------------------------------------------------------------- #
#                           F1-Score Distance to Root                          #
# ---------------------------------------------------------------------------- #

# transitionfscore = [0.868, 0.913, 0.868, 0.868, 0.908, 0.954, 0.979, 0.995, 0.999, 0.999, 0.999]
# graphfscore = [0.877, 0.888, 0.826, 0.801, 0.836, 0.724, 0.575, 0.485, 0.372, 0.258, 0.196]
# ArcDepth = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# plt.plot(ArcDepth, transitionfscore, label='Transition-Based Parser')
# plt.plot(ArcDepth, graphfscore, label='Graph-Based Parser')

# plt.xlabel('Arc Depth')
# plt.ylabel('F1-Score')
# plt.title('F1-Score vs Arc Depth')

# plt.legend()
# plt.savefig('analysis/figures/f1score.pdf')
# # plt.show()

# ---------------------------------------------------------------------------- #
#                           F-Score Dependency Length                          #
# ---------------------------------------------------------------------------- #

# transitionfscore = [0.868, 0.976, 0.973, 0.955, 0.91, 0.793, 0.629, 0.716, 0.857, 0.882, 0.896, 0.924, 0.95, 0.947, 0.967, 0.975, 0.991, 0.933, 0.994, 0.995, 0.99, 0.991, 0.999, 1, 0.998, 0.998, 1, 1, 0.999, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# graphfscore = [0.877, 0.962, 0.9, 0.878, 0.846, 0.607, 0.529, 0.644, 0.757, 0.739, 0.8, 0.885, 0.811, 0.55, 0.741, 0.791, 0.434, 0.255, 0.373, 0.4, 0.371, 0.354, 0.4, 0.397, 0.428, 0.348, 0.483, 0.496, 0.441, 0.416, 0.614, 0.505, 0.534, 0.635, 0.65, 0.611, 0.74, 0.681, 0.828, 0.778, 0.88, 0.928, 0.986, 0.982, 0.979]

# relation_length = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]

# plt.plot(relation_length, transitionfscore, label='Transition-Based Parser')
# plt.plot(relation_length, graphfscore, label='Graph-Based Parser')

# plt.xlabel('Relation Length')
# plt.ylabel('F1-Score')
# plt.title('F1-Score vs Relation Length')

# plt.legend()
# # plt.show()
# plt.savefig('analysis/figures/f1score_relation_length.pdf')

# ---------------------------------------------------------------------------- #
#                          Accuracies on different PoS                         #
# ---------------------------------------------------------------------------- #

# import matplotlib.pyplot as plt

# transitionposaccuracy = [0.883, 0.959, 1, 0.907, 1, 0.614, 0.964, 0.866, 0.994, 0.942]
# graphposaccuracy = [0.761, 0.942, 0.959, 0.793, 0.967, 0.592, 0.911, 0.967, 0.756, 0.833]
# Cpostag = ['ADP', 'AUX', 'DET', 'NOUN', 'PART', 'PRON', 'PROPN', 'PUNCT', 'SCONJ', 'VERB']

# N = 10

# plt.figure()
# width = 0.35

# ind = np.arange(N)

# plt.bar(ind, transitionposaccuracy, width, label='Transition-Based Parser')
# plt.bar(ind+width, graphposaccuracy, width, label='Graph-Based Parser')

# plt.xlabel('Part-of-Speech')
# plt.ylabel('Accuracy')
# plt.title('Accuracy on Different Part-of-Speech')

# plt.xticks(ind + width / 2, ('ADP', 'AUX', 'DET', 'NOUN', 'PART', 'PRON', 'PROPN', 'PUNCT', 'SCONJ', 'VERB'))

# plt.legend(loc='best')
# # plt.show()
# plt.savefig('analysis/figures/pos_accuracy.pdf')

# ---------------------------------------------------------------------------- #
#                 Accuracies on different dependency relations                 #
# ---------------------------------------------------------------------------- #

# transitiondepsfscore = [0.976, 0.957, 0.98, 0.989, 0.984, 0.999, 0.594, 0.994, 0.94, 0.931, 0.906, 0.971, 0.816, 0.883, 0.936, 0.814, 0.993, 0.875, 0.853]
# graphdepsfscore = [0.931, 0.946, 0.983, 0.94, 0.982, 0.999, 0.423, 0.99, 0.872, 0.911, 0.877, 0.965, 0.775, 0.869, 0.941, 0.656, 1, 0.877, 0.624]
# deprel = ['acl:relcl', 'aux', 'aux:pass', 'case', 'ccomp', 'det', 'iobj', 'mark', 'nmod:beside', 'nmod:in', 'nmod:on', 'nsubj', 'nsubj:pass', 'obj', 'obl:agent', 'obl:to', 'punct', 'root', 'xcomp']

# print("\\begin{table}[htbp]")
# print("\\centering")
# print("\\begin{tabular}{|c|c|c|}")
# print("\\hline")
# print("Dependency Relation & Transition-Based Parser & Graph-Based Parser \\\\")
# print("\\hline")
# for i in range(len(deprel)):
#     print(f"{deprel[i]} & {transitiondepsfscore[i]} & {graphdepsfscore[i]} \\\\")
# print("\\hline")
# print("\\end{tabular}")
# print("\\caption{F1-Score on Different Dependency Relations}")
# print("\\label{tab:dependency_relations}")
# print("\\end{table}")

# N = 19

# plt.figure()

# width = 0.35

# ind = np.arange(N)

# plt.bar(ind, transitiondepsfscore, width, label='Transition-Based Parser')
# plt.bar(ind+width, graphdepsfscore, width, label='Graph-Based Parser')

# plt.xlabel('Dependency Relation')
# plt.ylabel('F1-Score')
# plt.title('F1-Score on Different Dependency Relations')

# plt.xticks(ind + width / 2, ('acl:relcl', 'aux', 'aux:pass', 'case', 'ccomp', 'det', 'iobj', 'mark', 'nmod:beside', 'nmod:in', 'nmod:on', 'nsubj', 'nsubj:pass', 'obj', 'obl:agent', 'obl:to', 'punct', 'root', 'xcomp'))

# plt.legend(loc='best')
# plt.show()
# plt.savefig('analysis/figures/deprel_f1score.pdf')

