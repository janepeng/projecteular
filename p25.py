
f1 = [1]
f2 = [1]

counter = 3
carry = 0

while 1:
  for x in range(len(f2)):
    f1[x] += f2[x] + carry
    carry = f1[x] / 10
    f1[x] %= 10
  if carry > 0:
    f1.append(carry)
    carry = 0

  if len(f1) >= 1000:
    print counter
    break


  counter += 1
  f1, f2 = f2, f1
  while len(f2) > len(f1):
    f1.append(0)
