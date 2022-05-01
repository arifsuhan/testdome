
def life_period(age):
  
  if age == 0:
    return "INVALID"
  elif age > 0 and age < 16:
    return "CHILD"
  elif age >= 16:
    return "ADULT"