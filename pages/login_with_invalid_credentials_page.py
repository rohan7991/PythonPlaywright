import time
from commons import lib_global
class login_with_invalid_cred:
    def click_SignIn(driver):
        driver.wait_for_timeout(500)
        lib_global.click_element(driver, "xpath", ".nav-menu > a:nth-child(5)")
        pass
    def send_username_and_password(driver, username, password):
        lib_global.send_keys(driver, "xpath", "//input[@placeholder='Username or E-mail']", username)
        lib_global.send_keys(driver, "xpath", "//input[@placeholder='Password']", password)
        #lib_global.click_element(driver, "xpath", "//span[text()='Sign In']")

    def getCurrentURL(driver):
        return lib_global.fetchURL(driver)