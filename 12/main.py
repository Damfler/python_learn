import re

s = 'AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC'
result = re.match('AC', s)
print(result)

result = re.search('DC', s)
print(result)

result = re.findall('AC', s)
print(result)

result = re.split('/', s)
print(result)

result = re.match('AC', s)
print(result)

result = re.sub('A', 'D', s)
print(result)

result = re.fullmatch('AC', s)
print(result)