#Print Chess board (alternate black and white squares)
#print('\u25A0') - will print white Square. You can use "B" to print black squares


size_of_chessboard = 8 #size of the chessboard

for row in range (size_of_chessboard): #loop for row

    for column in range(size_of_chessboard):#loop for column
        if (row + column)%2==0: #if it is even
            print("\u25A1", end = "") #white boxes

        else:
            print("B",end ="") #black boxes
        
    print("\n")

    #OUTPUT:

# □B□B□B□B
# B□B□B□B□
# □B□B□B□B
# B□B□B□B□
# □B□B□B□B
# B□B□B□B□
# □B□B□B□B
# B□B□B□B□