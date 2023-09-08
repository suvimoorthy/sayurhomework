'''Get a number from the user. Divide it by 3 and print the result. 
Divide again by 3 and print the result. Keep dividing until the number is less than 3. 
Print the number of times the number was divided. '''



getnum=int(input("Enter number:")) #to get number from the user
count=0  #to calculate no of times the number was divided we initialize count as 0



while getnum>=3: #using while loop for dividing the number again and again
    getnum/=3 #dividing the number by 3
    count+=1 #using count for how many times the number can divide by 3
    print(getnum) #display the result of the number after dividing



print("number of times divided:",count)#display the number how many times it divided 


#OUTPUT:

# Enter number:9
# 3.0
# 1.0
# number of times divided: 2
