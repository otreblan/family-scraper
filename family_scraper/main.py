from selenium import webdriver

def main():
    driver = webdriver.Firefox()

    driver.get("https://google.com")
