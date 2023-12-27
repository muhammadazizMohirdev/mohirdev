from screens.screen import Screen
from selenium.common import NoSuchElementException
import time


class HomeScreen(Screen):

    def __init__(self, driver):
        super().__init__(driver)

    profile_owner_name = ("id", "trastpay.uz:id/textViewName")
    profile_icon = ("id", "trastpay.uz:id/imageViewProfile")
    profile_screen_title = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                    "android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                                    "android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/"
                                    "android.widget.LinearLayout/"
                                    "android.widget.TextView[@text=\'Profil\']")
    security_screen_title = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                      "android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                      "/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/"
                                      "android.widget.LinearLayout/android.widget.TextView[@text=\'Xavfsizlik\']")
    security_option = ("id", "trastpay.uz:id/textViewSecurity")
    time_limit_text = ("id", "trastpay.uz:id/textViewSec")
    back_arrow_icon = ("id", "trastpay.uz:id/imageViewBack")
    trastpay_app = ("accessibility_id", "TrastPay")
    """  Payments screen  """
    payments_bottom_navbar_icon = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                            "android.widget.FrameLayout/android.widget.LinearLayout/"
                                            "android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/"
                                            "android.widget.LinearLayout/android.widget.LinearLayout[3]/"
                                            "android.widget.TextView")
    """  Payments screen  """
    top_navbar_ids = ("id", "trastpay.uz:id/textViewTitle")
    money_exchange_widget_home_screen = ("xpath", "//*[@text='Valyuta ayirboshlash']")

    def is_home_screen_open(self):
        try:
            if "MUHAMMADAZIZ" in self.get_element_text(self.profile_owner_name):
                return True
        except Exception:
            raise NoSuchElementException
        return False

    def is_profile_screen_open(self):
        try:
            if self.is_visible(self.profile_screen_title):
                return True
        except Exception:
            raise NoSuchElementException
        return False

    def is_security_screen_open(self):
        try:
            if self.is_visible(self.security_screen_title):
                return True
        except Exception:
            raise NoSuchElementException
        return False

    def select_option_from_top_navbar(self, option):
        all_tabs = self.get_elements(self.top_navbar_ids)
        for tab in all_tabs:
            if option in tab.text:
                tab.click()
                break
            else:
                continue

    def get_time_limit_for_lock(self):
        time_limit = self.get_element_text(self.time_limit_text).split(" ")
        return int(time_limit[0])

    def scroll_to_open_apps(self):
        self.new_scroll(729, 2504, 729, 536)

    def click_on_profile_icon(self):
        self.click(self.profile_icon)

    def click_on_security_option(self):
        self.click(self.security_option)

    def select_time_to_lock_app(self):
        self.tap_on_by_coordinate((150, 1104))

    def click_on_home_button(self):
        self.press_keycode(3)

    def click_on_back_arrow(self):
        self.click(self.back_arrow_icon)

    def click_on_trastpay_app(self):
        self.click(self.trastpay_app)

    def click_on_payments_icon(self):
        self.click(self.payments_bottom_navbar_icon)

    def click_on_money_exchange_on_home_screen(self):
        self.click(self.money_exchange_widget_home_screen)