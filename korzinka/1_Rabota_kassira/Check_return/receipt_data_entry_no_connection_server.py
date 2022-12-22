from pywinauto.application import Application
import keyboard
import pyautogui


def test_receipt_data_entry_no_connection_server():
    try:
        # Старт и соединение с программой
        app = Application(backend='uia').start(r'cmd.exe /c C:\Users\a.liskin\Desktop\classic.bat',
                                               create_new_console=True,
                                               wait_for_idle=False).connect(title='MainWindow', timeout=20)
        # Вход в меню кассира
        app.MainWindow.child_window(title="1. Работа кассира", auto_id="btnKassa",
                                    control_type="Button").wrapper_object()
        keyboard.send('1')

        # Ввод пароля кассира
        app.InputPassword.child_window(auto_id="PasswordBox", control_type="Edit").wrapper_object()
        keyboard.send(['1', '2', '3', '4', '5', '6'])
        keyboard.send('enter')

        # Вызов режима возврата чека
        app.Kassir.wait('ready')
        pyautogui.press('f1')

        # Вызов окна ввода данных чека
        app.SelectCheqType.wait('ready')
        pyautogui.press('enter')

        # Закрытие окна ввода данных чека
        app.VozvratEnter.wait('ready')

        # Ввод данных чека
        keyboard.send(['1', '0'])
        keyboard.send('tab')
        keyboard.send(['2'])
        keyboard.send('tab')
        pyautogui.press(['2', '2', '1', '2', '2', '0', '2', '2'])
        keyboard.send('tab')
        pyautogui.press(['1', '7', '2', '1', '4', '8'])
        keyboard.send('enter')

        # Проверка появления информационного окна с сообщением об отсутствии связи с сервером
        app.MessageFormYes.wait('ready')
        textMessageFormYes = app.MessageFormYes.child_window(auto_id="Message", control_type="Text").wrapper_object()
        assert textMessageFormYes.window_text() == "Нет ответа от сервера"

    finally:
        app = Application().connect(title='MainWindow', timeout=10)
        pyautogui.press('enter')
        app.Kassir.wait('visible').close()
        app.MainWindow.wait('visible').close()
