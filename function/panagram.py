s = "A quick brown fox jumps over the lazy dog"
letters = "abcdefghijklmnopqrstuvwxyz"
ispanagram = True
for i in letters:
    if i not in s:
        ispanagram = False
        break
print(ispanagram)
if ispanagram:
    print(" panagram")

else:
    print("no,panagram")



