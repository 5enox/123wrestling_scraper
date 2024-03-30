# utils.scraper.py
from playwright.sync_api import sync_playwright


def run_playwright(url):
    # Initialize Playwright and perform scraping tasks
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=False)  # Keep False for testing purposes
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        # Perform scraping tasks such as extracting data or interacting with elements
        # Example:
        title = page.title()
        content = page.inner_html('body')
        # More scraping logic...
        context.close()
        browser.close()
    # Return scraped data or perform other actions as needed
    return title, content


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(
        "https://123wrestling.com/watch-wwe-nxt-level-up-3-22-2024-march-22-2024/")
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name=" FULL SHOW").first.click()
    time.sleep(20)
    page1 = page1_info.value
    iframe_element = page1.query_selector('iframe')
    # Get the value of the src attribute
    src = iframe_element.get_attribute('src')
    # ---------------------
    context.close()
    browser.close()

    return src
