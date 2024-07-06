from googlesearch import search
import time
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException


class ProfileUrlFetcher:
    def __init__(self):
        """Initializes the TwitterScraper with credentials and sets up API access."""
        self.driver = None 
        self.initialize_driver()

    def initialize_driver(self):
        options = webdriver.ChromeOptions() 
        options.add_argument("headless") 

        exe_path = ChromeDriverManager(version="114.0.5735.90").install() 
        service = Service(exe_path)
        self.driver = webdriver.Chrome(service=service, options=options)

    def get_profile_url(self, text: str) -> str:
        """Searches for Linkedin or Twitter Profile Page

        Args:
            text (str): name of the person and
            aditional descriptions if neccesary

        Returns:
            str: URL
        """
        try:
            self.driver.get('https://www.google.com')
            search_box = self.driver.find_element(By.NAME, 'q')
            search_box.send_keys(text)
            search_box.send_keys(Keys.RETURN)
            time.sleep(2)  # Allow some time for the search results to load

            # Extract the first result link
            results = self.driver.find_elements(By.CSS_SELECTOR, 'div.yuRUbf a')
            if results:
                first_link = results[0].get_attribute('href')
                return first_link
            else:
                return "No results found"

        except Exception as e:
            return f"An error occurred: {e}"

