#Bio data of students at Blockfuse Labs
print("Welcome to Blockfuse Labs Data Collection Center. \nKindly fill out the information required below on your form accurately")
full_name=input("Please enter your full name: \n>>>")
print(type(full_name)) #Data type of fullanme

height=float(input("Please enter your height in meters: \n>>>"))
print(type(height)) #Data type of height

age=int(input("Please enter your age: \n>>>"))
print(type(age)) #Data type of age

hobbies=input("Please enter all your hobbies: \n>>>")
print(type(hobbies)) #Data type of hobbies

marital_status=input("Are you married:\n>>>") 
is_married = True  #Represents a married individual
print(type(is_married)) #Data type of marital_status

print(f"Here are your details; Fullname: {full_name} | Age: {age} | Height: {height} | Hobbies: {hobbies} | Marital Status: {marital_status}")
