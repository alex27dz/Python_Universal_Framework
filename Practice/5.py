original = {
    "name": "Alex",
    "age": None,
    "email": "",
    "country": "Canada"
}

cleaned = {}
noncleaned = {}

for key in original:
    value = original[key]
    if value is not None and value != "":
        cleaned[key] = value
    else:
        noncleaned[key] = value

print(cleaned)
print(noncleaned)
