import csv
import pandas as pd
import time

course_list = {'Full stack web development': 20000,
'Machine learning and Data Science': 20000,
'Cyber Security Professional Course': 20000}


with open('student_details.csv', 'r') as file:
    try:
        # print('try start')
        file1 = pd.read_csv(file)
        # print('try end')
    
    except Exception:
        with open('student_details.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Address', 'Age', 'Course', 'Payment Made', 'Remaining Payment'])
            # print('except block executed')



with open('course_details.csv', 'w') as file:
    writer = csv.writer(file, delimiter = '\t')
    writer.writerow(['Course Name', 'Price'])
    for key, value in course_list.items():
        writer.writerow([key, value])
        

class Student:
    student_enrolled = 0

    def wish_to_leave(self,name):
        
        a = Academy()
        a.delete_and_refund(name)
        

    def register(self):
        name = input('\nPlease enter your full name here: ')
        while True:
            try:
                age = int(input('Please enter your age here: '))
                if age > 18 and age < 59:
                    break
            except Exception as e:
                print(e)
        address = input('Please enter your address here: ')

        while True:
            try:
                course = input('\nEnter the course name you want to enroll in: ')
                if course in course_list:
                    break
                else:
                    raise ValueError('Course name does not match with our course list. Please try again.')
            except Exception as e:
                print(e)
                
        while True:
            try:
                payment_made = int(input('\nEnter your first installment price: '))
                if payment_made == 10000:
                    break
                print('Please pay your first installment.')
                print('You have to pay Rs.20000 in two installments for Rs.10000 each.\n')
            except Exception as e:
                print(e)

        remaining_payment = 20000 - payment_made
        # add this in csv
        with open('student_details.csv', 'a') as file:
            writer = csv.writer(file, delimiter = ',')
            writer.writerow([name, address, age, course, payment_made, remaining_payment])

        Student.student_enrolled += 1

        time.sleep(2)
        print('\nYou have successfully enrolled in our academy for "',course,'"')
        time.sleep(1)
        print('\n\n')
        Academy.display_students_details()

        time.sleep(3)
        print('\nPlease pay your second installment to get your books and library card.')
        time.sleep(1)
        while True:
            try:
                amount = int(input('\nPlease enter the payment for second installment: '))
                if amount != 10000:
                    raise ValueError('Second installment payment must be of Rs.10000')
                break
            except Exception as e:
                print(e)
        a = Academy()
        a.update_student_details(name, amount)

        time.sleep(2)
        choice = input('\nHave you completed the course? [Y/N]: ')
        if choice == 'Y' or choice == 'y':
            a = Academy()
            a.delete_and_refund(name)
        

class Academy:
    def __init__(self):
        print('\n\tWelcome to the academy.\n')

    @staticmethod
    def display_students_details():
        with open('student_details.csv', 'r') as file:
            readed = pd.read_csv(file)
            print(readed)

    def update_student_details(self, name, amount):
        rows = []
        with open('student_details.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 0:
                    rows.append(row)
                    for field in row:
                        if field == name:
                            # print(rows[-1])
                            rows[-1][-1] = int(rows[-1][-1]) - amount
                            rows[-1][-2] = int(rows[-1][-2]) + amount
                            time.sleep(2)
                            print('\nPayment received successfully.')
                            # print(rows[-1])


        with open('student_details.csv', 'w') as file:
            writer = csv.writer(file)
            for row in rows:
                writer.writerow(row)

        time.sleep(1)
        # print(rows)
        print()
        Academy.display_students_details()
    
    def delete_and_refund(self, name):
        rows = []
        with open('student_details.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 0:
                    rows.append(row)
                    # print(row)
                    # print(rows)
                    # print()
                    for field in row:
                        if field == name:
                            # print(rows[-1])
                            print('Please wait for your refund amount...')
                            time.sleep(2)
                            print(f'\nPlease collect your money: {rows[-1][-2]}')
                            rows.remove(rows[-1])
                            time.sleep(1)
                            print(f'\nDetails of "{name}" is deleted successfully.\n')
                            # print(rows[-1])
                            time.sleep(1)
                            print('Thank you for enrolling in our course. We hope you had a good learning experience. Best of luck for your career ahead.')



        with open('student_details.csv', 'w') as file:
            writer = csv.writer(file)
            for row in rows:
                writer.writerow(row)

        time.sleep(1)
        # print(rows)
        print()
        Student.student_enrolled -= 1
        Academy.display_students_details()
    

    @staticmethod 
    def display_course_details():

        print('We have following course structure.\n')
        with open('course_details.csv', 'r') as file:
            readed = pd.read_csv(file, delimiter = '\t')
            print(readed)

        time.sleep(2)
        input1 = input('\nDo you wish to enroll in any of the above courses? [Y/N]: ')
        if input1 == 'y' or input1 == 'Y':
            s = Student()
            s.register()
        else:
            print('\nThank you for your time.')


        time.sleep(2)
        print('\nIf you have any unanswered queries please contact us.\n\npanthisulav4@gmail.com\n9822211111\n\n')



a = Academy()
Academy.display_course_details()

input2 = input('\nDo you wish to leave the program? [Y/N]: ')
if input2 == 'Y' or input2 == 'y':
    s = Student()
    name = input('Enter your full name: ')
    s.wish_to_leave(name)