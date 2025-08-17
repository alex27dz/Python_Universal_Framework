stringof = "Hello World ddddddd"

dictofchars = {}

for char in stringof:
    dictofchars[char] = stringof.count(char)

print(dictofchars)


