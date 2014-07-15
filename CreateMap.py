import csv
import re
from numpy import *
import scipy
from sklearn import svm
import pickle
from nltk.corpus import stopwords

if __name__ == "__main__":

    '''
    # Finds count of all words from trainingset
    inputReader = csv.reader(open('final_trainingset.csv'))
    wordCount = {}
    for line in inputReader:
        for col in [1, 2]:
            word = re.compile('\w+').findall(line[col].lower())
            for w in word:
                if w not in wordCount:
                    wordCount[w] = 1
                else:
                    wordCount[w] = wordCount[w] + 1

    writer = csv.writer(open('dict.csv', 'wb'), delimiter=':')
    for key, value in wordCount.items():
        writer.writerow([key, value])
    print(len(wordCount))
    '''
    '''
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass
        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass
        return False

    reader = csv.reader(open('dict.csv'), delimiter=':')
    writer = csv.writer(open("stop.csv", "wb"))
    for line in reader:
        if not line[0] in stopwords.words('english'):
            if(is_number(line[0])) == False:
                new_line = [val for col, val in enumerate(line) if col in range(0, 2)]
                writer.writerow(new_line)
    '''

    def rowCount(fileName):
        count = 0
        reader = csv.reader(open(fileName+'.csv'))
        for line in reader:
            count += 1
        return count

    # Creates utility matrix where rows are tagwords and columns are every word in training set


    # Reads every word from the word count file and creates the utility matrix with words as columns
    reader = csv.reader(open('stop.csv'))
    wordColMap = {}
    #testList = [('sudharshan_TagName', '|S20')]
    flag = 0
    col = 0
    for line in reader:
        if int(line[1]) > 5:
            wordColMap[line[0]] = col
            col += 1
    #testList.append(('viki_AlwaysTellsTruth', 'i4'))

    featureMatrix = []


    # Reads training set corresponding to tags and inserts 1 for every word in the tag files row
    #android, java,c++
    inputList = ['sample_Android', 'sample_aspdotnet', 'sample_c', 'sample_cplusplus', 'sample_Csharp', 'sample_css']
    inputList.extend(['sample_dotnet', 'sample_html', 'sample_ios', 'sample_Iphone'])
    inputList = ['sample_sql']

    for inputFile in inputList:
        print len(wordColMap)
        print rowCount(inputFile)
        featureMatrix = scipy.sparse.lil_matrix((rowCount(inputFile)-1, len(wordColMap)))
        classMatrix = []
        try:
            reader = csv.reader(open(inputFile+'.csv'))
            reader.next()
            rowNum = 0
            for line in reader:
                #rowNum = rowNumDictionary[line[3]]
                classMatrix.extend(line[4])
                for col in [1, 2]:
                    word = re.compile('\w+').findall(line[col].lower())
                    for w in word:
                        try:
                            featureMatrix[rowNum, wordColMap[w]] = 1
                        except Exception, e:
                            pass
                rowNum += 1

        except Exception, e:
            print "Except >>>>>"
            print str(e)
            classMatrix.extend([0])
            pass

        print "outside"
        clf = svm.SVC()
        clf.fit(featureMatrix, classMatrix)
        print "after"
        pickle.dump(clf, open(inputFile+".p","wb"))

    #print a[rowNumDictionary['c#']]['opacity']
