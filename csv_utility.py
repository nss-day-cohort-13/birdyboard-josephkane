import csv

class CSV:

	def build_dict_from_list(reader):
		"""
		Builds a dictionary from a list provided by a CSV file

		Args- any list
		"""
		a_dict = {a_list[0]: a_list[1:] for a_list in reader}
		return a_dict

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
		with open("{}".format(file), "r+", newline = "") as csv_file:
			reader = CSV.build_dict_from_list(csv.reader(csv_file))
			return reader

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
		with open("{}".format(file), "r+", newline = "") as csv_file:
			reader = CSV.build_dict_from_list(csv.reader(csv_file))
			return reader

	def write_new_convos_to_csv_file(convo_dict, file):
		"""
		Writes conversations dict to a CSV file

		Args- conversation dict, filepath
		"""
		with open("{}".format(file), "w+", newline = "") as csv_file:
			for k, v in convo_dict.items():
				writer = csv.writer(csv_file)
				some_list = [k]
				some_list.extend(v)
				writer.writerow(some_list)


	def write_updated_convos_to_csv_file(convo_dict, file):
		"""
		Writes conversations dict to a CSV file

		Args- conversation dict, filepath
		"""
		with open("{}".format(file), "w+", newline = "") as csv_file:
			for k, v in convo_dict.items():
				writer = csv.writer(csv_file)
				some_list = [k]
				some_list.extend([d for d in v])
				writer.writerow(some_list)

	def get_convos_from_csv_file(file):
		"""
		Gets information from a CSV file and returns a dictionary of chirps

		Args- filepath
		"""
		with open("{}".format(file), "r+", newline = "") as csv_file:
			reader = CSV.build_dict_from_list(csv.reader(csv_file))
			return reader
