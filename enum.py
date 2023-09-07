#Calculate the monthly salary for the phone salesman
#Base monthly pay Rs10000. 
#For every 5 phones sold, Rs 5000 bonus.
#For every phone aftr the first 5 phones, Rs1100 per phone bonus.
#If the salesman's salary is more than Rs20000 in the previous month and sells 20 or more phones 
# this month also, then he gets additional Rs5000.


monthlysaleslist =[5,23,21,14,23,12,4,12,22,34,12] # List of phones sold in each month
basepay=10000
bones5=5000
bonesafter5=1100
additionalbones=5000
previousmonthsalary=0 # Initialize previous month's salary


for month,phonecount in enumerate(monthlysaleslist): # Loop through each month and calculate salary
    # Calculate salary based on phone sales
    if phonecount<=5:
        currentmonthsalary=basepay

    else:
        currentmonthsalary=basepay+bones5+(phonecount -5)*bonesafter5

    print(f"This month {month+1} salary before additional bones {currentmonthsalary}")

    if previousmonthsalary > 20000 and phonecount >=20: # Check for additional bonus condition
        currentmonthsalary += additionalbones

    else: # Update previous month's salary for next iteration
        previousmonthsalary = currentmonthsalary
        continue


#OUTPUT:

# This month 1 salary before additional bones 10000
# This month 2 salary before additional bones 34800
# This month 3 salary before additional bones 32600
# This month 4 salary before additional bones 24900
# This month 5 salary before additional bones 34800
# This month 6 salary before additional bones 22700
# This month 7 salary before additional bones 10000
# This month 8 salary before additional bones 22700
# This month 9 salary before additional bones 33700
# This month 10 salary before additional bones 46900
# This month 11 salary before additional bones 22700

    