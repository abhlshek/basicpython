s = "mahendar  singh Dhoni".lower()
words = s.split()
# print(words)
answer = ""
n = len(words)
for i in range(n):
    # print(words[i])
    word = words[i]
    first = str(word[:1])
    second = str(word[1:])
    name = first.capitalize() + second
    print(name)
    answer=answer+ " "+ name



print(answer)