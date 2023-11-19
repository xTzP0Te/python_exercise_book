# Представьте, что вы открыли в банке сберегательный счет под 4 % годо-
# вых. Проценты банк рассчитывает в конце года и добавляет к сумме счета.
# Напишите программу, которая запрашивает у пользователя сумму перво-
# начального депозита, после чего рассчитывает и выводит на экран сумму
# на счету в конце первого, второго и третьего годов. Все суммы должны
# быть округлены до двух знаков после запятой.

import flet as ft



def main(page: ft.Page):
    def button_clicked(e):
        rupies_quntity = int(money.value)
        rupies_quntity_first_year = round(rupies_quntity+rupies_quntity/20, 2)
        rupies_quntity_second_year = round(rupies_quntity_first_year + rupies_quntity_first_year / 20, 2)
        rupies_quntity_third_year = round(rupies_quntity_second_year + rupies_quntity_second_year / 20, 2)

        text_output.value = f"В первый год у вас будет {rupies_quntity_first_year} рупиев \n"
        text_output.value += f"Во второй год у вас будет {rupies_quntity_second_year} рупиев \n"
        text_output.value += f"В третий год у вас будет {rupies_quntity_third_year} рупиев \n"

        page.update()

    money = ft.TextField(label="сколько вы положите рупиев в наш банк", width=200)
    button_calculate = ft.ElevatedButton(text="calculate",
                                         on_click=button_clicked)
    text_output = ft.Text()
    page.add(money, button_calculate, text_output)


ft.app(target=main)

