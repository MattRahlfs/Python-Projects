#generate a number for the bill
#ask if they want to split the bill (how many ways)
#let the user choose what percent of a tip to leave ( is it the same for each person?)
#
import random

bill_cost = round(random.uniform(10.0, 1000.00), 2)

print ("Your bill is: $" + str(bill_cost) )
input_value = input("Do you want to split you bill? y/n\n")

def get_tip_percent():
    tip_percent = int(input('Enter the tip percent you would like to apply to your bill.\n'))
    tip_percent = tip_percent / 100
    return tip_percent

def get_total_cost(bill_cost, tip_percent):
    total_bill = (bill_cost * tip_percent)
    total_bill = total_bill + bill_cost
    return round((total_bill), 2)

def split_bill(total_cost):
    
    split_n_ways = 0
    
    while split_n_ways not in [2, 3]:
        try:
            split_n_ways = int(input("How many ways do you want to split the bill? You can only split it 2 or 3 ways.\n"))
            continue
        except ValueError:
            continue
    
    bill_split_total = round((total_cost / split_n_ways), 2)
    
    return bill_split_total
    
                
    
    

if input_value == 'n':
   print(get_total_cost(bill_cost, get_tip_percent()))
elif input_value == 'y':
     split_bill(get_total_cost(bill_cost, get_tip_percent()))

    
    