
names = []

with open('names.txt', 'r') as f:
  for line in f:
    names = line.strip().split(',')

for x in range(len(names)):
  names[x] = names[x][1:-1]

names.sort()

scores = []
tempsum = 0;
for x in range(len(names)):
  for i in range(len(names[x])):
    tempsum += ord(names[x][i]) - 64
  tempsum = tempsum*(x+1)
  if names[x] == 'COLIN':
    print 'COLIN', x, tempsum
  scores.append(tempsum)
  tempsum = 0

tempsum = 0
for x in range(len(scores)):
  tempsum += scores[x]

print tempsum

