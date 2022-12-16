import pyautogui
from pywinauto.application import Application
import keyboard

def test_payment_cash_noncash_1goods_do_40k():
    try:
        ## Старт и соединение с программой
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

        #Ввод кода товара с клавиатуры
        app.Kassir.child_window(auto_id='labelInput', control_type='Text').wrapper_object()
        pyautogui.press(['4','7', '8', '0', '0', '7', '7', '6', '1', '0', '0', '3', '1'])
        keyboard.send('enter')
        app.Kassir.wait('ready', timeout=1)

        #Оплата товара частично наличными
        keyboard.send('space')
        pyautogui.press(['3', '0', '0', '0', '0'])
        keyboard.send('enter')
        keyboard.send('enter')

        # Обращение к полю статуса кассы
        lbl_ChequeStatus = app.Kassir.child_window(auto_id="lbl_ChequeStatus", control_type="Text").wrapper_object()

        # Проверка статуса кассы
        assert lbl_ChequeStatus.element_info.rich_text == "ОПЛАТА"

        # Проверка остатка оплаты:
        labelTextItogo = app.Kassir.child_window(auto_id="labelTextItogo", control_type="Text").wrapper_object()
        assert labelTextItogo.element_info.rich_text == "ИТОГО: "

        lblItogo = app.Kassir.child_window(auto_id="lblItogo", control_type="Text").wrapper_object()
        assert lblItogo.element_info.rich_text == "990,00"

        #ввод оставшейся суммы
        pyautogui.press(['9', '9', '0'])
        keyboard.send('enter')

        # выбор варианты оплаты(безналичный расчет)
        keyboard.send('tab')
        keyboard.send('enter')

        # Проверка статуса кассы
        lbl_ChequeStatus = app.Kassir.child_window(auto_id="lbl_ChequeStatus", control_type="Text").wrapper_object()
        assert lbl_ChequeStatus.element_info.rich_text == "КАССА СВОБОДНА"

        # Проверка остатка оплаты:
        labelTextItogo = app.Kassir.child_window(auto_id="labelTextItogo", control_type="Text").wrapper_object()
        assert labelTextItogo.element_info.rich_text == "ИТОГО: "

        lblItogo = app.Kassir.child_window(auto_id="lblItogo", control_type="Text").wrapper_object()
        assert lblItogo.element_info.rich_text == "0,00"

    finally:
        #Закрытие приложения
        app = Application().connect(title='MainWindow', timeout=1)
        app.kill()
