import time


class AndroidBaseFlow:
    def __init__(self, driver):
        self.driver = driver

    def install_application(self, login=True):
        if login:
            self.driver.remove_app('trastpay.uz')
            self.driver.install_app(
                "C:\\Users\\admin\\PycharmProjects\\pythonProject5\\apps\\trastPay_1.1.26.05.debug.apk")
            self.driver.activate_app('trastpay.uz')
            time.sleep(5)
            return True
        else:
            self.driver.install_app(
                "C:\\Users\\admin\\PycharmProjects\\pythonProject5\\apps\\trastPay_1.1.26.05.debug.apk")
            self.driver.activate_app('trastpay.uz')
            time.sleep(5)
            return True