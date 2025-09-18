fruits = ['apple', 'banana', 'cherry', 5]

print(fruits)
print(type(fruits))
print(isinstance(fruits, list))
print(len(fruits))

for i in fruits:
    print(i)
    print(type(i))




print(fruits[::-1])


name = 'alex'
print(name[::-1])


fruitnested = ['apple', 'banana', ['cherry', 'orange', 'grape'], 5]

for i in fruitnested:
    # print(type(i), fruitnested.index(i))
    if type(i) == list:
        print('List found!', fruitnested.index(i))


fruitnested[2][1] = 'alex'

print(fruitnested)


fruitnested.append(["kiwi", "mango"])
print(fruitnested)


fruitnested[2].remove('cherry')
print(fruitnested)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)


























