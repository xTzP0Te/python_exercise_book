# Упражнение 4. Площадь садового участка
# Создайте программу, запрашивающую у пользователя длину и ширину
# садового участка в футах. Выведите на экран площадь участка в акрах.

import flet as ft


def main(page: ft.Page):
    def button_clicked(e):
        width = int(number_a.value)
        length = int(number_b.value)
        text_output.value = "Ваш садовый участок равен " + str((width*length)/43560) + " акр"

        page.update()

    number_a = ft.TextField(label="ширина в футах", width=200)
    number_b = ft.TextField(label="длинна в футах", width=200)
    button_calculate = ft.ElevatedButton(text="calculate",
                                         on_click=button_clicked)
    text_output = ft.Text()
    page.add(number_a, number_b, button_calculate, text_output)


ft.app(target=main)

