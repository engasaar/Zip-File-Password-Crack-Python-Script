
with open(dictionary, 'r') as f:
	for line in f.readlines():
		password = line.strip('\n')
		try:
			zip_file.extractall(pwd=password)
			password = 'Password found: %s' % password
		except:
			pass