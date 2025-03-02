from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


def test_wiki(mobile_management):
    continue_button = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button'))
    screen_title = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView'))
    get_started_button = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_done_button'))

    with step("Открыть начальную страницу"):
        screen_title.should(have.text("Free Encyclopedia"))

    with step('Нажать на кнопку "Continue": Переход ко второму экрану'):
        continue_button.click()
        screen_title.should(have.text("New ways to explore"))

    with step('Нажать на кнопку "Continue": Переход к третьему экрану'):
        continue_button.click()
        screen_title.should(have.text("Reading lists with sync"))

    with step('Нажать на кнопку "Continue": Переход к четвертому экрану'):
        continue_button.click()
        screen_title.should(have.exact_text('Data & Privacy'))

    with step('Нажать на кнопку "Get started"'):
        get_started_button.click()
