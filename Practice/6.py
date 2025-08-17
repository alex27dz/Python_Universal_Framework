dictionary = {
    "Occupation":"senior qa dev",
    "name":"Alex",
    "age": 33
}

print(dictionary)

dictionary["Occupation"] = "Seftware Engineer"

print(dictionary)



print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())



for k,v in dictionary.items():
    print(k,v)

print(len(dictionary))

dictionary["city"] = "Toronto"

print(dictionary)

dictionary.pop("city")

print(dictionary)












