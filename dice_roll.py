#dice roll simulator
import random


def mainLoop():
	x = 6
	while True:
		print('\n---- current roll range: {} ----\n'.format(x))
		command = str(input('type "roll" to roll a dice\ntype "change" to change dice number range\ntype "exit" to exit the simulator\n: '))
		if command == 'roll':
			print(random.randint(1,x))
		elif command == 'change':
			while True:
				try:
					x = int(input('give me a new range!\n: '))
					break
				except:
					print('invalid number, try again\n')

		elif command == 'exit':
			print('thanks for playing! exiting now...')
			break
		else:
			'there isn\'t such a command'

if __name__ == "__main__":
	mainLoop()