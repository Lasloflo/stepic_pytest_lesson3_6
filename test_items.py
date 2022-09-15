import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_basket_button_is_on_page(browser):
    browser.get(link)
    try:
        basket_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-add-to-basket"))
        )
    except:
        basket_button = None

    assert basket_button is not None, "basket-button not on the page"
