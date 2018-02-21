
#generate a random 4 digit number

import random 
#generate 4 digit number 
num= list(str(random.randint(0,9999)))
#check the output of the number t
print (num)

#initilize boolean variable
correct= False
count=0
#while the number of cows are false 
#keep looping till the user win or exit 
while correct: 
    #initialize number of cows and bulls to zeros 
    cows=0
    bulls=0
    #take the guess from the user 
    user_guess=list(str(raw_input("Guess the 4 digit number? ")))
    #count the number of guess 
    count=count+1
    
    #if user entered exit, break 
    if user_guess==['e','x','i','t']:
        print "thank you for playing! "
        break 
    #otherwise loop and compare the user guess 
    #and random number generated 
    for i in range(0,4):
        # if they are eguals and in the correct position 
         #increment cow
        if user_guess[i]==num[i]:
            cows=cows+1

        #otherwise increment bulls 
        else: 
            bulls=bulls+1 
        
        

    #print the number of cows and bulls         
    print "cows %d" %cows
    print "bulls %d" %bulls

    #if user entered everything correctly, exit the loop
    if cows==4 and bulls==0:
        correct=True
        print "congrats! you got it right in %d guesses" %count
        break
    #otherwise guess again....
    else:
        print "guess again! \n"   
    
    
