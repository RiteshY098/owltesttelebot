import re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import requests as r
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests as r
import re

# Set up a headless Chrome browser
options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)

# Define a function to check if a URL is an Instagram Reels video
def is_reels_video(url) -> bool:

    # Use a regular expression to match the URL format
    pattern = r"https?://(?:www\.)?instagram\.com/reel/.*"
    return bool(re.match(pattern, url))

# Define a function to download the Reels video as bytes
def get_reels_video(url) -> bytes:

    # Load the URL in the browser
    browser.get(url)

    # Wait for the video element to appear
    wait = WebDriverWait(browser, 10)
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'video')))

    # Get the video source URL
    video_url = element.get_attribute('src')

    # Return the video content as bytes
    return r.get(video_url).content
