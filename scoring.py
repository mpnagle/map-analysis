import csv
import re
import nltk

ifile  = open('output-stem-4.csv', "rb")
reader = csv.reader(ifile)

ifile2 = open('word-frequency.csv', "rbU")
wordFreq = csv.reader(ifile2)

rownum = 0

commonWords = []

for row in  wordFreq:
    if rownum == 0:
        header = row
    else:
        colnum = 0
        for col in row:
            if colnum == 1:
                col = col[3:]
                commonWords.append(col)
#            print '%-8s: %s' % (header[colnum], col)
            colnum += 1   
    rownum += 1

commonWords1000 = commonWords[1:1001]
commonWords5000 = commonWords[1:5001]

stage2 = []
stage23 = []
stage3 = []
stage34 = []
stage4 = []
stage45 = []
stage5 = []
stage56 = []
stage6 = []



def rareWord5000 (stem):
    wordCount = 0
    stemWords = re.findall(r'\w+', stem)
    
    for word in stemWords:
        if ( (len(word) > 3) and (word not in commonWords5000)):
            wordCount +=1
            
    return wordCount

def rareWord1000 (stem):
    wordCount = 0
    stemWords = re.findall(r'\w+', stem)
    
    for word in stemWords:
        if ( (len(word) > 3) and (word not in commonWords1000)):
            wordCount +=1
            
    return wordCount

def indexToStage (index):
    
    if (index == 0):
        return "2"
    elif (index == 1):
        return "2/3"
    elif (index == 2):
        return "3"
    elif (index == 3):
        return "3/4"
    elif (index == 4):
        return "4"
    elif (index == 5):
        return "4/5"
    elif (index == 6):
        return "5"
    elif (index == 7):
        return "5/6"
    elif (index == 8):
        return "6"


minLengths = [2,1,0,2,3,6,11,19,19]
minReversed = reversed(minLengths)

maxLengths = [7,14,15,25,24,48,45,80,62]

for row in reader:
   
    lowerBound = 0
    upperBound = 8
    
    stem = row[2]

    if (not (rareWord5000(stem))):
        if (not (rareWord1000(stem))):
            upperBound = 4
        else:
            upperBound = 5

    
    

    
    entryWords = re.findall(r'\w+', stem)
    length = len(entryWords)

    
    
    for maxLength in maxLengths:
        if length > maxLength:
            lowerBound += 1


    tempUpperBound = 8
    for minLength in minLengths:
        if length < minLength:
            tempUpperBound -= 1
    
    if tempUpperBound < upperBound:
        upperBound = tempUpperBound



    
    tokens = nltk.word_tokenize(stem)
    tags = nltk.pos_tag(tokens)
        
    ccCount = 0

    for tag in tags:
        if (tag[1] == "CC"):
            ccCount += 1
    
    


    print "response: " + row[2]
    print "actual score: " + row[3]
    print "stem length: " + str(length)
    print "lower bound: " + indexToStage(lowerBound)
    print "upper bound: " + indexToStage(upperBound)
    print "\n"

    """if (row[3] == "2"):
        stage2.append(row[2])
    if (row[3] == "2/3"):
        stage23.append(row[2])
    if (row[3] == "3"):
        stage3.append(row[2])
    if (row[3] == "3/4"):
        stage34.append(row[2])
    if (row[3] == "4"):
        stage4.append(row[2])
    if (row[3] == "4/5"):
        stage45.append(row[2])
    if (row[3] == "5"):
        stage5.append(row[2])
    if (row[3] == "5/6"):
        stage56.append(row[2])
    if (row[3] == "6"):
        stage6.append(row[2])
"""
stageOrder = ["2","2/3","3","3/4","4","4/5","5","5/6","6"]
#              0   1     2   3     4    5    6    7   8


#rareWord5000 checks if given stem has a word up in the 5000 most common words



for row in reader: 
    print row



# does it have a word out of the top 5000?
# if no, upperBound = 5




# does it have a word out of the top 1000?
# if no, upperBound = 4

# set lower bound and upper bound based on word length


# within those parameters, guess by # of coordinating conjunctions

# compare to real stage 

# take abs value of difference and output it. 
