
def sum(array, addie):
  carry = 0
  for i in range(len(array)):
    if i >= len(addie): 
      if array[i] + carry >= 10:
        array[i] += carry
        carry = array[i]/10
        array[i] %= 10
      else:
        array[i] += carry
        carry = 0
        break
    elif array[i] + carry + addie[i] >= 10:
      array[i] += addie[i] + carry
      carry = array[i] / 10
      array[i] %= 10
    else:
      array[i] += carry + addie[i]
      carry = 0;
  if carry > 0:
    array.append(carry)
  return array

def main():
  temp = [0 for x in xrange(50)]
   
  with open('input.txt') as f:
    for line in f:
      line = line.rstrip()
      addie = []
      for c in line:
        num = int(c)
        addie.append(num)
      #print addie[::-1]
      temp = sum(temp, addie[::-1])
    print temp[::-1]


main()
