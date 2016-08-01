# Singleton pattern?

import csv

def write_user_to_csv_file(user, file):
	with open("{}".format(file), "a+", newline = "") as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow([user.user_id, user.screen_name, user.full_name])

def get_users_from_csv(file):
	with open("{}".format(file), "r", newline = "") as csv_file:
		reader = csv.reader(csv_file)
		for user in reader:
			yield user
