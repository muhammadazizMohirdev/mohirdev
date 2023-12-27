import allure
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from allure_commons.types import AttachmentType


@pytest.fixture()
def get_screenshot_on_failed_case(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(request.instance.driver.get_screenshot_as_png(),
                      name="failed_test",
                      attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def setup_virtual_device(request):
    global driver
    capabilities = {
        'platformName': 'Android',
        'platformVersion': '10.0',
        'deviceName': 'Pixel_XL_10',
        'avd': 'Pixel_XL_10',
        'newCommandTimeout': 7200,
        'noReset': True,
        'app': 'C:\\Users\\admin\\PycharmProjects\\pythonProject5\\apps\\trastPay_1.1.26.05.debug.apk',
        'appWaitDuration': 300000,
        'avdReadyTimeout': 500000,
        'adbExecTimeout': 500000,
        'automationName': 'UiAutomator2',
        'appPackage': 'trastpay.uz',
        'appActivity': 'uz.trastpay.ui.activity.MainActivity'
    }
    appium_server = AppiumService()
    appium_server.start(
        args=[
            '--address', '127.0.0.1',
            '--port', '4723',
            '--base-path', '/wd/hub',
        ]
    )
    request.addfinalizer(appium_server.stop)
    url = 'http://127.0.0.1:4723/wd/hub'
    capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
    request.instance.driver = webdriver.Remote(url, options=capabilities_options)

    def teardown():
        request.instance.driver.quit()
    request.addfinalizer(teardown)