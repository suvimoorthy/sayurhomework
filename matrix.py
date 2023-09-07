#print a multiplication table like below.
#get user intput for start and end numbers. 
#the following example uses 1 to 5.

#      1  2  3  4  5
#   ********************
# 1 |  1  2  3  4  5
# 2 |  2  4  6  8 10
# 3 |  3  6  9 12 15
# 4 |  4  8 12 16 20
# 5 |  5 10 15 20 25

start = int(input("Enter start number:")) # Get user input for the start and end numbers of the multiplication table

end = int(input("Enter end number:"))

for table in range(start,end+1): # Print the header row for the multiplication table
    print(f"{table}",end = " ")
print(f"\n{'*'*20}")

for table in range(start,end+1): #print table in row
    print(f"\n{table}|", end = " ")

    for multiplicand in range(start,end+1): # Calculate and print the products for each multiplication
        print(f"{table * multiplicand}", end = " ")



#OUTPUT:

# Enter start number:1
# Enter end number:5
# 1 2 3 4 5 
# ********************
# 1| 1 2 3 4 5        
# 2| 2 4 6 8 10       
# 3| 3 6 9 12 15      
# 4| 4 8 12 16 20     
# 5| 5 10 15 20 25 