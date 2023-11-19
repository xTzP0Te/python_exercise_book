# Многие люди на планете привыкли рассчитывать рост человека в футах
# и дюймах, даже если в их стране принята метрическая система. Напишите
# программу, которая будет запрашивать у пользователя количество футов,
# а затем дюймов в его росте. После этого она должна пересчитать рост
# в сантиметры и вывести его на экран.

feet = int(input("Введите ваш рост в футах: "))
inches = int(input("Введите оставшиеся дюймы: "))

total_inches = feet * 12 + inches
cm = total_inches * 2.54

print(f"Ваш рост составляет {cm:.2f} сантиметров.")