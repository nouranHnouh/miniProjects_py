import media 
import fresh_tomatoes

#define couples of movies to add into webpage
toy_story=media.Movie("Toy story 3 (2010)",
	                  "A story of a boy and his toys that come to life",
	                  "https://vignette.wikia.nocookie.net/disney/images/9/93/Toy_story.jpg/revision/latest?cb=20130526174438",
	                  "https://www.youtube.com/watch?v=KYz2wyBy3kc") 

#print(toy_story.storyline)

insidious=media.Movie("Insidious (2010)",
                      "the story centers on a couple whose son inexplicably enters a comatose state and becomes a vessel for ghosts in an astral dimension who want to inhabit his body",
                      "https://upload.wikimedia.org/wikipedia/en/2/2d/Insidious_poster.jpg",
                      "https://www.youtube.com/watch?v=0Q0x8KYwnns")
#print(insidious.storyline)
#insidious.show_trailer()
#toy_story.show_trailer()

anastasia=media.Movie("Anastasia (1997)",
	                  "A brave young woman sets out to discover the mystery of her past. Pursued by a ruthless Soviet officer determined to silence her, Anya enlists the aid of a dashing conman and a lovable ex-aristocrat. Together, they embark on an epic adventure to help her find home, love, and family",
	                  "https://vignette.wikia.nocookie.net/foxsanastasia/images/8/88/Anastasia_Golden.jpg/revision/latest?cb=20110710222949",
	                  "https://www.youtube.com/watch?v=eNj53-mu7xw")
annabella=media.Movie("Annabelle:Creation",
	                  "Former toy maker Sam Mullins and his wife, Esther, are happy to welcome a nun and six orphaned girls into their California farmhouse. Years earlier, the couple's 7-year-old daughter Annabelle died in a tragic car accident. Terror soon strikes when one child sneaks into a forbidden room and finds a seemingly innocent doll that appears to have a life of its own",
	                  "https://upload.wikimedia.org/wikipedia/en/0/08/Annabelle_Creation.jpg",
	                  "https://www.youtube.com/watch?v=KisPhy7T__Q&t=1s")
shutter_island=media.Movie("Shutter Island (2010)",
	                       "The implausible escape of a brilliant murderess brings U.S. Marshal Teddy Daniels (Leonardo DiCaprio) and his new partner (Mark Ruffalo) to Ashecliffe Hospital, a fortress-like insane asylum located on a remote, windswept island. The woman appears to have vanished from a locked room, and there are hints of terrible deeds committed within the hospital walls.",
                           "http://www.imfdb.org/images/7/76/Shutterislandposter.jpg",
                           "https://www.youtube.com/watch?v=5iaYLCiq5RM")

#list of movies to be added into the webpage 
movies=[toy_story,insidious,anastasia,annabella,shutter_island]
fresh_tomatoes.open_movies_page(movies)

