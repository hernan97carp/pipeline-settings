import pytest
from playwright.sync_api import Playwright, sync_playwright

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        # Crea el contexto sin grabación de video
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://playwright.dev/") 
        assert page.title() == "Fast and reliable end-to-end testing for modern web apps | Playwright"
        context.close()
        browser.close()