#Ass2 Day5

import string
isCapWord = lambda element : string.capwords(element,sep=None)
myList = ["hey this is omkar","i am in omerga","....."]
newlist = list(map(isCapWord,myList))
print(newlist)
