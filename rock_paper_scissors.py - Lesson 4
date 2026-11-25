# Rock Paper Scissors
# By Leah Williams, 11/25/26
import random
def main():
    # Function setup
    def continueGame(contGame): # checks that the input for whether or not to continue is valid or not.
        valid = 1               #the valid variable is here to ensure it can be input wihtout immediately changing the actual value if invalid.
        contGame = input("Would you like to play again? Please type 'y' or 'n' and hit Enter ")
        if contGame.lower() not in ("y","n", "yes", "no"): #checks that it's one of these approved values.
            valid = 0
            while valid != 1: #repeats until a valid value is presented
                print("That's not a valid input.")
                contGame = input("Would you like to play again? Please type 'y' or 'n' and hit Enter ")
                if contGame.lower() in ("y","n", "yes", "no"): #updates to correct value if found.
                    valid = 1
        if contGame.lower() == "yes": #converts "yes" to "y"
                contGame = "y"
        if contGame.lower() == "no": #converts "no" to "n"
                contGame = "n"
        return contGame
    def weaponChoice(): # Gathers the player's choice of weapon info
        usrWE = int(input("What weapon do you choose?:\nRock     -- 1\nPaper    -- 2\nScissors -- 3\nPlease type '1','2'. or '3' and hit Enter. \n"))
        return usrWE
    def compWeapon(): #Gathers the computer's choice of weapon info
        compWE  = random.randint(1,3)
        return compWE
    def labelWeapon(a, b): # cleanly converts both the player - a and the computer's - b weapon int into a label like "Rock"
        label = ["Rock", "Paper", "Scissors"]
        a = label[a - 1] 
        b = label[b - 1]
        return a, b
    def winner(usrWE, compWE): #decides the winner, match is tie, in the one scenario that 1 and 3 are chosen - 1 is winner, else lesser number loses.
        print("------------------------")
        print("(Player) " + a + " VS " + b + " (Computer)") # "Player Weapon VS Computer Weapon"
        if usrWE == compWE:
            print("Tie! Same Weapon chosen.")
        elif usrWE == 1 and compWE == 3: # Rock (1) beats scissors (3)
            print("You win!") 
        elif usrWE == 3 and compWE == 1: # Rock (1) beats scissors (3)
            print("You lose :()") 
        elif usrWE > compWE:
            print("You win!")
        else:
            print("You lose :(")
        print("-------------------------")
    # Game initializing
    contGame = "y" # Initially sets continueGame var to yes so it will play on first attempt.
    print("\n==========================") # A little line cleanup.
    #Actual gameplay
    while contGame == "y": #Continues the game until the player decides to stop.
        usrWE = weaponChoice()            #line 50 and 51 are for player and computer to choose weapons
        compWE = compWeapon()
        a, b = labelWeapon(usrWE, compWE) #Labels it cleanly
        winner(usrWE, compWE)             #Decides winner
        contGame = continueGame(contGame) #Asks user to continue or not 
    #End of game
    print("\n==========================")
    print("Completed by, Leah Williams.")
if __name__ == "__main__":
    main()




