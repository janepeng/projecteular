
import decimal

def longestRepeat(num):
  for j in range(len(num)/2):



for d in range(3, 1000):
  f = decimal.Decimal(1) / decimal.Decimal(d)
  num = str(f-int(f))[2:]
  for j in range(len(num)/2):
    for k in range(len(num)):
      tmp = num[j:j+j]
      temp = num[:j]
      if (tmp == temp):
        j += j
      



