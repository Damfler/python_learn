# # # with open('27-1a.txt') as f:
# # #     n = int(f.readline())
# # #     for i in range(n):
# # #         a, b = map(int, f.readline().split())
# # #         print(a,b)

# # def f(a,b):
# #     return a * b

# # a = map(f, [3,6,2], [6,2,7])
# # print(list(a))

# from functools import reduce
# print(reduce(lambda a, b: a * b, (1, 3, 2)))

a = [1,2,3,4,5]
b = 'abcde'
result = zip(a,b)
print(list(result))