def rock_paper_scissors(player1,player2):
	rock="rock"
	paper="paper"
	scissor="scissor"
	if player1==player2:
		return "it is a tie!"
	elif player1==rock:
		if player2==scissor:
			return "Rock wins!"
		else:
			return "Paper wins"
	elif player1==scissor:
		if player2==paper:
			return "Scissors win"
		else:
			return "Rock wins!"
	elif player1==paper:
		if player2==rock:
			return "Paper wins"
		else:
			return "Scissors win"
	else:
		return "Invalid inputs"
		sys.exist()
player1=raw_input("what is your name?")
player2=raw_input("and your name?")
user1=raw_input("%s, choose rock,paper,scissors?" %player1)
user2=raw_input("%s, choose rock,paper,scissors?" %player2)
print rock_paper_scissors(user1,user2)


    


