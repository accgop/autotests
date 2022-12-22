from pywinauto.application import Application
import keyboard
import pyautogui


def test_checking_press_Enter_in_VozvratEnter():
    try:
        # Старт и соединение с программой
        app = Application(backend='uia').start(r'cmd.exe /c C:\Users\a.liskin\Desktop\classic.bat',
                                               create_new_console=True,
                                               wait_for_idle=False).connect(title='MainWindow', timeout=10)

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

        # Переход в режим возврата чека без ввода данных чека
        app.VozvratEnter.wait('ready')
        pyautogui.press('enter')

        # Проверка видимости окна ввода данных чека
        assert app.VozvratEnter.is_visible()

    finally:
        app = Application().connect(title='MainWindow', timeout=10)
        app.VozvratEnter.wait('visible').close()
        app.Kassir.wait('visible').close()
        app.MainWindow.wait('visible').close()
