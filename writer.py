def write_to_csv(data, filename, header):
	if os.path.isfile(filename):
		with open(filename, 'a') as f:
			file_writer = csv.DictWriter(f, fieldnames=header)
			for line in data:
				file_writer.writerow(line)
	else:
		with open(filename, 'w') as f:
			file_writer = csv.DictWriter(f, fieldnames=header)
			file_writer.writeheader()
			for line in data:
				file_writer.writerow(line)
