import os

def get_input_row():
	try:
		row = int(input('Choose a row: '))
		while row<0 or row>2:
			row = int(input('invalid row you dumbfuck, choose again: '))
		return row
	except ValueError:
		print('invalid value you muffin head!')
		get_input_row()

def get_input_column():
	try:
		column = int(input('Choose a column: '))
		while column<0 or column>2:
			column = int(input('invalid column you dumbfuck, choose again: '))
		return column
	except ValueError:
		print('invalid value you muffin head!')
		get_input_column()

def make_move(even, board):
	is_avaible = False
	while not is_avaible:
		row = get_input_row()
		column = get_input_column()
		is_avaible = check_availability(board, row, column,)
	if even[0]:
		board[row][column] = 1
		even[0] = False
	else:
		board[row][column] = 2
		even[0] = True

def check_availability(board, row, column):
	if board[row][column] == 0:
		return True
	else:
		print('That field is already occupied\n')
		return False

def end_condition(board):
	for rows in range(3):
		#checking columns
		for columns in range(3):
			if board[0][columns] != 0 and board[0][columns] == board[1][columns]:
				if board[1][columns] == board[2][columns]:
					if board[0][columns] == 1:
						print('player number 1 wins!')
					else:
						print('player number 2 wins!')
					return True
		#checking rows
		if board[rows][0] != 0 and board[rows][0] == board[rows][1]:
			if board[rows][1] == board[rows][2]:
				if board[rows][0] == 1:
					print('player number 1 wins!')
				else:
					print('player number 2 wins!')
				return True

	#checking diagonals
	if board[0][0] != 0 and board[0][0] == board[1][1]:
		if board[1][1] == board[2][2]:
			if board[0][0] == 1:
				print('player number 1 wins')
			else:
				print('player number 2 wins')
			return True
	if board[0][2] != 0 and board[0][2] == board[1][1]:
		if board[1][1] == board[2][0]:
			if board[0][2] == 1:
				print('player number 1 wins')
			else:
				print('player number 2 wins')
			return True

	#none of the conditions were satisfied
	return False

def main_loop():
	board = [[0,0,0],[0,0,0],[0,0,0]]
	end_bool = False
	even =[True]
	i = 2

	while not end_bool:
		os.system('clear')
		for rows in range(3):
			for columns in range(3):
				print(str(board[rows][columns]) + ' ', end='')
			print('\n')
		if even[0]:
			print('it\'s cross turn\n')
		else:
			print('it\'s circle turn\n')

		make_move(even, board)
		end_bool = end_condition(board)

if __name__ == "__main__":
	main_loop()