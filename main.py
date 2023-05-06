from selenium import webdriver
import time

def auth(token: str) -> None: 
    url_login = 'https://discord.com/login'
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(executable_path='../chromedriver', options=options) 
    driver.get(url_login)
    time.sleep(2)
    driver.execute_script(
    f"setImmediate(() => document.body.appendChild(document.createElement('iframe')).contentWindow.localStorage.token = '\"{token}\"');"
        )
auth('YOUR_TOKEN')
