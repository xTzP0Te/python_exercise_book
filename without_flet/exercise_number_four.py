# Упражнение 4. Площадь садового участка
# Создайте программу, запрашивающую у пользователя длину и ширину
# садового участка в футах. Выведите на экран площадь участка в акрах.

width = int(input("Введите ширину в футах: "))
length = int(input("Введите длину в футах: "))

print("Ваш садовый участок равен", (width*length)/43560, "акр")
