#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time
from dateutil import parser


# Setup options
chrome_options = Options()
#chrome_options.add_argument("--headless")  # Optional: remove this if you want to see the browser
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Path to your ChromeDriver (update path as needed)
service = Service("/opt/homebrew/bin/chromedriver")  # <-- Change this to your correct path
driver = webdriver.Chrome(service=service, options=chrome_options)

# Load the page
driver.get("https://www.fastweb.com/college-scholarships")
# Wait for scholarships to load
time.sleep(5)

# Extract scholarships
cards = driver.find_elements(By.XPATH, "//div[starts-with(@id, 'scholarship_')]")
print(f"Found {len(cards)} scholarship cards")
scholarships =[]
for card in cards:  # limit to first 5
    try:
        name = card.find_element(By.TAG_NAME, "h3").text.strip()
        amount_elem = card.find_element(By.CSS_SELECTOR, "div[class*='award-amount']")
        amount = amount_elem.text.strip()
        dead_elem = card.find_element(By.CSS_SELECTOR, "div[class*='award-deadline']")
        deadline = dead_elem.text.strip()
        parsed_date = parser.parse(deadline);
        cons_dead = parsed_date.strftime("%d-%m-%Y")
        apply_link = card.find_element(By.CSS_SELECTOR, "div[class*='learn-more-button']")
        link = apply_link.find_element(By.TAG_NAME, "a").get_attribute("href")
        full_link = "https://www.scholarships.com" + link if link.startswith("/") else link
        scholarships.append({
            "name":name,
            "award":amount,
            "deadline":cons_dead,
            "eligibility":"None",
            "link":link
            })
        print(f"\n📚 {name}\n💵 {amount}\n⏳ {cons_dead} \n🔗 {full_link}")
    except Exception as e:
        print(f" Error extracting card: {e}")

driver.quit()

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://kshitizrai1065:425952722@scholarshipfinder.4rgblvl.mongodb.net/?retryWrites=true&w=majority&appName=scholarshipfinder"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["scholarship_db"]
collection = db["scholarship_info"]

collection.insert_many(scholarships)