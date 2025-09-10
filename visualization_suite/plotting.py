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

# PP_UAS = [100, 100, 100, 99.9, 95.0, 83.6, 74.2, 76.7, 86.0, 94.5, 98.7, 99.6, 100, 100]
# CP_UAS = [1, 1, 0.957, 0.668, 0.481, 0.595, 0.809, 0.992, 1, 1, 1, 1, 1, 1]
# CE_UAS = [1, 1, 1, 0.981, 0.983, 0.359, 0.412, 0.176, 0.955, 0.981, 1, 1, 1, 1]
# ArcDepth = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# CP_UAS = [x *100 for x in CP_UAS if x is not None]
# CE_UAS = [x * 100 for x in CE_UAS]

# plt.plot(ArcDepth, PP_UAS, label='PP')
# plt.plot(ArcDepth, CP_UAS, label='CP')
# plt.plot(ArcDepth, CE_UAS, label='CE')


# plt.xlabel('Arc Depth')
# plt.ylabel('Accuracy')
# plt.title('Accuracy vs Arc Depth')

# plt.legend()
# plt.show()
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

# ---------------------------------------------------------------------------- #
#                             POS Sentence Length                             #
# ---------------------------------------------------------------------------- #

# graphsentencelength = [1, 1, 1, 0.954, 0.879, 0.831, 0.809, 0.778, 0.832, 0.842, 0.848, 0.921, 0.954, 0.948, 0.977, 0.989, 0.926, 0.978, 0.978, 0.967, 0.960, 0.979, 0.998, 1, 0.993, 0.995, 0.988, 0.985, 0.988, 0.99, 0.937, 0.939, 0.948, 0.918, 0.858, 0.826, 0.849, 0.863, 0.770, 0.735, 0.784, 0.789, 0.701, 0.690, 0.732, 0.762, 0.613, 0.597, 0.650]
# # print(len(graphsentencelength))
# transitionsentencelength = [1, 0.775, 1, 0.951, 0.846, 0.829, 0.778, 0.85, 0.874, 0.855, 0.879, 0.935, 0.962, 0.949, 0.980, 0.991, 0.921, 0.982, 0.970, 0.958, 0.981, 0.998, 1, 0.995, 0.997, 1, 1, 0.996, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# # print(len(transitionsentencelength))
# sentencelength = [i for i in range(3,52)]
# # print(len(sentencelength))

# plt.plot(sentencelength, graphsentencelength, label='Graph-Based Parser')
# plt.plot(sentencelength, transitionsentencelength, label='Transition-Based Parser')

# plt.xlabel('Sentence Length')
# plt.ylabel('Accuracy')

# plt.legend()
# plt.show()

# ---------------------------------------------------------------------------- #
#                              POS RelationLength                              #
# ---------------------------------------------------------------------------- #

# graphrelationlength = [0.924, 0.966, 0.932, 0.884, 0.847, 0.701, 0.553, 0.534, 0.728, 0.737, 0.582, 0.653, 0.798, 0.623, 0.623, 0.694, 0.502, 0.422, 0.486, 0.582, 0.465, 0.413, 0.547, 0.616, 0.554, 0.392, 0.559, 0.703, 0.641, 0.448, 0.68, 0.804, 0.77, 0.572, 0.795, 0.939, 0.896, 0.717, 0.949, 0.995, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# transitionrelationlength = [0.868, 0.978, 0.981, 0.961, 0.908, 0.83, 0.624, 0.712, 0.853, 0.885, 0.89, 0.925, 0.947, 0.949, 0.966, 0.974, 0.99, 0.935, 0.993, 0.995, 0.99, 0.991, 0.999, 1, 0.998, 0.998, 1, 1, 0.999, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# relationlength = [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 58]

# plt.style.use('ggplot')

# plt.plot(relationlength, graphrelationlength, label='Graph-Based Parser')
# plt.plot(relationlength, transitionrelationlength, label='Transition-Based Parser')

# plt.xlabel('Relation Length')
# plt.ylabel('F-Score')

# plt.legend()
# # plt.show()
# plt.savefig('analysis/figures/pos_relationlength_fscore.pdf')

# ---------------------------------------------------------------------------- #
#                                 POS ArcDepth                                 #
# ---------------------------------------------------------------------------- #

grapharcdepth = [0.924, 0.911, 0.852, 0.851, 0.929, 0.916]
grapharcdepth7 = [0.916, 0.784, 0.664, 0.516, 0.392, 0.316, 0.234, 0.134, 0.106, 0.041, 0.002]

transitionarcdepth = [0.868, 0.913, 0.87, 0.864, 0.9, 0.952]
transitionarcdepth7 = [0.952, 0.981, 0.994, 0.999, 0.999, 1, 1, 1, 1, 1, 1]

arcdepth = [0, 1, 2, 3, 4, 5]
arcdepth7 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

plt.style.use('ggplot')

plt.plot(arcdepth, grapharcdepth, color='#F8766D', label='Graph-Based Parser')
plt.plot(arcdepth7, grapharcdepth7, color='#F8766D', linestyle=':')
plt.plot(arcdepth, transitionarcdepth, color='#00BFC4', label='Transition-Based Parser')
plt.plot(arcdepth7, transitionarcdepth7, color='#00BFC4', linestyle=':')

plt.xlabel('Distance to Root')
plt.ylabel('F-Score')

plt.legend(loc='lower left')
# plt.show() 
plt.savefig('analysis/figures/pos_arcdepth_fscore.pdf')

# ---------------------------------------------------------------------------- #
#                              POS Sentence Length                             #
# ---------------------------------------------------------------------------- #

# graphsentencelength = [1, 1, 1, 0.95, 0.87, 0.83, 0.80, 0.778, 0.832, 0.842, 0.848, 0.921, 0.954, 0.948, 0.977, 0.989, 0.926, 0.978, 0.967, 0.96 , 0.979, 0.998, 1, 0.993, 0.995, 0.988, 0.985, 0.988, 0.99 , 0.937, 0.939, 0.948, 0.918, 0.858, 0.826, 0.849, 0.863, 0.77 , 0.735, 0.784, 0.789, 0.701, 0.69 , 0.732, 0.762, 0.613, 0.597, 0.65 , 0.747, 0.529, 0.525, 0.567, 0.7, 0.714, 0.77 ]

# transitionsentencelength = [1,     0.775, 1,     0.951, 0.846, 0.829, 0.778, 0.85,  0.874, 0.855, 0.879, 0.935, 0.962, 0.949, 0.98,  0.991, 0.921, 0.982, 0.97,  0.958, 0.981, 0.998, 1,     0.995, 0.997, 1,     1,     0.996, 1,     1,     1,     1,     1,     1,     1,     1,     1,     1,     1,     1,     1,     1,     1,     1,     1,     1,     1,     1,     1,     1,     1,     1,     1,     1,     1]  

# sentencelength = [i for i in range(3, 58)]

# plt.style.use('ggplot')

# plt.plot(sentencelength, graphsentencelength, label='Graph-Based Parser')
# plt.plot(sentencelength, transitionsentencelength, label='Transition-Based Parser')

# plt.xlabel('Sentence Length')
# plt.ylabel('Accuracy')

# plt.legend()
# # plt.show()
# plt.savefig('analysis/figures/pos_sentencelength_accuracy.pdf')

# ---------------------------------------------------------------------------- #
#                              BERT RelationLength                             #
# ---------------------------------------------------------------------------- #

# graphbertrelationlength = [0.863, 0.977, 0.919, 0.899, 0.817, 0.531, 0.47, 0.6, 0.653, 0.763, 0.644, 0.716, 0.691, 0.531, 0.684, 0.642, 0.316, 0.222, 0.352, 0.362, 0.378, 0.332, 0.395, 0.388, 0.443, 0.343, 0.459, 0.498, 0.467, 0.431, 0.569, 0.521, 0.563, 0.555, 0.629, 0.661, 0.635, 0.533, 0.809, 0.745, 0.702, 0.708, 0.963, 0.902, 0.933, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# transitionbertrelationlength = [0.881, 0.977, 0.982, 0.963, 0.909, 0.825, 0.64, 0.719, 0.865, 0.898, 0.898, 0.933, 0.956, 0.95, 0.974, 0.978, 0.992, 0.953, 0.994, 0.997, 0.994, 0.991, 0.999, 1, 0.999, 0.997, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# bertrelationlength = [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 58]

# # plt.style.use('ggplot')

# # plt.plot(bertrelationlength, graphbertrelationlength, label='Graph-Based Parser')
# # plt.plot(bertrelationlength, transitionbertrelationlength, label='Transition-Based Parser')

# # plt.xlabel('Relation Length')
# # plt.ylabel('F-Score')

# # plt.legend()
# # # plt.show()
# # plt.savefig('analysis/figures/bert_relationlength_fscore.pdf')

# graphrelationlength = [0.924, 0.966, 0.932, 0.884, 0.847, 0.701, 0.553, 0.534, 0.728, 0.737, 0.582, 0.653, 0.798, 0.623, 0.623, 0.694, 0.502, 0.422, 0.486, 0.582, 0.465, 0.413, 0.547, 0.616, 0.554, 0.392, 0.559, 0.703, 0.641, 0.448, 0.68, 0.804, 0.77, 0.572, 0.795, 0.939, 0.896, 0.717, 0.949, 0.995, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# plt.style.use('ggplot')

# plt.plot(bertrelationlength, graphrelationlength, label='Standard')
# plt.plot(bertrelationlength, graphbertrelationlength, label='BERT')

# plt.xlabel('Relation Length')
# plt.ylabel('F-Score')

# plt.legend()
# plt.show()
# plt.savefig('analysis/figures/graph_bertvsnobert_relationlength_fscore.pdf')

# ---------------------------------------------------------------------------- #
#                             Train RelationLength                             #
# ---------------------------------------------------------------------------- #

# treebankcounter /    RelationLength
# -----------------------------------
# 32754                -1
# 115035               1
# 55086                2
# 28172                3
# 10625                4
# 4983                 5
# 6122                 6
# 2979                 7
# 3195                 8
# 2223                 9
# 916                  10
# 858                  11
# 488                  12
# 218                  13
# 185                  14
# 498                  15
# 189                  16
# 135                  17
# 170                  18
# 108                  19
# 15                   20
# 19                   21
# 10                   22
# 4                    23
# 2                    24
# 3                    25

