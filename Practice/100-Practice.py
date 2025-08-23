s = 'Python'
prints = 'tho'

startindex = s.find(prints)
print(startindex)
print(len(prints))

newS = s[startindex:startindex + len(prints)]
print(newS)

"----------------------------------------"


stringCount = 'Banana'
counta = stringCount.count('a')

counter = 0
for i in stringCount:
    if i == "a":
        counter += 1

if counta == counter:
    print("The count is correct")
    print(counter, counta)

"----------------------------------------"

stringcheck = 'pyword'
check = 'Py'
if stringcheck[0:len(check)].lower() == "Py".lower():
    print(True)
else:
    print(False)

"----------------------------------------"

convert = ' hello world '
conv1 = convert.strip()
print(conv1)
convert5 = conv1.replace(' ', '-')
print(convert5.upper())

convert2 = ' hello world '
convert3 = convert2.split()
print(type(convert3))
convert4 = '-'.join(convert3)
print(convert4.upper())

"----------------------------------------"

s = "DataScience"
for char in s:
    print(char + '\n')

"----------------------------------------"












