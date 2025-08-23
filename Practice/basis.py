listofnum = [5, 2, 9, 1, 5, 6]
rangeofi = len(listofnum)


for i in range(0,rangeofi):
    min = listofnum[0]
    for k in listofnum:
        if min > k:
            min = k
    print(min)
    listofnum.remove(min)







