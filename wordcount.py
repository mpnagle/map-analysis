import csv
import re

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

#print commonWords

commonWords500 = commonWords[1:501]
commonWords1000 = commonWords[1:1001]
commonWords2500 = commonWords[1:2501]

print commonWords500


# make a var with stage specific responses

stage2 = []
stage23 = []
stage3 = []
stage34 = []
stage4 = []
stage45 = []
stage5 = []
stage56 = []
stage6 = []

for row in reader:
    if (row[3] == "2"):
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

stageOrder = ["2","2/3","3","3/4","4","4/5","5","5/6","6"]



allStages = [stage2,stage23,stage3,stage34,stage4,stage45,stage5,stage56,stage6]

allWordCounts = []

allMinLengths = []

allMaxLengths = []


# getting min, ave, max word counts by stage
for stage in allStages:

    entryCount = 0
    totalLength = 0
    minLength = 1000
    maxLength = 0
    for entry in stage:
#        print entry
        entryCount += 1

        currentLength = len(re.findall(r'\w+', entry))
        totalLength += currentLength
        
        if currentLength < minLength:
            minLength = currentLength

        if currentLength > maxLength:
            maxLength = currentLength
        

    wordCount = totalLength / entryCount
    allWordCounts.append(wordCount)
    allMinLengths.append(minLength)
    allMaxLengths.append(maxLength)


print "average word counts:"
print allWordCounts

print "minimum word length"
print allMinLengths

print "maximum word length"
print allMaxLengths


#percentage of words in response out of top 5000 words (rarity test)

allRareWords = []
minRareWords = []
maxRareWords = []
zeroCount = 0

for stage in allStages:


    rareMin = 1000
#   rareMin = 1
    rareMax = 0
    totalFreq = 0
    
    entryCount = 0



    for entry in stage:

        entryCount += 1

        entryWords = re.findall(r'\w+', entry)
        entryLength = len(entryWords)

        rareWords = 0        
        for word in entryWords:

            if ( (len(word) > 3) and (word not in commonWords500)):
                rareWords +=1

    
        rarePercent = 0
        
        if entryLength > 0:

            rarePercent = (float(rareWords) / entryLength) 
        
#        if rarePercent == 1 :
#            print entry

        if rarePercent == 0:
#            print entry
            zeroCount += 1

        #print rarePercent
    
           
        if (rarePercent < rareMin):
            rareMin = rarePercent

        if (rarePercent > rareMax):
            rareMax = rarePercent

            


        totalFreq += rarePercent
        """

        if (rareWords < rareMin):
            rareMin = rareWords
    
        if (rareWords > rareMax):
            rareMax = rareWords
        
        totalFreq += rareWords
        """
        
    wordCount = float(totalFreq) / entryCount
    
    allRareWords.append(wordCount)
    minRareWords.append(rareMin)
    maxRareWords.append(rareMax)


print "average rare word percentage"
print allRareWords

print "minimum rare word percentage"
print minRareWords

print "maximum rare word percentage"
print maxRareWords
        
print "number of entries with zero rare words"
print zeroCount




ifile.close()
ifile2.close()
