print("""1
2
3
4
5
6
7
8
9
10""")

hi = 'Hello'
world = 'World'
print(hi+' '+world+'!')
print(hi*5)
print(hi[0])
print(hi[-1])
print(hi[0:4])

print(hi.upper())
print(hi.lower())
print(hi.capitalize())

text = 'Hello world i Dima'
text_split = text.split(' ')
print(text_split)

spisok = ['a', 'b', 'c']
spisok_join = ','.join(spisok)
print(spisok_join)

text = '               Hello world, i Dima               '
print(text.strip())
print(text.lstrip())
print(text.rstrip())
print(text.replace('Dima', 'Dmitriy'))