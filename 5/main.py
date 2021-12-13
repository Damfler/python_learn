spisok = []
numbers = [3, 4, 5, 9, 10, 12]
print(numbers)
numbers = [1, 5, 2, 7, 'name']
print(numbers)

# Список = массив

for number in numbers:
    print(number)

numbers.append(6)
print(numbers)

numbers.pop()
print(numbers)

n = numbers.index('name')
print(n)

print(len(numbers))

numbers = [3, 4, 5, 9, 10, 12]
numbers.sort(reverse=True)
print(numbers)