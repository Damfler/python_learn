s = []
for i in range(1, 21):
    if i % 5 == 0:
        s.append(i)
print(s)

s1 = [i for i in range(1, 21) if i % 5 == 0]
print(s1)

s2 = {i: i ** 2 for i in s}
print(s2)