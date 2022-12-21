from pywinauto.application import Application
import keyboard
import pyautogui
def test_enter_return_mode_Stkassir():
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

        # Проверка видимости окна выбора чека
        assert app.SelectCheqType.is_visible()

    finally:
        pyautogui.press('esc')
        app = Application().connect(title='MainWindow', timeout=10)
        app.Kassir.wait('visible').close()
        app.MainWindow.wait('visible').close()
