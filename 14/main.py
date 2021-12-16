# def rectangle_area(a, b):
#     return a * b
# print(rectangle_area(4,5))

print((lambda a, b: a * b)(4, 5))
print((lambda a, b: a if a > b else b)(4, 5))