from playwright.sync_api import sync_playwright

def test_basic():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://playwright.dev/")
        
        # Obtener el título de la página
        title = page.title()
        
        # Verificar que el título sea correcto
        assert title == "Fast and reliable end-to-end testing for modern web apps | Playwright"
        
        browser.close()