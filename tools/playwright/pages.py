import os
import shutil
from pathlib import Path

import allure
from playwright.sync_api import Playwright, Page

from config import settings, Browser
from tools.playwright.mocks import mock_static_resources


def _restore_webkit_executable() -> None:
    browsers_path = os.environ.get("PLAYWRIGHT_BROWSERS_PATH")
    if not browsers_path:
        return
    root = Path(browsers_path)
    exe = root / "webkit-2336" / "Playwright.exe"
    backup = root / "Playwright.exe.bak"
    if not exe.exists() and backup.exists():
        exe.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(backup, exe)


def initialize_playwright_page(
        playwright: Playwright,
        test_name: str,
        browser_type: Browser,
        storage_state: str | None = None
) -> Page:
    if browser_type == "webkit":
        _restore_webkit_executable()

    browser = playwright[browser_type].launch(headless=settings.headless)
    context = browser.new_context(
        base_url=settings.get_base_url(),
        storage_state=storage_state,
        record_video_dir=settings.videos_dir
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    mock_static_resources(page)

    yield page

    context.tracing.stop(path=settings.tracing_dir.joinpath(f'{test_name}.zip'))
    browser.close()

    allure.attach.file(settings.tracing_dir.joinpath(f'{test_name}.zip'), name='trace', extension='zip')
    allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)
