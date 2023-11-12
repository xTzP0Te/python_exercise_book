# Упражнение 3. Площадь комнаты
# Напишите программу, запрашивающую у пользователя длину и ширину
# комнаты. После ввода значений должен быть произведен расчет площади
# комнаты и выведен на экран. Длина и ширина комнаты должны вводиться
# в формате числа с плавающей запятой. Дополните ввод и вывод единицами
# измерения, принятыми в вашей стране. Это могут быть футы или метры.

import flet as ft


def main(page: ft.Page):
    def button_clicked(e):
        width = int(width_input.value)
        length = int(length_input.value)
        display_name.value = f"Площадь вашей квартире равна {width * length} метров"
        page.update()

    width_input = ft.TextField(label="ширина")
    length_input = ft.TextField(label="длина")
    button_calc = ft.ElevatedButton(text="Вычислить", on_click=button_clicked)
    display_name = ft.Text()
    page.add(
        width_input,
        length_input,
        display_name,
        button_calc,
    )


if __name__ == '__main__':
    ft.app(target=main)
