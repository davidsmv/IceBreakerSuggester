from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time


class TwitterScraper:
    """A class to fetch tweets from Twitter using the Tweepy API."""

    def __init__(self):
        """Initializes the TwitterScraper with credentials and sets up API access."""
        self.driver = None

    def initialize_driver(self):
        self.driver = None
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1200')
        print("Installing ChromeDriver...")
        service = Service(ChromeDriverManager().install())
        print("Starting ChromeDriver...")
        self.driver = webdriver.Chrome(service=service, options=options)
        print("ChromeDriver started successfully.")

    def fetch_tweets(self, username):
        query = f"latest tweets from {username} site:twitter.com"

        try:
            self.initialize_driver()
            self.driver.get('https://www.google.com')
            search_box = self.driver.find_element(By.NAME, 'q')
            search_box.send_keys(query)
            search_box.send_keys(Keys.RETURN)
            time.sleep(2)  # Allow some time for the search results to load

            # Extract the descriptions from the search results
            results = self.driver.find_elements(By.CSS_SELECTOR, 'div.VwiC3b')
            descriptions = []
            for result in results[:5]:  # Limiting to the first 5 results
                descriptions.append(result.text)

            # Join all descriptions into a single string message
            full_description = " | ".join(descriptions)  # Use a delimiter like " | " to separate each description

            # Create a final message including the username and the combined descriptions
            response_text = f"Username: {username} - Combined Tweets: {full_description}"
            return response_text

        except Exception as e:
            return f"An error occurred: {e}"

        finally:
            if self.driver is not None:
                self.driver.quit()
            self.driver = None
