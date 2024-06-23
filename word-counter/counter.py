
import operator
import sys;

filePath = sys.argv[1]
filename = sys.argv[1].replace("./word-counter/", "").replace(".txt", "")

file = open (filePath, "r")

print (sys.argv)

content = file.read()
file.close()
words = {};


for word in content.split():
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

sorted_x = sorted(words.items(), key =operator.itemgetter(1), reverse=True)

newFilePath = "./word-counter/{}-count.txt".format(filename)
file = open(newFilePath, "w")
print(sorted_x)
for word in sorted_x:
    file.write("{} - {}\n".format(word[0], word[1]))
file.close()
# open("./word-counter/word-count.txt", "w").write()