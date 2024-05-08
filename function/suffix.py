words = ["prettiest", "best", "nicest", "surest"]
n = len(words)
minwordposition = 0
minlength = len(words[minwordposition])
for i in range(1, n):
    if len(words[i]) < len(words[minwordposition]):
        minwordposition = 1
# print(minwordposition)
words[0], words[minwordposition] = words[minwordposition], words[0]
# print(words)
concorrentlength = 0
word = words[0]
# print(word)
# Found smallest word
#  t, st,est,best
n = len(word)
s = ""
length = -1
result = True
for i in range(-1, -n - 1, -1):
    # print(i)
    s = word[i:]
    # print(s)
    for currentword in words:
        print(currentword, s, currentword.endswith(s))
        if not currentword.endswith(s):
            result = False
            answer = s
            # print(answer)
            # print(result)
            break
    if not result:
        break

answer=answer[1:]
print(answer)
