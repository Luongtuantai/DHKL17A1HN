Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 5
>>> s = 1 + x + x**3/3 + x**5/5
>>> print(s)
672.6666666666666
>>> #bài 7.2
>>> result = 1 + 2
>>> print('result =',result)
result = 3
>>> original_result = result
>>> result = result + 1
>>> print('result =',result)
result = 4
>>> result = result - 1
>>> print('result =',result)
result = 3
>>> original_result = result
>>> result = result * 2
>>> original_result = result
>>> print('result =',result)
result = 6
>>> result = result ** 3
>>> original_result = result
>>> print('result =',result)
result = 216
>>> result = result + 8
>>> original_result = result
>>> print('result =',result)
result = 224
>>> result = result % 7
>>> original_result = result
>>> print('result =',result)
result = 0
>>> result = result // 2
>>> original_result = result
>>> print('result =',result)
result = 0
