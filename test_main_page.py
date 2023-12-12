from .pages.main_page import MainPage
import time
from .pages.login_page import LoginPage
#from selenium.webdriver.common.by import By

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) # инициируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open() # открываем страницу
    time.sleep(5)
    page.should_be_login_link() # выполняем метод страницы — переходим на страницу логина

def test_guest_can_go_to_login_page(browser): # Инициализируем LoginPage в теле теста
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    time.sleep(5)
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
