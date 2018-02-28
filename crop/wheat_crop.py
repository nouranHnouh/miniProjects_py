from cropV2 import *


class Wheat(Crop):
	""" A potato crop inherite from crop class"""
   
   #constructor 
	def __init__(self):
		#call the parent class constructor with default values
		# for potato
		#growth rate=2.3; light need=3; water need =6
		super().__init__(3,6,2.3)
		self._type="Wheat"

	# overide grow method for subclasses 
	def grow(self,light,water):
		# grow when enough water and water provided 
		if light>=self._light_need and water>=self._water_need: 
			#if the status is seedling and I got more water than I need 
			if self._status=="Seeding" and water >self._water_need:
				#grow more 
				self._growth+=self._growth_rate*0.5

			elif self._status=="Young" and water >self._water_need:
				self._growth+=self._growth_rate*1.5
			elif self._status=="Old" and water >self._water_need:
				self._growth+=self._growth_rate/4.0
			
			else:
				self._growth+=self._growth_rate

		#increament day growing 
		self._days_growing+=1
		#update status 
		self._update_status()
       

def main():
	#create new potato crop
	wheat_crop=Potato()
	#potato_crop.grow(10,10)
	print (wheat_crop.report())
	manual_grow(wheat_crop)
	print (wheat_crop.report())
	manual_grow(wheat_crop)
	print (wheat_crop.report())

if __name__ == "__main__":
	main()
