

#012 021 102 120 201 210

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def perm(array):
  if len(array) <= 1:
    yield array
    return
  else:
    for i in array:
      for j in perm(list(set(array) - set([i]))):
        yield [i] + j

counter = 0
for i in perm(array):
  counter += 1
  if counter == 1000000:
    print i
    break
 
