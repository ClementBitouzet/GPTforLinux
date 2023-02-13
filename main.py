import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import requests
import random


def get_proxy_list():
    # Make a request to the free proxy API to get a list of proxies
    response = requests.get("https://free-proxy-list.net/")

    # Extract the list of proxies from the response
    proxies = response.text.split("\n")

    # Filter the list of proxies to only include HTTP proxies
    proxy_list = [proxy for proxy in proxies if "HTTP" in proxy]

    return proxy_list


def get_random_proxy(proxy_list):
    return "200.105.215.22", "33630"



def check_proxy(host, port):
    # Try to make a request using the proxy
    try:
        response = requests.get("http://www.example.com", proxies={"http": f"http://{host}:{port}"}, timeout=5)
        return True
    except:
        return False

def bypass_cloudflare(url):
    # Get the list of proxies
    proxy_list = get_proxy_list()

    # Loop until a working proxy is found
    while True:
        # Get a random proxy from the list
        host, port = get_random_proxy(proxy_list)

        # Check if the proxy is working
        if check_proxy(host, port):
            break

    # Options for using a proxy
    firefox_options = Options()
    firefox_options.add_argument("--proxy-server=http://" + host + ":" + port)

    # Set up the Chrome driver with the options
    driver = webdriver.Firefox(options=firefox_options)

    # Navigate to the URL
    driver.get(url)
    driver.implicitly_wait(5)
    try:
        captcha_button = driver.find_element(By.XPATH, "//input[@type='checkbox']/following-sibling::span[1]")
    except:
        captcha_button = driver.find_element(By.XPATH, "//input[@value='Verify you are human']")
    captcha_button.click()



bypass_cloudflare("https://chat.openai.com/")