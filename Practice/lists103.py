

listofsqr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

new_list = []

k = 0
for i in listofsqr:
    k = i * i
    if k % 2 == 0:
        new_list.append(k)
print(new_list)
print('LENGTH:', len(new_list))


list_of_words = ['hello', 'world', 'my', 'name', 'is', 'alex']


new_list = []

for i in list_of_words:
    if len(i) > 3:
        new_list.append(i.upper())


print(new_list)


list_of_lists = [[1,2],[3,4,5],[6]]

special_list = []
print(len(list_of_lists))
for i in list_of_lists:
    print(i)
    for k in i:
        print(k)
        special_list.append(k)

print(special_list)




list_of_tuples = [1,2,3,4,5,6,7,8,9,10]
new_tuples_list = []

g = 0
k = 0

for i in list_of_tuples:
    k = i * i
    new_tuples_list.append((i, k))
    print(type(new_tuples_list[g]))
    g += 1

print(new_tuples_list)

'''
5
'''

list_of_50 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
new_list_50 = []

for i in list_of_50:
    if i % 3 == 0 and i % 5 != 0:
        new_list_50.append(i)


print(new_list_50)






































