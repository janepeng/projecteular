

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
  if year % 4 != 0:
    days[1] = 28
  elif year % 100 != 0:
    days[1] = 29
  elif year % 400 == 0:
    days[1] = 29
  else:
    days[1] = 28

date = 1
count = 0

for year in range(1900, 2001):
  isLeapYear(year)
  for month in range(1, 13):
    for day in range(1, days[month-1]+1):
      if day == 1 and year != 1900 and date == 7:
        count += 1
      date += 1
      if date > 7:
        date = 1


print count

