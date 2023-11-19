# Упражнение 7. Сумма первых n положительных чисел=
# Напишите программу, запрашивающую у пользователя число и подсчи-
# тывающую сумму натуральных положительных чисел от 1 до введенного
# пользователем значения. Сумма первых n положительных чисел может
# быть рассчитана по формуле:

import flet as ft


def main(page: ft.Page):
    def button_clicked(e):
        natural_number = int(natural.value)
        if natural_number > 0:
            text_output.value = f"Сумма первых {natural_number} положительных чисел: {(natural_number * (natural_number + 1)) // 2}"
        else:
            text_output.value = "Введите положительное число!"

        page.update()

    natural = ft.TextField(label="введите любое положительное число", width=200)
    button_calculate = ft.ElevatedButton(text="calculate",
                                         on_click=button_clicked)
    text_output = ft.Text()
    page.add(natural, button_calculate, text_output)


ft.app(target=main)

