# Создайте программу, которая запрашивает у пользователя два целых чис-
# ла a и b, после чего выводит на экран результаты следующих математи-
# ческих операций:
#  сумма a и b;
#  разница между a и b;
#  произведение a и b;
#  частное от деления a на b;
#  остаток от деления a на b;
#  десятичный логарифм числа a;
#  результат возведения числа a в степень b

import math
import flet as ft


def main(page: ft.Page):
    def button_clicked(e):
        a = int(number_a.value)
        b = int(number_b.value)
        text_output.value = "Сумма: " + str(a+b) + '\n'
        text_output.value += "Вычитание: " + str(a-b) + "\n"
        text_output.value += "Произведение: " + str(a*b) + "\n"
        text_output.value += "Частное: " + str(a/b) + "\n"
        text_output.value += "Остаток от деления: " + str(a % b) + "\n"
        text_output.value += ("Десятичный логарифм числа a: " +
                              str(math.log10(a)) + "\n")
        text_output.value += ("Возведения числа a в степень b: " +
                              str(a**b) + "\n")

        page.update()

    number_a = ft.TextField(label="Number a", width=200)
    number_b = ft.TextField(label="number b", width=200)
    button_calculate = ft.ElevatedButton(text="calculate",
                                         on_click=button_clicked)
    text_output = ft.Text()

    page.add(number_a, number_b, button_calculate, text_output)


ft.app(target=main)

