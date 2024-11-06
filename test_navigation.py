import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException  # Importing TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  
    yield driver
    driver.quit()
#test navigation
def test_navigation(driver):
    # Navigate to the home page
    driver.get("http://localhost/webopencart/index.php?route=common/home&language=en-gb")

    # Wait to ensure the page is fully loaded
    time.sleep(3)  # Adjust wait time if necessary

    # Check navigation to the Products page
    try:
        products_link = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Desktops")))
        products_link.click()

        # Wait and verify navigation
        WebDriverWait(driver, 2).until(
            EC.title_contains("Desktops"))  # Check if the title contains 'Desktops'
        print("Navigated to Products page:", driver.title)

        # Short wait before clicking the specific product link
        time.sleep(2)

        # Navigate to a specific product
        specific_product_link = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.LINK_TEXT, "MacBook")))  # Wait for the element to be present

        # Debug: Check if the link is clickable
        print("Product link is clickable:", specific_product_link.is_displayed())
        
        # Click the specific product link
        driver.execute_script("arguments[0].click();", specific_product_link)  # Force click using JavaScript

        # Wait and verify navigation to product details
        WebDriverWait(driver, 2).until(
            EC.title_contains("MacBook"))  # Check if the title contains 'MacBook'
        print("Navigated to specific product page:", driver.title)

    except TimeoutException:
        print("Timeout while waiting for the product link to be clickable.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        # Clean up and close the driver
        driver.quit()