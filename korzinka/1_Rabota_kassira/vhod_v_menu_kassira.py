from pywinauto.application import Application
import time
import keyboard

def test_vhod():

    global app
    try:
        # Старт и соединение с программой
        app = Application(backend='uia').start(r'cmd.exe /c C:\Users\a.liskin\Desktop\classic.bat',
            create_new_console=True,
            wait_for_idle=False).connect(title='MainWindow', timeout=10)

        # Вход в меню кассира
        btnKassa = app.MainWindow.child_window(title="1. Работа кассира", auto_id="btnKassa", control_type="Button").wrapper_object()
        keyboard.send('1')

        # Подключение к окну ввода пароля
        dlg = app.InputPassword

        # Проверка видимости окна
        assert dlg.is_visible()

    finally:
        # Закрытие приложения
        time.sleep(1)
        app.kill()
