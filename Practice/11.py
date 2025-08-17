s1 = "Alex is king"
s2 = "xela is King"

news1 = s1.replace(" ", "")
news2 = s2.replace(" ", "")

news1 = news1.lower()
news2 = news2.lower()

dictofchars1 = {}
dictofchars2 = {}

for char in news1:
    numofchars1 = news1.count(char)
    dictofchars1[char] = numofchars1

print(dictofchars1)

for char in news2:
    numofchars2 = news2.count(char)
    dictofchars2[char] = numofchars2

print(dictofchars2)


if dictofchars1 == dictofchars2:
    print("True")
else:
    print("False")

