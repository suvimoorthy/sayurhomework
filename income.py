"""" New regime of income tax """



slab = [300000,600000,900000,1200000,1500000]
tax = [0,0.05,0.10,0.15,0.20,0.30]
fixed_amount = [0,15000,45000,90000,150000]

while True:

    #getting income from user
    income = float(input("Enter your income:"))

    if income < 0 : #if they enter less than 0 it will display
        print(" Hey print valid income")
        break
    for i in range(len(slab)):
        if income <= slab[i]:
            finaltax = tax[i] * income
            if i > 0:
                finaltax =fixed_amount[i] + (tax[i]*(income-slab[i]))  # Deduct previous slab tax
            break
        
    cess = 0.04 * finaltax  # Health and education tax
    total_tax = finaltax + cess
        
    print("Your calculated income tax: ", total_tax)



#     OUTPUT:

# Enter your income:200000
# Your calculated income tax:  0.0
# Enter your income:500000
# Your calculated income tax:  10400.0
# Enter your income:-89
#  Hey print valid income