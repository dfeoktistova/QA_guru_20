import allure
import allure_commons
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selene import browser, support
from dotenv import load_dotenv
import os
from utils import attach


login = os.getenv('BROWSERSTACK_LOGIN')
access_key = os.getenv('BROWSERSTACK_ACCESS_KEY')
project = os.getenv('BROWSERSTACK_PROJECT')
timeout = os.getenv('BROWSERSTACK_TIMEOUT')
app = os.getenv('BROWSERSTACK_APP')


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


def android_management():
    options = UiAutomator2Options().load_capabilities({
        'platformName': 'android',
        'deviceName': 'Samsung Galaxy S22 Ultra',
        'platformVersion': '12.0',
        'app': app,
        'bstack:options': {
            'sessionName': 'Bstack first_test',
            'projectName': project,
            'buildName': 'browserstack-build-1',
            "userName": login,
            "accessKey": access_key
        }
    })
    return options


def pytest_addoption(parser):
    parser.addoption(
        '--platform',
        default='android'
    )


@pytest.fixture(scope='function', autouse=True)
def mobile_settings(request):
    platform = request.config.getoption('--platform')

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            'http://hub.browserstack.com/wd/hub',
            options=android_management(),
        )
    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield platform

    attach.add_screenshot(browser)
    attach.add_xml(browser)

    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    attach.add_video(session_id, login, access_key)