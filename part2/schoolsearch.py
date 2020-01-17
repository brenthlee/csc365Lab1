# Henry Luengas
# Ryan Nevils
# Brent Lee

import os

#arrayValues for data
LNAME = 0
FNAME = 1
GRADE = 2
CLSSRM = 3
BUS = 4
GPA = 5

#arrayValues for teacherData
TLNAME = 0
TFNAME = 1
TCLSSRM = 2

legalCommands = ['S', 'Student', 'T', 'Teacher', 'B',
                 'Bus', 'G', 'Grade', 'A', 'Average', 'I', 'Info', 'Q', 'Quit',
                 'SC', 'StudentClass', 'TC', 'TeacherClass',
                 'TG', 'TeacherGrade', 'E', 'Enrollment', 'TGPA', 'TeacherGPA',
                 'GGPA', 'GradeGPA', 'BGPA', 'BusGPA']


def parse_command(inpt, data, teacherData):
    # figure out what command it is, then run appropriate command
    # S[tudent]:  <lastname> [B[us]]
    # T[eacher]:  <lastname>
    # B[us]:  <number>
    # G[rade]:  <number> [H[igh]|L[ow]]
    # A[verage]:  <number>
    # I[nfo]
    # SC/StudentClass: <number>
    # TC/TeacherClass: <number>
    # TG/TeacherGrade: <number>
    # E[nrollment]
    # TGPA/TeacherGPA: [<lastname>]
    # GGPA/GradeGPA: [<number>]
    # Q[uit]

    command, *args = inpt.split(':')

    if command not in legalCommands:
        print("not a valid command!")
        return

    if (command == 'S' or command == 'Student'):
        printStudent(args, data, teacherData)

    elif (command == 'T' or command == 'Teacher'):
        printTeacher(args, data, teacherData)

    elif (command == 'B' or command == 'Bus'):
        printBus(args, data)

    elif (command == 'G' or command == 'Grade'):
        printGrade(args, data, teacherData)

    elif (command == 'A' or command == 'Average'):
        printAverage(args, data)

    elif (command == 'I' or command == 'Info'):
        printInfo(args, data)

    elif (command == 'SC' or command == 'StudentClass'):
        printStudentClass(args, data)

    elif (command == 'TC' or command == 'TeacherClass'):
        printTeacherClass(args, teacherData)

    elif (command == 'TG' or command == 'TeacherGrade'):
        printTeacherGrade(args, data, teacherData)

    elif (command == 'E' or command == 'Enrollment'):
        printEnrollment(args, data)

    elif (command == 'TGPA' or command == 'TeacherGPA'):
        printTeacherGPA(args, data, teacherData)

    elif (command == 'GGPA' or command == 'GradeGPA'):
        printGradeGPA(args, data)

    elif (command == 'BGPA' or command == 'BusGPA'):
        printBusGPA(args, data)


def main():
    if os.path.isfile("teachers.txt"):
        with open("teachers.txt") as f:
            teacher_data_list = [[val.strip() for val in r.split(",")]
                                 for r in f.readlines()]
    else:
        print("File 'teachers.txt' not found in current directory")
        return

    if os.path.isfile("list.txt"):
        with open("list.txt") as f:
            student_data_list = [[val.strip() for val in r.split(",")]
                                 for r in f.readlines()]
    else:
        print("File 'teachers.txt' not found in current directory")
        return

#    teacherDict = {}
#    for teacher in teacher_data_list:
#        teacherDict.update({int(teacher[2]): [teacher[0], teacher[1]]})

    inpt = input("> ")
    while (inpt != 'Q' and inpt != 'Quit'):
#        parse_command(inpt, student_data_list, teacherDict)
        parse_command(inpt, student_data_list, teacher_data_list)
        inpt = input("> ")
    print("See you next time!")


# S[tudent]: <lastname> [B[us]]
# Search for the entry (or entries) for students with
# the given last name.
# For each entry found, print the last name, first name, grade and classroom assignment for
# each student found and the name of their teacher (last and first name).

def printStudent(args, data, teacherData):
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
            for i in range(len(teacherData)):
                if (int(data[student][CLSSRM]) == int(teacherData[i][TCLSSRM])):
                    print(str(data[student][LNAME]) + ',' + str(data[student][FNAME]) + ',' + str(data[student][GRADE]) +
                        ',' + str(data[student][CLSSRM]) + ',' + str(teacherData[i][TLNAME]) + ',' + str(teacherData[i][TFNAME]))
                    break

# ###########################################################################################

# T[eacher]: <lastname>
# Search for the entry (or entries) for students with
# the given last name.
# For each entry found, print the last name, first name and the bus route the student takes.


def printTeacher(args, data, teacherData):
    if not args:
        return

    tname = args[0].strip()

    clss = -1
    for i in range(len(teacherData)):
        if (tname == teacherData[i][TLNAME]):
            clss = teacherData[i][TCLSSRM]
            break
    if (clss == -1):
        return
    
    for i in range(len(data)):
            if (clss == data[i][CLSSRM]):
                print(str(data[i][LNAME]) + ',' + str(data[i][FNAME]))
# ###########################################################################################

# B[us]: <number>
# Search for the entries where the bus route number
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
            print(str(data[i][FNAME]) + ',' + str(data[i][LNAME]) +
                ',' + str(data[i][GRADE]) + ',' + str(data[i][CLSSRM]))
# ###########################################################################################

# G[rade]: <number> [H[igh]|L[ow]]
# Search for the entries where the student’s grade
# matches the number provided in the instruction.
# For each entry, output the name (last and first) of the student.

def printGrade(args, data, teacherData):
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
            max = -1.0
            maxStudent = 0
            maxClass = -1
            for student in students:
                if (float(data[student][GPA]) > float(max)):
                    max = float(data[student][GPA])
                    maxStudent = student
                    maxClass = data[student][CLSSRM]
            for i in range(len(teacherData)):
                if (teacherData[i][TCLSSRM] == maxClass):
                    print(str(data[maxStudent][LNAME]) + ',' + str(data[maxStudent][FNAME]) + ',' + str(data[maxStudent][BUS]) +
                        ',' + str(data[maxStudent][GPA]) + ',' + str(teacherData[i][TLNAME]) + ',' + str(teacherData[i][TFNAME]))
                    break

        elif (sort == "L" or sort == "Low"):
            min = 5.0
            minStudent = 0
            minClass = -1
            for student in students:
                if (float(data[student][GPA]) < float(min)):
                    min = float(data[student][GPA])
                    minStudent = student
                    minClass = data[student][CLSSRM]
            for i in range(len(teacherData)):
                if (teacherData[i][TCLSSRM] == minClass):
                    print(str(data[minStudent][LNAME]) + ',' + str(data[minStudent][FNAME]) + ',' + str(data[minStudent][BUS]) +
                        ',' + str(data[minStudent][GPA]) + ',' + str(teacherData[i][TLNAME]) + ',' + str(teacherData[i][TFNAME]))
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
        ave = ave + round(float(data[student][GPA]), 2)
    ave = ave / len(students)
    print('Grade ' + str(grade) + ': ' + str(round(ave, 2)))
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
# SC/StudentClass
# Given a classroom number, list all students assigned to it
# ###########################################################################################

def printStudentClass(args, data):
    if not args:
        return
    classroom = args[0].strip()
    for i in range(len(data)):
        if (int(data[i][CLSSRM]) == int(classroom)):
            print(str(data[i][LNAME]) + "," + str(data[i][FNAME]))
# TC/TeacherClass
# Given a classroom number, find the teacher (or teachers) teaching in it
# ###########################################################################################

def printTeacherClass(args, teacherData):
    if not args:
        return
    classroom = args[0].strip()
    for i in range(len(teacherData)):
        if (int(teacherData[i][TCLSSRM]) == int(classroom)):
            print(str(teacherData[i][TLNAME]) + "," + str(teacherData[i][TFNAME]))
# TG/TeacherGrade
# Given a grade, find all teachers who teach it
# ###########################################################################################

def printTeacherGrade(args, data, teacherData):
    if not args:
        return
    grade = args[0].strip()
    classes = []
    for i in range(len(data)):
        if (int(data[i][GRADE]) == int(grade) and (int(data[i][CLSSRM]) not in classes)):
            classes.append(int(data[i][CLSSRM]))
    for clss in classes:
        for i in range(len(teacherData)):
            if (int(teacherData[i][TCLSSRM]) == int(clss)):
                print(str(teacherData[i][TLNAME]) + "," + str(teacherData[i][TFNAME]))
                break
# E[nrollment]
# Output a list of classrooms ordered by classroom number, with a total number
# of students in each of the classrooms
# ###########################################################################################

def printEnrollment(args, data):
    if args:
        return
    classes = {}
    for i in range(len(data)):
        classes.update({int(data[i][CLSSRM]) : (int(classes.get(int(data[i][CLSSRM]), 0)) + 1)})
    li = list(classes.items())
    li.sort()
    for i in li:
        print("Class " + str(i[0]) + " has " + str(i[1]) + 
            (" student" if (int(i[1]) == 1) else " students"))
# TGPA/TeacherGPA
# Given a teacher's last name, it outputs all of the students' GPA's in the teacher's class
# Without an argument, it outputs all of the students' GPA's of all the teachers
# ###########################################################################################

def printTeacherGPA(args, data, teacherData):
    if not args:
        return
    if not args[0]:
        for teacher in teacherData:
            print(str(teacher[0]), str(teacher[1]))
            printTeacherGPA(teacher, data, teacherData)
    else:

        tname = args[0].strip()

        clss = -1
        for i in range(len(teacherData)):
            if (tname == teacherData[i][TLNAME]):
                clss = teacherData[i][TCLSSRM]
                break
        if (clss == -1):
            return
        
        for i in range(len(data)):
                if (clss == data[i][CLSSRM]):
                    print(str(data[i][GPA]))
# GGPA/GradeGPA
# Given a grade, it outputs all of the students' GPA's in that grade
# Without an argument, it outputs all of the students' GPA's of all the grades
# ###########################################################################################

def printGradeGPA(args, data):
    if not args:
        return
    if not args[0]:
        grades = [[] for i in range(7)]
        for i in range(len(data)):
            grades[int(data[i][GRADE])].append(round(float(data[i][GPA]), 2))
        for i in range(len(grades)):
            print("Grade " + str(i) + ":")
            for grade in grades[i]:
                print(str(grade))
    else:
        grade = args[0].strip()
        for i in range(len(data)):
            if (grade == data[i][GRADE]):
                print(str(data[i][GPA]))


# BGPA/BusGPA
# Given a bus route, it outputs all of the students' GPA's in that route
# Without an argument, it outputs all of the students' GPA's of all the grades
# ###########################################################################################
def printBusGPA(args, data):
    if not args:
        return
    
    if not args[0]:
        buses = ['0', '51', '52', '53', '54', '55', '56']
        for bus in buses:
            print("Bus " + bus + ":")
            for entry in data:
                if (entry[BUS] == bus):
                    print(entry[GPA])

    else:
        bus = args[0].strip()
        for i in range(len(data)):
            if (bus == data[i][BUS]):
                print(str(data[i][GPA]))

if __name__ == '__main__':
    main()
