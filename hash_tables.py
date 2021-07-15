#Create a hash table all at once
items1 = dict({"key1":1, "key2":2, "key3":"three"})
print(items1)

#Create a hash table progressively
items2 = {}
items2["key1"] = 1
items2["key2"] = 2
items2["key3"] = 3
items2["key4"] = 4
print(items2)

#Iterate the keys and values in the dictionary
for key, value in items2.items():
    print("key: ", key, " value: ", value)