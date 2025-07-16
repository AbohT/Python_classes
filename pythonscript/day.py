# print("This is my first python script")
import time #the import time is a default used when working with anything time related
print( #use ''' to start and end a long sequence of print command. also used to write comments in python
'''*************  
Cohort III Microwave
**************
1. Open the Microwave
2. Put the rice
3. Set the time
''')
name=input("Enter your name: \n>>>") #use input command when you need user to enter a variable

time_to_micro_wave= input("Enter duration to use microwave: \n>>>") #the time_to_micro_wave is a variable

convert_to_int=float(time_to_micro_wave) #you can use int in plae of float. float contains decimals while int does not

price_to_charge=convert_to_int * 1000

print(f"You are charged: ₦ {price_to_charge} only")

print("Your rice will be ready in ", time_to_micro_wave, "mins(s)")

print("4. I will let you know when it is ready...")

minutes_in_seconds=60

time.sleep(convert_to_int * minutes_in_seconds)  #the time.sleep function makes the prgram inactive for the duration set

print("5. Your food is ready.")
