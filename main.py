import time
from user import *
from csv_utility import *
from random_id_generator import *
from chirps import *
from chirps_utility import *
from user_utility import *
from convo_utility import *

class MainMenu:

	def __init__(self):
		print("")
		print(" ~ WELCOME TO BIRDYBOARD ~ ")
		self.users = {}
		self.chirps = {}
		self.current_user = {}
		self.public_conversations = {}
		self.private_conversations = {}
		try:
			self.users = CSV.get_users_from_csv_file("users.csv")
			self.chirps = CSV.get_chirps_from_csv_file("chirps.csv")
			self.public_conversations = CSV.get_convos_from_csv_file("public_convos.csv")
			self.private_conversations = CSV.get_convos_from_csv_file("private_convos.csv")
		except FileNotFoundError:
			pass

	def show_menu(self):
		"""
		Displays menu from which users will navigate app

		Args- None
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
					print("\nEnter full name")
					full_name = input("> ")
					print("")
					print("Enter screen name")
					screen_name = input("> ")
					user = UserUtility.create_user(full_name, screen_name)
					CSV.write_user_to_csv_file(user, "users.csv")
					self.current_user = user
					self.users = CSV.get_users_from_csv_file("users.csv")
					print("Welcome, {}!".format(self.current_user.screen_name))

				elif action == "2":
					try:
						self.current_user = UserUtility.select_a_user(self.users, self.current_user)
						print("Welcome, {}!".format(self.current_user.screen_name))
					except AttributeError:
						print("")
						print("No users are registered.")

				elif action == "3":
					selected_convo_id = ChirpsUtility.view_chirps(
						self.public_conversations,
						self.private_conversations,
						self.chirps,
						self.current_user
					)
					if selected_convo_id[1] == "public":
						chirp_list = self.public_conversations[selected_convo_id[0]]
						updated_convo = ConvoUtility.show_public_reply_menu(
								self.chirps,
								chirp_list,
								self.current_user.screen_name
								)
						self.public_conversations[selected_convo_id[0]] = updated_convo
						CSV.write_updated_convos_to_csv_file(self.public_conversations, "public_convos.csv")
						self.public_conversations = CSV.get_convos_from_csv_file("public_convos.csv")
						self.chirps = CSV.get_chirps_from_csv_file("chirps.csv")
					elif selected_convo_id[1] == "private":
						chirp_list = self.private_conversations[selected_convo_id[0]]
						updated_convo = ConvoUtility.show_private_reply_menu(
								self.chirps,
								chirp_list,
								self.current_user.screen_name
								)
						self.private_conversations[selected_convo_id[0]] = updated_convo
						CSV.write_updated_convos_to_csv_file(self.private_conversations, "private_convos.csv")
						self.private_conversations = CSV.get_convos_from_csv_file("private_convos.csv")
						self.chirps = CSV.get_chirps_from_csv_file("chirps.csv")

				elif action == "4":
					public_chirp = ChirpsUtility.new_public_chirp(self.current_user.screen_name)
					self.chirps = CSV.get_chirps_from_csv_file("chirps.csv")
					convo = ConvoUtility.new_public_convo([public_chirp.chirp_id], self.current_user)
					self.public_conversations[convo.convo_id] = convo.chirp_list
					CSV.write_new_convos_to_csv_file(self.public_conversations, "public_convos.csv")
					self.chirps = CSV.get_chirps_from_csv_file("chirps.csv")

				elif action == "5":
					private_chirp = ChirpsUtility.new_private_chirp(self.current_user.screen_name, self.users)
					self.chirps = CSV.get_chirps_from_csv_file("chirps.csv")
					convo = ConvoUtility.new_private_convo([private_chirp.chirp_id], self.current_user)
					self.private_conversations[convo.convo_id] = convo.chirp_list
					CSV.write_new_convos_to_csv_file(self.private_conversations, "private_convos.csv")
					self.chirps = CSV.get_chirps_from_csv_file("chirps.csv")

				elif action == "6":
					exit()

				if action != "6":
					time.sleep(1)
					self.show_menu()

		except ValueError as ex:
			print(ex)
			print("\nPlease enter a valid choice.\n")
			time.sleep(1)
			self.show_menu()

if __name__ == "__main__":
	mm = MainMenu()
	mm.show_menu()
