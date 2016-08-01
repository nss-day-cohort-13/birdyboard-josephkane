import random
import csv

class User:

	def __init__(self, screen_name, full_name):
		self.screen_name: screen_name
		self.full_name: full_name
		self.user_id: self.random_id_generator()

	def random_id_generator(self):
		random_id = random.random() * 1000
		print("id: ", random_id)
		return random_id

	def write_user_to_csv_file(self, user, file):
		with open("{}".format(file), "w+", newline = " ") as csv_file:
			writer = csv.writer(csv_file)
			writer.writerow([user["user_id"], user["screen_name"], user["full_name"]])

	def get_users_from_csv(self, file):
		with open("{}".format(file), "r", newline = " ") as csv_file:
			reader = csv.reader(csv_file)
			for user in reader:
				print(user)
