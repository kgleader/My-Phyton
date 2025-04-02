# Уровень глюкозы - входные данные для этого программного обеспечения
glucose_level = int(input())

# Вывод сообщения, если уровень глюкозы меньше 70
if glucose_level < 70:
    print("Low glucose level")

# Вывод сообщения, если уровень глюкозы больше 140
elif glucose_level > 140:
    print("High glucose level")

# Вывод сообщения, если ни одно из условий выше не выполняется
else:
    print("Normal range")
