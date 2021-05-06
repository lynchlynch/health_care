import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score

frTrain = open('/Users/pei/pydir/health_care/horseColicTraining.txt') #打开训练集
frTest = open('/Users/pei/pydir/health_care/horseColicTest.txt')#打开测试集
trainingSet = []
trainingLabels = []
testSet = []
testLabels = []
for line in frTrain.readlines():
    currLine = line.strip().split('\t')
    lineArr = []
    for i in range(len(currLine)-1):
        lineArr.append(float(currLine[i]))
    trainingSet.append(lineArr)
    trainingLabels.append(float(currLine[-1]))

for line in frTest.readlines():
    currLine = line.strip().split('\t')
    lineArr =[]
    for i in range(len(currLine)-1):
        lineArr.append(float(currLine[i]))
        testSet.append(lineArr)
        testLabels.append(float(currLine[-1]))

# classifier = LogisticRegression(solver='liblinear',max_iter=10).fit(trainingSet, trainingLabels)
classifier2 = LogisticRegression(solver='sag',max_iter=3000).fit(trainingSet, trainingLabels)
test_accurcy = classifier2.score(testSet, testLabels) * 100
print('test_accurcy:' + str(test_accurcy))
print('--- params ---')
print(classifier2.coef_, classifier2.intercept_)
# test_accurcy:73.13432835820896