from flows.android_flow.android_base_flow import AndroidBaseFlow
from screens.android.home_screen import HomeScreen
from screens.android.welcome_screen import WelcomeScreen
import time


class AppLockTimeFlow(AndroidBaseFlow):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.welcome_screen = WelcomeScreen(driver)
        self.home_screen = HomeScreen(driver)

    def check_app_lock_time(self):
        self.install_application(False)
        time.sleep(5)
        self.welcome_screen.is_enter_pin_code_screen_open()
        self.welcome_screen.create_pin_code()
        assert self.home_screen.is_home_screen_open()
        self.home_screen.click_on_profile_icon()
        assert self.home_screen.is_profile_screen_open()
        self.home_screen.click_on_security_option()
        assert self.home_screen.is_security_screen_open()
        self.home_screen.select_time_to_lock_app()
        time_lim = self.home_screen.get_time_limit_for_lock()
        self.home_screen.click_on_back_arrow()
        self.home_screen.click_on_back_arrow()
        self.home_screen.click_on_home_button()
        time.sleep(time_lim + 1)
        self.home_screen.scroll_to_open_apps()
        self.home_screen.click_on_trastpay_app()
        self.welcome_screen.is_enter_pin_code_screen_open()
        self.welcome_screen.create_pin_code()
        self.welcome_screen.create_pin_code()
        assert self.home_screen.is_home_screen_open()
        return True