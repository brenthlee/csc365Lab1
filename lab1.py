#Henry Luengas
#Ryan Nevils
#Brent Lee

LNAME = 0
FNAME = 1
GRADE = 2
CLSSRM = 3
BUS = 4
GPA = 5
TLNAME = 6
TFNAME = 7

# data_dict = {}
legalCommands = ['S', 'Student', 'T', 'Teacher', 'B', 'Bus' 'G', 'Grade', 'A', 'Average', 'I', 'Info',]


def printStudent(args, data):

    # need to check for null
    bus = 0
    if not args:
        return

    checkbus = args[0].split()
    print(checkbus)

    if ( len(checkbus) > 1 and (checkbus[1] == 'B' or checkbus[1] == 'Bus')):
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
            print(str(data[student][LNAME]) + ',' +  str(data[student][FNAME]) + ',' + str(data[student][BUS]))
    else:
        for student in students:
            print(str(data[student][LNAME]) + ',' +  str(data[student][FNAME]) + ',' + str(data[student][GRADE]) + ',' +  str(data[student][CLSSRM]) + ',' + str(data[student][TLNAME]) + ',' + str(data[student][TFNAME]))
    return

def printTeacher(args, data):


    if not args:
        return

    tname = args[0].strip()

    students = []
    for i in range(len(data)):
        if (tname == data[i][TLNAME]):
            students.append(i)

    for student in students:
        print(str(data[student][LNAME]) + ',' +  str(data[student][FNAME]))


    return

def parse_command(inpt, data):
    # figure out what command it is, then run appropriate command


    command, *args = inpt.split(':')

    if command not in legalCommands:
        print ("not a valid command!")
        return

    if (command == 'S' or command == 'Student'):
        printStudent(args, data)

    elif (command == 'T' or command == 'Teacher'):
        printTeacher(args, data)

    # etc etc, keep fillling in
    return



def main():

    with open("students.txt") as f:
        data_list = [[val.strip() for val in r.split(",")] for r in f.readlines()]




    # for row in data_list:
    #     key, *values = row   
    #     data_dict[key] = row


    inpt = input("> ")
    while (inpt != 'Q'):
        parse_command(inpt, data_list)
        inpt = input("> ")


if __name__ == '__main__':
    main()
    
# data structure
# dictionary "data" {ID# : [infoList]}
# We were going to do {Lastname : [infoList]} but the key needs to be unique... so thats not going to work.



# S[tudent]: <lastname> [B[us]]

# Search the contents of the students.txt file for the entry (or entries) for students with
# the given last name.

# For each entry found, print the last name, first name, grade and classroom assignment for
# each student found and the name of their teacher (last and first name).

# ###########################################################################################

# T[eacher]: <lastname>

# Search the contents of the students.txt file for the entry (or entries) for students with
# the given last name.

# For each entry found, print the last name, first name and the bus route the student takes.
# ###########################################################################################

# B[us]: <number>

# Search the contents of the students.txt file for the entries where the bus route number
# matches the number provided in the instruction.

# For each such entry, output the first and the last name of the student and their grade and
# classroom.
# ###########################################################################################

# G[rade]: <number> [H[igh]|L[ow]]

# Search the contents of the students.txt file for the entries where the student’s grade
# matches the number provided in the instruction.

# For each entry, output the name (last and first) of the student.
# ###########################################################################################

# A[verage]: <number>

# Search the contents of the students.txt file for the entries where the student’s grade
# matches the number provided in the instruction.

# Compute the average GPA score for the entries found. Output the grade level (the number
# provided in command) and the average GPA score computed.
# ###########################################################################################

# I[nfo]

# For each grade (from 0 to 6) compute the total number of students in that grade.

# Report the number of students in each grade in the format
# <Grade>: <Number of Students>
# sorted in ascending order by grade.
# ###########################################################################################

# # Q[uit]
# ###########################################################################################