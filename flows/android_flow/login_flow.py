from flows.android_flow.android_base_flow import AndroidBaseFlow
from screens.android.welcome_screen import WelcomeScreen
from screens.android.home_screen import HomeScreen
from screens.android.p2p_screen import P2PScreen
from screens.screen import Screen
import time


class LoginFlow(AndroidBaseFlow):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.welcome_screen = WelcomeScreen(driver)

    def check_login(self, phone_number, password):
        self.install_application(True)
        time.sleep(5)
        self.welcome_screen.change_lang_to_uzb()
        assert self.welcome_screen.is_welcome_screen_open()
        self.welcome_screen.enter_phone_numb(phone_number)
        assert self.welcome_screen.is_kirish_screen_open()
        self.welcome_screen.enter_password(password)
        self.welcome_screen.click_on_davom_etish_button()
        assert self.welcome_screen.is_otp_tasdiqlash_screen_open()
        # assert self.welcome_screen.is_entered_phone_number_exist(phone_number)
        time.sleep(6)
        assert self.welcome_screen.is_pin_code_screen_open()
        self.welcome_screen.create_pin_code()
        assert self.welcome_screen.is_confirm_pin_code_screen_open()
        self.welcome_screen.create_pin_code()
        assert self.welcome_screen.is_dear_user_message_appear()
        return True
        time.sleep(2)