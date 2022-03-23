petrol = 109.52
disel = 95.10
cng = 60.55
oil = 10
mix=(petrol+oil)

def petrolPrice():
    return petrol

def diselPrice():
    return disel

def cngPrice():
    return cng    


def oilPrice():
    return oil    


def petroloilPrice():
    return oil   

import sys
from termcolor import colored,cprint
from datetime import datetime
import fuelprice


print("------------------------------------------------------------------------------------------------------------------------")
title=colored("Fuel Pricing", 'green', attrs=['reverse'])
print(title.center(70))
print("------------------------------------------------------------------------------------------------------------------------")
a=' Fuel Type:'
print(a)
print("    |---------------------------------------|")
print("    |  Sr.No.   |     Item    |    Price    |")
print("    |---------------------------------------|")
print("    |     1     |     Petrol  |  109.52/lit |")
print("    |---------------------------------------|")
print("    |     2     |     Diesel  |  95.10/lit  |")
print("    |-------------------------------+-------|")
print("    |     3     |     CNG     |  60.55/Kg   |")
print("    |---------------------------------------|")
print("    |     4     |     Oil     |  10/-       |")
print("    |---------------------------------------|")
print("    |     5     |  Petrol+Oil |  109.52+10  |")
print("    |---------------------------------------|")
print("------------------------------------------------------------------------------------------------------------------------")


ans='y'
while(1):
    if ans=='y':
        print("\n ABC Fuel Pump.\n")
        print("1.Petrol")
        print("2.Diesel")
        print("3.CNG")
        print("4.Oil")
        print("5.Petrol + Oil")
        print("6.Exit")
        choice=int(input("Enter Your Choice:"))
        if choice == 1 or choice == 2 or choice ==3 or choice ==4 or choice ==5 or choice ==6 :
            if choice==1:
                print("\nPetrol:\n")
                quantity = float(input("Enter Petrol Qunatity In Liters = "))
                rate_of_petrol = fuelprice.petrol
                total_fuel_cost = quantity * rate_of_petrol
                print(f"\nPay Rs. {total_fuel_cost} for Purchase of {quantity} Liters Petrol.")
                
                ans = input("\nDo you want to continue? [y/n] = \n")
            elif choice==2:
                print("\nDiesel:\n")
                quantity = float(input("Enter Diesel Qunatity In Liters = "))
                rate_of_diesel = fuelprice.disel
                total_fuel_cost = quantity * rate_of_diesel
                print(f"\nPay Rs. {total_fuel_cost} for Purchase of {quantity} Liters diesel.")
                ans = input("\nDo you want to continue? [y/n] = \n")
            elif choice==3:
                print("\nCNG:\n")
                quantity = float(input("Enter CNG Qunatity In Kilograms = "))
                rate_of_cng = fuelprice.cng
                total_fuel_cost = quantity * rate_of_cng
                print(f"\nPay Rs. {total_fuel_cost} for Purchase of {quantity} Kilograms CNG.")
                ans = input("\nDo you want to continue? [y/n] = \n")
            elif choice==4:
                print("\nOil:\n")
                quantity = int(input("Enter Oil Pacekt Qunatity  = "))
                rate_of_oil = fuelprice.cng
                total_fuel_cost = quantity * rate_of_oil
                print(f"\nPay Rs. {total_fuel_cost} for Purchase of {quantity} Oil Pacakets.")
                ans = input("\nDo you want to continue? [y/n] = \n")
            elif choice==5:
                print("\nPetrol + Oil:\n")
                quantity = float(input("Enter Petrol Qunatity In Liters = "))
                rate_of_mix = fuelprice.mix
                total_fuel_cost = quantity * rate_of_mix
                print(f"\nPay Rs. {total_fuel_cost} for Purchase of {quantity} Liters Petrol.")
                cprint("\nNote:- For 1 Liter Petrol minimum 1 oil pacaket is to be added.\n", 'white', 'on_red')
                ans = input("\nDo you want to continue? [y/n] = \n")
            elif choice==6:
                sys.exit
            else:
                print("Opps!!!! Invalid Choice!!!!")
        else:
                print("Opps!!!! Invalid Choice!!!!")
    else:
        print("Have A Great Day!!!!")
        sys.exit()






