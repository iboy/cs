# A fuller solution to the mastermind challenge
# 

from random import randint

# print instructions
print("Welcome to Mastermind")
print("-------------------------------------")
print("I have thought of 4 digit number")
print("You have five guesses to get it right")
print("I will tell when a guess is correct.")
print("-------------------------------------")

# generate a random number and set our variables

randomNumber = randint(1000,9999)
randomNumberStr = str(randomNumber) # convert the number to a string. Then we can access elements like this randomNumberStr[0]

numberOfGuessesAllowed = 10 # this is a nice thing to do. You can then use some logic to change the number of possible guesses if you wish
correctDigitCount = 0 # a variable to count for the number of correct answers
attempts = 1 # a variable to count the number of attempts.

guess = input("Enter a your first guess: ")

while attempts < numberOfGuessesAllowed:
    
    if guess == "" or len(guess) >= 5 or len(guess) <4:
        print ("Your guess needs to be 4 digits long")
        prompt = "Try again. "+ str(numberOfGuessesAllowed-attempts)+ " guesses remaining. Enter a four digit number: "
        attempts = attempts + 1
        correctDigitalCount = 0
        guess = input(prompt)
    else:
            
        print("You guessed: ", guess)
        print("Answer: ", randomNumber) # I put this in to help debug. Remove if you wish to 

        count = 0 # I am using this as an index 
        for digit in range(len(guess)):
            
            testDigit = guess[digit]
            if testDigit == randomNumberStr[count]:
                print("Digit ",count+1," CORRECT")
                correctDigitCount = correctDigitCount+1
                
            else:
                print("Digit ",count+1," FALSE")
            count = count + 1
        if correctDigitCount == 1:
            digitSingPlural = " digit"
        else:
            digitSingPlural = " digits"              
            
        if correctDigitCount == 4:
            print("You have ", correctDigitCount, digitSingPlural," correct.")
            print("You solved it. That was wonderful! Well done.")
            break;
        else:
            print("You have ", correctDigitCount, digitSingPlural," correct.")
            if attempts == 1:
                guessSingPlural = " guess"
            else:
                guessSingPlural = " guesses"
            prompt = "Try again. "+ str(numberOfGuessesAllowed-attempts)+ guessSingPlural + " remaining. Enter a four digit number: "
            attempts = attempts + 1
            correctDigitCount = 0
            guess = input(prompt)


if correctDigitCount == 4:
    print ("That's thest best I've seen today.")
elif correctDigitCount == 3 :
    print ("3 out of 4 isn't bad. Would you like to try again?")
elif correctDigitCount == 2 :
    print ("2 out of 4. Half way there. Would you like to try again?")
elif correctDigitCount == 1 :
    print ("1 out of 4. That's a start. Would you like to try again?")
elif correctDigitCount == 0 :
    print ("0 out of 4. Did something go wrong? Would you like to try again?")
else:
    pass
        




