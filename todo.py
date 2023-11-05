import flet as ft
from flet_core.control_event import ControlEvent
from TodoApp import TodoApp


def main(page: ft.page):
    page.title = "ToDo App"
    page.theme_mode = 'dark'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    todo = TodoApp()

    page.add(todo)


if __name__ == "__main__":
    print("Application...")
    ft.app(target=main)
