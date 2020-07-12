import csv

# with open('student_details.txt', 'r') as file:
#     reader = csv.reader(file, delimiter=' ')
#     for eachline in reader:
#         print(eachline)


# with open('student_details.txt', 'a') as file:
#     reader = csv.reader(file, delimiter=' ')
#     for eachline in reader:
#         print(eachline)

with open('student_details.txt', 'r') as file:
    file.read()



# with open('student_details.txt', 'w') as file:
#     file.writelines()



# def write_to_txt(filename, list_of_tuples):
#   with open(filename, 'a', newline = '') as file:
#     file.writelines(['Name', 'Address', 'Age'])
#     # writer.writerow(['Name', 'Address', 'Age'])
#     for i in range(len(list_of_tuples)):
#         file.write(list_of_tuples[i])

# write_to_txt('student_details.txt', [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)])