# CSC365 Lab1
Contributors: **Brent Lee, Henry Luengas, Ryan Nevils**

---

## How to run: ##

    * To run the lab by itself and make it interactive, type 'make'

    * To run the testing with all the commands, type 'make test'

    * To test that we make sure the file is in the directory, type 'make studs && make' (This command changes the name 'students.txt' to 'studs.txt' and runs the lab)

    * To run again with the students.txt, type 'make students && make' (This command changes the name back 'studs.txt' to 'students.txt' and runs the lab)

---

## New commands for part2:

    1. SC/StudentClass - Given a classroom number, list all students assigned to it

    2. TC/TeacherClass - Given a classroom number, find the teacher (or teachers) teaching in it

    3. TG/TeacherGrade - Given a grade, find all teachers who teach it

    4. E[nrollment] - Report a list of classrooms ordered by classroom number, with a total number of students in each of the classrooms



    Analytics commands:

    B[us]GPA [Number]
        if no bus number is provided, then this command prints out every GPA for all busses. Ex:
                Bus 0:
                3.15
                2.81
                3.11
                2.88
                2.8
                3.14
                2.88
                2.85
                Bus 51:
                2.92
                3.02
                .
                .
                etc
        if a bus number is provided, then it prints out all the GPAs for that bus number.


---

## Testing input/output: ##

    * It is in tests.txt

    * The input is left justified without any indentation

    * The output is left justified and is indented
