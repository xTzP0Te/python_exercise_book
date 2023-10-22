# Упражнение 1. Почтовый адрес
# Напишите несколько строк кода, выводящих на экран ваше имя и почто-
# вый адрес. Адрес напишите в формате, принятом в вашей стране. Ника-
# кого ввода от пользователя ваша первая программа принимать не будет,
# только вывод на экран и больше ничего.

import flet as ft


def main(page: ft.Page):
    page.bgcolor = ft.colors.WHITE

    name = "Ivan"
    post_index = "123098"
    address = "Pushkin Street Kolotushkin House"
    page.fonts = {
        # "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf",
        "PostIndex": "fonts/postindex.ttf",
        "HandWriting": "fonts/20279.otf"
    }
    page.add(
        ft.Text(
            name,
            size=50,
            # font_family="RobotoSlab",
            font_family="HandWriting",
            color=ft.colors.BLUE,
            # bgcolor=ft.colors.WHITE,
            weight=ft.FontWeight.NORMAL,
        ),
        ft.Text(
            post_index,
            size=50,
            # font_family="RobotoSlab",
            font_family="PostIndex",
            color=ft.colors.BLUE,
            # bgcolor=ft.colors.WHITE,
            weight=ft.FontWeight.NORMAL,
        ),
        ft.Text(
            address,
            size=50,
            font_family="HandWriting",
            color=ft.colors.BLUE,
            # bgcolor=ft.colors.WHITE,
            weight=ft.FontWeight.NORMAL,
        ),
    )


if __name__ == '__main__':
    ft.app(target=main)
