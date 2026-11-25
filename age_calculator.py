## Lesson 2 Assignment 10/4/26 ##
## By: Leah W. ##
print("\n \n") ## A little line cleanup...

first_name = input("Hello! What is your first name? (Please type and press enter) \n")
last_name = input("Thank you. What is your last name? (Please type and press enter) \n")
current_year = int(input("What year is it right now? ex:YYYY \n")) 
birth_year = int(input("What year were you born? ex:YYYY \n")) 

age = current_year - birth_year
print("Thank you for that info! \n ========================== \n") ## Done collecting info here

print("It's nice to meet you " + first_name + " " + last_name + ".") ##Output current info
print ("You're " + str(age) + " years old! \n")

age += 1 ##Set the upcoming year
print(f"In the next year, {current_year + 1}, you will be {age} years old. \n \n =========================") ##Output future age

print(f"Completed by Leah Williams") ## Sign off
print("\n \n") ## A little line cleanup...
