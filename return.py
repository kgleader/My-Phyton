#Определяющая функция
def bmi(weight, height):
  index = weight / (height * height)
  return index  #sends the return value back

#Вызов функции и использование
patient_5 = bmi(61, 1.83) #stores return value
print("underweight:", patient_5 < 18.5)

#Другой вызов 
patient_7 = bmi(75, 1.74)
print("underweight:", patient_7 < 18.5)