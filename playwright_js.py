from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login",
        wait_until="networkidle"
    )

    # Дождаться элемента для работы с ним в JavaScript
    auth_title = page.get_by_test_id("authentication-ui-course-title-text")
    expect(auth_title).to_be_visible()

    page.wait_for_timeout(3000)  # для демонстрации результата

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

    page.wait_for_timeout(3000)  # для демонстрации результата
