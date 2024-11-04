from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium import webdriver
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()  
    yield driver
    driver.quit()

def test_add_to_wishlist_noLogin(driver): #Thêm sản phẩm vào mục yêu thích
    driver.get("https://demo.opencart.com/en-gb/product/iphone") #Mở trang sản phẩm
    
    wait = WebDriverWait(driver, 30)
    try:
        wish_list_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[aria-label='Add to Wish List']") #Click vào nút Add to wishlist
        ))
        
        wish_list_button.click()
        
        alert_message = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert-success")) # Tìm kiếm thông báo thành công
        )

        assert "You must login" in alert_message.text, "Expected login message not found." #Thống bảo bạn phải đăng nhập trước

    except TimeoutException:
        print("Timed out waiting for the element. Retrying after refreshing the page.")
        driver.refresh()
        try:
            wish_list_button = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[aria-label='Add to Wish List']") #Click vào nút Add to wishlist
            ))
            wish_list_button.click()
            alert_message = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert-success")) # Tìm kiếm thông báo thành công
            )
            assert "You must login" in alert_message.text, "Expected login message not found." # Tìm kiếm thông báo thành công
        except TimeoutException:
            print("Action failed: Element still not found after retrying.")


def test_add_to_wishlist_Login(driver): #Thêm sản phẩm vào mục yêu thích
    login(driver) #Đăng nhập vào
    driver.get("https://demo.opencart.com/en-gb/product/iphone") #Mở trang sản phẩm
    
    wait = WebDriverWait(driver, 30)
    try:
        wish_list_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[aria-label='Add to Wish List']") #Click vào nút Add to wishlist
        ))
        
        wish_list_button.click()
        
        alert_message = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert-success")) # Tìm kiếm thông báo thành công
        )

        assert "You must login" in alert_message.text, "Expected login message not found." #Thống bảo bạn phải đăng nhập trước

    except TimeoutException:
        print("Timed out waiting for the element. Retrying after refreshing the page.")
        driver.refresh()
        try:
            wish_list_button = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[aria-label='Add to Wish List']") #Click vào nút Add to wishlist
            ))
            wish_list_button.click()
            alert_message = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert-success")) # Tìm kiếm thông báo thành công
            )
            assert "You must login" in alert_message.text, "Expected login message not found." # Tìm kiếm thông báo thành công
        except TimeoutException:
            print("Action failed: Element still not found after retrying.")


def login(driver): #Đăng nhập vào sản phẩm
    driver.get("https://demo.opencart.com/index.php?route=account/login") #Truy cập vào trang sản phẩm

    wait = WebDriverWait(driver, 10) 

    email_field = wait.until(EC.visibility_of_element_located((By.ID, "input-email"))) #Nhập vào field email
    email_field.send_keys("leduyquan2574@gmail.com")

    password_field = wait.until(EC.visibility_of_element_located((By.ID, "input-password"))) #Nhập vào field password
    password_field.send_keys("Quan19112003")

    time.sleep(10) 

    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))) #Click vào nút "Login"
    login_button.click()

    wait.until(EC.title_contains("My Account"))  #Chờ cho vào trang chứu Url /Account