# Questions

# Data Types 


1. Write a Python program to count the number of characters (character 
frequency) in a string. Sample String : google.com' 
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1} 


string = 'hello hahha'
char_list = []
dict1 = {}

for st in range(len(string)):
  if string[st] in char_list:
    dict1[string[st]] = dict1[string[st]] + 1

  else:
    char_list.append(string[st])
    dict1[string[st]] = 1

print(char_list)
print(dict1)

    
2. Write a Python program to get a string made of the first 2 and the last 2 chars 
from a given a string. If the string length is less than 2, return instead of the 
empty string. 
Sample String : 'Python' 
Expected Result : 'Pyon' 
Sample String : 'Py' 
Expected Result : 'PyPy' 
Sample String : ' w' 
Expected Result : Empty String 


str1 = input('Enter any string: ')
if len(str1)<2:
  new_str = 'Empty string'
else:
  new_str = str1[:2] + str1[-2:]
print(new_str)

    
3. Write a Python program to get a string from a given string where all 
occurrences of its first char have been changed to '$', except the first char itself. 
Sample String : 'restart' 
Expected Result : 'resta$t' 


str1 = input('Enter any string: ')
first = str1[0]
str1 = str1.replace(first,"$")
new_str = str1.replace("$",first,1)
print(new_str)


    
4. Write a Python program to get a single string from two given strings, separated 
by a space and swap the first two characters of each string. 
Sample String : 'abc', 'xyz' 
Expected Result : 'xyc abz' 


str1 = input('Enter any string: ')
str2 = input('Enter any string: ')
first1 = str1[0]
first2 = str2[0]

str1 = str1.replace(first1,first2,1)
str2 = str2.replace(first2,first1,1)
new_str = str1 + ' ' + str2
print(new_str)


    
5. Write a Python program to add 'ing' at the end of a given string (length should 
be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the 
string length of the given string is less than 3, leave it unchanged. 
Sample String : 'abc' 
Expected Result : 'abcing' 
Sample String : 'string' 
Expected Result : 'stringly' 


str1 = input('Enter any string: ')
if str1[-3:] == 'ing':
  str1 = str1 + 'ly'
elif len(str1)>=3:
  str1 = str1 + 'ing'
print(str1)


    
6. Write a Python program to find the first appearance of the substring 'not' and 
'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' 
substring with 'good'. Return the resulting string. 
Sample String : 'The lyrics is not that poor!' 
'The lyrics is poor!' 
Expected Result : 'The lyrics is good!' 
'The lyrics is poor!' 



str1 = input('Enter any string: ')

idx1 = str1.find('not')
print(idx1)

idx2 = str1.find('poor')
print(idx2)

print(str2)

if idx1 < idx2:
  str2 = str1[idx1:idx2+len("poor")]

  str1 = str1.replace(str2, 'good')


print(str1)



7. Write a Python function that takes a list of words and returns the length of the 
longest one. 



str1 = input('Enter multiple words separated by space: ')
list1 = list(str1.split(' '))
max_length = max(map(lambda x: len(x), list1))
print(max_length)



8. Write a Python program to remove the nth index character from a nonempty 
string. 


str1 = input('Enter the string: ')

idx = int(input('Enter the index: '))

if len(str1) != 0:
  str1 = str1.replace(str1[idx], '')
print(str1)



9. Write a Python program to change a given string to a new string where the first 
and last chars have been exchanged. 



str1 = input('Enter any string: ')
first = str1[0]
last = str1[-1]
str1 = str1.replace(first,last,1)
str1=str1[::-1]
str1 = str1.replace(last,first,1)
str1=str1[::-1]
print(str1)




10. Write a Python program to remove the characters which have odd index 
values of a given string. 



str1 = input('Enter the string: ')
result = ''
for i in range(len(str1)):
  if i%2 == 0:
    result = result + str1[i]
  
print(result)




11. Write a Python program to count the occurrences of each word in a given 
sentence. 



string = input('Enter any sentence: ')
char_list = []
dict1 = {}

for st in range(len(string)):
  if string[st] in char_list:
    dict1[string[st]] = dict1[string[st]] + 1

  else:
    char_list.append(string[st])
    dict1[string[st]] = 1

print(char_list)
print(dict1)




12. Write a Python script that takes input from the user and displays that input 
back in upper and lower cases. 



str1 = input('Enter any string: ')
print(str1.upper())
print(str1.lower())





13. Write a Python program that accepts a comma separated sequence of words 
as input and prints the unique words in sorted form (alphanumerically). 
Sample Words : red, white, black, red, green, black 
Expected Result : black, green, red, white,red 



input1 = input('Enter the words separated by comma only: ')
list1 = input1.split(',')

list1 = sorted(set(list1))

print(list1)



    
14. Write a Python function to create the HTML string with tags around the 
word(s). 
Sample function and result : 
add_tags('i', 'Python') -> '<i>Python</i>' 
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>' 



def add_tags(tag, word):
  html_string = f"'<{tag}>{word}</{tag}>'"
  print(html_string)

tag = input('Enter the tag: ')
word = input('Enter the word: ')
add_tags(tag,word)




15. Write a Python function to insert a string in the middle of a string. 
Sample function and result : 
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]] 
insert_sting_middle('{{}}', 'PHP') -> {{PHP}} 



def insert_string_middle(str1, str2):
  mid = len(str1)//2
  str1 = str1[:mid] + str2 + str1[mid:]
  print(str1)

insert_string_middle('[[[]]]', 'apple')




16. Write a Python program to sum all the items in a list. 



from functools import reduce

str1 = input('Enter numbers separated by space: ')
numbers_list = str1.split(' ')
result = reduce(lambda x,y: int(x) + int(y), numbers_list)
print(result)



17. Write a Python program to multiplies all the items in a list. 



from functools import reduce

str1 = input('Enter numbers separated by space: ')
numbers_list = str1.split(' ')
result = reduce(lambda x,y: int(x) * int(y), numbers_list)
print(result)




18. Write a Python program to get the largest number from a list. 



str1 = input('Enter numbers separated by space: ')
numbers_list = str1.split(' ')
list1 = map(lambda x: int(x), numbers_list)
print(max(list1))




19. Write a Python program to get the smallest number from a list. 



str1 = input('Enter numbers separated by space: ')
numbers_list = str1.split(' ')
list1 = map(lambda x: int(x), numbers_list)
print(min(list1))




20. Write a Python program to count the number of strings where the string 
length is 2 or more and the first and last character are same from a given list of 
strings. 
Sample List : ['abc', 'xyz', 'aba', '1221'] 
Expected Result : 2 



count = 0

str1 = input('Enter any number of words separated by space: ')
str_list = list(str1.split(' '))
for str_i in str_list:

  if len(str_i)>=2 and str_i[0]==str_i[-1]:
    count = count + 1

print(count)



    
21. Write a Python program to get a list, sorted in increasing order by the last 
element in each tuple from a given list of non-empty tuples. 
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)] 
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)] 



list1 = [(1,2), (2,1), (2,3), (4,1), (9,5), (2,7), (7,3), (1,9)]

list1.sort(key = lambda x: x[-1])
print(list1)



    
22. Write a Python program to remove duplicates from a list. 



list1 = [11,2,3,4,5,35,3,34,5,4,9,2,42,5,8,2,55,0,22,34]
list1 = list(set(list1))
print(list1)




23. Write a Python program to check a list is empty or not. 



list1 = []

if(len(list1) == 0):
  print('List is empty')
else:
  print('List is not empty')




24. Write a Python program to clone or copy a list. 



list1 = [1,2,2,3]
list2 = list1.copy()
print(id(list1))
print(id(list2))



25. Write a Python program to check whether all dictionaries in a list are empty or 
not. 
Sample list : [{},{},{}] 
Return value : True 
Sample list : [{1,2},{},{}] 
Return value : False 


list1 = [{}, {}]
list2 = [{'a':1}, {}]


print(not(any(list1)))


print(not(any(list2)))



    
26. Write a Python program to insert a given string at the beginning of all items in 
a list. 
Sample list : [1,2,3,4], string : emp 
Expected output : ['emp1', 'emp2', 'emp3', 'emp4'] 


lst=[1,2,4]
string='emp'
add_last = list(map(lambda x: string + str(x), lst))
print(add_last)



    
27. Write a Python program to replace the last element in a list with another list. 
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8] 
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8] 


list1 = [1,2,3,4,5,6,7,8,9]
list2 = [0,2,4,6,8]
list1.remove(list1[-1])
list1.extend(list2)
print(list1)



    
28. Write a Python script to add a key to a dictionary. 
Sample Dictionary : {0: 10, 1: 20} 
Expected Result : {0: 10, 1: 20, 2: 30} 


key=3
value=10000

dict1 = {0:10, 1:100, 2:1000}
dict1[key] = value
print(dict1)


    
29. Write a Python script to concatenate following dictionaries to create a new 
one. 
Sample Dictionary : 
dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60} 
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} 



dict1 = {0:10, 2:20}
dict2 = {3:30, 4:40}
dict3 = {5:50, 6:60}
final = {}

for key,value in dict1.items():
  final[key] = value
for key,value in dict2.items():
  final[key] = value
for key,value in dict3.items():
  final[key] = value
print(final)



    
30. Write a Python script to check whether a given key already exists in a 
dictionary. 



dict1 = {3:30, 4:40, 5:50, 6:60}
key_input = input('Enter the key to be searched: ')
print(int(key_input) in dict1)




31. Write a Python program to iterate over dictionaries using for loops. 



d = {'x': 1, 'y': 2, 'z': 3} 
for key, value in d.items():
    print(key, ':', value)





32. Write a Python script to generate and print a dictionary that contains a 
number (between 1 and n) in the form (x, x*x). 
Sample Dictionary ( n = 5) : 
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} 



dict1 = {}
input1 = int(input('Enter a number: '))
for i in range(1,input1+1):
  dict1[i] = i*i

print(dict1)


    
33. Write a Python script to print a dictionary where the keys are numbers 
between 1 and 15 (both included) and the values are square of keys 
Sample Dictionary 
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 
13: 169, 14: 196, 15: 225} 



dict1 = {}

for i in range(1,16):
  dict1[i] = i*i

print(dict1)




34. Write a Python script to merge two Python dictionaries. 



final = {}

def merge_dict(dict1, dict2):
  for key,value in dict1.items():
    final[key] = value
  for key,value in dict2.items():
    final[key] = value

merge_dict({'x': 1, 'y': 2, 'z': 3} , {3:30, 4:40, 5:50, 6:60})

print(final)




35. Write a Python program to iterate over dictionaries using for loops. 


n = int(input("Enter a value:"))
d = {}

for i in range(n):
    keys = input('Enter the key: ')
    values = input('Enter the value: ')
    d[keys] = values

for key, value in d.items():
    print(key, ':', value)




36. Write a Python program to sum all the items in a dictionary. 



dict = {'a': 100, 'b':200, 'c':300}    
sum = 0
for i in dict.values(): 
  sum = sum + i 
       
print(sum)



37. Write a Python program to multiply all the items in a dictionary. 


dict = {'a': 100, 'b':200, 'c':300}    
prod = 1
for i in dict.values(): 
  print(i)
  prod = prod * i 
       
print(prod) 




38. Write a Python program to remove a key from a dictionary. 



d = {'a': 100, 'b':200, 'c':300}
key_input = input('Enter the key you want to delete: ')
if key_input in d:
  d.pop(key_input)
print(d)



39. Write a Python program to unpack a tuple in several variables. 



tup1 = 1,2,4,4,4

a,b,c,d,e = tup1
print(a,b,c,d,e)



40. Write a Python program to add an item in a tuple. 



tup1 = (1,2,4,3)
item = int(input('Enter an item to be added to tuple: '))

tup1 = *tup1 , item
print(tup1)



41. Write a Python program to convert a tuple to a string. 



tup1 = ('s','u','l','a','v')
str_tuple = ''.join(tup1)
print(str_tuple)



42. Write a Python program to convert a list to a tuple. 


list1 = [1,2,4,5,6]
tup = tuple(list1)
print(tup)



43. Write a Python program to remove an item from a tuple. 


item1 = input('Enter an item to be deleted from tuple: ')
tup1 = ('s','u','l','a','v')
list1 = list(tup1)
list1.remove(item1)
tup1 = tuple(list1)
print(tup1)



44. Write a Python program to slice a tuple. 


tup1 = ('s','u','l','a','v')
idx1 = int(input('Enter the start index to slice: '))
idx2 = int(input('Enter the end index(not inclusive): '))
print(tup1[idx1:idx2])


45. Write a Python program to find the index of an item of a tuple. 


tup1 = ('s','u','l','a','v')
item1 = input('Enter the element whose index to be searched: ')
print(tup1.index(item1))



46. Write a Python program to find the length of a tuple 



input1 = input('Enter the elements for a tuple(separated by space): ')

input1 = input1.split(' ')
tup1 = ('s','u','l','a','v')
print('Length of tuple is: ', end = '')
print(len(input1))




# Functions 




1. Write a Python function to find the Max of three numbers. 



def find_max(a,b,c):
  max_number = max(a,b,c)
  print(max_number)



2. Write a Python function to sum all the numbers in a list. 
Sample List : (8, 2, 3, 0, 7) 
Expected Output : 20 


def sum_list(list1):
  sum_lst = sum(list1)
  print(sum_lst)

sum_list([1,4,5,5])


    
3. Write a Python function to multiply all the numbers in a list. 
Sample List : (8, 2, 3, -1, 7) 
Expected Output : -336 


from functools import reduce

list1 = [1,4,5,-5]
result = reduce(lambda x,y: x*y, list1)
print(result)


    
4. Write a Python program to reverse a string. 
Sample String : "1234abcd" 
Expected Output : "dcba4321" 


def reverse_string(str1):
  str1 = str1[::-1]
  print(str1)
reverse_string('a,23,3')


    
5. Write a Python function to calculate the factorial of a number (a non-negative 
integer). The function accepts the number as an argument. 


def fact(n):
  if n == 1:
    return 1
  else:
    return n*fact(n-1)

print(fact(4))





6. Write a Python function to check whether a number is in a given range. 


def is_in_range(num, range_value):
  return num in range(range_value)

print(is_in_range(5,100))



7. Write a Python function that accepts a string and calculate the number of 
upper case letters and lower case letters. 
Sample String : 'The quick Brow Fox' 
Expected Output : 
No. of Upper case characters : 3 
No. of Lower case Characters : 12 


a='stRiNgS HahA'
upperCount = 0
lowerCount = 0
otherCharacters = 0

def count_upper_lower(a):
  for i in range(len(a)):
    if ord(a[i])>=65 and ord(a[i])<=90:
      global upperCount
      upperCount += 1
    elif ord(a[i])>=97 and ord(a[i])<=122:
      global lowerCount
      lowerCount += 1
    else:
      global otherCharacters
      otherCharacters += 1

  print('Upper count ',upperCount)
  print('Lower count ',lowerCount)
  print('Lower count ',otherCharacters)

count_upper_lower(a)


    
8. Write a Python function that takes a list and returns a new list with unique 
elements of the first list. 
Sample List : [1,2,3,3,3,3,4,5] 
Unique List : [1, 2, 3, 4, 5] 



def unique_list(lst):
  return list(set(lst))

print(unique_list([1,2,3,4,1,2,3,4,22,2,2,3,4,5,]))



    
9. Write a Python function that takes a number as a parameter and check the 
number is prime or not. 
Note : A prime number (or a prime) is a natural number greater than 1 and that 
has no positive divisors other than 1 and itself. 


count = 0

def isPrime(num):
  for i in range(1,num+1):
    if num%i == 0:
      global count
      count = count + 1
  
  if count > 2:
    print('It is not a prime number')
  else:
    print('It is a prime number')

input1 = int(input('Enter any number other than 0 and 1: '))
isPrime(input1)



10. Write a Python program to print the even numbers from a given list. 
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9] 
Expected Result : [2, 4, 6, 8] 


num_list = [1,2,3,4,6,7,3,3,5,7,4,3,4,4,5,5]

even_list = filter(lambda x: x%2 == 0, num_list)
print(list(even_list))



    
11. Write a Python program to create a lambda function that adds 15 to a given 
number passed in as an argument, also create a lambda function that multiplies 
argument x with argument y and print the result. 



add_result = lambda x: x+15

mul_result = lambda x,y: x*y

print(add_result(2))
print(mul_result(2,4))



12. Write a Python program to create a function that takes one argument, and 
that argument will be multiplied with an unknown given number. 



mul_result = lambda x: x*10
print(mul_result(2))



13. Write a Python program to sort a list of tuples using Lambda. 


list1 = [(1,2), (2,1), (3,4), (4,3), (2,2), (1,99), (77,33), (5,9), (9,29), (4,1), (7,2)]

list1 = sorted(list1, key = lambda x: x[0])
print(list1)



14. Write a Python program to sort a list of dictionaries using Lambda. 



list_to_be_sorted = [{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}]

newlist = sorted(list_to_be_sorted, key=lambda k: k['name']) 
print(newlist)




15. Write a Python program to filter a list of integers using Lambda. 



list1 = [1,2,3,4,2,32,3]

filter_list = filter(lambda x: x%2 == 0, list1)

print(list(filter_list))



16. Write a Python program to square and cube every number in a given list of 
integers using Lambda. 


list1 = [1,2,3,4,5]

square_num = map(lambda x:x*x, list1)
cube_num = map(lambda x:x*x*x, list1)

print(list(square_num))
print(list(cube_num))



17. Write a Python program to find if a given string starts with a given character 
using Lambda. 


input1 = input('Enter any string: ')
input2 = input('Enter any character: ')

check = lambda x,y: x[0] == y
if check(input1, input2):
  print(f'Yes, the string starts with "{input2}"')
else:
  print(f'No, the string does not start with "{input2}"')



18. Write a Python program to check whether a given string is number or not 
using Lambda. 


import re

input1 = input('Enter any string: ')
regex = '[+-]?\d+\.?\d*'

isNumber = lambda input1: re.search(regex, input1)

if isNumber(input1):
  print(f'Yes the string is a number')
else:
  print('No the string is not a number')




19. Write a Python program to create Fibonacci series upto n using Lambda. 


from functools import reduce
 
fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])

n = int(input('Enter any number: '))
print(fib_series(n))



20. Write a Python program to find intersection of two given arrays using 
Lambda. 


array1 = [1,2,3,4,3,5,3,3,3]
array2 = [2,4,5,7,8,9,4,3,2,3,4,5,5]

result = list(filter(lambda x: x in array1, array2)) 

intersection_array = list(set(result))
print(intersection_array)





