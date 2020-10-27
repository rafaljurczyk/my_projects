import random

#here a problem occured:
#when I wanted to return x immediately in 'try' field it catched the error BUT the 'guess' variable that was the final destination of returned variable was defined as NoneType
#and that was a problem cause new right "returns" couldn't write into 'guess' variable due to it's NoneType. That's why I needed to make an 'x' outside try/except 
def getNumber():
	x = 0
	while True:
		try:
			x = int(input('gimme a number! '))
			break
		except ValueError:
			print('invalid value you fuckhead...')
	return x
			

def main():
	random_number = random.randint(0,10)
	guess = getNumber()
	turn = 1
	while guess != random_number:
		turn += 1
		if guess < random_number:
			print('aim higher!')
		else:
			print('too hight dude!')
		guess = getNumber()
	print('\n You win! It took you only '+str(turn))

if __name__ == "__main__":
	main()