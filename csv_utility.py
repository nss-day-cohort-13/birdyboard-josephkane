import csv

class CSV:

	def write_user_to_csv_file(user, file):
		"""
		Writes user object to a CSV file

		Args- user object, filepath
		"""
		with open("{}".format(file), "a+", newline = "") as csv_file:
			writer = csv.writer(csv_file)
			writer.writerow([user.user_id, user.screen_name, user.full_name])

	def get_users_from_csv_file(file):
		"""
		Gets information from a CSV file and returns a dictionary of users

		Args- filepath
		"""
		with open("{}".format(file), "r", newline = "") as csv_file:
			reader = CSV.build_user_dict(csv.reader(csv_file))
			return reader

	def build_user_dict(user_list):
		"""
		Builds a user dictionary from a list provided by a CSV file

		Args- list of users (from CSV file)
		"""
		user_dict = {user[0]: [user[1], user[2]] for user in user_list}
		return user_dict

	def write_public_chirp_to_csv_file(chirp, file):
		"""
		Writes public chirp object to a CSV file

		Args- public chirp object, filepath
		"""
		with open("{}".format(file), "a+", newline = "") as csv_file:
			writer = csv.writer(csv_file)
			writer.writerow([chirp.chirp_id, chirp.author, chirp.message, chirp.permission])

	def write_private_chirp_to_csv_file(chirp, file):
		"""
		Writes private chirp object to a CSV file

		Args- private chirp object, filepath
		"""
		with open("{}".format(file), "a+", newline = "") as csv_file:
			writer = csv.writer(csv_file)
			writer.writerow([chirp.chirp_id, chirp.author, chirp.recipient, chirp.message, chirp.permission])

	def get_chirps_from_csv_file(file):
		"""
		Gets information from a CSV file and returns a dictionary of chirps

		Args- filepath
		"""
		with open("{}".format(file), "r", newline = "") as csv_file:
			reader = CSV.build_chirps_dict(csv.reader(csv_file))
			return reader

	def build_chirps_dict(chirps_list):
		"""
		Builds a chirps dictionary from a list provided by a CSV file

		Args- list of chirps (from CSV file)
		"""
		chirps_dict = {chirps[0]: [chirps[1], chirps[2], chirps[3]] for chirps in chirps_list}
		return chirps_dict
