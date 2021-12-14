# tuple = ("first", 25, 25.1,)
# print(type(tuple))

# print(tuple([45,45,14,45]))
# print(list((45,45,14,45)))

dist = {
    'key':'value',
    'key-2': 'value-2',
    'key-3': 'value-3',
    }
print('all',dist)
for k in dist.keys():
    print(k)
for val in dist.values():
    print(val)
for k in dist.items():
    print(k)

del(dist['key-2'])
print(dist)