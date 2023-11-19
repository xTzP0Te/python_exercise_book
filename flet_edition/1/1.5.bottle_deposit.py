# Упражнение 5. Сдаем бутылки
# Во многих странах в стоимость стеклотары закладывается определенный
# депозит, чтобы стимулировать покупателей напитков сдавать пустые бу-
# тылки. Допустим, бутылки объемом 1 литр и меньше стоят $0,10, а бутыл-
# ки большего объема – $0,25.
# Напишите программу, запрашивающую у пользователя количество бу-
# тылок каждого размера. На экране должна отобразиться сумма, которую
# можно выручить, если сдать всю имеющуюся посуду. Отформатируйте
# вывод так, чтобы сумма включала

import flet as ft


def main(page: ft.Page):
    def button_clicked(e):
        small_bottles = int(number_a.value)
        gig_bottles = int(number_b.value)
        text_output.value = "вы получите " + str(small_bottles*0.1+gig_bottles*0.25) + " backs"

        page.update()

    number_a = ft.TextField(label="Введите сколько у вас бутылок ёмкостью меньше или равных одному литру", width=300)
    number_b = ft.TextField(label="Введите сколько у вас бутылок ёмкостью больше одного литра", width=300)
    button_calculate = ft.ElevatedButton(text="calculate",
                                         on_click=button_clicked)
    text_output = ft.Text()
    page.add(number_a, number_b, button_calculate, text_output)


ft.app(target=main)

