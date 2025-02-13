from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import ChromiumOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.webdriver import WebDriver as EdgeWebDriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.webdriver import WebDriver as FireFoxDriver


class SeleniumFactory:

    @staticmethod
    def set_desktop_options(options):
        options.add_argument("--start-maximized")
        options.add_argument("--headless=new")
        options.add_argument("--disable-extensions")
        options.add_argument("--no-sandbox")
        options.add_argument("disable-infobars")
        options.add_argument("enableNetwork")
        options.add_argument("--disable-cache")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-gpu")
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--disable-features=InsecureDownloadWarnings")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-extensions")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--unsafely-treat-insecure-origin-as-secure=http://www.automationpractice.pl/index.php")
        options.add_argument("--user-data-dir=/tmp/unique_dir")
        options.add_experimental_option("prefs", SeleniumFactory.set_browser_preferences())
        options.set_capability("cloud:options", SeleniumFactory.set_desired_capabilities())
        return options

    @staticmethod
    def set_mobile_options(options):
        options.add_argument("--no-sandbox")
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--user-data-dir=/tmp/unique_dir")
        mobile_emulation = {
            "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0, "touch": True, "mobile": True},
            "userAgent": "Mozilla/5.0 (Linux; Android 11; SM-G977U Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36",
            "clientHints": {"platform": "Android", "mobile": True}}
        options.add_experimental_option("mobileEmulation",
                                        mobile_emulation)
        return options

    @staticmethod
    def set_browser_preferences():
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "excludeSwitches": ["enable-automation"],
            "safebrowsing.profile_enabled": False
        }
        return prefs

    @staticmethod
    def set_desired_capabilities():
        caps = DesiredCapabilities.CHROME.copy()
        caps["acceptSslCerts"] = True
        return caps

    @staticmethod
    def create_driver(browser):
        options = SeleniumFactory.set_desktop_options
        match browser:
            case "chrome":
                return ChromeDriver(options=options(ChromiumOptions()), service=ChromeService())
            case "edge":
                return EdgeWebDriver(options=options(EdgeOptions()), service=EdgeService())
            case "firefox":
                return FireFoxDriver(options=options(FirefoxOptions()), service=FirefoxService())
            case _:
                raise NotImplementedError("Browser type not supported")