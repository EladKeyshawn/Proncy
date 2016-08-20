import dicts


normLetter = dicts.enLetterToHeb
remMidVowels = dicts.remMidVowels

def isRegLetter(letter):
    return letter in normLetter


def isVowelLetter(currLetter):
    return currLetter in dicts.vowelsDict


def checkBeginPronun(currLetter):
    return currLetter in dicts.wordBeginPronun



class WordAnalyzer:
    def __init__(self, givenInput, len):
        self.input = givenInput
        self.length = len


    def startAnalyzing(self):
        print("Starting analysis...")
        engString = self.input
        index = 0
        while index < len(engString):
           currLetter = engString[index]
           if checkBeginPronun(currLetter):
               print dicts.wordBeginPronun[currLetter] ,

           elif isRegLetter(engString[index]):
               print normLetter[engString[index]],

           elif (index + 1 < self.length and index > 0):
               befAndAf = engString[index-1] + engString[index+1]
               midLetter = engString[index]

               if isRegLetter(midLetter) and ( befAndAf in remMidVowels):
                   print(remMidVowels[befAndAf] , normLetter[midLetter] ,)

           elif isVowelLetter(currLetter):
               print dicts.vowelsDict[currLetter],

           index += 1



word = WordAnalyzer("idle", 6)
word.startAnalyzing()


'''
     *** Comments and new cases for improving algorithm ***
     - check 'u' letter between two reg letters

'''
