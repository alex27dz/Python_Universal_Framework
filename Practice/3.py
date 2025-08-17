'''Replace spaces in dictionary keys with hyphens'''

d = {'first name': 'Nikki', 'last name': 'Smith'}

s = 'first name'
news = s.replace(' ', '-')

print(news)


print(d.keys())

newd = {}

for key in d.keys():
    newkey = key.replace(' ', '-')
    newd[newkey] = d[key]

print(newd)