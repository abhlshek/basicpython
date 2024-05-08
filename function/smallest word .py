# a = "and", "andaman", "andorra"
# print("Andorra".startswith("And"))              # startswith()
# print("Andorra".startswith("No"))
# print("andaman".endswith("and"))                # endswith()
# print("andaman".endswith("man"))
# print("and".endswith("d"))
# print("and".endswith("s"))

words = ["antelope", "and", "andaman", "andorra","antelop"]
n = len(words)
minwordposition = 0
minlength = len(words[minwordposition])
for i in range(1, n):
    if len(words[i]) < len(words[minwordposition]):
        minwordposition = i
print(minwordposition)
words[0], words[minwordposition] = words[minwordposition], words[0]
print(words)
currentlength = 0
word = words[0]
print(word)
# char = word[0]
# for i in words:
#     if not i.startswith(char):
#         print("Done at ", i)
#         break
