from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pymongo import MongoClient
from bson import ObjectId
import datetime
import uuid
import time
import requests

# Setup Proxy and MongoDB
PROXY_URL = "PROXYMESH_URL"  # Update credentials
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "twitter_trends"
COLLECTION_NAME = "trends"

# Selenium Configuration
options = Options()
options.add_argument(f'--proxy-server={PROXY_URL}')
options.add_argument("--start-maximized")

service = Service("chromedriver_path")  # Replace with your chromedriver path
driver = webdriver.Chrome(service=service, options=options)

# MongoDB Client
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

def get_trending_topics():
    unique_id = str(uuid.uuid4())
    try:
        # Open Twitter login page
        driver.get("https://twitter.com/login")
        time.sleep(2)

        # Log in
        username = driver.find_element(By.NAME, "text")
        username.send_keys("TWITTER_USERNAME")  # Replace with your username
        username.send_keys(Keys.RETURN)
        time.sleep(2)

        password = driver.find_element(By.NAME, "password")
        password.send_keys("TWITTER_PASSWORD")  # Replace with your password
        password.send_keys(Keys.RETURN)
        time.sleep(5)

        # Fetch trending topics
        trending_section = driver.find_element(By.XPATH, "//section[@aria-labelledby='accessible-list-0']")
        trends = trending_section.find_elements(By.XPATH, ".//span[contains(@class, 'css-901oao')]")
        trending_topics = [trend.text for trend in trends[:5]]

        # Collect IP address
        current_ip = requests.get("http://ipinfo.io/ip", proxies={"http": PROXY_URL}).text.strip()

        # Save to MongoDB
        record = {
            "_id": ObjectId(unique_id),
            "trend1": trending_topics[0],
            "trend2": trending_topics[1],
            "trend3": trending_topics[2],
            "trend4": trending_topics[3],
            "trend5": trending_topics[4],
            "end_time": datetime.datetime.now(),
            "ip_address": current_ip
        }
        collection.insert_one(record)
        return record

    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

