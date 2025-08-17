'''Swap First and Last Elements in List'''

list = [1,2,3,4]
new_list = list[:]

leng = len(list)

new_list[0] = list[leng - 1]
new_list[leng - 1] = list[0]

print(new_list)
print(list)


''''Find the Maximum Number in a List'''
originallist = [1, 2, 9, 7, 5]
maxnum = originallist[0]
for i in range(len(originallist)):
    if maxnum <= originallist[i]:
        maxnum = originallist[i]

print(maxnum)


'''remove all even numbers from a list'''
listlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
newbrandlist = []

for i in range(len(listlist)):
    if listlist[i] % 2 != 0:
        newbrandlist.append(listlist[i])
print(newbrandlist)


'''Replace spaces in dictionary keys with hyphens'''
original = {
    "first name": "Alex",
    "last name": "Smith",
    "age": 30
}

new_dict = {}

for i in original:
    newkey = i.replace(" ", "-")
    new_dict[newkey] = original[i]

print(new_dict)


'''Remove Empty Values from Dictionary'''
original = {
    "name": "Alex",
    "age": None,
    "email": "",
    "hobbies": [],
    "city": "Toronto"
}

cleaned_dict = {}

for key, value in original.items():
    if value not in [None, "", [], {}, ()]:
        cleaned_dict[key] = value

print(cleaned_dict)


'''Sort Dictionary by Values Using External List and Dict'''
scores = {
    "Alice": 90,
    "Bob": 70,
    "Charlie": 85,
    "David": 95
}

# Copy of keys to track which keys remain unsorted
keys = list(scores.keys())

# External list to store keys sorted by their values
sorted_keys = []

# External dict to build the sorted dictionary
sorted_dict = {}

while keys:
    # Find key with smallest value
    min_key = keys[0]
    for key in keys:
        if scores[key] < scores[min_key]:
            min_key = key
    # Add min_key to sorted keys list
    sorted_keys.append(min_key)
    # Remove from keys list (unsorted keys)
    keys.remove(min_key)

# Build the sorted dict using sorted keys
for key in sorted_keys:
    sorted_dict[key] = scores[key]

print(sorted_dict)