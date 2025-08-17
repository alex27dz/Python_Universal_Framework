'''Find the second largest number in a list'''

originallist = [1, 2, 9, 7, 5]
first_max = second_max = originallist[1]
len = len(originallist)


for i in range(len):
    if originallist[i] > first_max:
        second_max = first_max
        first_max = originallist[i]
    elif originallist[i] > second_max and originallist[i] != first_max:
        second_max = originallist[i]

print(first_max, second_max)