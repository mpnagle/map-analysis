
averageCCarray = []
minCCarray = []
maxCCarray = []

allStages = [stage2,stage23,stage3,stage34,stage4,stage45,stage5,stage56,stage6]

for stage in allStages:
    
    entryCount = 0
    
    minCC = 1000
    maxCC = 0
    totalCC = 0

    for stem in stage: 
    
        tokens = nltk.word_tokenize(stem)
    #print tokens
        
        tags = nltk.pos_tag(tokens)
        
    #print tags
        
        ccCount = 0

        for tag in tags:
    
            #adjective counter
   #         if ((tag[1] == "JJR") or (tag[1] == "JJ") or (tag[1] == "JJS")):
            #adverb counter
             if ((tag[1] == "RB") or (tag[1] == "RBR") or (tag[1] == "RBS")):
                ccCount += 1
                #print "CC found"
        
        if (ccCount < minCC):
            minCC = ccCount
        
        if (ccCount > maxCC):
            maxCC = ccCount
    
        totalCC += ccCount    
        entryCount += 1

    aveCC = float(totalCC) / entryCount
    
    averageCCarray.append(aveCC)
    minCCarray.append(minCC)
    maxCCarray.append(maxCC)


print "average CCs used within a stage"
print averageCCarray

print "minimum CCs used across all stems in a stage"
print minCCarray

print "maximum CCs used across all stems in a stage"
print maxCCarray


allLengths = []
for stage in allStages:
    length = len(stage)
    allLengths.append(length)

print allLengths
