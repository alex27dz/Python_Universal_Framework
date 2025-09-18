fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']


print(fruits[1], fruits[4])

fruits[2] = 'kiwi'
print(fruits[2])



fruits.append('mango')
print(fruits)

fruits.insert(1, 'orange')
A

print(fruits)
fruits.pop(-1)
print(fruits)

fruits.remove('apple')
print(fruits)


matrix = [[1,2], [3,4], [5,6]]
print(matrix[1][1])

j = 0
for i in fruits:
    print(i, fruits[j])
    j += 1


comp_list = [1,2,3,4,5,6,7,8,9,10]
new_list = []

for i in comp_list:
    k = i * i
    new_list.append(k)

print(new_list)
