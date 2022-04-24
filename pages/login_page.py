from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        # регистрация нового пользователя
        self.email = email
        self.password = password

        # находим элементы на странице: поля ввода почты, пароля и кнопку регистрации
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL)
        pass_input = self.browser.find_element(*LoginPageLocators.PASS)
        pass_confirm = self.browser.find_element(*LoginPageLocators.PASS_CHECK)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)

        # вводим почту, пароль
        email_input.send_keys(email)
        pass_input.send_keys(password)
        pass_confirm.send_keys(password)

        # нажимаем на кнопку: зарегистрировать
        reg_button.click()
