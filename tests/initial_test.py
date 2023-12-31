import pytest
from flows.android_flow.login_flow import LoginFlow
from flows.android_flow.app_lock_time_flow import AppLockTimeFlow
from flows.android_flow.p2p_flow import P2PFlow


@pytest.mark.usefixtures('setup_virtual_device', 'get_screenshot_on_failed_case')
class InitialTest:

    @pytest.fixture
    def init(self):
        driver = self.driver
        self.login_f = LoginFlow(driver)
        self.app_lock_time_f = AppLockTimeFlow(driver)
        self.p2p_f = P2PFlow(driver)