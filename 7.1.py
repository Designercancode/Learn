fname = input("Enter file name: ") #words.txt
fh = open(fname)
for i in fh:
    i = i.rstrip().upper()
    print(i)
