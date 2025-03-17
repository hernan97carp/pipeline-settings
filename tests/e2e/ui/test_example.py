import pytest
from playwright.sync_api import Playwright, sync_playwright

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        # Crea el contexto sin grabación de video
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://playwright.dev/docs/intro") 
        assert page.title() == "Playwright"
        context.close()
        browser.close()