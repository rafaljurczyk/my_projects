#conatct book
import os

class Contact():
	#class that we will use for every invidual contact in our ContactBook
	def __init__(self, first_name, last_name, phone_num):
		self.first_name = first_name
		self.last_name  = last_name
		self.phone_num  = phone_num

	def add_phone_num(self, phone_num):
		self.phone_num.append(phone_num)

	def details(self):
		print('Contact: {} {}'.format(self.first_name, self.last_name))
		print('Phone numbers: ',end='')
		for number in range(len(self.phone_num)):
			print(self.phone_num[number])

def start_text():
	option = 0
	while True:
		try:
			print('\n\nType a number that represent what would you like to do')
			option = int(input('1. add a new contact\n2. show contact list\n3. delete existing contact\n4. show details\n5. exit ContactBook\n'))
			break
		except ValueError:
			os.system('clear')
			print('\n!!! The option you choose has to be a number! Try again. !!!\n')
	return option

def add_contact():
	first_name = input('\nType contact\'s first name: ')
	last_name  = input('\nType contact\'s last name: ')
	phone_num  = input('\nType contact\'s phone number: ')
	return Contact(first_name, last_name, phone_num)


def main_loop():
	contact_list = []
	while True:
		option = start_text()
		if option == 1:
			os.system('clear')
			contact_list.append(add_contact())

		elif option == 2:
			os.system('clear')
			for x in range(len(contact_list)):
				print(str(x+1) + '. ' + contact_list[x].first_name + ' ' + contact_list[x].last_name)

		elif option == 3:
			os.system('clear')
			print('In order delete a contact you have to type it\'s full first and lastname: ')
			contact = str(input(' '))
			for x in range(len(contact_list)):
				if (contact_list[x].first_name + ' ' + contact_list[x].last_name) == contact:
					del contact_list[x]

		elif option == 4:
			os.system('clear')
			print('In order to see contact details you have to type it\'s full first and lastname: ')
			contact = str(input(' '))
			for x in contact_list:
				if (x.first_name + ' ' + x.last_name) == contact:
					x.details()


		elif option == 5:
			os.system('clear')
			print('exiting...')
			break

		else:
			os.system('clear')
			print('No option attached to this number. Try again.')
			continue




if __name__ == "__main__":
	main_loop()

