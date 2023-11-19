# Упражнение 6. Налоги и чаевые
# Программа, которую вы напишете, должна начинаться с запроса у поль-
# зователя суммы заказа в ресторане. После этого должен быть произведен
# расчет налога и чаевых официанту. Вы можете использовать принятую
# в вашем регионе налоговую ставку для подсчета суммы сборов. В качестве
# чаевых мы оставим 18 % от стоимости заказа без учета налога. На выхо-
# де программа должна отобразить отдельно налог, сумму чаевых и итог,
# включая обе составляющие. Форматируйте вывод таким образом, чтобы
# все числа отображались с двумя знаками после запятой.

import flet as ft


def main(page: ft.Page):
    def button_clicked(e):
        check_cost = int(check.value)
        text_output.value = f"Налог: {check_cost*0.2:.2f} руб." + "\n"
        text_output.value += f"Чаевые: {check_cost*0.18:.2f} руб." + "\n"
        text_output.value += f"Игого: {check_cost+check_cost*0.18+check_cost*0.2:.2f} руб."
        page.update()

    check = ft.TextField(label="сумма заказа", width=200)
    button_calculate = ft.ElevatedButton(text="calculate",
                                         on_click=button_clicked)
    text_output = ft.Text()
    page.add(check, button_calculate, text_output)


ft.app(target=main)
