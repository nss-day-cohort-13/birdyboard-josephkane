import unittest
from user import *
from chirps import *
from csv_utility import *
from random_id_generator import *

class TestCSVMethods(unittest.TestCase):

	def test_csv_methods_return_user_dict(self):
		test_user_dict = {19108: ["jkane", "joe"]}
		user = User("joe", "jkane", random_id_generator())
		CSV.write_user_to_csv_file(user, "test_csv.csv")
		user_dict = CSV.get_users_from_csv_file("test_csv.csv")
		for key, value in user_dict.items():
			self.assertEqual(value, test_user_dict[19108])

	def test_csv_methods_return_public_chirps_dict(self):
		test_chirps_dict = {19108: ["jkane", "Hello world", "public"]}
		chirp = PublicChirp("Hello world", "jkane", 19108)
		CSV.write_public_chirp_to_csv_file(chirp, "test_chirp_csv.csv")
		chirps_dict = CSV.get_chirps_from_csv_file("test_chirp_csv.csv")
		for key, value in chirps_dict.items():
			self.assertEqual(value, test_chirps_dict[19108])

	def test_csv_methods_return_private_chirps_dict(self):
		test_chirps_dict = {19108: ["jkane", "ekane", "Hello world"]}
		chirp = PrivateChirp("Hello world", "jkane", "ekane", 19108)
		CSV.write_private_chirp_to_csv_file(chirp, "test_chirp_csv.csv")
		chirps_dict = CSV.get_chirps_from_csv_file("test_chirp_csv.csv")
		for key, value in chirps_dict.items():
			self.assertEqual(value, test_chirps_dict[19108])

if __name__ == "__main__":
	unittest.main()
