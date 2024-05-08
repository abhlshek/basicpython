s = "mahender singh dhoni"
words = s.split()
print(words)
answer = ""
n = len(words)
for i in range(n - 1):
    word = words[i]
    answer = answer + word[0]
answer = answer + " " + words[-1]
print(answer)



s = "abhishek singh yadav"
words = s.split()
print(words)
answer = ""
n = len(words)
for i in range(n - 1):
    word = words[i]
    answer = answer + word[0]
answer = answer + ' ' + words[-1]
print(answer)
