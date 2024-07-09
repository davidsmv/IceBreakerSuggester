from time import sleep 
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException
from dotenv import load_dotenv, find_dotenv
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
from configurations.settings import settings


class LinkedinScraper:
    def __init__(self) -> None:
        self.linkedin_username = settings.LINKEDIN_USERNAME
        self.linkedin_password = settings.LINKEDIN_PASSWORD
        self.driver = None 
        self.initialize_driver()

    def initialize_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")

         # Define only necessary capabilities
        options.set_capability('browserName', 'chrome')

        print("Installing ChromeDriver...")
        service = Service(ChromeDriverManager(driver_version="2.26").install())
        print("Starting ChromeDriver...")
        self.driver = webdriver.Chrome(service=service, options=options)
        print("ChromeDriver started successfully.")
        self.login()

    def login(self):
        self.driver.get("https://www.linkedin.com/login") 
        sleep(0.1) 


        self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(self.linkedin_username) 
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(self.linkedin_password) 
        sleep(0.1) 
        self.driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()
        sleep(0.1) 

    def is_driver_active(self):
        try:
            # Attempting to fetch the current URL to check if the driver is still active
            self.driver.current_url
            return True
        except WebDriverException:
            return False

    def linkedin_profile(self, linkedin_profile_url: str):
        if not self.is_driver_active:
            self.initialize_driver()

        self.driver.get(linkedin_profile_url) 
        sleep(1)

        elements = [
            {"name": "name", "xpath": "//h1[@class='text-heading-xlarge inline t-24 v-align-middle break-words']", "default": "Name not found"},
            {"name": "description", "xpath": "//div[@class='text-body-medium break-words']", "default": "Description not found"},
            {"name": "about", "xpath": "//div[@class='display-flex ph5 pv3']/div/div/div/span", "default": "About not found"},
            {"name": "company", "xpath": "//*[@id='profile-content']/div/div[2]/div/div/main/section[1]/div[2]/div[2]/ul/li/button/span/div", "default": "Company not found"}
        ]

        profile_info = {}

        for element in elements:
            try:
                element_text = self.driver.find_element(By.XPATH, element["xpath"]).text
                profile_info[element["name"]] = element_text
            except:
                profile_info[element["name"]] = element["default"]

        # Compile the message
        message = (
            f"Profile Summary:\n"
            f"Name: {profile_info['name']}\n"
            f"Description: {profile_info['description']}\n"
            f"About: {profile_info['about']}\n"
            f"Company: {profile_info['company']}\n"
        )
        return message
        
