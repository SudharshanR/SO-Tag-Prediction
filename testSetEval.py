import re
import csv
from numpy import *
from sklearn import svm
import pickle
from sklearn.externals import joblib
import scipy
import random
from nltk.corpus import stopwords

# Reads every word from the word count file and creates the utility matrix with words as columns
reader = csv.reader(open('stop.csv'))
wordColMap = {}
flag = 0
col = 0
for line in reader:
    if int(line[1]) > 5:
        wordColMap[line[0]] = col
        col += 1

reader = csv.reader(open('testingset.csv'))
Writer = csv.writer(open('Accuracy_svm_cplusplus.txt', 'wb'))

#clfList = ['sample_Csharp', 'sample_Java', 'sample_Php', 'sample_Javascript', 'sample_dotnet']
#clfList.extend(['sample_aspdotnet', ''])
clfList = ['sample_cplusplus']

for clf in clfList:
    clf2 = pickle.load(open(clf+".p", "rb"))

    featureMatrix = []
    clfTrue = []
    actTrue = []
    trueFalse = 0
    totalRows = 0
    true = 0
    totalTrue = 0

    for line in reader:
        if line[3] == 'c++':
            totalTrue += 1
            actTrue.append(1)
        else:
            actTrue.append(0)
        featureMatrix = scipy.sparse.lil_matrix((1, len(wordColMap)))
        for col in [1, 2]:
            word = re.compile('\w+').findall(line[col].lower())
            for w in word:
                try:
                    featureMatrix[0, wordColMap[w]] = 1
                except Exception, e:
                    pass
        predict = clf2.predict(featureMatrix)
        clfTrue.append(predict)
   #     print "ghhhhh"
    #    print line[3]
     #   print predict
        if predict == [1] and line[3] == 'c++':
            print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
            true += 1
        if (predict == [0] and line[3] != 'c++') or (predict == [1] and line[3] == 'c++'):
        #if predict == [1]:
  #          print "dsi>>>>>>>>>>>>>>"
            trueFalse += 1
        totalRows += 1

    print "Done >>>"
    try:
        print "trueFalse"
        print trueFalse
        print "total Rows"
        print totalRows
        print "true"
        print true
        print "totalTrue"
        print totalTrue
        maxFreqAccuracy = float(trueFalse * 100 / totalRows)
        print maxFreqAccuracy
        trueFrequency = float(true * 100 / totalTrue)
        print trueFrequency
        #accuracy_score(
        Writer.writerow(["trueFalse", trueFalse])
        Writer.writerow(["total rows", totalRows])
        Writer.writerow(["true", true])
        Writer.writerow(["totalTrue", totalTrue])
        Writer.writerow(["Max Freq Accuracy", maxFreqAccuracy])
        Writer.writerow(["trueFrequency", trueFrequency])


    except Exception, e:
        print "2>>>>>>>>>>>"
        print str(e)
        pass

