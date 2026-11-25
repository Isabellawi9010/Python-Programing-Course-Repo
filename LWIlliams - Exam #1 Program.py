#Random Number Test, Exam 1
# By Leah Williams, 11/25/26

import random


#V Informs the user of the 5 guess limit V 
print("\nLet's play a guessing game, but with a challenge!\nI'm going to think of a number and it's up to you to guess it, BUT in only 5 guesses.\nCan you do it? Let's see!\n\n")

contGame = "y" # tells the code to repeat the game if the user chooses to.
valid = 1

while contGame == "y":
    random_number = random.randint(0, 100)
    attempts = 0
    guess = int(input("Please type a guess for what number it could be!: "))
    while guess != random_number: #run the game for as long as the user's guess doesn't match the secret number
    
        if attempts >= 9: # 10 try limitation
            print("================================================================")
            print("That's 10 tries! Sorry, you lose :)")
            print("The correct answer was " + str(random_number) + "\n")
            break
        else:
            if guess < random_number: #Incorrect guess less than secret number hint
                print("\nNope! That's not it. Let's try again!\nHint: Your guess was LESS than the secret number.")
        
            if guess > random_number: #Incorrect guess Greater than secret number hint
                print("\nNope! That's not it. Let's try again!\nHint: Your guess was GREATER than the secret number.")
            print("-------------------------------------------")
            attempts += 1 #adds one to the incorrect attempts counter
            print("Attempts used: " + str(attempts) + ", Attempts left: " + str(10 - attempts))
            guess = int(input("Please type a guess for what number it could be!: "))
       
    if guess == random_number: #Win notice + stats
        print("\n\n================================================================")
        print("You won!\nAfter " + str(attempts) + " incorrect attempts ") 
    
    contGame = input("Would you like to play again? Please type 'y' or 'n' and hit Enter ")
    if contGame.lower() not in ("y","n", "yes", "no"):
        valid = 0
        while valid != 1:
            print("That's not a valid input.")
            contGame = input("Would you like to play again? Please type 'y' or 'n' and hit Enter ")
            if contGame.lower() in ("y","n", "yes", "no"):
                valid = 1
    if contGame.lower() == "yes":
        contGame = "y"
    if contGame.lower() == "no":
            contGame = "n"
    

print("Completed by, Leah Williams")