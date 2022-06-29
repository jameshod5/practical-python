# sears.py
bill_thickness = 0.11 * 0.001
sears_height = 442 #metres 
number_of_bills = 1
day = 1

name = input("What is your name?")
print("Your name is", name)


while number_of_bills * bill_thickness < sears_height:
    height = (bill_thickness*number_of_bills)
    day = day + 1
    number_of_bills = number_of_bills*2


print("The number of bills exceeds the height after:")
print("Number of days", day)
    
    
