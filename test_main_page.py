from .pages.main_page import MainPage
import time
#from selenium.webdriver.common.by import By

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) # инициируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open() # открываем страницу
    time.sleep(5)
    page.should_be_login_link() # выполняем метод страницы — переходим на страницу логина
