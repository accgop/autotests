import pyautogui
from pywinauto.application import Application
import keyboard

def test_input_good_keyboard_price_ot_40k():
    try:
        # Старт и соединение с программой
        app = Application(backend='uia').start(r'cmd.exe /c C:\Users\a.liskin\Desktop\classic.bat',
            create_new_console=True,
            wait_for_idle=False).connect(title='MainWindow',timeout=10)


        # Вход в меню кассира
        app.MainWindow.child_window(title="1. Работа кассира", auto_id="btnKassa", control_type="Button").wrapper_object()
        keyboard.send('1')

        # Ввод пароля кассира
        app.InputPassword.child_window(auto_id="PasswordBox", control_type="Edit").wrapper_object()
        keyboard.send(['6', '5', '4', '3', '2', '1'])
        keyboard.send('enter')

        #Ввод кода товара с клавиатуры
        app.Kassir.child_window(auto_id='labelInput', control_type='Text').wrapper_object()
        pyautogui.press(['2', '2', '0', '2', '3', '2', '6', '1'])
        keyboard.send('enter')
        keyboard.send('enter')
        keyboard.send('space')
        keyboard.send('enter')

        # Обращение к полю статуса кассы
        lbl_ChequeStatus = app.Kassir.child_window(auto_id="lbl_ChequeStatus", control_type="Text").wrapper_object()

        # Проверка статуса кассы
        assert lbl_ChequeStatus.element_info.rich_text == "ПРОДАЖА"

    finally:
        # Закрытие чека
        app = Application().connect(title='MainWindow', timeout=1)
        keyboard.send('space')
        app.Kassir.wait('ready')
        pyautogui.press(['4', '5', '0', '0', '0'])
        keyboard.send('enter')
        keyboard.send('enter')
        app.Kassir.wait('ready').close()
        app.MainWindow.wait('ready').close()
