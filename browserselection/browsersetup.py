from playwright.sync_api import sync_playwright


def browser_factory(browser_name):
        p=sync_playwright().start()

        if browser_name.lower() == "chrome":
            # Launch Chrome browser
            #chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_argument("--headless")
            #driver = webdriver.Chrome(options=chrome_options)
            browser = p.chromium.launch(args=['--start-maximized'],headless=False)
            page = browser.new_page()

        elif browser_name.lower() == "firefox":
            # Launch Firefox browser
            #firefox_options = webdriver.FirefoxOptions()
            #driver = webdriver.Firefox(options=firefox_options)
            browser = p.chromium.launch(args=['--start-maximized'],headless=False)
            page = browser.new_page()

        else:
            raise ValueError("Invalid browser name. Supported browsers are: Chrome, Edge, Firefox")
        return page