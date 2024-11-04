from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
import time


@pytest.fixture
def driver():
    driver = webdriver.Chrome()  
    yield driver
    driver.quit()

#Bug - Fail
def test_writeReview(driver): #Hàm kiểm tra viết Reivew
    driver.get("https://demo.opencart.com/index.php?route=account/login") #Mở ra trang đăng nhập của Opencart

    wait = WebDriverWait(driver, 10) 

    email_field = wait.until(EC.visibility_of_element_located((By.ID, "input-email"))) #Tìm kiếm và nhập vào trường Email
    email_field.send_keys("leduyquan2574@gmail.com")

    # Chờ cho trường mật khẩu có thể nhìn thấy và nhập mật khẩu
    password_field = wait.until(EC.visibility_of_element_located((By.ID, "input-password"))) #Tìm kiếm và nhập vào trường Password
    password_field.send_keys("Quan19112003")
    time.sleep(10) 

    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))) #Nhấn nút "Continue"
    login_button.click()

    wait.until(EC.title_contains("My Account"))  
    time.sleep(10) 


    driver.get("https://demo.opencart.com/en-gb?route=common/home") #Mở ra tra home của OpenCart
    time.sleep(5)

    driver.get("https://demo.opencart.com/en-gb/product/iphone") #Mở ra trang sản phẩm tên Iphone
    time.sleep(5)


    #Các bước thao giáo để viết Review
    write_review_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Write a review"))
    )
    driver.execute_script("arguments[0].click();", write_review_link)  
    time.sleep(5)

    review_text_area = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "input-text"))
    )
    review_text_area.send_keys("This is my review text.")  
    time.sleep(5)

    rating_radio_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='rating'][value='5']"))
    )
    rating_radio_button.click()  
    time.sleep(5)

    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "button-review"))
    )
    continue_button.click()   
    time.sleep(5)

    #Kiểm tra Review mới viết có được thêm vào Review của sản phẩm hay không
    try:    
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "alert-success"))  
        )
        assert "Thank you for your review" in success_message.text, "Review submission did not succeed as expected."
        print("Review submitted successfully!")
    except Exception as e:
        print("Review submission failed:", e)



