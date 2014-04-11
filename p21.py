
diversors = [0, 1]

sumofd = 0

for x in range(2, 10000):
  for y in range(1, x):
    if x % y == 0:
      sumofd += y
  diversors.append(sumofd)
  sumofd = 0

total = 0;

for x in range(1, len(diversors)):
  if diversors[x] < 10000 and diversors[diversors[x]] == x and diversors[x] > x:
    total += x
    total += diversors[x]
    print x, diversors[x]

print total      
