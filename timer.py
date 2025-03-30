import time

number = int(input("Сан киргиз (секунд): "))

while number >= 0:
    print(number)
    time.sleep(1)  #1 sekunda kutot
    number = number + 1

print("Ubakyt buttu!")
