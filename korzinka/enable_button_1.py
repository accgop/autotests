from pywinauto.application import Application

def test_enable_button_1():
    try:
        # Старт и соединение с программой
        app = Application(backend='uia').start(r'cmd.exe /c C:\Users\a.liskin\Desktop\classic.bat',
            create_new_console=True, wait_for_idle=False).connect(title='MainWindow', timeout=10)

        # Поиск кнопки 1
        btnKassa = app.MainWindow.child_window(title="1. Работа кассира", auto_id="btnKassa", control_type="Button").wrapper_object()

        # Проверка, что кнопка включена
        assert btnKassa.is_enabled()

    finally:
        # Закрытие приложения
        app = Application().connect(title='MainWindow', timeout=1)
        app.kill()
