def view_chirps(chirps_list):
	print("")
	counter = 1
	chirps_id_list = list()
	for k, v in chirps_list.items():
		print("{0}. {1}: {2}".format(counter, v[0], v[1]))
		chirps_id_list.append(k)
		counter += 1