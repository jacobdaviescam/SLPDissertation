import pandas as pd
import pandas as pd

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

# UAS = [100, 100, 100, 99.9, 95.0, 83.6, 74.2, 76.7, 86.0, 94.5, 98.7, 99.6, 100, 100]
# LA = [100, 100, 100, 99.9, 96.9, 92.7, 95.4, 98.6, 99.7, 100, 100, 100, 100, 100]
# ArcDepth = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# plt.plot(ArcDepth, UAS, label='UAS')
# plt.plot(ArcDepth, LA, label='LA')


# plt.xlabel('Arc Depth')
# plt.ylabel('Accuracy')
# plt.title('Accuracy vs Arc Depth')

# plt.legend()
# plt.savefig('analysis/figures/graph_accuracy_arcdepth_pp_5-12.pdf')



