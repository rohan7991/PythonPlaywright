from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.w3schools.com/')
    page.click('//*[@id="navbtn_tutorials"]')
    page.wait_for_timeout(500)

    page.fill('//*[@id="filter-tutorials-input"]','Java')

    page.wait_for_timeout(500)

    page.click('a.ga-top-drop-tut-java:nth-child(2)')

    page.wait_for_timeout(2000)
    browser.close()