import random
import csv

class User:

	def __init__(self):
		self.screen_name = None
		self.full_name = None
		self.user_id = None

	def random_id_generator(self):
		random_id = int((random.random() + 1) * 10000)
		return random_id

	def create_new_user(self, screen_name, full_name):
		user = User()
		user.screen_name = screen_name
		user.full_name = full_name
		user.user_id = self.random_id_generator()
		return user

	def write_user_to_csv_file(self, user, file):
		with open("{}".format(file), "w+", newline = "") as csv_file:
			writer = csv.writer(csv_file)
			writer.writerow([user.user_id, user.screen_name, user.full_name])

	def get_users_from_csv(self, file):
		with open("{}".format(file), "r", newline = "") as csv_file:
			reader = csv.reader(csv_file)
			for user in reader:
				print(user)
