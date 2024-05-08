s = "Madam"
rev = ""
for x in s:
    rev = x + rev
print(rev)
if s.capitalize() == rev.capitalize():
    print(s ," is Palindrome")
else:
    print(s ,"not is palindrome")
