import unittest
from user import *
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

if __name__ == "__main__":
	unittest.main()
