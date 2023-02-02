from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
from pages.DiskPage import DiskPage
from data_for_test import *


def test_create_file(browser):
    MainPage(browser).open().go_to_login_page()
    LoginPage(browser).login("user.simbirsoft", "USERsimbirsoft")
    MainPage(browser).go_to_disk()
    DiskPage(browser)\
        .create_content(browser.dir, "dir")\
        .open_content(browser.dir)\
        .create_content(browser.file, "file")\
        .close_file()
    assert DiskPage(browser).search_content(browser.file) == browser.file + ".\ndocx"
