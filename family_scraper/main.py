import argparse
from selenium import webdriver

def main():
    parser = argparse.ArgumentParser(description="Scraper")

    parser.add_argument("url", metavar="URL", type=str)

    args = parser.parse_args()

    driver = webdriver.Firefox()

    driver.get(args.url)
