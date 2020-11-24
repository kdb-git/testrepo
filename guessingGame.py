import random 

def computerGuess(lowval, highval, randum, count=0):
    if highval >= lowval:
        guess = lowval + (highval - lowval) // 2
        # If guess is in the middle, it is found! 
        if guess == randum:
            return count

        # If "guess" is greater than the number ,
        # it must be found in the lower half of the set of numbers
        # between the lower value and the guess.
        elif guess > randum:
            count = count + 1
            return computerGuess(lowval, guess-1, randum, count)
        
        # The number must be in the upper set of the numbers
        # betwee the guess and the upper value
        else:
            count = count + 1
            return computerGuess(guess + 1, highval, randum, count)
    else:
        # Number not found
        return -1
        #end of function

#generate a random number between 1 and 100
randum = random.randint(1,101)

count = 0
guess = -99

while(guess != randum):
    #Get the user's guess
    guess = (int) (input("Enter your guess between 1 and 100:"))
    if guess < randum:
        print("higher")
    elif guess > randum:
        print("lower")
    else:
        print("you guessed it!")
        break
    count = count + 1
#end of while loop

print("You took" + str(count) + "steps to guess the number")
print("computer took " + str(computerGuess(0,100, randum))+ " steps!")