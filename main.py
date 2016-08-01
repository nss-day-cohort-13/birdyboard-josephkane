import time

class MainMenu:

	def __init__(self):
		print("")
		print(" ~ WELCOME TO BIRDYBOARD ~ ")

	def show_menu(self):
		"""
		Displays menu from which users will navigate app
		"""
		print("")
		print("What would you like to do?")
		print("1. New user account")
		print("2. Select user")
		print("3. View chirps")
		print("4. Public chirp")
		print("5. Private chirp")
		print("6. Quit")
		action = input("> ")

		try:
			if int(action) > 0 and int(action) < 7:
				if action == "1":
					print("create a new user")
				elif action == "2":
					print("select a user")
				elif action == "3":
					print("view all chirps")
				elif action == "4":
					print("new public chirp")
				elif action == "5":
					print("new private chirp")
				elif action == "6":
					exit()

				if action != "6":
					time.sleep(1)
					self.show_menu()

		except ValueError:
			print("")
			print("Please enter a valid choice.")
			print("")
			time.sleep(1)
			self.show_menu()

if __name__ == "__main__":
	mm = MainMenu()
	mm.show_menu()
