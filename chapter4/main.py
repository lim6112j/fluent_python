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
import sys, locale
expressions = """
locale.getpreferredencoding()
type(my_file)
sys.stdout.isatty()
sys.stdout.encoding
sys.stdin.isatty()
sys.stdin.encoding
sys.stderr.isatty()
sys.stderr.encoding
sys.getdefaultencoding()
sys.getfilesystemencoding()
"""
my_file = open('dummy', 'w')
for expression in expressions.split():
    value = eval(expression)
    print(expression.rjust(30), '->', repr(value))
