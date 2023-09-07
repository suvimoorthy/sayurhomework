# Get and print the 2 marks each for 3 students. Also, get each studen't name
# output should be
# Mark 1 for Student 1 is 55
# Mark 2 for Student 1 is 67
# Mark 1 for Student 2 is 56 
#etc


no_of_student = int(input("Enter no of student:")) # Get the number of students from the user

for student in range(1,no_of_student+1): # Loop through each student
    name = input("Enter student name:")  # Get the student's name
    for mark in range(1,3): # Loop through each mark for the student
        getmark = float(input(f"Enter mark {mark}:"))  # Get the mark from the user

        if getmark < 0 : # Check if the entered mark is valid
            print("enter valid mark")

        else:
            print(f"Mark {mark} for {name} is {getmark}") # Print the mark along with student's name and mark number


#OUTPUT:

# Enter no of student:2
# Enter student name:suvi
# Enter mark 1:54
# Mark 1 for suvi is 54.0
# Enter mark 2:67
# Mark 2 for suvi is 67.0
# Enter student name:shivu
# Enter mark 1:90
# Mark 1 for shivu is 90.0
# Enter mark 2:89
# Mark 2 for shivu is 89.0