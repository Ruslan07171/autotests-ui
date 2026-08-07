from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"
    )

    # Неправильный локатор
    unknown = page.locator("#unknown")
    expect(unknown).to_be_visible()

    # Неправильное взаимодествие с элементом
    login_button = page.get_by_test_id("login-page-login-button")
    login_button.fill("abra")

    # Попытка взаимодействовать с элементом до того как он появился в DOM-дереве.
    new_title = "Новый title"
    page.evaluate(
        """
    (new_title) => {
        title = document.getElementById("authentication-ui-course-title-text");
        title.textContent = new_title;
    }
        """,
        new_title,
    )
