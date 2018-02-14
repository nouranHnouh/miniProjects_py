#this is a mini project called take a break
# it allws you to take a 3 breaks after 2 hours and open a webbrowser
#so you can listen to video in the break. 
import webbrowser 
import time 
#let the program wait 2 hour before take a break 
break_count=0
total_break=3
print ("This program started on"+time.ctime())
while break_count<total_break:

   #let program wait 2hours before take a break and open the webbrowser 
   time.sleep(10)
   print ("time for a break")
#open a webbrowser
   webbrowser.open("https://www.youtube.com/watch?v=JGwWNGJdvx8")
   break_count+=1 
