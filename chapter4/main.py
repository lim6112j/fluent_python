# chap4 Text Versus Bytes
s = 'café'
len(s)
b = s.encode('utf8')
len(b)
b.decode('utf8')

# byte essential
cafe = bytes('café', encoding='utf_8')
cafe[0]
cafe_arr = bytearray(cafe)
cafe_arr[-1:]

