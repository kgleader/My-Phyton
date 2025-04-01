age = 16
is_student = True

if age < 18:

  #выполнить, если возраст меньше 18
  if is_student:
    #выполнить, если меньше 18 и студент
    print("20% discount")
  else:
    #выполнить, если меньше 18 и не студент
    print("10% discount")
else:
  #выполнить этот код, если возраст 18 или больше
  print("Regular price")
