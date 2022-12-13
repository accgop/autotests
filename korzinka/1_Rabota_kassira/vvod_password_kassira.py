from pywinauto.application import Application
import time
import keyboard

def test_kassa_svobodna():

    global app
    try:
        # Старт и соединение с программой
        app = Application(backend='uia').start(r'cmd.exe /c C:\Users\a.liskin\Desktop\classic.bat',
            create_new_console=True,
            wait_for_idle=False).connect(title='MainWindow', timeout=10)

        # Вход в меню кассира
        app.MainWindow.child_window(title="1. Работа кассира", auto_id="btnKassa", control_type="Button").wrapper_object()
        keyboard.send('1')

        # Ввод пароля кассира
        app.InputPassword.child_window(auto_id="PasswordBox", control_type="Edit").wrapper_object()
        keyboard.send(['6','5', '4', '3', '2', '1'])
        keyboard.send('enter')

        #Обращение к полю статуса кассы
        lbl_ChequeStatus = app.Kassir.child_window(title="КАССА СВОБОДНА", auto_id="lbl_ChequeStatus", control_type="Text").wrapper_object()
        status = lbl_ChequeStatus.element_info.rich_text

        # Проверка статуса кассы
        assert status == "КАССА СВОБОДНА"

    finally:
        #Закрытие приложения
        time.sleep(1)
        app.kill()
