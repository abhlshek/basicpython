a = [1, 2, 1, 1, 3, 3, 1, 1, 1]

frequencies = dict()
for x in a:
    f = frequencies.get(x, 0) + 1
    frequencies[x] = f
print(frequencies)

x = {"apple": 1, "banana": 2, "cherry": 3}
apple_value = x.get("apple")
print(apple_value)
