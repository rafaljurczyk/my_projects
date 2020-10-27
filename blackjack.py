#game of blackjack
#SO YES, I DIDN'T SEPARATE THESE CLASSES INTO INDIVIDUAL FILES BUT!
#I just was writing this stuff on my holidays and didn't really care back then
#and well it's short program so I didn't really bother to update it because of how little classes it have
import random
import os

################################################################################

class Card:
	def __init__(self, suit, value, points):
		self.suit 	= suit
		self.value 	= value
		self.points = points

	def show(self):
		print("{} of {} - point = {}".format(self.value, self.suit, self.points))

################################################################################

class Deck:
	def __init__(self):
		self.cards = []
		self.build()

	def build(self):
		for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
			for value in range(2,15):
				points = value
				if value > 10:
					if value == 14:
						points = 11
					else:
						points = 10
					
				self.cards.append(Card(suit, value, points))

	def show(self):
		for card in self.cards:
			card.show()

	def deck_shuffle(self):
		random.shuffle(self.cards)
	
	def draw_a_card(self):
		return self.cards.pop()

################################################################################

class Player():
	def __init__(self, name, balance):
		self.name = name
		self.cards_on_hand = []
		self.points_on_hand = 0
		self.choice = 0
		self.is_dealer = False
		self.balance = balance
		self.stake = 0

	def draw_another_card(self, deck):
		new_card = deck.draw_a_card()
		self.cards_on_hand.append(new_card)

		self.points_on_hand += new_card.points

		if self.points_on_hand > 21:
			for card in self.cards_on_hand:
				if card.value == 14 and card.points == 11:
					card.points = 1
					self.points_on_hand -= 10
					break
				if self.points_on_hand > 21:
					break


	def show(self):
		print('\n'+self.name + ':')
		points_on_hand = 0
		for card in self.cards_on_hand:
			points_on_hand += card.points
			card.show()
		print('< {} points >'.format(points_on_hand))

	def get_balance(self):
		if not self.is_dealer:
			print('Your balance < {} $ >'.format(self.balance))

	def empty_hand(self):
		self.points_on_hand = 0
		self.cards_on_hand.clear()
		if self.is_dealer:
			self.balance = 1000000 #this is supposed to represent infinite balance for the casino

	def bet(self):
		print("How much you want to put on the stake {}? < {} $ > ".format(self.name, self.balance), end='')
		stake = 0

		while True:
			try:
				while True:
					stake = int(input(": "))
					if stake < 0 or stake > self.balance:
						print("invalid amount of money, try again")
					else:
						break
				break
			except ValueError:
				print("invalid value, try again")
		self.stake = stake
		self.balance -= self.stake

################################################################################

class Set_of_decks(Deck):
	def __init__(self):
		self.cards = []

	def add_deck(self, deck):
		for card in deck.cards:
			self.cards.append(card)

	# def split(self):

################################################################################

# class Individual_bet():
# 	def __init__(self, dealer, player):
# 		self.dealer = dealer
# 		self.player = player
# 		self.completed = False

# 	def win_check(self, decks):
# 		if player.points_on_hand == 21:
# 			while dealer.points_on_hand < 21:
# 				dealer.draw_another_card(decks())
# 			if dealer.points_on_hand == 21:
# 				print('draw! two blackjacks')
# 				player.balance += player.stake
# 			else:
# 				print('{} won!'.format(player.name))
# 				player.balance += (player.stake * 2.5)
# 			self.completed = True
# 		elif player.points_on_hand > 21 and dealer.points_on_hand <= 21:
# 			print('dealer won!')
# 			self.completed = True
# 		elif player.choice == 2:
# 			if player.points_on_hand < dealer.points_on_hand:
# 				print('dealer won!')
# 			elif player.points_on_hand == dealer.points_on_hand:
# 				print('draw')
# 				player.balance += player.stake
# 			elif player.points_on_hand > dealer.points_on_hand:
# 				while dealer.points_on_hand <players_in_the_game and dealer.points_on_hand < 21:
# 					dealer.draw_another_card
# 				if dealer.points_on_hand > 21:
# 					print('{} won!'.format(player.name))
# 					player.balance += (2 * player.stake)
# 				elif dealer.points_on_hand == player.points_on_hand:
# 					print('draw')
# 					player.balance += player.stake
# 				elif dealer.points_on_hand > player.points_on_hand:
# 					print('dealer won!')
# 			self.completed = True


################################################################################
#  /\ classes /\                      						\/ definitions \/  #
################################################################################

def turn_course():
	choice = 0
	while True:
		try:
			choice = int(input('What you want to do?:\n1.draw another card\n2.pass\n'))
			if choice<1 or choice>2:
				print('invalid number, try agian!\n')
			else:
				break
		except ValueError:
			print('invalid value, try again!\n')
		print('\n\n')
	return choice

################################################################################

def win_check(players_in_the_round, decks, dealer):
	winners = []
	for player in players_in_the_round:
		if player.points_on_hand == 21:
			winners.append(player)
		if player.points_on_hand > 21:
			players_in_the_round.remove(player)
	
	if len(winners) > 0:
		while dealer.points_on_hand < 21:	
			dealer.draw_another_card(decks)
		if dealer.points_on_hand == 21 and dealer not in winners:
			winners.append(dealer)
		if len(winners) > 1:
			print('BLACKJACK! The winners are: ')
			for player in winners:
				print(player.name)
				player.balance += (2* player.stake)
		else:
			print('BLACKJACK! The winner is: {}'.format(winners[0].name))
			winners[0].balance += (2.5* winners[0].stake)
		return True

	return False

################################################################################

def pass_check(players_in_the_round, decks, dealer):
	biggest_score = 0
	for p in players_in_the_round:
		if p.is_dealer:
			continue
		if p.points_on_hand < 21:
			biggest_score = p.points_on_hand

	if biggest_score == 0:
		print('dealer won!')
		return True

	while True:
		if dealer.points_on_hand < biggest_score:
			dealer.draw_another_card(decks)
		if dealer.points_on_hand > 21:
			for p in players_in_the_round:
				if p.is_dealer:
					continue
				if p.points_on_hand == biggest_score:
					print('{} won!'.format(p.name))
					p.balance += (2* p.stake)
			return True
		if dealer.points_on_hand > biggest_score:
			print('dealer won!')
			return True
		elif dealer.points_on_hand == biggest_score:
			print('tie!')
			p.balance += p.stake
			return True

################################################################################

# def game_menu():
# 	print("Welcome to my own BLACKJACK game!\nChoose one of the options:\n1.Play the game\n2.Add a player\n3.Show balance\n4.exit the game")
# 	choice = 4
# 	while True:
# 		try:
# 			choice = int(input(': '))
# 			if choice < 1 or choice > 4:
# 				print('ivalid number, try again')
# 			break
# 		except ValueError:
# 			print('invalid value, try again')
# 	return choice

################################################################################

def main():
	
	players_in_the_game = []
	# bets_in_the_game = []
	dealer = Player('Dealer', 1000000)
	dealer.is_dealer = True
	player1 = Player('Marta', 10000)
	players_in_the_game.append(dealer)
	players_in_the_game.append(player1)

	decks = Set_of_decks()
	decks.add_deck(Deck())

	end_game = False
	while not end_game:
		os.system('clear')

		if len(players_in_the_game) < 1:
			print("there is at least 1 player required excluding the Dealer")
			break

		if not players_in_the_game[0].is_dealer:
			print("the first player should always be a Dealer")
			break

		# bets_in_the_game.clear()
		players_in_the_round = players_in_the_game

		for p in players_in_the_round:
			p.empty_hand()
			if not p.is_dealer:
				p.bet()
				# bets_in_the_game.append(Individual_bet(dealer, p))


			
		#you can change the value ( 60 ) so more decks are in game and it is harder to count the cards

		if len(decks.cards) < 60:
			decks.add_deck(Deck())
			decks.deck_shuffle()
			decks.deck_shuffle() #we shuffle two times just to be sure that this deck is shuffled!

		for i in range(0,2): #all players have to draw 2 cards at the beggining of every round
			for p in players_in_the_round:
				p.draw_another_card(decks)

		win_condition = win_check(players_in_the_round, decks, dealer)
		# for b in bets_in_the_game:
		# 	if not b.completed:
		# 		b.win_check(decks)
		# 	if b.completed:
				


		if win_condition:
			break

		for p in players_in_the_round:
			if p.is_dealer:
				continue
			p.show()
			p.choice = turn_course()


		while not win_condition:
			# os.system('clear')
			pass_bool = True
			for p in players_in_the_round:
				if p.is_dealer:
					continue

				if p.choice == 1:
					p.draw_another_card(decks)
					if p.points_on_hand < 21:
						pass_bool = False
				elif p.choice == 2:
					pass

			if pass_bool:
				win_condition = pass_check(players_in_the_round, decks, dealer)
				break

			for p in players_in_the_round:
				if p.is_dealer:
					continue
				p.show()
				p.choice = turn_course()

			win_condition = win_check(players_in_the_round, decks, dealer)

		end_game = win_condition



		for p in players_in_the_round:
			p.show()
			p.get_balance()

################################################################################

if __name__ == "__main__":
	main()



