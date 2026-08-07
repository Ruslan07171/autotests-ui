from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    PASSWORD = "password"
    EMAIL = "user@gmail.com"

    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"
    )

    email_input = page.get_by_test_id("login-form-email-input").locator("//div//input")
    email_input.focus()
    for ch in EMAIL:
        page.keyboard.press(ch, delay=300)
    page.keyboard.press("ControlOrMeta+A")

    page.wait_for_timeout(3000)  # для демонстрации результата

    password_input = page.get_by_test_id("login-form-password-input").locator(
        "//div//input"
    )
    for ch in PASSWORD:
        password_input.press(ch, delay=300)
    password_input.press("ControlOrMeta+A")

    page.wait_for_timeout(3000)  # для демонстрации результата
