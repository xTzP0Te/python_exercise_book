# Упражнение 8. Сувениры и безделушки
# Интернет-магазин занимается продажей различных сувениров и безде-
# лушек. Каждый сувенир весит 75 г, а безделушка – 112 г. Напишите про-
# грамму, запрашивающую у пользователя количество тех и других покупок,
# после чего выведите на экран общий вес посылки.

import flet as ft

weight_souvenir = 75
weight_trinket = 112


def main(page: ft.Page):
    def button_clicked(e):
        trinkets_quantity = int(trinkets.value)
        souvenir_quantity = int(souvenir.value)
        text_output.value = (f"общий вес посылки составит:"
                             f" {trinkets_quantity * weight_trinket + souvenir_quantity * weight_souvenir} грамм")

        page.update()

    trinkets = ft.TextField(label="количество безделушек", width=200)
    souvenir = ft.TextField(label="количество сувениров", width=200)
    button_calculate = ft.ElevatedButton(text="calculate",
                                         on_click=button_clicked)
    text_output = ft.Text()
    page.add(trinkets, souvenir, button_calculate, text_output)


ft.app(target=main)


