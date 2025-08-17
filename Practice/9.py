original = {'apple': 5, 'banana': 2, 'orange': 8}

listofdict = list(original.items())

print(listofdict)

for i in range(len(listofdict)):
    for j in range(i + 1, len(listofdict)):
        if listofdict[i][1] < listofdict[j][1]:
            temp = listofdict[i]
            listofdict[i] = listofdict[j]
            listofdict[j] = temp

print(listofdict)

sorted_dict = dict(listofdict)
print(sorted_dict)