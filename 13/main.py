import re

s = '43-589589453984343          jfkjsfldjhf ---- sldf sdsfdskldsflkk 993408955039490439034 JGGJGJGJjjjfjldlsoeo'

result = re.search(r'k.s', s)
print(result)

result = re.search(r'\d\d\d', s)
print(result)

result = re.search(r'\D', s)
print(result)

result = re.search(r'\s', s)
print(result)

result = re.search(r'\S', s)
print(result)

result = re.search(r'\w', s)
print(result)

result = re.search(r'\W', s)
print(result)

result = re.search(r'\bsd', s)
print(result)

result = re.search(r'\Bsd', s)
print(result)

result = re.search(r'\d*', s)
print(result)

result = re.search(r'\d+', s)
print(result)