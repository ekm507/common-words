import io

textBook = io.open('input.txt', 'r', encoding='utf-8')

wordList = list()
for line in textBook:
    wordList.extend(list(str(line).split(' ')))

wordDict = dict()

for word in wordList:
    wordDict[word] = 0

for word in wordList:
    wordDict[word] += 1

sortedWordDict = list(sorted(wordDict.items(), key=lambda x: x[1], reverse=True))

print(len(wordDict), ' words found.')

print('most common words:')

outputFile = io.open('common.txt', 'w', encoding='utf-8')

i = 0
for k in sortedWordDict:
    i += 1
    outputFile.write(str(k[0]) + ' ' + str(k[1]) + '\n')
    if(i < 20):
        print(i, k)


textBook.close()
outputFile.close()
