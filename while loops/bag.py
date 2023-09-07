#Write a program for a bag shop. Shop has 100 red bags (each Rs 1000) and 200 white bags (each Rs 1500)
#Customers can buy one or more bags at a time.
#The program ends when the sales reached Rs10000 or at least 10 bags are sold. 
#Display total sales and total number of bags sold

#initialize variables
redBags, whiteBags = 100, 200
totalSales, totalBagsSold = 0 ,0

while (totalSales < 10000 or totalBagsSold < 10) :
    
    print(f"Available bags: Red - {redBags}, White - {whiteBags}") #Availabe bags
    color = input("Enter the bag color (Red/White): ") # Ask customer for input
    color.lower()

    if color == "red" and redBags > 0: # Check if the customer chose red and if there are red bags available.
        ask_customer = int(input("Enter how many redbag you want:")) # Ask customer for input
       
        if ask_customer > redBags: # Check if the customer wants to buy more red bags than are available.
            ask_customer = redBags # Limit the purchase to the available quantity of red bags.
        cost = ask_customer * 1000 # Calculate the cost of the red bags.
        redBags -= ask_customer  # Update the quantity of red bags available after the purchase

    elif color == "white" and whiteBags > 0: # Check if the customer chose white and if there are white bags available.
        ask_customer = int(input("Enter how many whitebag you want:")) # Ask customer for input
        if ask_customer > whiteBags: # Check if the customer wants to buy more white bags than are available
            ask_customer = whiteBags # Check if the customer wants to buy more white bags than are available
        cost = ask_customer * 1500 # Calculate the cost of the white bags.
        whiteBags -= ask_customer # Update the quantity of white bags available after the purchase.
    else:
        print("Invalid choice or no bags available.")
        continue

    totalSales += cost # Update the total sales amount.
    totalBagsSold += ask_customer # Update the total number of bags sold.

# Display total sales and total number of bags sold
print("Total sales: Rs.", totalSales)
print("Total bags sold:", totalBagsSold)

   
#OUTPUT:
# Available bags: Red - 100, White - 200
# Enter the bag color (Red/White): red
# Enter how many redbag you want:10
# Total sales: Rs. 10000
# Total bags sold: 10 