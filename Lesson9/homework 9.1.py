str_b = b'r\xc3\xa9sum\xc3\xa9'
str_utf = str_b.decode(encoding='utf-8')
print(str_utf)
print(str_utf.encode(encoding='Latin 1'))

