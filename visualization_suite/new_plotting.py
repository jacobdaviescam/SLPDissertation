import pandas as pd
import pandas as pd
import numpy as np
import seaborn as sn

import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------- #
#                            Grouped RelationLength                            #
# ---------------------------------------------------------------------------- #

# graphgroupedrelationlength = [0.966, 0.932, 0.878, 0.901]
# transitiongroupedrelationlength = [0.978, 0.981, 0.929, 0.941]

# graphgroupedrelationlength = [0.985, 0.956, 0.848, 0.886]
# transitiongroupedrelationlength = [0.964, 0.97, 0.945, 0.962]
# groupedrelationlength = ['1', '2', '3-6', '7-...']

# plt.style.use('ggplot')

# plt.plot(groupedrelationlength, graphgroupedrelationlength, label='Graph-Based Parser', color='#F8766D')
# plt.plot(groupedrelationlength, transitiongroupedrelationlength, label='Transition-Based Parser', color='#00BFC4')

# plt.xlabel('Dependency Length')
# plt.ylabel('Recall')


# plt.legend(loc='best')
# # plt.show()
# plt.savefig('./analysis/figures/pos-groupedrelationlength-recall.pdf')

# ---------------------------------------------------------------------------- #
#                                   ArcDepth                                   #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
#                       StartWordPosition Graph Recursion                      #
# ---------------------------------------------------------------------------- #

# pp = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.978, 0.972, 0.98, 0.841, 0.733, 0.842, 0.787, 0.718, 0.787, 0.754, 0.717, 0.7, 0.709, 0.753, 0.726, 0.775, 0.835, 0.839, 0.845, 0.92, 0.897, 0.914, 0.973, 0.956, 0.976, 0.997, 0.997, 1, 0.996, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# cp = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0.999, 0.999, 0.98, 0.908, 0.802, 0.872, 0.867, 0.792, 0.759, 0.776, 0.774, 0.743, 0.74, 0.751, 0.725, 0.767, 0.794, 0.791, 0.845, 0.849, 0.884, 0.902, 0.935, 0.956, 0.971, 0.985, 0.992, 0.996, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# ce = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.769, 0.488, 0.361, 0.398, 0.402, 0.299, 0.409, 0.446, 0.388, 0.527, 0.553, 0.481, 0.658, 0.628, 0.53, 0.691, 0.665, 0.627, 0.805, 0.681, 0.632, 0.818, 0.723, 0.72, 0.787, 0.793, 0.672, 0.614, 0.65, 0.563, 0.454, 0.4, 0.493, 0.582, 0.578, 0.52, 0.76, 0.919, 0.993, 1, 1, 1, 1]



# swp = [i for i in range(0, 48)]
# swpce = [i for i in range(0, 54)]

# plt.style.use('ggplot')

# plt.plot(swp, pp, label='Prepositional Phrase')
# plt.plot(swp, cp, label='Clausal Phrase')
# plt.plot(swpce, ce, label='Center Embedded Phrase')

# plt.xlabel('Start Word Position')
# plt.ylabel('Accuracy')

# plt.legend(loc='best')
# # plt.show()
# plt.savefig('./analysis/figures/pos-cp-pp-ce-accuracy.pdf')

# ---------------------------------------------------------------------------- #
#                              Recursion ArcDepth                              #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
#                               Overall Bar Graph                              #
# ---------------------------------------------------------------------------- #

# ShallowerTransitionRecursion = 100
# ShallowerGraphRecursion = 100

# DeeperTransitionRecursion = 100
# DeeperGraphRecursion = 36.3

# TransitionModifier = 39.35
# GraphModfier = 27.8

# TransitionModifierIobj = 73.25
# GraphModfierIobj = 55.25

# TransitionModifierSubj = 5.45
# GraphModfierSubj = 0.35

# TransitionGap = 0.0
# GraphGap = 0.0

# TransitionQuestions = 55.2
# GraphQuestions = 56.7

# plt.style.use('ggplot')

# labels = ['Shallower Recursion', 'Deeper Recursion', ' Indirect Object Modifier', ' Subject Modifier', ' Gap Positions', ' Wh-questions']

# Transition_means, Transition_std = [ShallowerTransitionRecursion, DeeperTransitionRecursion, TransitionModifierIobj, TransitionModifierSubj, TransitionGap, TransitionQuestions], [0, 0, 19.65, 1.45, 0, 37.6]
# Graph_means, Graph_std = [ShallowerGraphRecursion, DeeperGraphRecursion, GraphModfierIobj, GraphModfierSubj, GraphGap, GraphQuestions], [0, 15.1, 7.15, 0.35, 0, 38.7 ]

# x = np.arange(len(labels))
# width = 0.35

# fig, ax = plt.subplots()
# rects1 = ax.bar(x - width/2, Transition_means, width, yerr=Transition_std, label='Transition')
# rects2 = ax.bar(x + width/2, Graph_means, width, yerr=Graph_std, label='Graph')

# ax.set_xlabel('Generalisation Types', fontsize=12)
# ax.set_ylabel('Accuracy (%)', fontsize=12)
# # ax.set_title('Comparison of Transition and Graph', fontsize=14)
# ax.set_xticks(x)
# ax.set_xticklabels(labels, fontsize=10, rotation=30, ha='right')
# ax.legend(fontsize=10, loc='best')

# fig.tight_layout()

# # plt.show()
# plt.savefig('./analysis/figures/error-analysis-graph-fine.pdf')

# ---------------------------------------------------------------------------- #
#                     Graph Generalisation Type Sentence Length                     #
# ---------------------------------------------------------------------------- #

# --------------------------------- Recursion -------------------------------- #

gce3 = [1, 1, 1]
gce3label = [16, 17, 18]

gce3dict = {}
for k, v in zip(gce3label, gce3):
    gce3dict[k] = v

gce5 = [1, 1, 1, 0.971, 0.971, 0.981, 0.882, 0.894, 0.902, 0.741, 0.757, 0.783, 0.636, 0.663, 0.682, 0.58, 0.613, 0.645, 0.531, 0.557, 0.58, 0.486, 0.51, 0.527]
gce5label = [24, 25, 26, 28, 29, 30, 32, 33, 34, 36, 37, 38, 40, 41, 42, 44, 45, 46, 48, 49, 50, 52, 53, 54]

gce5dict = {}
for k, v in zip(gce5label, gce5):
    gce5dict[k] = v

gcp3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
gcp3label = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

gcp3dict = {}
for k, v in zip(gcp3label, gcp3):
    gcp3dict[k] = v

gcp5 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.999, 0.999, 0.998, 0.987, 0.981, 0.964, 0.956, 0.924, 0.917, 0.912, 0.886, 0.849, 0.828, 0.833, 0.796, 0.784, 0.762, 0.772, 0.729, 0.738, 0.747, 0.738, 0.748, 0.716, 0.7, 0.714, 0.77]
gcp5label = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 61]

gcp5dict = {}
for k, v in zip(gcp5label, gcp5):
    gcp5dict[k] = v

gpp3 = [1, 1, 1, 1, 1, 1, 1, 1, 1]
gpp3label = [14, 15, 16, 17, 18, 19, 20, 21, 22]

gpp3dict = {}
for k, v in zip(gpp3label, gpp3):
    gpp3dict[k] = v

gpp5 = [1, 1, 1, 1, 1, 1, 0.999, 0.999, 1, 0.99, 0.99, 0.976, 0.942, 0.943, 0.901, 0.878, 0.885, 0.828, 0.827, 0.815, 0.795, 0.749, 0.766, 0.726, 0.713, 0.704, 0.739, 0.766, 0.708]
gpp5label = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]

gpp5dict = {}
for k, v in zip(gpp5label, gpp5):
    gpp5dict[k] = v

grecursion3 = {}
grecursion3dicts = [gcp3dict, gce3dict,gpp3dict]
for dict in grecursion3dicts:
    for k, v in dict.items():
        if k in grecursion3.keys():
            grecursion3[k].append(v)
        else:
            grecursion3[k] = [v]

for k, v in grecursion3.items():
    grecursion3[k] = round(sum(v) / len(v), 3)

grecursion5 = {}
grecursion5dicts = [gcp5dict, gce5dict, gpp5dict]
for dict in grecursion5dicts:
    for k, v in dict.items():
        if k in grecursion5.keys():
            grecursion5[k].append(v)
        else:
            grecursion5[k] = [v]

for k, v in grecursion5.items():
    grecursion5[k] = round(sum(v) / len(v), 3)

# ---------------------------- Modifier Positions ---------------------------- #

gpmi = [0.763, 0.952, 0.997, 0.897, 0.944, 0.984, 0.903, 0.973, 0.97, 1, 0.89, 1, 1]
gpmilabel = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

gpmidict = {}
for k, v in zip(gpmilabel, gpmi):
    gpmidict[k] = v

gpms = [0.575, 0.636, 0.631, 0.657, 0.659, 0.702, 0.736, 0.714, 0.675, 0.719, 0.705, 0.675, 0.78, 0.7, 0.671, 0.788, 0.658, 0.667, 0.744, 0.63, 0.667]
gpmslabel = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 30]

gpmsdict = {}
for k, v in zip(gpmslabel, gpms):
    gpmsdict[k] = v

grcmi = [0.778, 0.808, 0.894, 0.951, 0.926, 0.893, 0.921, 0.907, 0.95, 0.972, 0.921, 0.883, 1, 0.909, 1]
grcmilabel = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

grcmidict = {}
for k, v in zip(grcmilabel, grcmi):
    grcmidict[k] = v

grcms = [0.514, 0.507, 0.494, 0.492, 0.531, 0.56, 0.614, 0.645, 0.664, 0.688, 0.721, 0.745, 0.778, 0.789, 0.8, 0.762]
grcmslabel = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

grcmsdict = {}
for k, v in zip(grcmslabel, grcms):
    grcmsdict[k] = v

gmodifier = {}
gmodifierdicts = [grcmsdict, gpmidict, grcmidict, gpmsdict ]
for dict in gmodifierdicts:
    for k, v in dict.items():
        if k in gmodifier.keys():
            gmodifier[k].append(v)
        else:
            gmodifier[k] = [v]

for k, v in gmodifier.items():
    gmodifier[k] = round(sum(v) / len(v), 3)

# ------------------------------- Gap Positions ------------------------------ #

gqdi = [0.75, 0.778]
gqdilabel = [8,9]

gqdidict = {}
for k, v in zip(gqdilabel, gqdi):
    gqdidict[k] = v

grcie = [0.818, 0.833, 0.846, 0.857, 0.867, 0.875, 0.882, 0.944, 0.947]
grcielabel = [11, 12, 13, 14, 15, 16, 17, 18, 19]

grciedict = {}
for k, v in zip(grcielabel, grcie):
    grciedict[k] = v

ggap = {}
ggapdicts = [gqdidict, grciedict]
for dict in ggapdicts:
    for k, v in dict.items():
        if k in ggap.keys():
            ggap[k].append(v)
        else:
            ggap[k] = [v]

for k, v in ggap.items():
    ggap[k] = round(sum(v) / len(v), 3)

# --------------------------------- Questions -------------------------------- #

gqdd = [0.833, 0.898, 0.96, 0.996]
gqddlabel = [6, 7, 8, 9]

gqdddict = {}
for k, v in zip(gqddlabel, gqdd):
    gqdddict[k] = v

gqlm = [0.875, 0.889, 0.9, 0.909, 0.917, 0.923, 0.929]
gqlmlabel = [8, 9, 10, 11, 12, 13, 14]

gqlmdict = {}
for k, v in zip(gqlmlabel, gqlm):
    gqlmdict[k] = v

gqmn = [1, 0.875, 0.719, 0.808, 0.789, 0.779, 0.804, 0.836, 0.733, 0.75, 0.818, 0.889, 0.737]
gqmnlabel = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

gqmndict = {}
for k, v in zip(gqmnlabel, gqmn):
    gqmndict[k] = v

gqsa = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.733, 1]
gqsalabel = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

gqsadict = {}
for k, v in zip(gqsalabel, gqsa):
    gqsadict[k] = v

gqsp = [1, 1, 1, 1, 1, 1]
gqsplabel = [4, 6, 7, 8, 9, 10]

gqspdict = {}
for k, v in zip(gqsplabel, gqsp):
    gqspdict[k] = v

gquestions = {}
gquestionsdicts = [gqsadict, gqdddict, gqlmdict,gqspdict, gqmndict]
for dict in gquestionsdicts:
    for k, v in dict.items():
        if k in gquestions.keys():
            gquestions[k].append(v)
        else:
            gquestions[k] = [v]

for k, v in gquestions.items():
    gquestions[k] = round(sum(v) / len(v), 3)

# # grecursion5 = {19: 1.0, 20: 1.0, 21: 1.0, 22: 1.0, 23: 1.0, 24: 1.0, 25: 1.0, 26: 1.0, 27: 1.0, 28: 0.99, 29: 0.987, 30: 0.99, 31: 0.988, 32: 0.941, 33: 0.945, 34: 0.93, 35: 0.929, 36: 0.863, 37: 0.847, 38: 0.845, 39: 0.866, 40: 0.781, 41: 0.766, 42: 0.766, 43: 0.777, 44: 0.709, 45: 0.704, 46: 0.723, 47: 0.764, 48: 0.67, 49: 0.643, 50: 0.659, 51: 0.747, 52: 0.612, 53: 0.629, 54: 0.621, 55: 0.7, 56: 0.714, 61: 0.77}

# # ---------------------------------- Average --------------------------------- #

graphaverage = [1    ,1    ,1    ,0.954,0.879,0.831,0.809,0.778 ,0.832 ,0.842 ,0.848 ,0.921 ,0.954 ,0.948 ,0.977 ,0.989 ,0.926 ,0.978 ,0.967 ,0.96  ,0.979 ,0.998 ,1     ,0.993 ,0.995 ,0.988 ,0.985 ,0.988 ,0.99  ,0.937 ,0.939 ,0.948 ,0.918 ,0.858 ,0.826 ,0.849 ,0.863 ,0.77  ,0.735 ,0.784 ,0.789 ,0.701 ,0.69  ,0.732 ,0.762 ,0.613 ,0.597 ,0.65  ,0.747 ,0.529 ,0.525 ,0.567 ,0.7   ,0.714 ,0.77  ]


sentencelength = [i for i in range(3,57)]
sentencelength.append(61)

# # --------------------------------- Plotting --------------------------------- #

plt.style.use('ggplot')

plt.plot(sentencelength, graphaverage, label='Average', color='black')

plt.plot(grecursion3.keys(), grecursion3.values(), label='Shallower Recursion', alpha=0.5)
plt.plot(grecursion5.keys(), grecursion5.values(), label='Deeper Recursion', alpha=0.5)

plt.plot(gmodifier.keys(), gmodifier.values(), label='Modifier Positions', alpha=0.5)

plt.plot(ggap.keys(), ggap.values(), label='Gap Positions', alpha=0.5)

plt.plot(gquestions.keys(), gquestions.values(), label='Questions', alpha=0.5)



# # plt.plot(gce3label, gce3, label='Center Embedded Depth 3', linestyle=':')
# # plt.plot(gce5label, gce5, label='Center Embedded Depth 5', linestyle=':')

# # plt.plot(gcp3label, gcp3, label='Clausal Phrase Depth 3', linestyle=':')
# # plt.plot(gcp5label, gcp5, label='Clausal Phrase Depth 5', linestyle=':')

# # plt.plot(gpp3label, gpp3, label='Prepositional Phrase Depth 3', linestyle=':')
# # plt.plot(gpp5label, gpp5, label='Prepositional Phrase Depth 5', linestyle=':')

# # plt.plot(gpmilabel, gpmi, label='Modifier Indirect Object', linestyle=':')
# # plt.plot(gpmslabel, gpms, label='Modifier Subject', linestyle=':')

# # plt.plot(gqddlabel, gqdd, label='Question Direct Object Ditransitive', linestyle=':')
# # plt.plot(gqdilabel, gqdi, label='Question Indirect Object Ditransitive', linestyle=':')

# # plt.plot(gqlmlabel, gqlm, label='Question Long Movement', linestyle=':')
# # plt.plot(gqmnlabel, gqmn, label='Question Modified NPs', linestyle=':')

# # plt.plot(gqsalabel, gqsa, label='Question Subject Active', linestyle=':')
# # plt.plot(gqsplabel, gqsp, label='Question Subject Passive', linestyle=':')

# # plt.plot(grcielabel, grcie, label='Relative Clause Indirect Object Extracted', linestyle=':')
# # plt.plot(grcmilabel, grcmi, label='Relative Clause Modifier Indirect Object', linestyle=':')
# # plt.plot(grcmslabel, grcms, label='Relative Clause Modifier Subject', linestyle=':')



plt.xlabel('Sentence Length')
plt.ylabel('Accuracy')

plt.legend(loc='upper right', prop={'size': 9})
# plt.show()
plt.savefig('./analysis/figures/graph-pos-generalisation-sentence-length-accuracy.pdf')

# ---------------------------------------------------------------------------- #
#                    Sentence Generalistion Type Sentence Length                    #
# ---------------------------------------------------------------------------- #

# ---------------------------------- Average --------------------------------- #

# transitionsentencelength = [1, 0.775, 1, 0.951, 0.846, 0.829, 0.778, 0.85, 0.874, 0.855, 0.879, 0.935, 0.962, 0.949, 0.980, 0.991, 0.921, 0.982, 0.970, 0.958, 0.981, 0.998, 1, 0.995, 0.997, 1, 1, 0.996, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# sentencelength = [i for i in range(3,57)]

# # --------------------------------- Recursion -------------------------------- #

# tce3 = [1, 1, 1]
# tce3label = [16, 17, 18]

# tce5 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# tce5label = [24, 25, 26, 28, 29, 30, 32, 33, 34, 36, 37, 38, 40, 41, 42, 44, 45, 46, 48, 49, 50, 52, 53, 54]

# tcp3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# tcp3label = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

# tcp5 = [1 for i in range(19, 58)]
# tcp5label = [i for i in range(19, 57)]
# tcp5label.append(61)

# tpp3 = [1 for i in range(14, 23)]
# tpp3label = [i for i in range(14, 23)]

# tpp5 = [1 for i in range(20, 49)]
# tpp5label = [i for i in range(20,49)]

# trecursion3 = [1 for i in range(12, 27)]
# trecursion3label = [i for i in range(12, 27)]

# trecursion5 = [1 for i in range(19, 58)]
# trecursion5label = [i for i in range(19, 57)]
# trecursion5label.append(61)

# # ---------------------------- Modifier Positions ---------------------------- #

# tpmi = [1, 0.999, 1, 0.976, 0.982, 1, 0.96, 0.985, 1, 1, 0.91, 1, 1]
# tpmilabel = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

# tpmidict = {}
# for k, v in zip(tpmilabel, tpmi):
#     tpmidict[k] = v

# tpms = [0.422, 0.789, 0.506, 0.588, 0.67, 0.665, 0.701, 0.698, 0.706, 0.686, 0.737, 0.698, 0.76, 0.75, 0.705, 0.773, 0.683, 0.667, 0.795, 0.704, 0.6]
# tpmslabel = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 30]

# tpmsdict = {}
# for k, v in zip(tpmslabel, tpms):
#     tpmsdict[k] = v

# trcmi = [0.778, 0.894, 0.905, 0.935, 0.935, 0.938, 0.945, 0.907, 0.966, 0.967, 0.947, 0.933, 1, 0.939, 1]
# trcmilabel = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

# trcmidict = {}
# for k, v in zip(trcmilabel, trcmi):
#     trcmidict[k] = v

# tcrms = [0.428, 0.552, 0.624, 0.646, 0.665, 0.715, 0.706, 0.717, 0.745, 0.728, 0.779, 0.792, 0.852, 0.829, 0.8, 0.714]
# tcrmslabel = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

# tcrmsdict = {}
# for k, v in zip(tcrmslabel, tcrms):
#     tcrmsdict[k] = v

# tmodifier = {}
# tmodifierdicts = [tcrmsdict, tpmidict, trcmidict, tpmsdict ]
# for dict in tmodifierdicts:
#     for k, v in dict.items():
#         if k in tmodifier.keys():
#             tmodifier[k].append(v)
#         else:
#             tmodifier[k] = [v]

# for k, v in tmodifier.items():
#     tmodifier[k] = round(sum(v) / len(v), 3)



# # ------------------------------- Gap Positions ------------------------------ #

# tqdi = [0.676, 0.718]
# tqdilabel = [8, 9]

# tqdidict = {}
# for k, v in zip(tqdilabel, tqdi):
#     tqdidict[k] = v

# trcie = [0.869, 0.868, 0.866, 0.9, 0.889, 0.881, 0.902, 0.889, 0.895]
# trcielabel = [11, 12, 13, 14, 15, 16, 17, 18, 19]

# trciedict = {}
# for k, v in zip(trcielabel, trcie):
#     trciedict[k] = v

# tgap = {}
# tgapdicts = [tqdidict, trciedict]
# for dict in tgapdicts:
#     for k, v in dict.items():
#         if k in tgap.keys():
#             tgap[k].append(v)
#         else:
#             tgap[k] = [v]

# for k, v in tgap.items():
#     tgap[k] = round(sum(v) / len(v), 3)



# # --------------------------------- Questions -------------------------------- #

# tqdd = [0.833, 0.86, 0.954, 1]
# tqddlabel = [6, 7, 8, 9]

# tqdddict = {}
# for k, v in zip(tqddlabel, tqdd):
#     tqdddict[k] = v


# tqlm = [0.875, 0.889, 0.9, 0.909, 0.917, 0.923, 0.929]
# tqlmlabel = [8, 9, 10, 11, 12, 13, 14]

# tqlmdict = {}
# for k, v in zip(tqlmlabel, tqlm):
#     tqlmdict[k] = v


# tqmn = [0.971, 0.867, 0.571, 0.915, 0.781, 0.766, 0.854, 0.822, 0.733, 0.775, 0.818, 0.917, 0.684]
# tqmnlabel = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# tqmndict = {}
# for k, v in zip(tqmnlabel, tqmn):
#     tqmndict[k] = v


# tqsa = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# tqsalabel = [3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16]

# tqsadict = {}
# for k, v in zip(tqsalabel, tqsa):
#     tqsadict[k] = v


# tqsp = [0.775, 1, 1, 1, 1, 1]
# tqsplabel = [4, 6, 7, 8, 9, 10]

# tqspdict = {}
# for k, v in zip(tqsplabel, tqsp):
#     tqspdict[k] = v

# tquestions = {}
# tquestionsdicts = [tqsadict, tqdddict, tqlmdict,tqspdict, tqmndict]
# for dict in tquestionsdicts:
#     for k, v in dict.items():
#         if k in tquestions.keys():
#             tquestions[k].append(v)
#         else:
#             tquestions[k] = [v]

# for k, v in tquestions.items():
#     tquestions[k] = round(sum(v) / len(v), 3)



# tmodifier = {6: 0.428, 7: 0.487, 8: 0.707, 9: 0.643, 10: 0.787, 11: 0.822, 12: 0.827, 13: 0.832, 14: 0.841, 15: 0.845, 16: 0.833, 17: 0.87, 18: 0.879, 19: 0.884, 20: 0.848, 21: 0.855, 22: 0.904, 23: 0.842, 24: 0.667, 26: 0.795, 27: 0.704, 30: 0.6}

# tgap = {8: 0.676, 9: 0.718, 11: 0.869, 12: 0.868, 13: 0.866, 14: 0.9, 15: 0.889, 16: 0.881, 17: 0.902, 18: 0.889, 19: 0.895}

# tquestions = {3: 1.0, 4: 0.775, 5: 1.0, 6: 0.944, 7: 0.958, 8: 0.939, 9: 0.892, 10: 0.954, 11: 0.897, 12: 0.894, 13: 0.926, 14: 0.917, 15: 0.733, 16: 0.887, 17: 0.818, 18: 0.917, 19: 0.684}

# plt.style.use('ggplot') 

# plt.plot(sentencelength, transitionsentencelength, label='Average', color='black')

# plt.plot(trecursion3label, trecursion3, label='Shallower Recursion', alpha=0.5)

# plt.plot(trecursion5label, trecursion5, label='Deeper Recursion', alpha=0.5)

# plt.plot(tmodifier.keys(), tmodifier.values(), label='Modifier Positions', alpha=0.5)

# plt.plot(tgap.keys(), tgap.values(), label='Gap Positions', alpha=0.5)

# plt.plot(tquestions.keys(), tquestions.values(), label='Questions', alpha=0.5)

# plt.plot(tce3label, tce3, label='Center Embedded Depth 3', linestyle=':', alpha=0.5)
# plt.plot(tce5label, tce5, label='Center Embedded Depth 5', linestyle=':', alpha=0.5)

# plt.plot(tcp3label, tcp3, label='Clausal Phrase Depth 3', linestyle=':', alpha=0.5)
# plt.plot(tcp5label, tcp5, label='Clausal Phrase Depth 5', linestyle=':', alpha=0.5)

# plt.plot(tpp3label, tpp3, label='Prepositional Phrase Depth 3', linestyle=':', alpha=0.5)
# plt.plot(tpp5label, tpp5, label='Prepositional Phrase Depth 5', linestyle=':', alpha=0.5)

# plt.plot(tpmilabel, tpmi, label='Modifier Indirect Object', linestyle=':', alpha=0.5)
# plt.plot(tpmslabel, tpms, label='Modifier Subject', linestyle=':', alpha=0.5)
# plt.plot(tqddlabel, tqdd, label='Question Direct Object Ditransitive', linestyle=':', alpha=0.5)
# plt.plot(tqdilabel, tqdi, label='Question Indirect Object Ditransitive', linestyle=':', alpha=0.5)
# plt.plot(tqlmlabel, tqlm, label='Question Long Movement', linestyle=':', alpha=0.5)
# plt.plot(tqmnlabel, tqmn, label='Question Modified NPs', linestyle=':', alpha=0.5)
# plt.plot(tqsalabel, tqsa, label='Question Subject Active', linestyle=':', alpha=0.5)
# plt.plot(tqsplabel, tqsp, label='Question Subject Passive', linestyle=':', alpha=0.5)
# plt.plot(trcielabel, trcie, label='Relative Clause Indirect Object Extracted', linestyle=':', alpha=0.5)
# plt.plot(trcmilabel, trcmi, label='Relative Clause Modifier Indirect Object', linestyle=':', alpha=0.5)
# plt.plot(tcrmslabel, tcrms, label='Relative Clause Modifier Subject', linestyle=':', alpha=0.5)
# plt.xlabel('Sentence Length')
# plt.ylabel('Accuracy')
# plt.legend(loc='best', labelcolor='linecolor', prop={'size': 12})
# # plt.show()
# plt.savefig('./analysis/figures/transition-pos-generalisation-sentence-length-accuracy.pdf')


# ---------------------------------------------------------------------------- #
#                          ArcDepth Confusion Matrices                         #
# ---------------------------------------------------------------------------- #

# matrix = [
# [np.nan, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, np.nan, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, np.nan, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, np.nan, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, np.nan, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 124, np.nan, 392, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 16, 345, np.nan, 328, 10, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 1, 180, 469, np.nan, 156, 2, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 73, 260, 659, np.nan, 8, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 8, 133, 393, 641, np.nan, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 15, 248, 415, 526, np.nan, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 29, 280, 391, 502, np.nan, 0, 0, 0, 0, 0],
# [0,   0 ,  0 ,  0,   0,   0 ,  0 ,  0 ,  28  ,299 ,393, 330, np.nan,  0 ,  0 , 0,  0],
# [0 ,    0 ,    0 ,    0 ,    0 ,    0,     0 ,    0 ,    0,     35,    310,   241,   91,   np.nan ,    0 ,   0,    0]
# ]

# matrix = [
#     [np.nan, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, np.nan, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, np.nan, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, np.nan, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0,     0,     0,     0,     np.nan,     0,     0,    0,      0,     0,     0,     0,     0,     0,     0,     0,     0],
# [0,     0,     0,    0,     0,     np.nan,     0,     0,       0,     0,     0,     0,     0,     0,     0,     0,     0],    
# [0,     0,     0,    0,     0,     0,     np.nan,     0,       0,     0,     0,     0,     0,     0,     0,     0,     0],    
# [0,     0,     0,    0,     0,     630,   0,     np.nan,       0,     0,     0,     0,     0,     0,     0,     0,     0],    
# [0,     0,     0,    0,     0,     0,     916,   0,       np.nan,     0,     0,     0,     0,     0,     0,     0,     0],    
# [0,     0,     0,    0,     0,     0,     0,     1115,    0,     np.nan,     0,     99,    0,     0,     0,     0,     0],    
# [0,     0,     0,    0,     0,     0,     522,   0,       825,   0,     np.nan,     0,     0,     0,     0,     0,     0],    
# [0,     0,     0,    0,     0,     0,     0,     649,     0,     706,   0,     np.nan,     0,     1,     0,     0,     0],    
# [0,     0,     0,    0,     0,     0,     199,   0,       876,   0,     393,   0,     np.nan,     0,     0,     0,     0],    
# [0,     0,     0,    0,     0,     0,     0,     424,     0,     707,   0,     367,   0,     np.nan,     0,     0,     0],    
# [0,     0,     0,    0,     0,     0,     94,    0,       673,   0,     469,   0,     262,   0,     np.nan,     0,     0],    
# [0,     0,     0,    0,     0,     0,     0,     255,     0,     591,   0,     424,   0,     228,   0,     np.nan,     0],    
# [0,     0,     0,    0,     0,     0,     49,    0,       446,   0,     478,   0,     280,   0,     37,    0,     np.nan]
# ]

# matrix = [
#     [np.nan,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,    0,    0],    
#     [0,     np.nan,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,    0,    0],    
#     [0,     0,     np.nan,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,    0,    0],    
#     [0,     0,     0,     np.nan,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,    0,    0],    
#     [0,     0,     0,     0,     np.nan,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,    0,    0],    
#     [0,     0,     0,     0,     0,     np.nan,     86,    1,     0,     0,     0,     0,     0,     0,     0,    0,    0],    
#     [0,     0,     0,     0,     0,     166,   np.nan,     494,   34,    2,     0,     0,     0,     0,     0,    0,    0],    
#     [0,     0,     0,     0,     0,     49,    431,   np.nan,     251,   11,    0,     0,     0,     0,     0,    0,    0],    
#     [0,     0,     0,     0,     0,     8,     196,   706,   np.nan,     57,    0,     0,     0,     0,     0,    0,    0],    
#     [0,     0,     0,     0,     0,     1,     61,    361,   807,   np.nan,     15,    0,     0,     0,     0,    0,    0],    
#     [0,     0,     0,     0,     0,     0,     15,    150,   488,   635,   np.nan,     2,     0,     0,     0,    0,    0],    
#     [0,     0,     0,     0,     0,     0,     0,     34,    239,   450,   488,   np.nan,     0,     0,     0,    0,    0],    
#     [0,     0,     0,     0,     0,     0,     0,     0,     63,    241,   395,   293,   np.nan,     0,     0,    0,    0],    
#     [0,     0,     0,     0,     0,     0,     0,     0,    0,    65,    221,   276,   87,    np.nan,     0,    0,    0]    
# ]

# matrix = pd.DataFrame(matrix, columns=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'], index=['0','1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'])

# yticks = matrix.index
# xticks = matrix.columns

# sn.set_theme(font_scale=1.0) # for label size
# sn.heatmap(matrix, yticklabels=yticks, xticklabels=xticks, annot=True, annot_kws={"size": 8}, fmt='g', cmap=sn.cubehelix_palette(as_cmap=True)) # font size
# plt.xlabel("Gold")
# plt.ylabel("Predicted")

# plt.yticks(rotation=0)
# plt.xticks(rotation=0)

# # plt.show()
# plt.savefig('./analysis/figures/pos-arcdepth-confusion-pp.pdf')


# ---------------------------------------------------------------------------- #
#                               Treebank Accuracy                              #
# ---------------------------------------------------------------------------- #

# graphpp = [1, 1, 1, 1, 1, 0.971, 0.729, 0.659, 0.689, 0.751, 0.852, 0.944, 0.99, 1, 1, 1, 1]
# graphpplabel = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# graphcp = [1, 1, 1, 1, 0.999, 0.814, 0.7, 0.735, 0.797, 0.885, 0.966, 0.998, 1, 1, 1, 1, 1]
# graphcplabel = [i for i in range(0, 17)]

# graphce = [1, 1, 1, 1, 1, 1, 1, 0.685, 0.81, 0.36, 0.403, 0.329, 0.379, 0.344, 0.415, 0.381, 0.467, 0.463, 0.586, 0.553, 0.737, 0.711, 0.833, 1, 1, 1, 1]
# graphcelabel = [i for i in range(0, 27)]

# plt.style.use('ggplot')
# fig, axs = plt.subplots(3, 1, sharex=True)

# fig.subplots_adjust(hspace=0)



# axs[0].plot(graphpplabel, graphpp, color='#F8766D', label = 'PP')
# axs[0].axvline(x=8, color='black', linestyle=':')

# axs[1].plot(graphcplabel, graphcp, color='#00BFC4', label='CP')
# axs[1].axvline(x=8, color='black', linestyle=':')

# axs[2].plot(graphcelabel, graphce, color='#00BA38', label='CE')
# axs[2].axvline(x=13, color='black', linestyle=':')


# # plt.plot(graphpplabel, graphpp, label='PP')
# # plt.plot(graphcplabel, graphcp, label='CP')
# # plt.plot(graphcelabel, graphce, label='CE')

# fig.supxlabel('Dependency Depth')
# fig.supylabel('Accuracy')

# axs[0].legend(loc='lower right')
# axs[1].legend(loc='lower right')
# axs[2].legend(loc='lower right')

# # plt.show()
# plt.savefig('./analysis/figures/pos-treebank-accuracy-arcdepth.pdf')

# ---------------------------------------------------------------------------- #
#                         Graph vs Transition ArcDepth                         #
# ---------------------------------------------------------------------------- #

# grapharcdepth = [0.924, 0.884, 0.893, 0.895, 0.977, 0.948, 0.83, 0.757]
# grapharcdepth7 = [0.757, 0.778, 0.681, 0.736, 0.712, 0.716, 0.627, 0.564, 0.419, 0.473, 0.463, 0.586, 0.553, 0.737, 0.711, 0.833, 1, 1, 1, 1]

# transitionarcdepth = [0.868, 0.862, 0.913, 0.96, 0.994, 1, 1, 1]
# transitionarcdepth7 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# arcdepth = [i for i in range(0, 8)]
# arcdepth7 = [i for i in range(7, 27)]

# plt.style.use('ggplot')

# plt.plot(arcdepth, grapharcdepth, label='Graph-Based Parser', color='#F8766D')
# plt.plot(arcdepth7, grapharcdepth7, color='#F8766D', linestyle=':')
# plt.plot(arcdepth, transitionarcdepth, label='Transition-Based Parser', color='#00BFC4')
# plt.plot(arcdepth7, transitionarcdepth7, color='#00BFC4', linestyle=':')

# plt.xlabel('Dependency Depth')
# plt.ylabel('Accuracy')

# plt.legend(loc='best')
# # plt.show()
# plt.savefig('./analysis/figures/pos-graph-transition-arcdepth-accuracy.pdf')