def removeNewLine(word):
    return word[:-1].lower()

def testSubWord(fullWord,subWord):
    subwordLen = len(subWord)
    fullwordLen = len(fullWord)
    if len(fullWord) < len(subWord):
        return
    else:
        for i in range(0,fullwordLen-subwordLen):
            if fullWord[i:i+subwordLen] == subWord:
                if i == 0:
                    output = [2,subWord + "-" + fullWord[i+subwordLen:], fullWord]
                elif i == fullwordLen:
                    output = [3,fullWord[:i] + "-" + subWord, fullWord]
                else:
                    output = [1,fullWord[:i] + "-" + subWord + "-" + fullWord[i+subwordLen:], fullWord]
                return(output)
    return

def Main():
    inputWord = input("\nPlease input the word you would like to generate puns for.\n> ").lower()
    returnList1 = []
    returnList2 = []
    returnList3 = []
    if inputWord == "":
        return False

    for word in wordsList:
        possibleSubWord = testSubWord(word,inputWord)
        if possibleSubWord != None:
            if possibleSubWord[0] == 1:
                returnList1.append([possibleSubWord[1],possibleSubWord[2]])
            elif possibleSubWord[0] == 2:
                returnList2.append([possibleSubWord[1],possibleSubWord[2]])
            elif possibleSubWord[0] == 3:
                returnList3.append([possibleSubWord[1],possibleSubWord[2]])
            else:
                print("ERROR - word type not recognised: " + str(possibleSubWord[0]))
    
    if len(returnList2) > 0:
        print("STARTING WORDS:")
        for word in returnList2:
            print(word[0])
    
    if len(returnList1) > 0:
        print("\nCENTRAL WORDS:")
        for word in returnList1:
            print(word[0])
        
    if len(returnList3) > 0:
        print("\nFINISHING WORDS:")
        for word in returnList3:
            print(word[0])

    return True

mode = ""
while mode != "AW" and mode != "CW":
    mode = input("Would you like to use All Words (AW) or Common Words (CW)?\n>")

if mode == "CW":
    filename = "commonWords.txt"
else:
    filename = "words.txt" 

with open(filename) as wordsDoc:
    lines = wordsDoc.readlines()
wordsList = list(map(removeNewLine, lines))

running = True
if __name__ == "__main__":
    while running:
        running = Main()
        input()