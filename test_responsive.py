from selenium.webdriver.common.by import By # Import các lớp và phương thức cần thiết từ thư viện Selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
import time

# Tạo một fixture 'driver' cho pytest
@pytest.fixture
def driver():
    driver = webdriver.Chrome()  
    yield driver
    driver.quit()

# Hàm kiểm thử responsive design cho trang web
def test_responsive_design(driver):
    driver.get("https://demo.opencart.com/en-gb?route=common/home") # Mở trang chủ của trang web OpenCart demo

    # Định nghĩa các kích thước viewport cho Desktop, Tablet và Mobile
    viewports = {
        "Desktop": (1200, 800),
        "Tablet": (768, 1024),
        "Mobile": (375, 667)
    }

    # Lặp qua từng viewport để kiểm tra giao diện ở các kích thước khác nhau
    for device, (width, height) in viewports.items():
        # Đặt kích thước cửa sổ trình duyệt tương ứng với kích thước viewport
        driver.set_window_size(width, height)
        driver.refresh()  # Làm mới trang để áp dụng kích thước mới

        # Chờ cho phần tử 'body' của trang web xuất hiện, với thời gian chờ tối đa là 10 giây
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
        )

        try:
            # Kiểm tra hộp tìm kiếm có hiển thị hay không
            search_box = driver.find_element(By.NAME, "search")
            assert search_box.is_displayed(), f"Search box is not displayed on {device}."

            # Kiểm tra menu 'My Account' có hiển thị hay không
            my_account_dropdown = driver.find_element(By.XPATH, "//a[@class='dropdown-toggle' and @data-bs-toggle='dropdown']")
            assert my_account_dropdown.is_displayed(), f"My Account dropdown is not displayed on {device}."

            # Kiểm tra phần nội dung chính của trang có hiển thị hay không
            main_content = driver.find_element(By.ID, "content")
            assert main_content.is_displayed(), f"Main content is not displayed on {device}."

            # Tìm và nhập từ khóa 'Iphone' vào hộp tìm kiếm, sau đó nhấn Enter
            search_box.clear()
            search_box.send_keys("Iphone" + Keys.RETURN)

            # Nhấp vào nút 'Add to Cart' để thêm sản phẩm vào giỏ hàng
            add_to_cart_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit'][data-bs-toggle='tooltip']")
            add_to_cart_button.click() 

            # Chờ cho liên kết 'Shopping Cart' có thể nhấp được, rồi nhấp vào
            shopping_cart_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@title='Shopping Cart']"))
            )
            shopping_cart_link.click() 

            # Chờ cho phần tử div chứa giỏ hàng xuất hiện, với thời gian chờ tối đa là 20 giây
            checkout_cart_div = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "checkout-cart"))
            )

            # Kiểm tra giỏ hàng có chứa sản phẩm nào không
            products_in_cart = checkout_cart_div.find_elements(By.CLASS_NAME, "product-thumb")
            assert len(products_in_cart) > 0, "No products found in the cart."

            # Kiểm tra div giỏ hàng có hiển thị hay không
            assert checkout_cart_div.is_displayed(), "Checkout cart div is not displayed."
            print("Checkout cart div is displayed successfully.")

        # Bắt lỗi nếu có phần tử không hiển thị hoặc xuất hiện lỗi
        except Exception as e:
            print(f"Responsive test failed for {device}: {e}")

    # In thông báo hoàn thành kiểm tra responsive design
    print("Responsive design test completed.")
