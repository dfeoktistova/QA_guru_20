from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


def test_onboarding(mobile_management):
    continue_button = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button'))
    screen_title = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView'))
    done_button = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_done_button'))

    with step("First onboarding screen is opened"):
        screen_title.should(have.text("Free Encyclopedia"))

    with step('Click on continue button to open the second screen'):
        continue_button.click()
        screen_title.should(have.text("New ways to explore"))

    with step('Click on continue button to open the third screen'):
        continue_button.click()
        screen_title.should(have.text("Reading lists with sync"))

    with step('Click on continue button to open the fourth screen'):
        continue_button.click()
        screen_title.should(have.exact_text('Data & Privacy'))

    with step('Finish onboarding by clicking on done button'):
        done_button.click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/main_toolbar_wordmark')).should(be.visible)
