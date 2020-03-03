# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 15:13:47 2019

@author: Abirmoy
"""
from sklearn import tree

# COLLECTING TRAINING DATA
# IN FEATURE SMOOTH = 1, BUMPY = 0
# IN LABELS APPLE = 0, ORANGE = 1
features = [[140,1], [130,1], [150,0], [170,0]]
labels = [0,0,1,1]

# TRAIN CLASSIFIER
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

# PREDICT DECISION
print(clf.predict([[150,0]])) # --> 1--> ORANGE
