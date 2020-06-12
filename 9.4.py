fname = input('Enter file name: ')
try:
	fhandle = open(fname)
except:
	print ('File cannot be opened:', fname)
	exit()
emails = dict()
for line in fhandle:
	if line.startswith('From '):
		line = line.split()
		email = line[1]
		emails[email] = emails.get(email,0) + 1
largest = None
for key in emails:
	if largest is None or emails[key] > largest:
		largest = emails[key]
		sender = key
print(sender, largest)