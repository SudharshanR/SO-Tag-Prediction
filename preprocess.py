import re
import csv
import sys
import random
from nltk import PorterStemmer
from nltk.corpus import stopwords

if __name__ == "__main__":

    '''
    # Combine two files and replace \n,wc and ,
    inputFileList = ['train', 'train_October_9_2012']
    inter_outputWriter = csv.writer(open('inter_output.csv', 'wb'))

    # Merge two files and replace CR, \n and ,
    firstFile = True
    totalLines = -1 # Keep as -1 to avoid the header row
    for inputFile in inputFileList:
        print inputFile
        inputReader = csv.reader(open(inputFile+'.csv'))
        fileRowNum = 0;

        for line in inputReader:
            if (not(firstFile)) and fileRowNum == 0:
                fileRowNum+=1
                continue

            line[6] = line[6].replace('\015\n','####')
            line[7] = line[7].replace('\015\n','####')
            line[6] = line[6].replace('\n','##')
            line[7] = line[7].replace('\n','##')
            line[6] = line[6].replace(',','~~~~')
            line[7] = line[7].replace(',','~~~~')
            line[6] = line[6].replace('\015','##')
            line[7] = line[7].replace('\015','##')

            postId = [0, 6, 7, 8, 9, 10, 11, 12]
            newLine = [val for col, val in enumerate(line) if col in postId]
            inter_outputWriter.writerow(newLine)
            totalLines += 1
        firstFile = False

    '''

    '''
    # Reservoir sampling
    inputReader = csv.reader(open('inter_output.csv'))
    N = totalLines * 20 / 100 # Create testing set as 20%
    sample = []
    outputWriter = csv.writer(open('testingset.csv', 'wb'))

    for i,line in enumerate(inputReader):
        if i < N:
            sample.append(line)
        elif i >= N and random.random() < N/float(i+1):
            replace = random.randint(0,len(sample)-1)
            sample[replace] = line

    for line in sample:
        outputWriter.writerow(line)
    '''
    '''
    # Split the tags

    inputFileList = ['inter_trainingset', 'inter_testingset']

    for inputFile in inputFileList:
        print inputFile
        inputReader = csv.reader(open(inputFile+'.csv'))
        outputWriter = csv.writer(open('final_'+inputFile+'.csv', 'wb'))

        rowNum = 0
        totalRows = 0
        for line in inputReader:
            if len(line)>7:
                new_line = [val for col, val in enumerate(line) if col not in range(3, 8)] #Read all columns except those having tags
                if rowNum == 0: #Header row
                    outputWriter.writerow(new_line + ['Tag']) #Move the tag column to last
                    rowNum += 1
                else: #Data row
                    for num in range(3, 8): #For all other rows, read Tag1, Tag2 etc
                        if line[num].strip() != "":
                            totalRows += 1
                            outputWriter.writerow(new_line + [line[num]])
        print totalRows
    '''


    # Read top 20 tags from file and delete other rows from testing file
    directoryReader = csv.reader(open('directory.csv'), delimiter=" ")
    topTwentyTags = []
    rowNum = 1
    for line in directoryReader:
        colNum = 1
        if rowNum > 20:
            break
        for num in range(0, len(line)):
            if colNum == 2:
                topTwentyTags.append(line[num])
                break
            elif line[num].strip() != "":
                colNum += 1
        rowNum += 1

    print topTwentyTags

    inputReader = csv.reader(open('final_inter_testingset.csv'))
    outputWriter = csv.writer(open('final_testingset.csv', 'wb'))
    for row in inputReader:
        if row[3] in topTwentyTags:
            line = [val for col, val in enumerate(row) if col in range(0, 4)]
            outputWriter.writerow(row)



    # Read top 20 tags from file and delete other rows from training file
    directoryReader = csv.reader(open('directory.csv'), delimiter=" ")
    topTwentyTags = []
    rowNum = 1
    for line in directoryReader:
        colNum = 1
        if rowNum > 20:
            break
        for num in range(0, len(line)):
            if colNum == 2:
                topTwentyTags.append(line[num])
                break
            elif line[num].strip() != "":
                colNum += 1
        rowNum += 1

    print topTwentyTags

    inputReader = csv.reader(open('final_inter_trainingset.csv'))
    outputWriter = csv.writer(open('final_trainingset.csv', 'wb'))
    total = 0
    for row in inputReader:
        if row[3] in topTwentyTags:
            line = [val for col, val in enumerate(row) if col in range(0, 4)]
            outputWriter.writerow(line)
            total += 1
    print total
