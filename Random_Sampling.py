'''import subprocess

inputFile = "inter_output.csv"
trainingset = "trainingset.csv"

process = subprocess.Popen(['sampling.sh', inputFile, trainingset], stdout=subprocess.PIPE)
process.wait()

'''

import sys, re, string, random

f = open("inter_output.csv", "r")
f1 = open("inter_testingset.csv", "w")
f2 = open("inter_trainingset.csv", "w")

firstline = 0
for l in f:
    if firstline == 0:
        firstline = 1
        f1.write(l)
        f2.write(l)
    else:
        if random.randint(0,4) == 0:
            f1.write(l)
        else:
            f2.write(l)
