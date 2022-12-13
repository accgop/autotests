import time
from pywinauto.application import Application

def test_start_app():
    try:
        # Старт и соединение с программой
        app = Application(backend='uia').start(r'cmd.exe /c C:\Users\a.liskin\Desktop\classic.bat',
            create_new_console=True,
            wait_for_idle=False).connect(title='MainWindow',timeout=10)

        dlg = app.MainWindow

        #Проверка видимости акна
        assert dlg.is_visible()

    finally:

        #Закрытие приложения
        time.sleep(1)
        app.kill()
