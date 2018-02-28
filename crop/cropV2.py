import random 
class Crop():
	"""class crop would simulate the amount of water and light the crop needs to grow
	it has the following attributes:
	light_need: the amount of light it will need 
	water_need: the amount of water it needs 
	growth rate= how much the crop will grow each time recives water and light 
	"""
	#constructor 
	def __init__(self,light_need,water_need,growth_rate):
		self._light_need=light_need
		self._water_need=water_need
		self._growth_rate=growth_rate
		#represent the growth of the crop
		self._growth=0
		self._days_growing=0
		self._status="Seed"
		self._type="Generic"

	def needs(self):
		"""return dictionary of water and water needs"""
		return {'light need':self._light_need,'water need':self._water_need}
		#print(crop_needs['light need'])
		#print (crop_needs['water need'])

	def report(self):
		"""method that report the provide information about current state"""
		return {'type':self._type,'status':self._status,'growth':self._growth,'days growing':self._days_growing}
		#print (crop_type['type'])
		#print (crop_status['status']) 
	def _update_status(self):
		"""update status of crop based on the value of the growth"""
		if self._growth>15:
			self._status="Old"
		elif self._growth>10:
			self._status="Mature"
		elif self._growth>5:
			self._status="Young"
		elif self._growth>0:
			self._status="Seedings"
		elif self._growth==0:
			self._status="Seed"
		 
	def grow(self,light,water):
		if light>=self._light_need and water>=self._water_need:
			#grow by growth rate 
			self._growth +=self._growth_rate
		#grow days by one 
		self._days_growing +=1
		#update status 
		self._update_status()


	

	#test the functionality using auto_grow function
	# it takes the number of days
def auto_grow(crop,days):
	for day in range(days):
		light=random.randint(1,10)
		water=random.randint(1,10)
		crop.grow(light,water)

""" manual_grow() function will allow us to provide specific values 
to the crop so that we can test that,it 
receives a particular pairing of light and water. 
It will only grow the crop over a single day."""
def manual_grow(crop):
	#get the light and water value from the user 
	valid=False
	while not valid:
		try:
			light=int(input("pleaser enter a light value (1-10): "))
			if 1<=light<=10:
				valid=True 
			else:
				print("value entered not valid, value should be between 1 and 10 ")
		except ValueError:
			print("value entered not valid, value should be between 1 and 10 ")

	valid=False
	while not valid:
		try:
			water=int(input("please enter a water value (1-10): "))
			if 1<=water<=10:
				valid=True
			else:
				print("value enetered not valid, enter value between (1-10)")
		except ValueError:
			rint("value enetered not valid, enter value between (1-10)")

#display the menu
def display_menu():
	print("1. Grow manually over 1 day")
	print("2. Grow automatically over 30 days")
	print("3. Report status ")
	print("0. Exit test program")
	print()
	print("please select option from menu")

#create a menu option for the user
def get_menu_choice():
	option_valid=False
	while not option_valid:
		try:
			choice=int(input("option selected: "))
			if 0<= choice<=4:
				option_valid=True
			else:
				print("please enter a valid option")
		except ValueError:
			print("value is invalid, eneter valid option")
	return choice 
# function that will manage the crop by providing to the user
# options
def manage_crop(crop):
	print("this is the crop managment program ")
	print()
	noexit=True
	while noexit:
		display_menu()
		option=get_menu_choice()
		print()
		if option==1:
			manual_grow(crop)
			print()
		elif option==2:
			auto_grow(crop,30)
			print()
		elif option==3:
			print(crop.report())
			print()
		elif option==0:
			noexit=False
			print()
	print("thank you for using the program ")



	


#testing 
#instances 
def main():
	crop1=Crop(10,3,10)
	manage_crop(crop1)

if __name__ == "__main__":
	main()


