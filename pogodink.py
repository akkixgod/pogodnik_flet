import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Home"
    page.theme_mode = "dark"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    user_input = ft.TextField(label="Введите город", width=450) #label
    current_weather = ft.Text("")

    def get_weather(e):
        try:
            api = "API from openweather" #api
            url = f"https://api.openweathermap.org/data/2.5/weather?q={user_input.value}&appid={api}&units=metric" #chtobi gradusi bili
            request_from = requests.get(url).json()
            fever = request_from["main"]["temp"]
            current_weather.value = f"Нынешная погода на городе {user_input.value} состовляет {fever}°C" #vivod
            page.update()
        except KeyError:
            # esli polzovatel eblan i vvel ne to
            current_weather.value = "Error, Please try again!"
            page.update()


    def change_theme(e):
        # smena temi
        if page.theme_mode == "dark":
            page.theme_mode = "light"
        else:
            page.theme_mode = "dark"
        page.update()
    

    page.add(
        ft.Row([ft.Text("Погода")], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([user_input], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([current_weather], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.OutlinedButton(text="Узнать погоду", on_click=get_weather)], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.IconButton(ft.icons.SUNNY, on_click=change_theme)], alignment=ft.MainAxisAlignment.END)
        # vse knopki i prochee
    )

ft.app(target = main)