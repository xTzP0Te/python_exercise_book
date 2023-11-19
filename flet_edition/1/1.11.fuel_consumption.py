# В США потребление автомобильного топлива исчисляется в милях на
# галлон (miles-per-gallon – MPG). В то же время в Канаде этот показатель
# обычно выражается в литрах на 100 км (liters-per-hundred kilometers –
# L/100 km). Используйте свои исследовательские способности, чтобы опре-
# делить формулу перевода первых единиц исчисления в последние. После
# этого напишите программу, запрашивающую у пользователя показатель
# потребления топлива автомобилем в американских единицах и выводя-
# щую его на экран в канадских единицах.

import flet as ft



def main(page: ft.Page):
    def button_clicked(e):
        mile_per_gallon = int(mile.value)
        text_output.value = f"Потребление топлива в канадских единицах: {round(235.214 / mile_per_gallon, 2)} L/100 km"

        page.update()

    mile = ft.TextField(label="Введите показатель MPG (миль на галлон)", width=200)
    button_calculate = ft.ElevatedButton(text="calculate",
                                         on_click=button_clicked)
    text_output = ft.Text()
    page.add(mile, button_calculate, text_output)


ft.app(target=main)

