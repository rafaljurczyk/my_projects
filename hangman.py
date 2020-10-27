#hangman program
import random
import os

word_list = ('duoking', 'trioking', 'troll', 'marnotractwo', 'dobra zabawa')

def pickLetter():
	x = 'a'
	try:
		x = input('choose a letter: ').split(' ')[0]
		x = x[0]
	except ValueError:
		print('we\'ve got a problem with value dude... pick again')
		pickLetter()
	os.system('clear')
	return x

def pickWord(picked_word):
	print('Welcome to Hangman by Rafał Jurczyk. \nYou\'ll see a blank word which you have to uncover by guessing single letters. \nThe game is designed that even if you input full word only the first letter will matter. \nGood luck!\n\n')
	player_word = []
	for letter in picked_word:
		if letter == ' ':
			player_word.append(' ')
		else:
			player_word.append('_')
	print(picked_word)
	return player_word

def mainLoop():
	picked_word = random.choice(word_list)
	player_word = pickWord(picked_word)

	lose_condition = 0
	#MainLoop
	while True:
		for letter in player_word:
			print(letter+' ', end='')
		print('\n')
		letter = pickLetter()
		if letter in picked_word:
			for x in range(len(picked_word)):
				if picked_word[x] == letter:
					player_word[x] = letter
		else:
			print('nie ma!')
			lose_condition += 1
			if lose_condition >= 5:
				print('You suck! And, you lose!')
				break
		if not '_' in player_word:
			print('Congratulation! You win!')
			break
		
		
	


if __name__ == "__main__":
	mainLoop()