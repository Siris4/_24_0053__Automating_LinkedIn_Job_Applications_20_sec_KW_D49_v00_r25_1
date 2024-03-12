from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException, \
    ElementClickInterceptedException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime


# Function to get the current timestamp
def get_timestamp():
    """Return the current timestamp."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Constants
LINKEDIN_LOGIN_URL = "https://www.linkedin.com/login"
FILTER_SEARCH_URL = "https://www.linkedin.com/jobs/search/?currentJobId=3813109947&f_AL=true&f_E=2%2C3&f_JT=F%2CC&f_SB2=4&f_WT=2&keywords=python&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R"

linkedin_dictionary = {
    "email": "YOUROWNEMAIL",
    "linkedin_password": "YOUROWNPASSWORD",
}


# Setup webdriver
def setup_chrome_driver_for_selenium():
    """Setup Chrome WebDriver."""
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(LINKEDIN_LOGIN_URL)
    return driver


driver = setup_chrome_driver_for_selenium()


# Login procedure
def login_to_linkedin(driver, email, password):
    """Log in to LinkedIn."""
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(email)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(
        password + Keys.ENTER)
    print(f"{get_timestamp()}: Successfully logged in.")


# Click pre-easy apply links interactively
def click_pre_easy_apply_links_interactively(driver):
    """Click on pre-easy apply links interactively."""
    pre_easy_apply_links = driver.find_elements(By.CSS_SELECTOR,
                                                "li.job-card-container__apply-method.job-card-container__footer-item.inline-flex.align-items-center")
    for index, link in enumerate(pre_easy_apply_links):
        print(f"{get_timestamp()}: Clicking pre-Easy Apply Link #{index + 1}")
        driver.execute_script("arguments[0].scrollIntoView(true);", link)
        link.click()
        print(f"{get_timestamp()}: Clicked pre-Easy Apply Link #{index + 1}")
        time.sleep(2)  # Adjust based on actual page behavior

        if index > 0:  # Start asking for permission from the second index onwards
            proceed = input(f"Ready to proceed with pre-Easy Apply Link #{index + 1}? (Y/N): ").strip().upper()
            if proceed != 'Y':
                print("Process stopped as requested.")
                break

        # Additional steps like clicking the main Easy Apply button and handling the Next button would go here


# Main script execution
login_to_linkedin(driver, linkedin_dictionary["email"], linkedin_dictionary["linkedin_password"])
print(f"{get_timestamp()}: Navigating to the filter search URL.")
driver.get(FILTER_SEARCH_URL)
click_pre_easy_apply_links_interactively(driver)

# Additional functions and logic to implement the rest of your script's functionality
# would follow here, ensuring to apply best practices for dynamic waiting, error handling, and user interaction as outlined

# Reminder: This script outline focuses on integrating your requested improvements and may require adjustments to fit your specific scenario.
