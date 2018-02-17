#website that contains favouirite movie 
import webbrowser
class Movie():
	#define init 
	#create space in memory for new instances
	def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
		#intialize pieces of information about the movies
		self.title=movie_title
		self.storyline=movie_storyline
		self.poster_image_url=poster_image
		self.trailer_youtube_url=trailer_youtube
#create a method that opens trailers webpage
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url,new=2)
