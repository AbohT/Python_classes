 # print("This is my first python script")
import time
print(
'''*************
Cohort III Microwave
**************
1. Open the Microwave
2. Put the rice
3. Set the time ''')
customers = []  #key for all customers
customer = {}  #key for individual customer
name=input("Enter your name: \n>>>")
customer["name"]=name #key for customer name
#print(customer["name"])
time_to_micro_wave= input("Duration: \n>>>")
convert_to_int=float(time_to_micro_wave)
customer["duration"]=convert_to_int #key for customer duration
#print(customer["duration"])
price_to_charge=convert_to_int * 1000
customer["amount"] = price_to_charge #key for customer amount
#print(customer["amount"])
print("You are charged: ₦", price_to_charge, "only")
print("Your rice will be ready in ", time_to_micro_wave, "mins(s)")
print("4. I will let you know when it is ready...")
print(customer)
#customer.append(customer) #to add new customer
minutes_in_seconds=60
time.sleep(convert_to_int * minutes_in_seconds)
print("5. Your food is ready.")                           
