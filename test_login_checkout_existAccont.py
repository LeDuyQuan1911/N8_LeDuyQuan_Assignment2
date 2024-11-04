import time # Import các module cần thiết để thực hiện các tác vụ về thời gian và tương tác với trang web
from selenium.webdriver.support.ui import Select
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Định nghĩa fixture để tạo và hủy driver cho mỗi test
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def login(driver):
    driver.get("https://demo.opencart.com/index.php?route=account/login")     # Truy cập vào trang đăng nhập của OpenCart
    wait = WebDriverWait(driver, 10) 

    email_field = wait.until(EC.visibility_of_element_located((By.ID, "input-email"))) # Tìm trường email và điền vào thông tin đăng nhập
    email_field.send_keys("leduyquan2574@gmail.com")

    password_field = wait.until(EC.visibility_of_element_located((By.ID, "input-password"))) # Tìm trường mật khẩu và điền vào mật khẩu
    password_field.send_keys("Quan19112003")
    time.sleep(10) 

    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))) # Nhấn nút "Login"
    login_button.click()

    wait.until(EC.title_contains("My Account"))  #Chờ đến khi URL xuất hiên .../My Acount
    
    
    
def test_checkout_with_existAddress(driver): # Test đặt hàng với địa chỉ tồn tại trong tài khoản
    login(driver) # Gọi hàm đăng nhập
    driver.get("https://demo.opencart.com/en-gb/product/htc-touch-hd")   # Truy cập vào trang sản phẩm iPhone
    wait = WebDriverWait(driver, 30)
    time.sleep(20) 

    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, "button-cart")))  # Chờ nút "Add to Cart" và nhấn vào
    add_to_cart_button.click()
    time.sleep(20)  

    driver.get("https://demo.opencart.com/index.php?route=checkout/cart") # Truy cập vào giỏ hàng
    time.sleep(20)  

    checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Checkout"))) # Chờ nút "Checkout" và nhấn vào
    checkout_button.click()
    time.sleep(20)  

    # Chọn địa chỉ giao hàng đã lưu
    wait = WebDriverWait(driver, 20)
    shipping_address_dropdown = wait.until(EC.presence_of_element_located((By.ID, "input-shipping-address")))
    select = Select(shipping_address_dropdown)
    select.select_by_visible_text("Lê Quân, Jung Talents, 264/50 Lê Văn Quới, Quận Bình Tân, Bac Kan, Viet Nam")
    time.sleep(20)  

    # Thực hiện các bước chọn phương thức giao hàng và thanh toán, rồi xác nhận đơn hàng
    shipping_method = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#button-shipping-methods"))
    )
    shipping_method.click()
    time.sleep(20)


    method_flat = driver.find_element(By.CSS_SELECTOR, "#input-shipping-method-flat-flat")
    method_flat.click()
    time.sleep(20)

    continue_1 = driver.find_element(By.CSS_SELECTOR, "#button-shipping-method")
    continue_1.click()
    time.sleep(20)

    payment_method = driver.find_element(By.CSS_SELECTOR, "#button-payment-methods")
    payment_method.click()
    time.sleep(20)

    cash_method = driver.find_element(By.CSS_SELECTOR, "#input-payment-method-cod-cod")
    cash_method.click()
    time.sleep(20)

    continue_2 = driver.find_element(By.CSS_SELECTOR, "#button-payment-method")
    continue_2.click()
    time.sleep(20)

    confirm_order = driver.find_element(By.CSS_SELECTOR, "#button-confirm")
    confirm_order.click()
    time.sleep(30)

    # Kiểm tra thông báo đặt hàng thành công
    notification = driver.find_element(By.CSS_SELECTOR, "#content > h1")
    notification_actual = notification.text
    notification_expected = "Your order has been placed!"
    assert notification_expected == notification_actual, "Đơn hàng không được đặt thành công"


# Test đặt hàng với địa chỉ giao hàng mới
def test_checkout_with_newAddress(driver):
    login(driver) # Gọi hàm đăng nhập
    driver.get("https://demo.opencart.com/en-gb/product/htc-touch-hd")   # Truy cập vào trang sản phẩm iPhone
    wait = WebDriverWait(driver, 5)

    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, "button-cart"))) # Chờ nút "Add to Cart" và nhấn vào
    add_to_cart_button.click()
    time.sleep(5)  

    driver.get("https://demo.opencart.com/index.php?route=checkout/cart") # Truy cập vào giỏ hàng
    time.sleep(50)  

    checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Checkout"))) # Chờ nút "Checkout" và nhấn vào
    checkout_button.click()
    time.sleep(5)  

    # Chọn hộp kiểm "New Address" nếu chưa được chọn
    shipping_checkbox = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "input-shipping-new"))
    )
    if not shipping_checkbox.is_selected():
        shipping_checkbox.click()  
    time.sleep(20) 


    #Điền thông tin cá nhân và địa chỉ mới
    first_name = "Lê"
    last_name = "Quân"
    email = "leduyquan2574@gmail.com"
    company = "Jung Talents"
    address1 = "264/50 Lê Văn Quới"
    address2 = "drgrdfgdf"
    city = "Ho Chi Minh City"
    post_code = "191103"
    country = "Viet Nam"
    region = "Ho Chi Minh City"

    input_first_name = driver.find_element(By.CSS_SELECTOR, "#input-shipping-firstname")
    input_first_name.send_keys(first_name)
    time.sleep(20)

    input_last_name = driver.find_element(By.CSS_SELECTOR, "#input-shipping-lastname")
    input_last_name.send_keys(last_name)
    time.sleep(20)

    input_company = driver.find_element(By.CSS_SELECTOR, "#input-shipping-company")
    input_company.send_keys(company)
    time.sleep(20)

    input_address1 = driver.find_element(By.CSS_SELECTOR, "#input-shipping-address-1")
    input_address1.send_keys(address1)
    time.sleep(20)

    input_address2 = driver.find_element(By.CSS_SELECTOR, "#input-shipping-address-2")
    driver.execute_script("arguments[0].scrollIntoView(true);", input_address2)
    time.sleep(20)
    input_address2.send_keys(address2)

    input_city = driver.find_element(By.CSS_SELECTOR, "#input-shipping-city")
    input_city.send_keys(city)
    time.sleep(20)

    input_post_code = driver.find_element(By.CSS_SELECTOR, "#input-shipping-postcode")
    input_post_code.clear()
    input_post_code.send_keys(post_code)
    time.sleep(20)

    # Chọn quốc gia và vùng miền
    input_country = driver.find_element(By.CSS_SELECTOR, "#input-shipping-country")
    selection_country = Select(input_country)
    selection_country.select_by_visible_text(country)
    time.sleep(20)

    input_region = driver.find_element(By.CSS_SELECTOR, "#input-shipping-zone")
    selection_region = Select(input_region)
    selection_region.select_by_visible_text(region)
    time.sleep(20)

    # Xác nhận thông tin địa chỉ và tiếp tục đặt hàng
    continue_btn = driver.find_element(By.CSS_SELECTOR, "#button-shipping-address")
    continue_btn.click()
    time.sleep(20)

    #Chọn phương thức thanh toán 
    shipping_method = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#button-shipping-methods"))
    )
    shipping_method.click()
    time.sleep(20)

    method_flat = driver.find_element(By.CSS_SELECTOR, "#input-shipping-method-flat-flat")
    method_flat.click()
    time.sleep(20)

    continue_1 = driver.find_element(By.CSS_SELECTOR, "#button-shipping-method")
    continue_1.click()
    time.sleep(20)

    payment_method = driver.find_element(By.CSS_SELECTOR, "#button-payment-methods")
    payment_method.click()
    time.sleep(20)

    cash_method = driver.find_element(By.CSS_SELECTOR, "#input-payment-method-cod-cod")
    cash_method.click()
    time.sleep(20)

    continue_2 = driver.find_element(By.CSS_SELECTOR, "#button-payment-method")
    continue_2.click()
    time.sleep(20)

    confirm_order = driver.find_element(By.CSS_SELECTOR, "#button-confirm")
    confirm_order.click()
    time.sleep(5)

    # Kiểm tra thông báo đặt hàng thành công
    notification = driver.find_element(By.CSS_SELECTOR, "#content > h1")
    notification_actual = notification.text
    notification_expected = "Your order has been placed!"
    assert notification_expected == notification_actual, "Đơn hàng không được đặt thành công"


