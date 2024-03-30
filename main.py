from playwright.sync_api import Playwright, sync_playwright, expect
import time
import os
import requests
import json
import urllib.request

os.system("clear")


def download_data(url):
    p1 = "https://api.w03.savethevideo.com/tasks"
    obj = {"type": "info", "url": url}
    r = requests.post(p1, json=obj)
    h = json.loads(r.text)['href']
    g1 = "https://api.w03.savethevideo.com//" + h
    time.sleep(5)
    r2 = requests.get(g1)
    jr2 = json.loads(r2.text)
    return jr2['result']['url']


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


with sync_playwright() as playwright:
    url = run(playwright)
    print('Got Video Download Url ', url)
    download_url = download_data(url)
    # Download the video
    print("Downloading video...")
    urllib.request.urlretrieve(
        download_url, "./videos/video.mp4")
    print("Video downloaded and saved successfully.")
