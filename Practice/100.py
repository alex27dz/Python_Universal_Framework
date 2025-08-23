st1= ' alex '
st2 = 'King'
st3 = st1 + " " + st2
dicthelper = {}
print(len(st1))

for i in range(len(st1)):
    dicthelper[i] = st1[i]

print(dicthelper)


st4 = st1 * 3
print(st4)

print(st1.lower())
print(st1.upper())
print(st1.strip())

st5 = '-'.join(st1)
print(st5)

listof = ['life','is','good']
finalste = " ".join(listof)
print(finalste)

st6 = st2.replace('K','A')
print(st6.lower())




word = 'python'

for i in word:
    print(i)


print('I wanna print somethin {}{}{} and nice'.format(word, st1, st2))