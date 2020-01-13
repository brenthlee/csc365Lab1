# Henry Luengas
# Ryan Nevils
# Brent Lee

import os

LNAME = 0
FNAME = 1
GRADE = 2
CLSSRM = 3
BUS = 4
GPA = 5
TLNAME = 6
TFNAME = 7

legalCommands = ['S', 'Student', 'T', 'Teacher', 'B',
                 'Bus', 'G', 'Grade', 'A', 'Average', 'I', 'Info', 'Q', 'Quit']


def parse_command(inpt, data):
    # figure out what command it is, then run appropriate command
    # S[tudent]:  <lastname> [B[us]]
    # T[eacher]:  <lastname>
    # B[us]:  <number>
    # G[rade]:  <number> [H[igh]|L[ow]]
    # A[verage]:  <number>
    # I[nfo]
    # Q[uit]

    command, *args = inpt.split(':')

    if command not in legalCommands:
        print("not a valid command!")
        return

    if (command == 'S' or command == 'Student'):
        printStudent(args, data)

    elif (command == 'T' or command == 'Teacher'):
        printTeacher(args, data)

    elif (command == 'B' or command == 'Bus'):
        printBus(args, data)

    elif (command == 'G' or command == 'Grade'):
        printGrade(args, data)

    elif (command == 'A' or command == 'Average'):
        printAverage(args, data)

    elif (command == 'I' or command == 'Info'):
        printInfo(args, data)


def main():
    if os.path.isfile("students.txt"):
        with open("students.txt") as f:
            data_list = [[val.strip() for val in r.split(",")]
                        for r in f.readlines()]
    else:
        print("File 'students.txt' not found in current directory")
        return

    # for row in data_list:
    #     key, *values = row
    #     data_dict[key] = row

    inpt = input("> ")
    while (inpt != 'Q' and inpt != 'Quit'):
        parse_command(inpt, data_list)
        inpt = input("> ")
    print("See you next time!")


# S[tudent]: <lastname> [B[us]]
# Search the contents of the students.txt file for the entry (or entries) for students with
# the given last name.
# For each entry found, print the last name, first name, grade and classroom assignment for
# each student found and the name of their teacher (last and first name).

def printStudent(args, data):
    # need to check for null
    bus = 0
    if not args:
        return

    checkbus = args[0].split()

    if (len(checkbus) > 1 and (checkbus[1] == 'B' or checkbus[1] == 'Bus')):
        bus = 1
        lname = checkbus[0]
    else:
        lname = args[0].strip()

    students = []
    for i in range(len(data)):
        if (lname == data[i][LNAME]):
            students.append(i)
    if (bus == 1):
        for student in students:
            print(str(data[student][LNAME]) + ',' +
                  str(data[student][FNAME]) + ',' + str(data[student][BUS]))
    else:
        for student in students:
            print(str(data[student][LNAME]) + ',' + str(data[student][FNAME]) + ',' + str(data[student][GRADE]) +
                  ',' + str(data[student][CLSSRM]) + ',' + str(data[student][TLNAME]) + ',' + str(data[student][TFNAME]))
# ###########################################################################################

# T[eacher]: <lastname>
# Search the contents of the students.txt file for the entry (or entries) for students with
# the given last name.
# For each entry found, print the last name, first name and the bus route the student takes.


def printTeacher(args, data):
    if not args:
        return

    tname = args[0].strip()

    students = []
    for i in range(len(data)):
        if (tname == data[i][TLNAME]):
            students.append(i)

    for student in students:
        print(str(data[student][LNAME]) + ',' + str(data[student][FNAME]))
# ###########################################################################################

# B[us]: <number>
# Search the contents of the students.txt file for the entries where the bus route number
# matches the number provided in the instruction.
# For each such entry, output the first and the last name of the student and their grade and
# classroom.


def printBus(args, data):
    if not args:
        return

    busRoute = args[0].strip()

    students = []
    for i in range(len(data)):
        if (busRoute == data[i][BUS]):
            students.append(i)

    for student in students:
        print(str(data[student][FNAME]) + ',' + str(data[student][LNAME]) +
              ',' + str(data[student][GRADE]) + ',' + str(data[student][CLSSRM]))
# ###########################################################################################

# G[rade]: <number> [H[igh]|L[ow]]
# Search the contents of the students.txt file for the entries where the student’s grade
# matches the number provided in the instruction.
# For each entry, output the name (last and first) of the student.

def printGrade(args, data):
    if not args:
        return

    if (len(args[0])):
        grade = args[0].split()[0].strip()
    else:
        return

    students = []
    for i in range(len(data)):
        if (grade == data[i][GRADE]):
            students.append(i)
    if (len(students) == 0):
        return

    if (len(args[0].split()) > 1):
        sort = args[0].split()[1].strip()

        if (sort == "H" or sort == "High"):
            max = 0.0
            maxStudent = 0
            
            for student in students:
                if (float(data[student][GPA]) > float(max)):
                    max = float(data[student][GPA])
                    maxStudent = student

            print(str(data[maxStudent][LNAME]) + ',' + str(data[maxStudent][FNAME]) + ',' + str(data[maxStudent][BUS]) + ',' + str(data[maxStudent][GPA]) + ',' + str(data[maxStudent][TLNAME]) + ',' + str(data[maxStudent][TFNAME]))


        elif (sort == "L" or sort == "Low"):
            min = 4.0
            minStudent = 0

            for student in students:
                if (float(data[student][GPA]) < float(min)):
                    min = float(data[student][GPA])
                    minStudent = student

            print(str(data[minStudent][LNAME]) + ',' + str(data[minStudent][FNAME]) + ',' + str(data[minStudent][BUS]) + ',' + str(data[minStudent][GPA]) + ',' + str(data[minStudent][TLNAME]) + ',' + str(data[minStudent][TFNAME]))

    else:
        for student in students:
            print(str(data[student][LNAME]) + ',' + str(data[student][FNAME]))


    

    
# ###########################################################################################

# A[verage]: <number>
# Search the contents of the students.txt file for the entries where the student’s grade
# matches the number provided in the instruction.
# Compute the average GPA score for the entries found. Output the grade level (the number
# provided in command) and the average GPA score computed.
# ###########################################################################################

def printAverage(args, data):
    if not args:
        return
    
    grade = args[0].strip()

    students = []
    for i in range(len(data)):
        if (grade == data[i][GRADE]):
            students.append(i)

    ave = 0.0
    if (len(students) == 0):
        return
    for student in students:
        ave = ave + round(float(data[student][GPA]),2)
    ave = ave / len(students)
    print('Grade ' + str(grade) + ': ' + str(round(ave,2)))

# I[nfo]
# For each grade (from 0 to 6) compute the total number of students in that grade.
# Report the number of students in each grade in the format
# <Grade>: <Number of Students>
# sorted in ascending order by grade.
# ###########################################################################################

def printInfo(args, data):
    if args:
        return

    students = [0] * 7
    for i in range(len(data)):
        students[int(data[i][GRADE])] = students[int(data[i][GRADE])] + 1

    for i in range(len(students)):
        if (i == 0):
            print('Kindergarden: ' + str(students[i]))
        elif (i == 1):
            print('1st Grade: ' + str(students[i]))
        elif (i == 2):
            print('2nd Grade: ' + str(students[i]))
        elif (i == 3):
            print('3rd Grade: ' + str(students[i]))
        else:
            print(str(i) + 'th Grade: ' + str(students[i]))

if __name__ == '__main__':
    main()
