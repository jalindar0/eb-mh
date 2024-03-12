
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import pyautogui
import easyocr
import pyscreeze
from selenium.webdriver.common.keys import Keys
#catpach reader
reader = easyocr.Reader(['en'], gpu=True)


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.delete_all_cookies()


# driver = webdriver.Chrome()
driver.get("https://bhulekh.mahabhumi.gov.in")
wait = WebDriverWait(driver, 5)


time.sleep(1)

driver.maximize_window()





#image to text
def easy(reader,link):
  result = reader.readtext(link, detail = 0)
  return result[0]


original_window = driver.current_window_handle

assert len(driver.window_handles) == 1

SelectDivision  = driver.find_elements(by=By.TAG_NAME,value="option")  
i=0
#jk


#jk end    

while i<len(SelectDivision ):
    if SelectDivision [i].text == "पुणे":
        SelectDivision [i].click()
    i+=1


Go_button=driver.find_element(by=By.XPATH,value='//*[@id="ctl00_ContentPlaceHolder1_Panel1"]/p[2]/input')
Go_button.click()
time.sleep(1)



# wait.until(EC.number_of_windows_to_be(2))
# driver.switch_to.new_window('tab')
wait.until(EC.number_of_windows_to_be(2))   
for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
original_window2 = driver.current_window_handle
# assert len(driver.window_handles) == 2

# driver.forward()
# district = driver.find_elements(by=By.TAG_NAME,value="option")  
# i=0
# while i<len(district):
#     if select_element[i].text == "पुणे":
#         select_element[i].click()
#     i+=1
time.sleep(5)

District=driver.find_element(by=By.ID,value="distSelect")
DistrictSelect=District.find_elements(by=By.TAG_NAME,value="option") 
i=0

#distict list
select_element = driver.find_element(by=By.ID,value="distSelect")
select = Select(select_element)
options = [option.text for option in select.options]
options.pop(0)

# Print the list of options
print("jalindar")
print(options)
print("end me")

while i<len(DistrictSelect ):
    if DistrictSelect [i].text == "पुणे":
        DistrictSelect [i].click()
    i+=1

time.sleep(2)



# Find the select element by ID



Taluka=driver.find_element(by=By.ID,value="talSelect")
TalukaSelect=Taluka.find_elements(by=By.TAG_NAME,value="option") 
i=0


#distict list
select_element1 = driver.find_element(by=By.ID,value="talSelect")
select1 = Select(select_element1)
options = [option.text for option in select1.options]
options.pop(0)
# Print the list of options
print("jalindar")
print(options)
print("end me")

while i<len(TalukaSelect ):
    if TalukaSelect [i].text == "हवेली":
        TalukaSelect [i].click()
    i+=1



time.sleep(3)
# Village=driver.find_element(by=By.XPATH,value='//*[@id="vilSelect"]/option[5]')
# Village.click()



Village  = driver.find_element(by=By.ID,value="vilSelect") 
VillageSelect=Village.find_elements(by=By.TAG_NAME,value="option") 
i=0


#distict list
select_element2 = driver.find_element(by=By.ID,value="vilSelect")
select2 = Select(select_element2)
options = [option.text for option in select2.options]
options.pop(0)
# Print the list of options
print("jalindar")
print(options)
print("end me")

while i<len(VillageSelect ):
    if VillageSelect [i].text == "कोपरे":
        VillageSelect [i].click()
    i+=1


time.sleep(2)

radio_button=driver.find_element(by=By.XPATH,value='//*[@id="rbsryno"]')
radio_button.click()


try:
    # Wait for the input field to be located
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='number'][ng-model='sno']"))
    )
    
    # Extract data from the input field
    input_data = input_field.get_attribute('value')

    # Print or process the data as needed
    print("Data in the input field:", input_data)

finally:
    # Close the WebDriver
    driver.quit()
'''

for i in range(35, 44):
    try:
        time.sleep(2)
        serve_no = driver.find_element(by=By.XPATH, value='//*[@id="aspnetForm"]/div[4]/div/div/div[3]/div/div[4]/table/tbody/tr[1]/td[1]/input[1]')
        serve_no.clear()
        serve_no.send_keys(f'{i}')

        time.sleep(2)
        shodh_button = driver.find_element(by=By.XPATH, value='//*[@id="aspnetForm"]/div[4]/div/div/div[3]/div/div[4]/table/tbody/tr[1]/td[2]/input')
        shodh_button.click()

        time.sleep(3)
        serve_dowpdown = driver.find_element(by=By.XPATH, value='//*[@id="aspnetForm"]/div[4]/div/div/div[3]/div/div[4]/table/tbody/tr[3]/td/select[1]/option[2]')
        serve_dowpdown.click()

        time.sleep(2)
        mobile_no = driver.find_element(by=By.XPATH, value='//*[@id="aspnetForm"]/div[4]/div/div/div[3]/div/div[4]/table/tbody/tr[5]/td/div/input')
        mobile_no.send_keys('9999999999')

        time.sleep(2)
        button_7_12 = driver.find_element(by=By.XPATH, value='//*[@id="aspnetForm"]/div[4]/div/div/div[3]/div/div[4]/table/tbody/tr[6]/td/input[1]')
        button_7_12.click()

        wait.until(EC.number_of_windows_to_be(3))
        time.sleep(2)

        for window_handle in driver.window_handles:
            if window_handle != original_window: 
                if window_handle != original_window2:
                    driver.switch_to.window(window_handle)
                    break

        time.sleep(5)
        original_window3 = driver.current_window_handle

        driver.find_element(by=By.XPATH, value='//*[@id="ctl00_ContentPlaceHolder1_Image3"]').screenshot('./i5.png')

        time.sleep(2)
        driver.find_element(by=By.XPATH, value='//*[@id="ctl00_ContentPlaceHolder1_txtCaptcha"]').send_keys(f"{easy(reader, './i5.png')}")

        time.sleep(5)
        driver.find_element(by=By.XPATH, value='//*[@id="ctl00_ContentPlaceHolder1_Button1"]').click()
        time.sleep(3)

        pyautogui.hotkey('ctrl', 'p')
        time.sleep(2)
        time.sleep(2)
        pyautogui.hotkey('enter')

        time.sleep(2)

        file_name = pyscreeze.locateCenterOnScreen("file_.png", confidence=0.3)
        pyautogui.moveTo(file_name)
        time.sleep(2)

        pyautogui.write(f"pune_haveli_Akurdi_{i}")
        time.sleep(2)

        pyautogui.hotkey('enter')
        time.sleep(1)
        time.sleep(3)

        pyautogui.hotkey('ctrl', 'w')
        time.sleep(2)

        driver.switch_to.window(original_window2)
    except Exception as e:
        print(f"Error occurred in iteration {i}: {e}")
        continue  # Skip to the next iteration if any error occurs

time.sleep(5)
 
'''