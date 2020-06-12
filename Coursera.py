fname = input("Enter file name: ")
fh = open(fname)
s = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue

    start = line.find(":")
    piece = line[start+1:len(line)]
    end = float(piece)

    s = s + end
    count = count+1
    avg = s/count
print("Average spam confidence:", avg)
#mbox-short.txt