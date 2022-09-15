import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru", help="Choose languages")


@pytest.fixture(scope="function")
def browser(request):

    user_language = request.config.getoption("--language")
    if user_language:
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])  # настройки чтобы в терминале не выпадали ненужные системные предупреждения
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be browser language")
    yield browser
    browser.quit()
