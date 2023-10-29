# Упражнение 2. Приветствие
# Напишите программу, запрашивающую у пользователя его имя. В ответ
# на ввод на экране должно появиться приветствие с обращением по имени,
# введенному с клавиатуры ранее.

import flet as ft


def main(page: ft.Page):
    def button_clicked(e):
        if name_input.value:
            display_name.value = f"Уважаемый, {name_input.value}, иди в лес."
            page.update()

    name_input = ft.TextField(label="Имя")
    button_submit = ft.ElevatedButton(text="Отправить", on_click=button_clicked)
    display_name = ft.Text()
    page.add(
        name_input,
        button_submit,
        display_name
    )


if __name__ == '__main__':
    ft.app(target=main)