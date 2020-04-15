'''10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
time = list()
for line in handle:
    if line.startswith("From "):
        time.append(line.rstrip().split()[5][0:2])
count = dict()
for hour in time:
    count[hour] = count.get(hour,0)+1
for key,value in sorted(count.items()):
    print(key,value)



'''OUTPUT

Enter file:mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1

'''