# Упражнение 8. Сувениры и безделушки
# Интернет-магазин занимается продажей различных сувениров и безде-
# лушек. Каждый сувенир весит 75 г, а безделушка – 112 г. Напишите про-
# грамму, запрашивающую у пользователя количество тех и других покупок,
# после чего выведите на экран общий вес посылки.

weight_souvenir = 75
weight_trinket = 112

num_souvenirs = int(input("Введите количество сувениров: "))
num_trinkets = int(input("Введите количество безделушек: "))

total_weight = (num_souvenirs * weight_souvenir) + (num_trinkets * weight_trinket)

print(f"Общий вес посылки: {total_weight} г")