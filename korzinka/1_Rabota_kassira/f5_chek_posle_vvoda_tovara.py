import pyautogui
from pywinauto.application import Application
import keyboard
import time

def test_f5_check_after_enter_product_code():
    try:
        ## Старт и соединение с программой
        app = Application(backend='uia').start(r'cmd.exe /c C:\Users\a.liskin\Desktop\classic.bat',
                                               create_new_console=True,
                                               wait_for_idle=False).connect(title='MainWindow', timeout=10)

        # Вход в меню кассира
        app.MainWindow.child_window(title="1. Работа кассира", auto_id="btnKassa",
                                    control_type="Button").wrapper_object()
        keyboard.send('1')

        # Ввод пароля кассира
        app.InputPassword.child_window(auto_id="PasswordBox", control_type="Edit").wrapper_object()
        keyboard.send(['6', '5', '4', '3', '2', '1'])
        keyboard.send('enter')

        # Ввод кода товара с клавиатуры
        app.Kassir.child_window(auto_id='labelInput', control_type='Text').wrapper_object()
        pyautogui.press(['4', '7', '8', '0', '0', '7', '7', '6', '1', '0', '0', '3', '1'])
        keyboard.send('enter')

        # отложить чек
        keyboard.send('f5')

        # Обращение к статусу чека
        lblSecondCheck = app.Kassir.child_window(title="Есть отложенный чек", auto_id="lblSecondCheck", control_type="Text").wrapper_object()

        #Проверка статуса чека
        StatusCheck = lblSecondCheck.element_info.rich_text
        assert StatusCheck == 'Есть отложенный чек'

    finally:
        # Закрытие чека
        keyboard.send('f5')
        keyboard.send('space')
        pyautogui.press(['3', '1', '0', '0', '0'])
        keyboard.send('enter')
        keyboard.send('enter')

        time.sleep(1)
        app.kill()