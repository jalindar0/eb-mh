from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import pyautogui
import easyocr
import pyscreeze
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

# Captcha reader
reader = easyocr.Reader(['en'], gpu=True)

def find_element_by_text(text):
    elements = driver.find_elements(By.XPATH, f'//*[text()="{text}"]')
    if elements:
        return elements[0]
    return None

def select_option_by_text(element, option_text):
    options = element.find_elements(By.TAG_NAME, 'option')
    for option in options:
        if option.text == option_text:
            option.click()
            break

def switch_to_new_window():
    for window_handle in driver.window_handles:
        if window_handle != original_window and window_handle != original_window2:
            driver.switch_to.window(window_handle)
            break

def process_captcha():
    driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_Image3"]').screenshot('./i5.png')
    captcha_text = easy(reader, './i5.png')
    driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_txtCaptcha"]').send_keys(captcha_text)

def save_pdf_file(file_name, index):
    pyautogui.hotkey('ctrl', 'p')
    time.sleep(2)
    pyautogui.hotkey('enter')
    time.sleep(2)
    file_center = pyscreeze.locateCenterOnScreen("file_.png", confidence=0.3)
    pyautogui.moveTo(file_center)
    time.sleep(2)
    pyautogui.write(f"pune_haveli_Akurdi_{index}")
    time.sleep(2)
    pyautogui.hotkey('enter')
    time.sleep(2)

def handle_iteration(index):
    time.sleep(2)
    serve_no = driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/div[4]/div/div/div[3]/div/div[4]/table/tbody/tr[1]/td[1]/input[1]')
    serve_no.clear()
    serve_no.send_keys(str(index))

    time.sleep(2)
    shodh_button = driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/div[4]/div/div/div[3]/div/div[4]/table/tbody/tr[1]/td[2]/input')
    shodh_button.click()

    time.sleep(3)
    serve_dropdown = driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/div[4]/div/div/div[3]/div/div[4]/table/tbody/tr[3]/td/select[1]/option[2]')
    serve_dropdown.click()

    time.sleep(2)
    mobile_no = driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/div[4]/div/div/div[3]/div/div[4]/table/tbody/tr[5]/td/div/input')
    mobile_no.send_keys('9999999999')

    time.sleep(2)
    button_7_12 = driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/div[4]/div/div/div[3]/div/div[4]/table/tbody/tr[6]/td/input[1]')
    button_7_12.click()

    wait.until(EC.number_of_windows_to_be(3))
    switch_to_new_window()

    time.sleep(5)
    process_captcha()

    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_Button1"]').click()
    time.sleep(3)

    save_pdf_file("pune_haveli_Akurdi", index)

    pyautogui.hotkey('ctrl', 'w')
    time.sleep(2)

def process_data():
    for index in range(35, 44):
        try:
            handle_iteration(index)
        except Exception as e:
            print(f"Error occurred in iteration {index}: {e}")
            continue

# Your existing code starts here
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get("https://bhulekh.mahabhumi.gov.in")
wait = WebDriverWait(driver, 5)
time.sleep(1)
driver.maximize_window()
original_window = driver.current_window_handle

# Handle the selection steps
select_element = find_element_by_text("पुणे")
if select_element:
    select_element.click()

Go_button = driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_Panel1"]/p[2]/input')
Go_button.click()
time.sleep(1)
wait.until(EC.number_of_windows_to_be(2))
for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break
original_window2 = driver.current_window_handle

District = driver.find_element(By.ID, 'distSelect')
select_option_by_text(District, "पुणे")

time.sleep(2)
Taluka = driver.find_element(By.ID, 'talSelect')
select_option_by_text(Taluka, "हवेली")

time.sleep(2)
Village = driver.find_element(By.ID, 'vilSelect')
select_option_by_text(Village, "कोपरे")

time.sleep(2)
radio_button = driver.find_element(By.XPATH, '//*[@id="rbsryno"]')
radio_button.click()

# Process data
process_data()
