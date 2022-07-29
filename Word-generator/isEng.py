def getDict(file):
	words = set()
	with open(file) as d:
		for w in d.read().split("\n"):
			words.add(w.lower())
	return words

def isEng(word):
	englishWords = getDict("dictionary.txt")
	return word in englishWords
print(isEng("boot"))