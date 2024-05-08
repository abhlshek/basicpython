# word = 'andd'
words = ["andelope", "and", "andaman", "andorra"]
n = len(words)
minwordposition = 0
minlength = len(words[minwordposition])
for i in range(1, n):
    if len(words[i]) < len(words[minwordposition]):
        minwordposition = 1
print(minwordposition)
words[0], words[minwordposition] = words[minwordposition], words[0]
print(words)
concurrentlenth = 0
word = words[0]

n = len(word)
s = ""
length = 0
while length <= n:
    result = True
    s = word[:length]
    # print(s)

    for currentword in words:
        if not currentword.startswith(s):
            result = False
            break
    length += 1
    if not result:
        length -= 2
        s = s[:length]
        break
print(s, length)

