from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1920x1080')

chrome_options.add_argument("lang=ko_KR")
chrome_options.add_argument("--disable-setuid-sandbox")
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
browser = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=chrome_options)
browser.execute_script(
    "Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5];},});")
browser.execute_script(
    "Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")


alert_url = "https://buly.kr/1c3oOE6"
delay_url = "https://tdeal.kr/app/16D6YH?seq=1650721354&date=1130"
target = [alert_url, delay_url]

for url, idx in zip(target, range(len(target))):
    try:
        browser.get(url)
        test = WebDriverWait(browser, 3).until(EC.alert_is_present())
        alert = browser.switch_to.alert
        alert.accept()
        print("Alert Exist")
        test = WebDriverWait(browser, 3)
    except TimeoutException as e:
        print("No alert")
    except Exception as e:
        print(str(e))
    browser.get_screenshot_as_file(f"test_{idx}.png")
    print(browser.window_handles)
browser.quit()
