'''Remove all even numbers from a list'''

listlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
newbrandlist = []

len = len(listlist)


for i in range(len):
    if listlist[i] %2 != 0:
        print(listlist[i])
        newbrandlist.append(listlist[i])

print(newbrandlist)