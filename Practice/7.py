dictionary = {
    "Occupation is good": "senior qa dev",
    "name is mine": "Alex",
    "age of me": 33
}

new_dictionary = {}

for k,v in dictionary.items():
    print(type(k), type(v))
    new_k = k.replace(" ", "-")
    new_dictionary[new_k] = v

print(new_dictionary)


