import flet as ft
import math


def main(page: ft.Page):
    def button_clicked(e):
        lat1 = float(latitude_1.value)
        long1 = float(longitude_1.value)
        lat2 = float(latitude_2.value)
        long2 = float(longitude_2.value)
        lat1, long1, lat2, long2 = map(math.radians, [lat1, long1, lat2, long2])
        distance = 6371.01 * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1)
                                       * math.cos(lat2) * math.cos(long1 - long2))

        text_output.value = f"Расстояние между точками: {distance:.2f} км"

        page.update()

    latitude_1 = ft.TextField(label="широта первой точки", width=200)
    longitude_1 = ft.TextField(label="долгота первой точки", width=200)
    latitude_2 = ft.TextField(label="широта второй точки", width=200)
    longitude_2 = ft.TextField(label="долгота второй точки", width=200)
    calc_button = ft.ElevatedButton(text="calculate",
                                         on_click=button_clicked)
    text_output = ft.Text()

    page.add(latitude_1, latitude_2, longitude_1, longitude_2, text_output, calc_button)


ft.app(target=main)
