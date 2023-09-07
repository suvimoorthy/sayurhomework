# Get and print the 2 marks each for 3 students. Also, get each studen't name
# output should be
# Mark 1 for Student 1 is 55
# Mark 2 for Student 1 is 67
# Mark 1 for Student 2 is 56 
#etc

######### Problem 1.1
#same problem as above, but output should have the student name and all the marks in the same line.
# Eg - Input - Student Name - Chitra, Mark1 1 55, Mark 2 67
#output -  Chitra's marks 55, 67


no_of_student = int(input("Enter no of student:")) # Get the number of students from the user
marks =[]  # Create an empty marks list for each student

for student in range(1,no_of_student+1): # Loop through each student
    name = input("Enter student name:")
    for mark in range(1,3):  # Loop through each mark for the student
        getmark = float(input(f"Enter mark {mark}:"))
        marks.append(getmark) #given mark is add to the list 
    
    print(f"{name}'s marks {marks[0]},{marks[1]}") # Print marks for each student (all marks on the same line)



# OUTPUT:

# Enter no of student:1
# Enter student name:suvi
# Enter mark 1:45
# Enter mark 2:78
# suvi's marks 45.0,78.0