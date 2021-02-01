def name_format(name, lname):
  name.split()
  lname.split()
  name.lower()
  lname.lower()
  f_name=name.capitalize()
  l_name=lname.capitalize()
  return print(f"{f_name} {l_name}\n")


name=input("Your name: ")
lname=input("Your last name:")
name_format(name, lname)
  