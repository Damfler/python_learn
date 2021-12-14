# f = open('1.txt', 'w')
# f.write('Hello file!')
# f.close()

# f = open('1.txt', 'r')
# print(f.read())
# f.close()

# with open('1.txt', 'a') as f:
#     f.write('\nHi, test two!')

try:
    a = int(input('a: '))
    b = int(input('b: '))
    print(a/b)
except ZeroDivisionError:
    print('ERROR: number zero')