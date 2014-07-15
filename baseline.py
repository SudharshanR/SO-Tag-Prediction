import csv
import sys
import random
import difflib

if __name__ == "__main__":

    # Generate dictionary of postID and list of tags from testing set
    # This is to verify to accuracy of our top and random tag assignment
    inputReader = csv.reader(open('final_testingset.csv'))
    postFreq = {}
    inputReader.next()
    for line in inputReader:
        if line[0] not in postFreq:
            postFreq[line[0]] = list()
        for col in range(1, len(line)):
            postFreq[line[0]].append(line[col])


    # Read top 5 tags from file
    directoryReader = csv.reader(open('directory.csv'), delimiter=" ")
    mostFreqTag = ""
    mostFreqTagCount = 0
    topFiveTags = []
    rowNum = 1
    for line in directoryReader:
        colNum = 1
        if rowNum > 5:
            break
        for num in range(0, len(line)):
            if colNum == 2:
                topFiveTags.append(line[num])
                if rowNum == 1:
                    mostFreqTag = line[num]
                break
            elif line[num].strip() != "":
                if rowNum == 1:
                    mostFreqTagCount = int(line[num])
                colNum += 1
        rowNum += 1

    # Frequency calculation
    totalRows = len(postFreq)
    mostFreqTagCount = 0
    randTagCount = 0

    for postID in postFreq:
        if mostFreqTag in postFreq[postID]:
            mostFreqTagCount += 1
        if random.choice(topFiveTags) in postFreq[postID]:
            randTagCount += 1

    maxFreqAccuracy = float(mostFreqTagCount * 100 / totalRows)
    randTagAccuracy = float(randTagCount * 100 / totalRows)
    print maxFreqAccuracy
    print randTagAccuracy

    '''
        # Write most frequent tag
        inputReader = csv.reader(open('output.csv'))
        outputWriter = csv.writer(open('output_max_freq.csv', 'wb'))
        totalRows = 0
        rowNum = 1
        # tagMatch = [[[] for i in range(6)] for i in range(6)]
        for line in inputReader:
            totalRows += 1
            if rowNum == 1:
                newLine = [val for col, val in enumerate(line) if col in range(0, 4)]
                rowNum += 1
            else:
                newLine = [val for col, val in enumerate(line) if col in range(0, 3)]
                newLine.append(mostFreqTag)
            outputWriter.writerow(newLine)

        # Write top 5 tags in random
        inputReader = csv.reader(open('output.csv'))
        outputWriter = csv.writer(open('output_rand_freq.csv', 'wb'))
        randTag = ""
        randTagCount = 0
        rowNum = 1

        for line in inputReader:
            if rowNum == 1:
                newLine = [val for col, val in enumerate(line) if col in range(0, 4)]
                rowNum += 1
            else:
                newLine = [val for col, val in enumerate(line) if col in range(0, 3)]
                randTag = random.choice(topFiveTags)
                newLine.append(randTag)
                if randTag == line[3]:
                    randTagCount += 1

            outputWriter.writerow(newLine)

        maxFreqAccuracy = float(mostFreqTagCount * 100 / totalRows)
        randTagAccuracy = float(randTagCount * 100 / totalRows)
        print "maxFreqAccuracy"
        print maxFreqAccuracy
        print "randTagAccuracy"
        print randTagAccuracy
    '''

    '''

        inputReader = csv.reader(open('output.csv'))
        randFreqReader = csv.reader(open('output_rand_freq.csv'))
        randTagCount = 0
        rowNum = 0
        inputReader.next()
        randFreqReader.next()

        for line in inputReader:
            columns.append(line[3])
        print "col ??"
        print len(columns)

        for line in randFreqReader:
            print rowNum
            if line[3] == columns[rowNum]:
                randTagCount += 1
            rowNum += 1

        randFreqAccuracy = (randTagCount * 100 / totalRows)
        print " >>>> "
        print randFreqAccuracy
    '''