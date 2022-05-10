
def deposit_interest(deposit, age):
  
  if deposit < 100 or deposit > 10000 or age < 18:
    return "Unavailable"
  else:
    if age >= 60:
      return 2.0
    else:
      if deposit >= 100 and deposit <= 999:
        return 1.0
      elif deposit >= 1000 and deposit <= 4999:
        return 1.3
      elif deposit >= 5000 and deposit <= 10000:
        return 1.5
