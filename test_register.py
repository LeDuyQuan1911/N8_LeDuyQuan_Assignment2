import unittest # Nhập các thư viện cần thiết để thực hiện kiểm thử
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
import logging  
from selenium.webdriver.firefox.options import Options

import pytest
logging.basicConfig(level=logging.ERROR)  # Thiết lập logging để ghi lại các lỗi và ngoại lệ trong quá trình kiểm thử

# Khởi tạo một fixture 'driver' cho pytest
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# # PASS
# def test_register_valid_data(driver): # Hàm kiểm thử: Kiểm tra đăng ký với dữ liệu hợp lệ
#     driver.get("http://localhost/webopencart/index.php?route=account/register&language=en-gb") # Mở trang đăng ký
#     time.sleep(2)  

#     first_name_field = WebDriverWait(driver, 2).until( # Tìm và điền tên vào trường 'First Name'
#         EC.presence_of_element_located((By.ID, "input-firstname"))
#     )
#     first_name_field.send_keys("Nguyễn Thị Thảo")

#     last_name_field = WebDriverWait(driver, 2).until( # Tìm và điền họ vào trường 'Last Name'
#         EC.presence_of_element_located((By.ID, "input-lastname"))
#     )
#     last_name_field.send_keys("Nguyên")

#     email_field = WebDriverWait(driver, 2).until( # Tìm và điền email vào trường 'Email'
#         EC.presence_of_element_located((By.ID, "input-email"))
#     )
#     email_field.send_keys("nttn1234@gmail.com")

#     password_field = WebDriverWait(driver, 2).until(  # Tìm và điền mật khẩu vào trường 'Password'
#         EC.presence_of_element_located((By.ID, "input-password"))
#     )
#     password_field.send_keys("1234")

#     driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.NAME, "agree"))
#     time.sleep(5)

#     privacy_policy_checkbox = driver.find_element(By.NAME, "agree") # Chọn checkbox chấp nhận chính sách bảo mật
#     driver.execute_script("arguments[0].click();", privacy_policy_checkbox)
#     time.sleep(2)

#     continue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary") # Nhấp vào nút 'Continue' để đăng ký
#     continue_button.click()
#     time.sleep(2)  

#     try: # Kiểm tra xem thông báo thành công có xuất hiện không
#         success_message = WebDriverWait(driver, 20).until(
#             EC.visibility_of_element_located((By.XPATH, "//div[@id='content']/h1"))
#         )

#         assert success_message.is_displayed(), "Success message is not displayed after registration."
#         assert "Your Account Has Been Created!" in success_message.text, \
#             "The account creation message did not appear as expected."

#     except Exception as e:
#         print("Error or assertion failed:", e)
#         print("Current page source:", driver.page_source)

# # PASS
# def test_register_empty_required_input(driver): # Kiểm tra đăng ký khi để trống các trường bắt buộc
#     driver.get("http://localhost/webopencart/index.php?route=account/register&language=en-gb") #Mở trang đăng ký của OpenCart
#     time.sleep(2)  


#     driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.NAME, "agree"))
#     time.sleep(2)

#     # Nhấp nút 'Continue' mà không điền thông tin
#     continue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
#     continue_button.click()
#     time.sleep(2)  

#     # Kiểm tra các thông báo lỗi xuất hiện cho các trường bắt buộc
#     try: 
#         first_name_error = driver.find_element(By.XPATH, "//input[@id='input-firstname']/following-sibling::div[@class='text-danger']")
#         assert first_name_error.is_displayed(), "First name error message not displayed."
#         assert "First Name must be between 1 and 32 characters!" in first_name_error.text, "First name error message text is incorrect."

#         last_name_error = driver.find_element(By.XPATH, "//input[@id='input-lastname']/following-sibling::div[@class='text-danger']")
#         assert last_name_error.is_displayed(), "Last name error message not displayed."
#         assert "Last Name must be between 1 and 32 characters!" in last_name_error.text, "Last name error message text is incorrect."

#         email_error = driver.find_element(By.XPATH, "//input[@id='input-email']/following-sibling::div[@class='text-danger']")
#         assert email_error.is_displayed(), "Email error message not displayed."
#         assert "E-Mail Address does not appear to be valid!" in email_error.text or "E-Mail Address must be between 1 and 96 characters!" in email_error.text, "Email error message text is incorrect."

#         password_error = driver.find_element(By.XPATH, "//input[@id='input-password']/following-sibling::div[@class='text-danger']")
#         assert password_error.is_displayed(), "Password error message not displayed."
#         assert "Password must be between 4 and 20 characters!" in password_error.text, "Password error message text is incorrect."


#     except Exception as e:
#         print("Error or assertion failed:", e)
#         print("Current page source:", driver.page_source)


# # PASS
# def test_register_invalid_email(driver): #Kiểm tra đăng ký với email không hợp lệ
#     driver.get("http://localhost/webopencart/index.php?route=account/register&language=en-gb") #Mở trang đăng ký của OpenCart
#     time.sleep(2)  

#     # Điền thông tin hợp lệ trừ trường 'Email' không hợp lệ
#     first_name_field = WebDriverWait(driver, 2).until( #Tìm kiếm và nhập vào trường Username
#         EC.presence_of_element_located((By.ID, "input-firstname"))
#     )
#     first_name_field.send_keys("Nguyễn Thị Thảo")

#     last_name_field = WebDriverWait(driver, 2).until( #Tìm kiếm và nhập vào trường Lastname
#         EC.presence_of_element_located((By.ID, "input-lastname"))
#     )
#     last_name_field.send_keys("Nguyên")

#     email_field = WebDriverWait(driver, 2).until( #Tìm kiếm và nhập sai cáu trúc email
#         EC.presence_of_element_located((By.ID, "input-email"))
#     )
#     email_field.send_keys("nttn1234.com")

#     password_field = WebDriverWait(driver, 2).until( #Tìm kiếm và nhập vào trường Passwrod
#         EC.presence_of_element_located((By.ID, "input-password"))
#     )
#     password_field.send_keys("123444444444")

#     driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.NAME, "agree"))
#     time.sleep(2)

#     # Nhấp vào checkbox chính sách và nút tiếp tục
#     privacy_policy_checkbox = driver.find_element(By.NAME, "agree")
#     driver.execute_script("arguments[0].click();", privacy_policy_checkbox)
#     time.sleep(2)

#     continue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary") #Click nút "Continue để hoàn thành thao tác"
#     continue_button.click()
#     time.sleep(2) 

#     # Kiểm tra lỗi email không hợp lệ
#     try:
#         email_error = driver.find_element(By.XPATH, "//input[@id='input-email']/following-sibling::div[@class='text-danger']")
#         assert email_error.is_displayed(), "Email error message not displayed."
#         assert "E-Mail Address does not appear to be valid!" in email_error.text, "Email error message text is incorrect."
#     except Exception as e:
#         print("Error or assertion failed:", e)
#         print("Current page source:", driver.page_source)


# # PASS
# def test_register_exist_account(driver): #Kiểm tra đăng ký tài khoản đã tồn tại
#     driver.get("http://localhost/webopencart/index.php?route=account/register&language=en-gb") #Mở ra trang đăng ký của OpenCart
#     time.sleep(2)  

#     first_name_field = WebDriverWait(driver, 2).until( #Tìm kiếm và nhập vào trường Firstname
#         EC.presence_of_element_located((By.ID, "input-firstname"))
#     )
#     first_name_field.send_keys("Nguyễn Thị Thảo")

#     last_name_field = WebDriverWait(driver, 2).until( #Tìm kiếm và nhập vào trường Lastname
#         EC.presence_of_element_located((By.ID, "input-lastname"))
#     )
#     last_name_field.send_keys("Nguyên")

#     email_field = WebDriverWait(driver, 2).until( #Tìm kiếm và nhập vào trường Email đã đăng ký 
#         EC.presence_of_element_located((By.ID, "input-email"))
#     )
#     email_field.send_keys("nttn1234@gmail.com")

#     password_field = WebDriverWait(driver, 2).until( #Tìm kiếm và nhập vào trường Password đã đăng ký
#         EC.presence_of_element_located((By.ID, "input-password"))
#     )
#     password_field.send_keys("1234")

#     driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.NAME, "agree"))
#     time.sleep(2)

#     # Nhấp vào checkbox chính sách và nút tiếp tục
#     privacy_policy_checkbox = driver.find_element(By.NAME, "agree")
#     driver.execute_script("arguments[0].click();", privacy_policy_checkbox)
#     time.sleep(2)

#     continue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary") #Click vào nút "Continue" để tiếp tục
#     continue_button.click()
#     time.sleep(2) 

#     try: #kiểm tra thông báo có hợp lệ hay không
#         email_error = driver.find_element(By.XPATH, "//input[@id='input-email']/following-sibling::div[@class='text-danger']")
#         assert email_error.is_displayed(), "Email error message not displayed."
#         assert "E-Mail Address is already registered!" in email_error.text, "Email error message text is incorrect."
#     except Exception as e:
#         print("Error or assertion failed:", e)
#         print("Current page source:", driver.page_source)


# # Pass
# def test_no_click_policy(driver): #Kiểm tra không check chính sách bảo mật
#     driver.get("http://localhost/webopencart/index.php?route=account/register&language=en-gb") #Mở ra trang đăng ký của OpenCart
#     time.sleep(2)  

#     first_name_field = WebDriverWait(driver, 2).until( #Tìm kiếm và nhập vào trường Username
#         EC.presence_of_element_located((By.ID, "input-firstname"))
#     )
#     first_name_field.send_keys("Nguyễn Thị Thảo")

#     last_name_field = WebDriverWait(driver, 2).until( #Tìm kiếm và nhập vào trường Lastname
#         EC.presence_of_element_located((By.ID, "input-lastname"))
#     )
#     last_name_field.send_keys("Nguyên")

#     email_field = WebDriverWait(driver, 2).until( #Tìm kiếm và nhập vào trường Email
#         EC.presence_of_element_located((By.ID, "input-email"))
#     )
#     email_field.send_keys("nttn1111111@gmail.com")

#     password_field = WebDriverWait(driver, 2).until( #Tìm kiếm và nhập vào trường Password
#         EC.presence_of_element_located((By.ID, "input-password"))
#     )
#     password_field.send_keys("123444444")

#     driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.NAME, "agree"))
#     time.sleep(2)

#     #Không click nut Policy và Click nút "Continue"
#     continue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
#     continue_button.click()
#     time.sleep(2) 

#     try: #Kiểm ra thông báo để xác nhận đúng hay sai
#         error_message = driver.find_elements(By.CLASS_NAME, "alert-danger")
#         if error_message:
#             assert error_message[0].is_displayed(), "Error message not displayed for not agreeing to privacy policy."
#             assert "Warning: You must agree to the Privacy Policy!" in error_message[0].text, "Unexpected error message content."
#             print("Error message displayed as expected:", error_message[0].text)
#         else:
#             print("No error message displayed. Test failed.")

#     except Exception as e:
#         print("Error or assertion failed:", e)
#         print("Current page source:", driver.page_source)

# Pass
def test_register_special_characters_in_name(driver):
    # Mở trang đăng ký
    driver.get("http://localhost/webopencart/index.php?route=account/register&language=en-gb")
    time.sleep(2)

    # Nhập vào trường FirstName bằng kí tự đặc biệt
    first_name_field = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, "input-firstname"))
    )
    first_name_field.send_keys("!!!!!!!!!")

    # Nhập vào trường LastName bằng kí tự đặc biệt
    last_name_field = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, "input-lastname"))
    )
    last_name_field.send_keys("!!!!!!!!!")

    # Nhập vào trường email
    email_field = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, "input-email"))
    )
    email_field.send_keys("nttn13444!!!123@gmail.com")

    # Nhập vào trường Password
    password_field = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, "input-password"))
    )
    password_field.send_keys("1234")

    # Cuộn xuống và tích vào ô điều khoản
    driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.NAME, "agree"))
    time.sleep(1)
    privacy_policy_checkbox = driver.find_element(By.NAME, "agree")
    driver.execute_script("arguments[0].click();", privacy_policy_checkbox)
    time.sleep(1)

    # Nhấn nút "Continue"
    continue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    continue_button.click()
    time.sleep(2)

    # Kiểm tra nếu có thông báo lỗi ở trường FirstName
    errorMessageFirstName = WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='input-firstname']/following-sibling::div[@class='text-danger']"))
    )
    assert errorMessageFirstName.is_displayed(), "First name error message is not displayed."
    assert "First Name must be between 1 and 32 characters!" in errorMessageFirstName.text, "Error message text for first name is incorrect."

    # Kiểm tra nếu có thông báo lỗi ở trường LastName
    errorMessageLastName = driver.find_element(By.XPATH, "//input[@id='input-lastname']/following-sibling::div[@class='text-danger']")
    assert errorMessageLastName.is_displayed(), "Last name error message is not displayed."
    assert "Last Name must be between 1 and 32 characters!" in errorMessageLastName.text, "Error message text for last name is incorrect."

