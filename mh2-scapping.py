
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import easyocr
import pyscreeze
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert 


reader = easyocr.Reader(['en'], gpu=True)
def easy(reader,link):
  result = reader.readtext(link, detail = 0)
  return result[0]

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get("https://bhulekh.mahabhumi.gov.in")
wait = WebDriverWait(driver, 5)
time.sleep(1)
driver.maximize_window()


def webScrape(IDivision,IDistrict,ITaluka,IVillage):
    original_window = driver.current_window_handle
    assert len(driver.window_handles) == 1
    SelectDivision  = driver.find_elements(by=By.TAG_NAME,value="option")  
    i=0

    while i<len(SelectDivision ):
        if SelectDivision [i].text == IDivision:
            SelectDivision [i].click()
        i+=1
    Go_button=driver.find_element(by=By.XPATH,value='//*[@id="ctl00_ContentPlaceHolder1_Panel1"]/p[2]/input')
    Go_button.click()
    time.sleep(1)

    wait.until(EC.number_of_windows_to_be(2))   
    for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break
    original_window2 = driver.current_window_handle

    time.sleep(5)

    District=driver.find_element(by=By.ID,value="distSelect")
    DistrictSelect=District.find_elements(by=By.TAG_NAME,value="option") 
    i=0

    while i<len(DistrictSelect ):
        if DistrictSelect [i].text == IDistrict:
            DistrictSelect [i].click()
        i+=1

    time.sleep(2)
    Taluka=driver.find_element(by=By.ID,value="talSelect")
    TalukaSelect=Taluka.find_elements(by=By.TAG_NAME,value="option") 
    i=0

    while i<len(TalukaSelect ):
        if TalukaSelect [i].text == ITaluka:
            TalukaSelect [i].click()
        i+=1

    time.sleep(3)

    for IIVillage, last in IVillage.items():
        Village  = driver.find_element(by=By.ID,value="vilSelect") 
        VillageSelect=Village.find_elements(by=By.TAG_NAME,value="option") 
        i=0
        while i<len(VillageSelect ):
            if VillageSelect [i].text == IIVillage:
                VillageSelect [i].click()
            i+=1

        
        time.sleep(5)
        radio_button=driver.find_element(by=By.XPATH,value='//*[@id="rbsryno"]')
        radio_button.click()
        time.sleep(2)

        for i in range(1,last):
            time.sleep(2)
            serve_no=driver.find_element(by=By.XPATH,value='//*[@id="aspnetForm"]/div[4]/div/div/div[3]/div/div[4]/table/tbody/tr[1]/td[1]/input[1]')
            serve_no.clear()
            serve_no.send_keys(f'{i}')
            time.sleep(2)
            shodh_button=driver.find_element(by=By.XPATH,value='//*[@id="aspnetForm"]/div[4]/div/div/div[3]/div/div[4]/table/tbody/tr[1]/td[2]/input')
            shodh_button.click()
            time.sleep(2)
            dropdown = Select(driver.find_element(by=By.XPATH,value='//*[@id="aspnetForm"]/div[4]/div/div/div[3]/div/div[4]/table/tbody/tr[3]/td/select'))
            for j in range (1,len(dropdown.options)):
                dropdown.select_by_index(str(j))
                time.sleep(3)
                time.sleep(2)
                mobile_no=driver.find_element(by=By.XPATH,value='//*[@id="aspnetForm"]/div[4]/div/div/div[3]/div/div[4]/table/tbody/tr[5]/td/div/input')
                mobile_no.send_keys('9999999999')
                time.sleep(2)
                button_7_12=driver.find_element(by=By.XPATH,value='//*[@id="aspnetForm"]/div[4]/div/div/div[3]/div/div[4]/table/tbody/tr[6]/td/input[1]')
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
                driver.find_element(by=By.XPATH,value='//*[@id="ctl00_ContentPlaceHolder1_Image3"]').screenshot('./i5.png')
                time.sleep(2)
                driver.find_element(by=By.XPATH,value='//*[@id="ctl00_ContentPlaceHolder1_txtCaptcha"]').send_keys(f"{easy(reader,'./i5.png')}")
                time.sleep(2)
                driver.find_element(by=By.XPATH,value='//*[@id="ctl00_ContentPlaceHolder1_Button1"]').click()
                time.sleep(5)
                a=True
                while a:
                    try:
                        Alert(driver).accept()
                    except:
                        a=False
                    else:
                        time.sleep(2)
                        driver.find_element(by=By.XPATH,value='//*[@id="ctl00_ContentPlaceHolder1_Image3"]').screenshot('./i5.png')
                        driver.find_element(by=By.XPATH,value='//*[@id="ctl00_ContentPlaceHolder1_txtCaptcha"]').send_keys(f"{easy(reader,'./i5.png')}")
                        time.sleep(2)
                        driver.find_element(by=By.XPATH,value='//*[@id="ctl00_ContentPlaceHolder1_Button1"]').click()
                        time.sleep(5)
                pyautogui.hotkey('ctrl','p')
                time.sleep(2)
                time.sleep(2)
                pyautogui.hotkey('enter')
                time.sleep(2)
                file_name=pyscreeze.locateCenterOnScreen("file_.png",confidence = 0.3)
                pyautogui.moveTo(file_name)
                time.sleep(2)
                pyautogui.write(f"avasarenagar{i}-{j}")
                time.sleep(2)
                pyautogui.hotkey('enter')
                time.sleep(1)
                time.sleep(3)
                pyautogui.hotkey('ctrl','w')
                time.sleep(2)
                driver.switch_to.window(original_window2)
    

Division="पुणे"
District="पुणे"
Taluka="हवेली"

Village={
    "अवसरेनगर": 414,
    "अष्टापूर" :1144,
    "आकुर्डी": 193,
    "आगळंबे":1109, 
    "आर्वी" :522,
    "आळंदी म्हातोबाची":1245 ,
    "आव्हाळवाडी" :988,
    "आंबी" :1166,
    # "आंबेगाव खुर्द" :
    # "आंबेगाव बु." 
    # "उरुळी कांचन" 
    # "उरुळी देवाची" 
    # "उंड्री" 
    # "औताडे-हांडेवाडी" 
    # "कदमवाक -वस्ती" 
    # "कल्याण" 
    # "कळस" 
    # "कात्रज" 
    # "किन्हई" 
    # "किरकटवाडी" 
    # "वळे" 
    # "कुडजे" 
    # "कुंजीरवाडी" 
    # "केसनंद" 
    # "कोथरुड" 
    # "कोपरे" 
    # "कोरेगावमूळ" 
    # "कोलवडी" 
    # "कोळेवाडी" 
    # "कोंढणपुर" 
    # "कोंढवे खुर्द." 
    # "कोंढवे धावडे" 
    # "कोंढवे बु." 
    # "खडकवाडी" 
    # "खडकवासला" 
    # "खराडी" 
    # "खाडेवाडी" 
    # "खानापूर" 
    # "खामगाव टेक" 
    # "खामगांव मावळ" 
    # "खेडशिवापूर" 
    # "गाऊडदरा" 

    # "गावडेवाडी" 
    # "गुजर निंबाळकरवाडी" 

    # "गोगलवाडी" 
    # "गो-हे खुर्द" 

    # "घेरा सिंहगड"
    # "चऱ्होली बु" 
    # "चिखली" 
    # "चिंचवड"
    # "चिंचोली"
    # "चोविसावाडी" 
    # "जांभळी" 
    # "जांभुळवाडी" 
    # "टिळेकरवाडी"
    # "डुडुळगाव" 
    # "डोणजे" 
    # "डोंगरगाव" 
    # "तरडे" 
    # "तळवडे" 
    # "तळेरानवाडी" 
    # "तानाजीनगर"
    # "तुळापुर" 
    # "थेऊर" 
    # "थोपटे वाडी" 
    # "दापोडी" 
    # "दिघी" 
    # "देहु" 
    # "धनकवडी" 
    # "धानोरी" 
    # "धायरी"
    # "नऱ्हे" 
    # "नायगाव" 
    # "नांदेड" 
    # "नांदोशी" 
    # "निगडी" 
    # "निरगुडी"
    # "न्हावी सांडस" 
    # "पाषाण" 
    # "पिसोळी" 
    # "पिंपरी वाघेरे" 
    # "पिंपरी सांडस" 
    # "पिंपळे गुरव" 
    # "पिंपळे निलख" 
    # "पिंपळे सौदागर"
    # "पेठ" 
    # "पेरणे" 
    # "फुरसुंगी"
    # "फुलगाव"
    # "बकोरी" 
    # "बहुली" 
    # "बाणेर" 
    # "बालेवाडी"
    # "बिवरी" 
    # "बुरके गाव"
    # "बोपखेल"
    # "बोऱ्हाडेवाडी"
    # "भगतवाडी"
    # "भवरापुर"
    # "भावडी"
    # "भिलारेवाडी" 
    # "भोसरी" 
    # "म .कर्वेनगर" 
    # "मणेरवाडी" 
    # "महंमदवाडी" 
    # "मामुर्डी" 
    # "मालखेड" 
    # "माळीनगर" 
    # "मांगडेवाडी" 
    # "मांजरी खुर्द" 
    # "मांजरी बु." 
    # "मांडवी खुर्द"
    # "मांडवी बुद्रुक" 
    # "मुरकुटे नगर" 
    # "मोकरवाडी" 
    # "मोगरवाडी" 
    # "मोरदरवाडी" 
    # "मोशी" 
    # "येवलेवाडी" 
    # "रहाटणी" 
    # "रहाटवडे" 
    # "रावेत" 
    # "लोणी काळभोर" 
    # "लोणीकंद" 
    # "लोहगाव" 
    # "वडकी" 
    # "वडगाव बु।।" 
    # "वडगाव शिंदे" 
    # "वडगाव शेरी" 
    # "वडगांव खुर्द" 
    # "वडदरे" 
    # "वडमुखवाडी" 
    # "वडाची वाडी" 
    # "वढु खुर्द" 
    # "वळती" 
    # "वाघोली" 
    # "वाडे बोल्हाई" 
    # "वारजे" 
    # "वांजळेवाडी" 
    # "विठ्ठलनगर" 
    # "शिवणे" 
    # "शिंदवणे" 
    # "शिंदेवाडी" 
    # "शेवाळवाडी" 
    # "श्रीप्रयागधाम" 
    # "सणस नगर" 
    # "साष्टे" 
    # "सांगरुण" 
    # "सांगवी सांडस" 
    # "सांगवी हवेली" 
    # "सांबरेवाडी" 
    # "सिरसवडी" 
    # "सुतारवाडी" 
    # "सोनापुर" 
    # "सोरतापवाडी" 
    # "हडपसर" 
    # "हिंगणगाव" 
    # "हिंगणे खुर्द" 
    # "होळकरवाडी" 
    }
webScrape(Division,District,Taluka,Village)
driver.quit()

time.sleep(5)