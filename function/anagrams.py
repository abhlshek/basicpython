x1 = "worth"
x2 = "throw"
x = [x1[i]for i in range(0, len(x1))]
x.sort()
y = [x2[i]for i in range(0, len(x2))]
y.sort()

if x == y:
    print("the string are anagrams")
else:
    print("the string are not anagram")
