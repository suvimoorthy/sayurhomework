# Computer will guess a random number. 
# user has to guess that number. for each guess, print 'High' or 'Low'
# eg - computer number - 189
# user guess 56 - print low
# user guess 678 - print high
# Get user input and print 'high' or 'low' until the user guesses the number correctly 
# https://www.w3schools.com/python/ref_random_randint.asp - read this to learn how to create a random number


import random  # Import the random module to generate random numbers

computerNo = random.randint(3, 9)  # Generate a random number between 3 and 9

attempt = 0  # Initialize the attempt counter

while(True):
    userNo = int (input("Guess the number:"))  # Get input from user

    if (userNo < computerNo):
        print("Low")

    elif (userNo > computerNo):
        print("High")

    elif userNo == computerNo:
        print("you guesses correct number")
        break  # Exit the loop when the user's guess is correc

    attempt +=1  # Increment the attempt counter

print ("User guessed the number in ", attempt, "attempts")  # Print the number of attempts it took the user to guess correctly

#OUTPUT:

# Guess the number:2
# Low
# Guess the number:11
# High
# Guess the number:4
# you guesses correct number
# User guessed the number in  2 attempts