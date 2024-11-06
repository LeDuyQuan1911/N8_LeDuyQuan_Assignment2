import unittest # Import các thư viện cần thiết cho việc kiểm thử đơn vị và điều khiển trình duyệt
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException  
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pytest
from selenium.webdriver.firefox.options import Options

# Định nghĩa hàm fixture `driver` để khởi tạo và tắt trình duyệt Chrome
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# @pytest.fixture
# def driver():
#     options = Options()
#     options.add_argument("--start-maximized")

#     driver = webdriver.Firefox(options=options)
#     yield driver
#     driver.quit()


def test_checkout_with_guest_account(driver): # Hàm kiểm thử cho phép đặt hàng với tài khoản khách
    driver.get("http://localhost/webopencart/index.php?route=product/product&language=en-gb&product_id=28&search=touch")  # Truy cập vào trang sản phẩm iPhone
    wait = WebDriverWait(driver, 2)
    time.sleep(2)  

    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, "button-cart"))) # Nhấp vào nút thêm sản phẩm vào giỏ hàng
    add_to_cart_button.click()
    time.sleep(2)  

    driver.get("http://localhost/webopencart/index.php?route=checkout/cart&language=en-gb") # Chuyển đến trang giỏ hàng

    time.sleep(2)  

    checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Checkout"))) # Nhấp vào nút "Checkout" để tiến hành thanh toán
    checkout_button.click()

    time.sleep(2)  
    input_guest = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-guest")) # Chọn tùy chọn tài khoản khách
    )
    input_guest.click()
    time.sleep(2)

    # Nhập thông tin giao hàng
    first_name = "Nguyễn Thị Thảo"
    last_name = "Nguyên"
    email = "nttn1234@gmail.com"
    company = "ABC Company"
    address1 = "Xuân Lộc, Đồng Nai"
    address2 = "Lũy Bán Bích"
    city = "Ho Chi Minh City"
    post_code = "150703"
    country = "Viet Nam"
    region = "Ho Chi Minh City"

    # Điền thông tin cá nhân và địa chỉ giao hàng
    input_first_name = driver.find_element(By.CSS_SELECTOR, "#input-firstname")
    input_first_name.send_keys(first_name)
    time.sleep(2)

    input_last_name = driver.find_element(By.CSS_SELECTOR, "#input-lastname")
    input_last_name.send_keys(last_name)
    time.sleep(2)

    input_email = driver.find_element(By.CSS_SELECTOR, "#input-email")
    input_email.send_keys(email)
    time.sleep(2)

    input_company = driver.find_element(By.CSS_SELECTOR, "#input-shipping-company")
    input_company.send_keys(company)
    time.sleep(2)

    input_address1 = driver.find_element(By.CSS_SELECTOR, "#input-shipping-address-1")
    input_address1.send_keys(address1)
    time.sleep(2)

    input_address2 = driver.find_element(By.CSS_SELECTOR, "#input-shipping-address-2")
    driver.execute_script("arguments[0].scrollIntoView(true);", input_address2)
    time.sleep(2)
    input_address2.send_keys(address2)

    input_city = driver.find_element(By.CSS_SELECTOR, "#input-shipping-city")
    input_city.send_keys(city)
    time.sleep(2)

    input_post_code = driver.find_element(By.CSS_SELECTOR, "#input-shipping-postcode")
    input_post_code.clear()
    input_post_code.send_keys(post_code)
    time.sleep(2)

    input_country = driver.find_element(By.CSS_SELECTOR, "#input-shipping-country")
    selection_country = Select(input_country)
    selection_country.select_by_visible_text(country)
    time.sleep(2)

    input_region = driver.find_element(By.CSS_SELECTOR, "#input-shipping-zone")
    selection_region = Select(input_region)
    selection_region.select_by_visible_text(region)
    time.sleep(2)

    # Bấm vào nút "Tiếp tục" để xác nhận thông tin
    continue_btn = driver.find_element(By.CSS_SELECTOR, "#button-register")
    continue_btn.click()
    time.sleep(2)

    driver.execute_script("arguments[0].scrollIntoView(false);", driver.find_element(By.CSS_SELECTOR, "#button-shipping-methods"))
    time.sleep(4)

    shipping_method = driver.find_element(By.CSS_SELECTOR, "#button-shipping-methods") # Chọn phương thức giao hàng
    shipping_method.click()
    time.sleep(2)

    method_flat = driver.find_element(By.CSS_SELECTOR, "#input-shipping-method-flat-flat") 
    method_flat.click()
    time.sleep(2)

    continue_1 = driver.find_element(By.CSS_SELECTOR, "#button-shipping-method") # Chọn phương thức giao hàng
    continue_1.click()
    time.sleep(2)

    payment_method = driver.find_element(By.CSS_SELECTOR, "#button-payment-methods")  # Chọn phương thức thanh toán và xác nhận đơn hàng
    payment_method.click()
    time.sleep(2)

    cash_method = driver.find_element(By.CSS_SELECTOR, "#input-payment-method-cod-cod")
    cash_method.click()
    time.sleep(2)

    continue_2 = driver.find_element(By.CSS_SELECTOR, "#button-payment-method")
    continue_2.click()
    time.sleep(2)

    driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.CSS_SELECTOR, "#button-confirm"))
    time.sleep(5)

    confirm_order = driver.find_element(By.CSS_SELECTOR, "#button-confirm") #Button "Confirm" để xác nhận thanh toán
    confirm_order.click()
    time.sleep(2)

    notification = driver.find_element(By.CSS_SELECTOR, "#content > h1") #Chuyển qua trang mới và hiện thong báo
    notification_actual = notification.text

    notification_expected = "Your order has been placed!"

    assert notification_expected == notification_actual, "Đơn hàng không được đặt thành công" #Check thông báo ở trang mới

