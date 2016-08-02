# Singleton pattern?

import csv

def write_user_to_csv_file(user, file):
	with open("{}".format(file), "a+", newline = "") as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow([user.user_id, user.screen_name, user.full_name])

def get_users_from_csv_file(file):
	with open("{}".format(file), "r", newline = "") as csv_file:
		reader = build_user_dict(csv.reader(csv_file))
		return reader

def build_user_dict(user_list):
	user_dict = {user[0]: [user[1], user[2]] for user in user_list}
	return user_dict

