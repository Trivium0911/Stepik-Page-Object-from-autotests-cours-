from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    PASS_CHECK = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators(object):
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")



class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_LINK_FROM_MAIN = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs")
    BASKET_HIDDEN_NOT_EMPTY_TITLE = (By.CSS_SELECTOR, "#content_inner > div.basket-title.hidden-xs")
    MESSAGE_ABOUT_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_LINK_FROM_PRODUCT = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span")

class LinksLocators:
    LOGIN_PAGE = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    MAIN_PAGE = "http://selenium1py.pythonanywhere.com/"
    PROMO_PAGE = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    PRODUCT_PAGE = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"