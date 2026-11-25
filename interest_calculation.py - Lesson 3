# Lesson 3 Assignment
# interest calculation by Leah Williams 11/25/26

# Gather investment amount info
investmentAmount = int(input("Please enter an investment amount \n(Between the ranges of 0 and 50,000.) Hit enter when finished: "))
# V Check if the user can actually read instructions :) V
while investmentAmount <= 0 or investmentAmount >= 50000: #checks investmentAmount input is valid. If it's not, it will continually ask for a valid input and break at that point.
    if investmentAmount <= 0: #explains min range (less than 0) error
        print("You have provided an investment amount that is outside the minimum range of 0. \n Your input: " + str(investmentAmount) + ". Please try again. ")
        investmentAmount = int(input("Please try again with a new value above 0 but less than 50k. ")) #attempt to correct amount
    if investmentAmount >= 50000: #explains max range (greater than 50k) error
        print("You have provided an investment amount that is outside the maximum range of 50,000. \n Your input: " + str(investmentAmount) + ". Please try again.")
        investmentAmount = int(input("Please try again with a new value above 0 but less than 50k. ")) #attempt to correct amount

# Gather interest rate info
interestRate = int(input("Please enter the interest rate you'd like to inquire about. (Up to 15%) \n Hit enter when done. "))
# V Check if the user can actually read instructions :) V
while interestRate <= 0 or interestRate >= 15: #checks investmentAmount input is valid. If it's not, it will continually ask for a valid input and break at that point.
    if interestRate <= 0: #explains min range (less than 0) error
        print("You have provided an intrest rate that is outside the minimum range of 0. \n Your input: " + str(interestRate) + "%. Please try again. ")
        interestRate = int(input("Please try again with a new value above 0 but less than 15%. ")) #attempt to correct amount
    if interestRate >= 15: #explains max range (greater than 15) error
        print("You have provided an intrest rate that is outside the maximum range of 15%. \n Your input: " + str(interestRate) + "%. Please try again. ")
        interestRate = int(input("Please try again with a new value above 0 but less than 15%. ")) #attempt to correct amount

# Gather duration info
duration = int(input("Please enter over how many years you would like to calculate: \n Hit enter when finished. "))
while duration <= 0 : #checks duration input is valid. If it's not, it will continually ask for a valid input and break at that point.
    if duration <= 0: #explains min range (less than 0) error
        print("You have provided a duration of time that is outside the minimum range of 0. \n Your input: " + str(duration) + " years. Please try again. ")
        duration = int(input("Please try again with a new value above 0. ")) #attempt to correct amount

# Done gathering info, now make the needed adaptations/calculations.
yTm = duration * 12 # Years to Months, takes duration var and multiplies by 12 to get months.
irTp = interestRate / 100 # Interest Rate to Percent, Takes interestRate var and multiplied by one onehundreth to make it a percent. 
perMoIR = (irTp / 12) # Per Month Interest Rate, takes the calculated interest rate in percent form and / by 12 to get a per month rate then multiplies by 100.
total = 0 

monthCounter = 0 # counter, each interation represents a month. 
yrCounter = 0 #same as above, but for years!

print("\n============================================================\n")
for monthCounter in range(1, yTm + 1): #iterates by month
        total = total + investmentAmount
        calculation = round(total * perMoIR, 2)
        total = total + calculation  #new total
        
        if monthCounter % 12 == 0: #Checks if monthCounter is cleanly divisible by 12, meaning a year has elapsed. If so, it'll add a yr label, skip otherwise.
                    yrCounter += 1
                    print("Year: "+ str(yrCounter) + " $" + format(total, ".2f"))
        monthCounter += 1

print("\n-----------------------------------------------------------\nMonthly Investment: $" + str(investmentAmount) + " X " + str(interestRate) + "% " + " interest over " + str(duration) + " years. \n============================================================\n")

print("\nCompleted by, Leah Williams")



