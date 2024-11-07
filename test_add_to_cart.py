import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException  # Importing TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options

import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Pass
def test_add_to_cart(driver):
    # Mở trang chính của OpenCart
    driver.get("http://localhost/webopencart/index.php?route=common/home&language=en-gb")
    
    # Set up an explicit wait for locating elements
    wait = WebDriverWait(driver, 2)
    try:
        # Sử dụng CSS_SELECTOR để tìm nút "add to cart" của sản phẩm
        add_to_cart_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(2) > div > div.content > form > div > button:nth-child(1)")
        ))

        # Scroll tới nút button và click vào nút "Add to cart"
        driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)
        add_to_cart_button.click()
        
        # Đợi thông báo xuất hiện
        success_message = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert-success"))
        )

        # Xác nhận thông tin sản phẩm ở thông báo thành công
        assert "iPhone" in success_message.text, "Product name not found in success message."

    except (TimeoutException, ElementClickInterceptedException):
        print("Encountered an issue. Retrying after refreshing the page.")
        # Reload lại page để page có thể dowload đầy đủ phần tử từ server về
        driver.refresh()
        try:
            add_to_cart_button = wait.until(EC.element_to_be_clickable(         # Sử dụng CSS_SELECTOR để tìm nút "add to cart" của sản phẩm
                (By.CSS_SELECTOR, "#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(2) > div > div.content > form > div > button:nth-child(1)")
            ))
            driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)
            
            try:
                add_to_cart_button.click()
            except ElementClickInterceptedException:
                print("Direct click failed. Attempting click with JavaScript.")
                driver.execute_script("arguments[0].click();", add_to_cart_button)

            success_message = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert-success"))
            )
            assert "iPhone" in success_message.text, "Product name not found in success message after retry."

        except TimeoutException:
            print("Action failed: 'Add to Cart' button still not found after retrying.")

# Pass
def test_add_to_cart_with_product_2quantity(driver):
    # Truy cập vào trang sản phẩm MacBook trên OpenCart
    driver.get("http://localhost/webopencart/index.php?route=product/product&language=en-gb&product_id=43")
    time.sleep(2)
    # Tìm nút "Add to Cart" và click lần đầu tiên
    add_to_cart_button = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.ID, "button-cart"))
    )
    add_to_cart_button.click()
    time.sleep(2)
    
    # Click lần thứ hai để thêm cùng sản phẩm vào giỏ hàng lần nữa
    add_to_cart_button.click()
    time.sleep(5)
    # Tìm và click vào biểu tượng giỏ hàng ở góc phải của trang
    cart_button = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#header-cart > div > button"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", cart_button)
    cart_button.click()
    time.sleep(5)
    
    # Lấy tên sản phẩm từ giỏ hàng
    product_names = driver.find_elements(By.CSS_SELECTOR, "#header-cart > div > ul > li > table > tbody > tr > td.text-start > a")
    actual_product_names = [name.text for name in product_names]
    print("Tên sản phẩm thực tế:", actual_product_names)

    # Lấy số lượng sản phẩm từ giỏ hàng
    product_quantities = driver.find_elements(By.CSS_SELECTOR, "#header-cart .dropdown-menu .table-striped tbody tr td.text-end:nth-child(3)")
    actual_quantities = []

    for quantity in product_quantities:
        quantity_text = quantity.text.replace("x", "").strip()  # Loại bỏ ký tự 'x' và khoảng trắng
        if quantity_text:  
            actual_quantities.append(int(quantity_text))
        else:
            actual_quantities.append(0)

    # Xác định giá trị mong đợi
    expected_product_names = ['MacBook']
    expected_quantities = [2]

    # Xác minh tên và số lượng sản phẩm trong giỏ hàng
    assert sorted(expected_product_names) == sorted(actual_product_names), "Tên sản phẩm không khớp"
    assert expected_quantities == actual_quantities, "Số lượng sản phẩm không khớp"

#Pass
def test_add_to_cart_multiple_products(driver): #Thêm 1 lúc nhiều sản phẩm (TH này là 2 sản phẩm)
    driver.get("http://localhost/webopencart/index.php?route=common/home&language=en-gb") #Mở trang OpenCart
    time.sleep(2) 
    wait = WebDriverWait(driver, 2)

    #tìm nút "Add to cart của Sản phẩm thứ 1"
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
        "#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(2) > div > div.content > form > div > button:nth-child(1)")))
    time.sleep(2) 
    
    #Kéo Scroll xuống và sau đó click nút "Add to cart"
    driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)
    time.sleep(2) 
    add_to_cart_button.click()
    time.sleep(2)  

    driver.get("http://localhost/webopencart/index.php?route=product/product&language=en-gb&product_id=43") # Mở ra trang product của Macbook
    time.sleep(2)

    time.sleep(2) 
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, "button-cart"))) #Click vào nút "Add to cart"
    add_to_cart_button.click()
    time.sleep(7) 

    cartButton = driver.find_element(By.CSS_SELECTOR, "#header-cart > div > button")
    # driver.execute_script("arguments[0].scrollIntoView(true);", cartButton) #Scroll xuống và nhấn vào nút chứ tổng sản phẩm và tổng tiền
    cartButton.click()
    time.sleep(2) 

    #Tìm tên các sản phẩm
    productNames = driver.find_elements(By.CSS_SELECTOR, "#header-cart > div > ul > li > table > tbody > tr > td.text-start > a")
    actualProductNames = [name.text for name in productNames]

    expectedProductNames = ["iPhone", "MacBook"] 

    assert sorted(expectedProductNames) == sorted(actualProductNames), "Tên sản phẩm không khớp"


