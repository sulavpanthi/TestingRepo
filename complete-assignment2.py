1. Create a variable, paragraph, that has the following content:
"Python is a great language!", said Fred. "I don't ever remember
having this much fun before."


paragraph = f'"Python is a great language!", said Fred. "I don\'t ever remember having this much fun before."'

print(paragraph)


2. Write an if statement to determine whether a variable holding a year
is a leap year.


while True:
  try:
    year_input = input('Enter any year: ')
    year_input = int(year_input)
    if year_input > 0:
      break
    print('Invalid age entered.')
  except Exception as e:
    print(e)
    
  
if year_input % 400 == 0:
  print('It is a leap year.')
elif year_input % 100 == 0:
  print('It is not a leap year.')
elif year_input % 4 == 0:
  print('It is a leap year.')
else:
  print('It is not a leap year.')



3. Write code that will print out the anagrams (words that use the same
letters) from a paragraph of text.




para = input('Enter a paragraph: ')
para = para.split(' ')

char_list = []

dict1 = {}
dict2 = {}

for word in para:
  for st in range(len(word)):
    if word[st] in char_list:
      dict1[word[st]] = dict1[word[st]] + 1

    else:
      char_list.append(word[st])
      dict1[word[st]] = 1
  dict2[word] = dict1
  dict1 = {}
  char_list = []

list_dict2 = list(dict2)

count = 0
anagrams_list = []
final_anagrams_list = []

for i in range(len(dict2)):
  for j in range(i+1, len(dict2)):
    for k in dict2[list_dict2[i]]:
      if k in dict2[list_dict2[j]]:
        if dict2[list_dict2[i]][k] == dict2[list_dict2[j]][k]:
          count += 1
    if count == len(dict2[list_dict2[i]]) and count == len(dict2[list_dict2[j]]):
      anagrams_list.append(list_dict2[i])
      anagrams_list.append(list_dict2[j])
  count = 0
  if len(anagrams_list) != 0:
    final_anagrams_list.append(anagrams_list)
  anagrams_list = []

print(final_anagrams_list)



4. Create a list. Append the names of your colleagues and friends to it.
Has the id of the list changed? Sort the list. What is the first item on
the list? What is the second item on the list?



friends_list = []
print(id(friends_list))

friends_list.append('Suman')
print(id(friends_list))

friends_list.append('Rahul')
# print(id(friends_list))

friends_list.append('Aman')
# print(id(friends_list))

friends_list.append('Raghav')
# print(id(friends_list))

friends_list.append('Akash')
# print(id(friends_list))

print('No the id of the list is not changed.')

friends_list.sort()

print('Sorted list: ',friends_list)

print('First item on the list is :',friends_list[0])
print('Second item on the list is :',friends_list[1])



5. Create a tuple with your first name, last name, and age. Create a list,
people, and append your tuple to it. Make more tuples with the
corresponding information from your friends and append them to the
list. Sort the list. When you learn about sort method, you can use the
key parameter to sort by any field in the tuple, first name, last name,
or age.


my_tuple = ('Sulav', 'Panthi', 22)
people = []
people.append(my_tuple)

my_tuple = ('Tejas', 'Rajbanshi', 23)
people.append(my_tuple)

my_tuple = ('Anuj', 'Ghimire', 21)
people.append(my_tuple)

my_tuple = ('Aman', 'Sharma', 22)
people.append(my_tuple)

my_tuple = ('Raj', 'Poudel', 23)
people.append(my_tuple)

def sortBySecond(val):
  return val[2]

print('Before sort: ',people)

people.sort(key = sortBySecond) # sort by age
print('\nAfter sort by age: ',people)



6. Create a list with the names of friends and colleagues. Search for the
name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.



friends_list = ['Suman', 'Aman', 'Raj', 'Anuj', 'Pratik', 'Sandesh', 'Hemanta', 'Bishal', 'Akash', 'John']

count = 0
for friend in friends_list:
  if friend == 'John':
    count = 0
    break
  else:
    count += 1


if count == 0:
  print('Found')
else:
  print('Not Found')



7. Create a list of tuples of first name, last name, and age for your
friends and colleagues. If you don't know the age, put in None.
Calculate the average age, skipping over any None values. Print out
each name, followed by old or young if they are above or below the
average age.




my_list = [('Raj', 'Poudel', 23), ('Samikshya', 'Kunwar', None), ('Sulav', 'Panthi', 22), ('Tejas', 'Rajbanshi', 23), ('Rachana', 'Sharma', None), ('Anuj', 'Ghimire', 21), ('Aman', 'Sharma', 22), ('Bijita', 'KC', None)]

average = 0
count = 0

for person in my_list:
  if person[2] == None:
    continue
  else:
    count += 1
    average += person[2]

average = average/count

for person in my_list:
  if person[2] == None:
    continue
  else:
    if person[2] > average:
      print(f"{person[0]} --> Old")
    if person[2] < average:
      print(f"{person[0]} --> Young")



8. Write a function, is_prime, that takes an integer and returns True if
the number is prime and False if the number is not prime.



count = 0
def is_prime(num):
  if num >= 2:
    for i in range(1, num+1):
      if num % i == 0:
        global count
        count += 1
  else:
    print('Number should be greater than 1')
    return 
    
  if count == 2:
    return True

  return False

print(is_prime(11))



9. Write a binary search function. It should take a sorted sequence and
the item it is looking for. It should return the index of the item if found.
It should return -1 if the item is not found.



def binary_search(seq, item):
  global l,r
  if len(seq[l:r+1]) >= 1:
    if item == seq[(l+r) // 2]:
      return (l+r)//2
    elif item > seq[(l+r)//2]:
      l = (l+r)//2 + 1
      r = r
      return binary_search(seq, item)
    elif item < seq[(l+r) // 2]:
      l = l
      r = (l+r)//2 - 1
      return binary_search(seq, item)
    else:
      return None
  else:
    if item == seq[(l+r) // 2]:
      return l
    else:
      return -1


seq = [1,2,4,5,7,8,9,22,33]
l=0
r=len(seq)
mid = (l+r)//2

res = binary_search(seq, 11)
print(res)




10. Write a function that takes camel-cased strings (i.e.
ThisIsCamelCased), and converts them to snake case (i.e.
this_is_camel_cased). Modify the function by adding an argument,
separator, so it will also convert to the kebab case
(i.e.this-is-camel-case) as well.



str1 = 'ThisIsCamelCase'
temp = 'a'

def kebab_case_with_argument(str1, arg = "_"):
  for i in range(len(str1)):
    if i == 0 and ord(str1[i]) >= 65 and ord(str1[i]) <= 90 :
      str1 = str1.replace(str1[i], str1[i].lower())
    else:
      if ord(str1[i]) >= 65 and ord(str1[i]) <= 90:
        temp = str1[i]
        str_list = str1.split(temp, 1)
        str1 = str_list[0] + arg + temp.lower() + str_list[1]
  return str1

print(kebab_case_with_argument(str1, "-"))



11. Create a variable, filename. Assuming that it has a three-letter
extension, and using slice operations, find the extension. For
README.txt, the extension should be txt. Write code using slice
operations that will give the name without the extension. Does your
code work on filenames of arbitrary length?


filename = 'my_file.txt'

extension = filename[-3:]
filename = filename[:-4]

print(filename)
print(extension)



12. Create a function, is_palindrome, to determine if a supplied word is
the same if the letters are reversed.



def is_palindrome(str1):
  if str1 == str1[::-1]:
    print('It is a palindrome.')
  else:
    print('Sorry! this is not a palindrome.')

is_palindrome("ololo")



13. Write a function to write a comma-separated value (CSV) file. It
should accept a filename and a list of tuples as parameters. The
tuples should have a name, address, and age. The file should create
a header row followed by a row for each tuple. If the following list of
tuples was passed in:
[('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]

it should write the following in the file:

name,address,age
George,4312 Abbey Road,22
John,54 Love Ave,21



import csv

def write_to_csv(filename, list_of_tuples):
  with open(filename, 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Address', 'Age'])
    for i in range(len(list_of_tuples)):
      writer.writerow(list_of_tuples[i])

write_to_csv('new.csv', [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)])




14. Write a function that reads a CSV file. It should return a list of
dictionaries, using the first row as key names, and each subsequent
row as values for those keys.
For the data in the previous example it would return:
[{'name': 'George', 'address': '4312 Abbey Road', 'age': 22}, {'name':
'John', 'address': '54 Love Ave', 'age': 21}]



import csv

lst = []
def read_csv_file(filename):
  with open(f"{filename}", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        lst.append(dict(dict(row)))
  return lst
      
dict1 = read_csv_file("new.csv")
print(dict1)



15. Imagine you are designing a banking application. What would a
customer look like? What attributes would she have? What methods
would she have?



class Customer:
  first_name = ''
  middle_name = ''
  last_name = ''
  mobile_num = ''
  email_address = ''
  resident_phone_num = ''
  temporary_address = ''
  mailing_address = ''
  date_of_birth = ''
  fathers_name = ''
  mothers_name = ''
  husbands_name = ''
  monthly_electric_bill = ''
  requires_ATM = ''
  requires_cheque = ''
  requires_credit_card = ''
  citizenship_photocopy = ''

  def open_account(self):
    pass
  def close_account(self):
    pass
  def enquire_account(self):
    pass
  def deposit_money(self):
    pass
  def withdraw_money(self):
    pass
  def update_details(self):
    pass
  def apply_for_loan(self):
    pass
  def enable_eBanking(self):
    pass
  def disable_eBanking(self):
    pass
  def apply_for_ATM_card(self):
    pass
  def update_ATM_PIN(self):
    pass
  def disable_ATM_card(self):
    pass
  def update_eBanking_credentials(self):
    pass
  def apply_for_credit_card(self):
    pass
  def freeze_credit_card(self):
    pass
  def disable_credit_card(self):
    pass




16. Imagine you are creating a Super Mario game. You need to define
a class to represent Mario. What would it look like? If you aren't
familiar with SuperMario, use your own favorite video or board game
to model a player.



class Mario:
    avatar = ''
    color = ''
    height = ''
    width = ''
    score = ''
    lives_remained = ''
    achievements = ''
    ranking = ''
    performance = ''
    skills = ''
    weapons = ''
    powers = ''

    def jump(self):
        pass
    def move_forward(self):
        pass
    def move_backward(self):
        pass
    def kill_enemies(self):
        pass
    def get_bigger(self):
        pass
    def change_weapons(self):
        pass
    def change_speed(self):
        pass



17. Write a program that serves as a basic calculator. It asks for two
numbers, then it asks for an operator. Gracefully deal with input that
doesn't cleanly convert to numbers. Deal with division by zero errors.



while True:
  try:
    input1 = input('Enter first number: ')
    input1 = int(input1)
    input2 = input('Enter second number: ')
    input2 = int(input2)
  
  except Exception as e:
    print(e)
  
  else:
    try:
      oper = input('Enter any one operator(+,-,*,/,%): ')
      if oper == "+":
        print('The result is: ', end = '')
        print(input1 + input2)
        break
      elif oper == "-":
        print('The result is: ', end = '')
        print(input1 - input2)
        break
      elif oper == "*":
        print('The result is: ', end = '')
        print(input1 * input2)
        break


      elif oper == "/":
        while True:
          try:
            if input2 != 0:
              print('The result is: ', end = '')
              print(input1 / input2)
              break
            else:
              input2 = int(input('Re-enter the second number: '))
          except Exception as e:
            print(e)
            


      elif oper == "%":
        print('The result is: ', end = '')
        print(input1 % input2)
        break
      else:
        raise ValueError('Invalid operator')
      break
    except Exception as e:
      print(e)





18. Find a package in the Python standard library for dealing with
JSON. Import the library module and inspect the attributes of the
module. Use the help function to learn more about how to use the
module. Serialize a dictionary mapping 'name' to your name and 'age'
to your age, to a JSON string. Deserialize the JSON back into
Python.



import json

# print(help(json))
# print(dir(json))

my_dict = {'name': 'Sulav Panthi', 'age': 22}
print("Dictionary: ",my_dict)
print(type(my_dict))

json_serialized = json.dumps(my_dict)
print("Serialized json: ",json_serialized)
print(type(json_serialized))

json_deserialized = json.loads(json_serialized)
print("Deserialized json: ",json_deserialized)
print(type(json_deserialized))




19. Write a Python class to find validity of a string of parentheses, '(',
')', '{', '}', '[' and ']. These brackets must be close in the correct order,
for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.



class Validity:
  

  def is_valid(self, str1):
    lst, dict1 = [], {"(": ")", "{": "}", "[": "]"}
    for bracket in str1:
      if bracket in dict1:
        lst.append(bracket)
      elif len(lst) == 0 or dict1[lst.pop()] != bracket:
        return False
    return len(lst) == 0

val = Validity()
print(val.is_valid("{}[][{{()}}]([])"))




20. Write a Python class to find the three elements that sum to zero
from a list of n real numbers.
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]




list1 = [-2,1,-10,2,3,-1,0,33,0,4,55,-3,-1,8,12,-53,-30]

list1 = list(set(list1))

empty_list = []
empty_list2 = []

final_list2 = []
rem = 0
total = 0

for lst in list1:
  empty_list.append(lst)
  final_list = []
  rem = total - lst
  lst_index = list1.index(lst)
  for i in range(lst_index+1, len(list1)):
    empty_list2.append(list1[i])
    rem2 = rem - list1[i]
    lst_index2 = list1.index(list1[i])
    for j in range(lst_index2+1, len(list1)):
      if list1[j] == rem2:
        empty_list2.append(list1[j])
    if len(empty_list2) >= 2:
      final_list.extend(empty_list)
      final_list.extend(empty_list2)
      # final_list.append('&')
      if len(final_list) == 3:
        final_list2.append(final_list)
      final_list = []
    empty_list2 = []
    rem2 = 0
  
  rem = 0 
  empty_list = []

# print(len(final_list2))
for i in final_list2:
  print(i,end="\n")
