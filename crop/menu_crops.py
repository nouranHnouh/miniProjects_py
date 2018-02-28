from wheat_crop import *
from potato_crop import *

#display the menu for the user 
def display_menu():
	print("which crop do you want to grow? ")
	print("1. Potato")
	print("2. Wheat")
	print("choose an option from the menu :")

#function to check if the option enetered valid 
def check_option():
	valid=False
	while not valid:
		try:
			option=int(input("option selected: "))
			if option in (1,2):
				valid=True
			else:
				print("Enter valid option")
		except ValueError:
			print("valid input, please Enter valid option")
	return option 

def manage_menu():
	display_menu()
	choice=check_option()
	if choice==1:
		crop=Potato()
	if choice==2:
		crop=Wheat()
	return crop 

def main():
	new_crop=manage_menu()
	manage_crop(new_crop)

if __name__=="__main__":
        main()




