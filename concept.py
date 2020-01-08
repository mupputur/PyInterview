Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = "S101-23-45"
>>> 
>>> x
'S101-23-45'

>>> x.split("-")
['S101', '23', '45']
>>> 
>>> def get_splited_values(str1):
	x = str1.split("-")
	return x[-1]

>>> 
>>> ["S101-23-45","S102-24-23","S103-23-62","S104-23-20","S105-23-23"]
['S101-23-45', 'S102-24-23', 'S103-23-62', 'S104-23-20', 'S105-23-23']
>>> 
>>> x = ["S101-23-45","S102-24-23","S103-23-62","S104-23-20","S105-23-23"]
>>> x
['S101-23-45', 'S102-24-23', 'S103-23-62', 'S104-23-20', 'S105-23-23']
>>> 
>>> for e in x:
	print(get_splited_values(e))

	
45
23
62
20
23
>>> y = lambda str1: str1.split("-")[-1]
>>> y
<function <lambda> at 0x03208C88>
>>> x = ["S101-23-45","S102-24-23","S103-23-62","S104-23-20","S105-23-23"]
>>> for e in x:
	print(y(e))

	
45
23
62
20
23
>>> 
