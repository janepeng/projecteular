

def mult(array, multi):
  temp1 = []
  temp2 = [0]
  carry = 0
  for x in range(len(array)):
    digit = array[x]*multi[0]+carry
    carry = digit / 10
    digit %= 10
    temp1.append(digit)
  if carry != 0:
    temp1.append(carry)
  carry = 0
  if len(multi) > 1:
    for x in range(len(array)):
      digit = array[x]*multi[1]+carry
      carry = digit / 10
      digit %= 10
      temp2.append(digit)
    if carry != 0:
      temp2.append(carry)
    carry = 0
    for x in range(len(temp2)):
      if x >= len(temp1):
        temp2[x] += carry
      else:
        digit = temp2[x] + temp1[x] + carry
        carry = digit / 10
        digit %= 10
        temp2[x] = digit
    return temp2 
  else:
    return temp1

array = [0, 0, 1]
multi = []
for x in range(99, 2, -1):
  if x % 10 > 0:
    multi.append(x%10)
    multi.append(x/10)
  else:
    multi.append(x)
  array = mult(array, multi)
  multi = []

print array
sumnyan = 0
for x in range(len(array)):
  sumnyan += array[x]
print sumnyan
