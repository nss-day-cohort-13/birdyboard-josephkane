from main import *
from chirps import *
from user import *
from chirps_utility import *
from user_utility import *
from random_id_generator import *
from csv_utility import *
from test_chirps import *
from test_csv_methods import *
from test_user import *
from test_conversation import *

if __name__ == "__main__":
	unittest.main()

# python -m unittest discover -s . -p "test*.py" -v
