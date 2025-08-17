string = "alex is the king"

revstring = string.split()
revdict = {}
tempstring = []

print(revstring)
print(len(revstring))


for i in range(0, len(revstring)):
    tempstring.append(revstring[i][::-1])


print(tempstring)