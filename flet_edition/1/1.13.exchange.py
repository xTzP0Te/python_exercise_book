import flet as ft


def main(page: ft.Page):
    def button_clicked(e):
        change = int(number_a.value)

        toonies = change // 200
        change %= 200

        loonies = change // 100
        change %= 100

        quarters = change // 25
        change %= 25

        dimes = change // 10
        change %= 10

        nickels = change // 5
        change %= 5

        pennies = change

        text_output.value = "Для сдачи потребуется:\n"
        text_output.value += f"{toonies} монет достоинством 2 доллара \n"
        text_output.value += f"{loonies} монет достоинством 1 доллар \n"
        text_output.value += f"{quarters} монет достоинством 25 центов \n"
        text_output.value += f"{dimes} монет достоинством 10 центов \n"
        text_output.value += f"{nickels} монет достоинством 5 центов\n"
        text_output.value += f"{pennies} монет достоинством 1 цент\n"

        page.update()
    number_a = ft.TextField(label="change", width=200)
    calc_button = ft.ElevatedButton(text="calculte", on_click=button_clicked)
    text_output = ft.Text()
    page.add(number_a, calc_button, text_output)


ft.app(target=main)
