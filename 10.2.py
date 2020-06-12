# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of
# the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a
# second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = input('Enter file name: ')
try:
    fhandle = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
emails = dict()
for line in fhandle:
    if line.startswith('From '):
        line = line.split()
        email = line[5]
        email = email.split(':')
        hour = email[0]
        emails[hour] = emails.get(hour, 0) + 1
hourslist = []
for hour, count in emails.items():
    hourslist.append((hour, count))
hourslist.sort()
for hour, count in hourslist:
    print(hour, count)
