from pywinauto import MatchError
from pywinauto.application import Application
import keyboard

def test_cancel_input_password():

    try:
        # Старт и соединение с программой
        app = Application(backend='uia').start(r'cmd.exe /c C:\Users\a.liskin\Desktop\classic.bat',
            create_new_console=True,
            wait_for_idle=False).connect(title='MainWindow',timeout=10)

        # Вход в меню кассира
        app.MainWindow.child_window(title="1. Работа кассира", auto_id="btnKassa", control_type="Button").wrapper_object()
        keyboard.send('1')

        #Закрытие окна ввода пароля
        app.InputPassword.wait('ready')
        keyboard.send('esc')

        #Обращение к полю ввода пароля
        app.InputPassword.child_window(auto_id="PasswordBox", control_type="Edit").wrapper_object()

        #Исключение ожидаемой ошибки отсутствия окна ввода пароля и проверка видимости основного окна MainWindow
    except MatchError:
        app = Application().connect(title='MainWindow', timeout=1)
        assert app.MainWindow.is_visible()

    finally:
        #Закрытие приложения
        app = Application().connect(title='MainWindow', timeout=1)
        app.kill()
