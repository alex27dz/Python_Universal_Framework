original = {
    "name": "Alex",
    "age": None,
    "email": "",
    "country": "Canada"
}

# First collect the keys to remove
keys_to_remove = []
for key in original:
    if original[key] is None or original[key] == "":
        keys_to_remove.append(key)
print(keys_to_remove)
# Then remove them
for key in keys_to_remove:
    del original[key]

print(original)








