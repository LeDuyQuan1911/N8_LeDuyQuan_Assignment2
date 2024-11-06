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
from selenium.webdriver.firefox.options import Options
import pytest

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

#Pass
def test_correct_search_products(driver): #Hàm kiểm tra khi nhập đúng dữ liệu
        existent_keyword = "Iphone"  
        results = search_products(driver, existent_keyword)
        time.sleep(2)  
        assert len(results) > 0, "No products found for 'Iphone'"

#Pass
def test_search_with_noExistProducts(driver): #Nhập dữ liệu tìm kiếm với sản phẩm không tồn tại
        nonexistent_keyword = "noExistProducts"  
        results = search_products(driver, nonexistent_keyword)
        time.sleep(2)  
        assert len(results) == 0, f"Expected no products for '{nonexistent_keyword}', but found some."

#Pass
def test_search_with_uppercaseAllText(driver): #Nhập dữ liệu với kí tự Hoa
        uppercase_keyword = "IPHONE"  
        results = search_products(driver, uppercase_keyword)
        time.sleep(2)  
        assert len(results) > 0, f"Expected products for '{uppercase_keyword}', but none were found."
        print(f"Test for uppercase keyword '{uppercase_keyword}' passed. Products found: {len(results)}.")

#Pass
def test_search_with_lowercaseAllText(driver): #Nhập dữ liệu với kí tự thường
        lowercase_keyword = "iphone"  
        results = search_products(driver, lowercase_keyword)
        time.sleep(2)  
        assert len(results) > 0, f"Expected products for '{lowercase_keyword}', but none were found."
        print(f"Test for lowercase keyword '{lowercase_keyword}' passed. Products found: {len(results)}.")

#Pass        
def test_search_special_characters(driver): #Nhập vào với kí tự đặc biệt
        special_character_search_query = "!@#$%^&*()_+"  
        results = search_products(driver, special_character_search_query)
        time.sleep(2)  
        assert len(results) == 0, f"Expected no products for the special character search, but found {len(results)} products."

        print("Test for special character search passed. No products found.")
        
#Pass
def test_search_with_Whitespace_surrounded(driver): #Nhập vào dữ liệu với kí tự trắng xung quanh
        keyword_with_whitespace = "  Iphone  "  
        results = search_products(driver, keyword_with_whitespace)
        time.sleep(2)  
        assert len(results) > 0, f"Expected to find products for '{keyword_with_whitespace}', but found none."

        print(f"Test for keyword surrounded by whitespace '{keyword_with_whitespace}' passed. Products found.")

#Pass
def test_search_empty_characters(driver): #Tìm kiếm với dữ liệu trống
        empty_search_query = ""  
        results = search_products(driver, empty_search_query)
        time.sleep(2)  
        assert len(results) == 0, f"Expected no products for an empty search, but found {len(results)} products."

        print("Test for empty search characters passed. No products found.")
        
#Pass
def test_search_with_specialCharacterInText(driver): #Nhập diệu liệu với kí tự đặc biệt trong tên sản phẩm
        special_characters_keyword = "!Iphone" 
        results = search_products(driver, special_characters_keyword)
        time.sleep(2)  
        assert len(results) == 0, f"Expected no products for '{special_characters_keyword}', but found some."

        print(f"Test for special characters keyword '{special_characters_keyword}' passed. No products found.")


#Fail
def test_search_with_longCharacterInText(driver): #Nhập diệu liệu với số lượng chữ nhiều
    special_characters_keyword = "................................................................................."
    results = search_products(driver, special_characters_keyword)

    # Verify no products are found with the special characters keyword
    assert len(results) == 0, f"Expected no products for '{special_characters_keyword}', but found some."
    print(f"Test for special characters keyword '{special_characters_keyword}' passed. No products found.")

    # Check for horizontal scrolling by comparing the page width with the viewport width
    page_width = driver.execute_script("return document.body.scrollWidth;")
    viewport_width = driver.execute_script("return window.innerWidth;")
    
    # Assert that the page width does not exceed the viewport width
    assert page_width <= viewport_width, "The page layout is broken and has horizontal scrolling."

    print("Layout test passed. No horizontal scrolling is present.")

#Pass
def search_products(driver, search_query): #Hàm bổ trợ có chức năng tìm kiếm
            driver.get("http://localhost/webopencart/index.php?route=account/login&language=en-gb") #Mở ra trang login của Opencart
            WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.ID, "input-email")) #Tìm kiếm và nhập vào trường Email
            ).send_keys("nttn1234@gmail.com")
            WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.ID, "input-password")) #Tìm kiếm và nhập vào trường Password
            ).send_keys("1234")
    
            #Tìm kiếm nút "button" và nhấn Click
            driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()   
            time.sleep(2)         
            try:
                search_box = WebDriverWait(driver, 2).until(
                    EC.visibility_of_element_located((By.NAME, "search")) #Tìm kiếm vị trí của Search
                )

                search_box.clear() #Xóa các kí tự có sẵn trong đó
                search_box.send_keys(search_query + Keys.RETURN)  # Nhập vào các kí tự mới được thêm vào

                WebDriverWait(driver, 2).until( #Tìm kiếm vị trí contnt
                    EC.presence_of_element_located((By.ID, "content"))
                )

                products = driver.find_elements(By.XPATH, "//div[@id='content']//div[@class='product-thumb']") #Tìm phần tử chứ content là sản phẩm

                product_details = []

                #check sản phẩm có được thểm vào giỏ hàng hay không
                if not products:
                    print("No products found for the search query.")
                    return product_details  

                for product in products: #Kiểm tra sản phẩm trong giỏ hàng
                    product_name = product.find_element(By.XPATH, ".//h4/a").text
                    product_price = product.find_element(By.XPATH, ".//span[@class='price-new']").text
                    product_link = product.find_element(By.XPATH, ".//h4/a").get_attribute('href')

                    product_details.append({
                        "name": product_name,
                        "price": product_price,
                        "link": product_link
                    })

                    print(f"Product Name: {product_name}")
                    print(f"Price: {product_price}")
                    print(f"Link: {product_link}")
                    print("=" * 40)  

                return product_details  

            except Exception as e:
                print(f"An error occurred: {e}")
                return []  
