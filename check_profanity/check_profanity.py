import urllib
#read a text, and return true if there is a curse word 
def read_text():
	# open a file 
	file_quotes=open("/Users/nourannouh/Desktop/check_profanity/movie_quotes/movie_quotes.txt")
	#read the contents of the file 
	contents_of_file=file_quotes.read()
	print contents_of_file
	file_quotes.close()
	check_profanity(contents_of_file)

def check_profanity(check_text):
	#opening URLs on internet using urllib.urlopen
	connection=urllib.urlopen("http://www.wdylike.appspot.com/?q=shit"+check_text)
	output=connection.read() # read response from that website
	#print (output) #print the response
	connection.close()
	if "true" in output:
		print "profanity Alert"
	elif "false" in output:
		print "this document has no curese word"
	else:
		print "couldnot scan the document properly" 








read_text()


