def makeDictionary():
    wordDic = dict()
    pw = open("positive-words.txt", "r")
    nw = open("negative-words.txt", "r")

    for word in pw:
        wordDic[word] = 1

    for word in nw:
        wordDic[word] = -1
        
    return wordDic

worddict = makeDictionary()