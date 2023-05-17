from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Initialize Chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Go to Google.com
driver.get("https://www.google.com")

# Find the search bar element and enter "aeroplane"
search_bar = driver.find_element_by_name("q")
search_bar.send_keys("aeroplane")

# Submit the search query
search_bar.send_keys(Keys.RETURN)

# Click on the "Images" tab
images_tab = driver.find_element_by_link_text("Images")
images_tab.click()
