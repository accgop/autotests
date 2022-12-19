import pyautogui
from pywinauto.application import Application
import keyboard

def test_return_from_f5_check_do_40k_after_payment_noncash():
    try:
        #Старт и соединение с программой
        app = Application(backend='uia').start(r'cmd.exe /c C:\Users\a.liskin\Desktop\classic.bat',
            create_new_console=True,
            wait_for_idle=False).connect(title='MainWindow', timeout=10)

        # Вход в меню кассира
        app.MainWindow.child_window(title="1. Работа кассира", auto_id="btnKassa", control_type="Button").wrapper_object()
        keyboard.send('1')

        # Ввод пароля кассира
        app.InputPassword.child_window(auto_id="PasswordBox", control_type="Edit").wrapper_object()
        keyboard.send(['6', '5', '4', '3', '2', '1'])
        keyboard.send('enter')

        # Ввод кода товара с клавиатуры
        app.Kassir.child_window(auto_id='labelInput', control_type='Text').wrapper_object()
        pyautogui.press(['4', '7', '8', '0', '0', '7', '7', '6', '1', '0', '0', '3', '1'])
        keyboard.send('enter')
        app.Kassir.wait('ready', timeout=1)

        # Оплата товара наличными
        keyboard.send('space')
        pyautogui.press(['3', '0', '9', '9', '0'])

        # Отложить чек
        keyboard.send('f5')

        # Обращение к статусу чека
        lblSecondCheck = app.Kassir.child_window(auto_id="lblSecondCheck", control_type="Text").wrapper_object()

        # Проверка статуса чека
        assert lblSecondCheck.element_info.rich_text == 'Есть отложенный чек'

        keyboard.send('f5')
        app.Kassir.wait('ready', timeout=5)

        # Обращение к полю статуса кассы
        lbl_ChequeStatus = app.Kassir.child_window(auto_id="lbl_ChequeStatus", control_type="Text").wrapper_object()

        # Проверка статуса кассы
        assert lbl_ChequeStatus.element_info.rich_text == "ОПЛАТА"

    finally:
        # Закрытие чека
        app = Application().connect(title='Kassir', timeout=5)
        pyautogui.press(['3', '0', '9', '9', '0'])
        app.Kassir.wait('ready', timeout=5)
        keyboard.send('enter')
        app.CashlessWindow.wait('ready', timeout=5)
        keyboard.send('tab')
        keyboard.send('enter')

        # Закрытие приложения
        app.Kassir.close()
        app.MainWindow.close()
