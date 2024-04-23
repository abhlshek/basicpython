a = [1,2,3,2,1]
n = len(a)
left = 0
result = "Palindrome"
right = n - 1
while left < right:
    print(a[left], a[right])
    if a[left] != a[right]:
        result = "Not Palindrome"
        break
    left += 1
    right -= 1
print(result)
