from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.dashboard_list_item_icon = page.get_by_test_id(
            "dashboard-drawer-list-item-icon"
        )
        self.dashboard_list_item_title = page.get_by_test_id(
            "dashboard-drawer-list-item-title-text"
        )
        self.dashboard_list_item_button = page.get_by_test_id(
            "dashboard-drawer-list-item-button"
        )

        self.courses_list_item_icon = page.get_by_test_id(
            "courses-drawer-list-item-icon"
        )
        self.courses_list_item_title = page.get_by_test_id(
            "courses-drawer-list-item-title-text"
        )
        self.courses_list_item_button = page.get_by_test_id(
            "courses-drawer-list-item-button"
        )

        self.logout_list_item_icon = page.get_by_test_id("logout-drawer-list-item-icon")
        self.logout_list_item_title = page.get_by_test_id(
            "logout-drawer-list-item-title-text"
        )
        self.logout_list_item_button = page.get_by_test_id(
            "logout-drawer-list-item-button"
        )

    def check_visible(self):
        expect(self.dashboard_list_item_icon).to_be_visible()
        expect(self.dashboard_list_item_title).to_be_visible()
        expect(self.dashboard_list_item_title).to_have_text("Dashboard")
        expect(self.dashboard_list_item_button).to_be_visible()

        expect(self.courses_list_item_icon).to_be_visible()
        expect(self.courses_list_item_title).to_be_visible()
        expect(self.courses_list_item_title).to_have_text("Courses")
        expect(self.courses_list_item_button).to_be_visible()

        expect(self.logout_list_item_icon).to_be_visible()
        expect(self.logout_list_item_title).to_be_visible()
        expect(self.logout_list_item_title).to_have_text("Logout")
        expect(self.logout_list_item_button).to_be_visible()
