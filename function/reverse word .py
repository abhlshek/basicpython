s = "this is a train"
words = s.split()
print(words)
rev = ""
for i in words:
    rev = i + " " + rev
print(rev)
