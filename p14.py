
maxlen = 1
starting = 2
length = 1

for n in range(2, 1000000):
#for n in range(13, 14):
  if length > maxlen:
    maxlen = length
    starting = n - 1
  length = 1 
  while n > 1:
    if n % 2 == 0:
      n /= 2
    else:
      n = 3 * n + 1
    length += 1

print starting
