import random

#generate random number from 1 to 9
a=random.randint(1,9)
#define count to count how many guesses user made till
#right answer entered
count=0


while True:
	#ask user for guess
	user_guess=raw_input("Enter your Guess: ")
	#if user entered exit break
	if user_guess=="exit":
		break
		#else increase the count 
	else:
		count+=1
		user_guess=int(user_guess)
	#if usser guess == the random number 
	if user_guess==a:
		print"exactly right"+"you took only"+ " "+str(count)
	elif user_guess > a:
		print "too high"
	else:
		print"two low"





