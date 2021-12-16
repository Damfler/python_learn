number = set([5, 1, 1, 1, 3, 4, 2, 3])
number.add(6)
number.discard(2)
number.remove(4)
number.pop()

# for i in number:
#     print(i)
# number.clear()
# print(3 in number)

numbers = {2, 6, 54, 42, 3}
# numbers_two = number.union(numbers)
# numbers_two = number | numbers

# numbers_two = number.intersection(numbers)
# numbers_two = number & numbers

# numbers_two = number - numbers

numbers_two = numbers.copy()

# print(numbers_two)
# print(len(numbers_two))

number = frozenset({5, 1, 1, 1, 3, 4, 2, 3})
print(number)