#Brent Lee, Henry Luengas, Ryan Nevils

run:
	@python3 schoolsearch.py

test:
	@python3 schoolsearch.py < commands

studs:
	@mv students.txt studs.txt

students:
	@mv studs.txt students.txt

