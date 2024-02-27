import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

class RunFileOps:

    def __init__(self,url,chrome_driver_path):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
        self.driver.get(url)
       
    def load_folder(self,file_path):
        co_x = 0.82 * (self.driver.get_window_size().get("width"))
        co_y =  0.36 * (self.driver.get_window_size().get("height"))
        WebDriverWait(self.driver, timeout=22).until(EC.presence_of_element_located((By.XPATH, "//button[@title='Open a folder to start working (Ctrl+O)']")))
        self.driver.find_element(By.XPATH,"//button[@title='Open a folder to start working (Ctrl+O)']").click()
        time.sleep(0.5)
        pyautogui.typewrite(file_path)
        pyautogui.press('enter')
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.moveTo(co_x, co_y)
        time.sleep(1)
        pyautogui.click()
        try:
            WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located((By.XPATH,"//a[@title='Yes']")))
            self.driver.find_element(By.XPATH,"//a[@title='Yes']").click()
        except TimeoutException:
            pass    

    def new_file(self):
        #WebDriverWait(self.driver, timeout=30).until(EC.presence_of_element_located((By.XPATH, "//button[@title='Open a new untitled text file, notebook, or custom editor. (Ctrl+Alt+Windows+N)']")))
        action = ActionChains(self.driver)
        action.key_down(Keys.CONTROL).key_down("k").key_up("k").key_up(Keys.CONTROL).perform()
        time.sleep(0.5)
        action.key_down("n").perform()
    
    def remote_write_line(self,text):
        WebDriverWait(self.driver, timeout=30).until(EC.presence_of_element_located((By.XPATH, "//textarea")))
        action = ActionChains(self.driver)
        action.send_keys(text).perform()

    def save_file(self,file_name):
        co_x = 0.82 * (self.driver.get_window_size().get("width"))
        co_y =  0.36 * (self.driver.get_window_size().get("height"))
        action = ActionChains(self.driver)
        action.key_down(Keys.CONTROL).key_down('s').key_up(Keys.CONTROL).key_up('s').perform()
        time.sleep(0.5)
        pyautogui.typewrite(file_name)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.moveTo(co_x, co_y)
        time.sleep(1)
        pyautogui.click()

    def navigate_file(self,file_name):
        action = ActionChains(self.driver)
        try:
            WebDriverWait(self.driver, timeout=22).until(EC.presence_of_element_located((By.XPATH, f"//span[text()='{file_name}']")))
            click_file_name = self.driver.find_element(By.XPATH,f"//span[text()='{file_name}']")
            action.move_to_element(click_file_name).click().perform()
        except TimeoutException:
            print("No file found")
    
    def close_files(self):
        try:
            li = self.driver.find_elements(By.XPATH,"//a[@aria-label='Close (Ctrl+F4)']")
            for i in li:
                i.click()
        except TimeoutException:
            pass        
            
    #Keyboard actions

    def key_enter(self):
        action = ActionChains(self.driver)
        action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()    

class RunPythonProgram:

    def __init__(self,url,profile_path,profile_name,chrome_driver_path):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument(f"user-data-dir={profile_path}")
        options.add_argument(f"--profile-directory={profile_name}")
        self.driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
        self.driver.get(url)
        
    def remote_connect_folder(self,folder_name):
        action = ActionChains(self.driver)
        WebDriverWait(self.driver, timeout=22).until(EC.presence_of_element_located((By.XPATH, "//a[@aria-label='Remote Explorer']")))
        self.driver.find_element(By.XPATH,"//a[@aria-label='Explorer (Ctrl+Shift+E)']").click()
        self.driver.find_element(By.XPATH,"//a[@aria-label='Remote Explorer']").click()
        try:
            WebDriverWait(self.driver, timeout=22).until(EC.presence_of_element_located((By.XPATH, f"//span[text()='{folder_name}']")))
            click_host_name = self.driver.find_element(By.XPATH,f"//span[text()='{folder_name}']")
            action.move_to_element(click_host_name).click().perform()
            self.driver.switch_to.active_element
            self.driver.find_element(By.XPATH,"(//a[@aria-label='Connect in Current Window...'])[2]").click()
        except TimeoutException:
            print("No available hosts")

    def remote_new_file(self):
        action = ActionChains(self.driver)
        action.key_down(Keys.CONTROL).key_down("k").key_up("k").key_up(Keys.CONTROL).perform()
        time.sleep(1)
        action.key_down("n").perform()   

    def remote_write_line(self,one_line):
        action = ActionChains(self.driver)
        action.send_keys(one_line).perform()
        time.sleep(1)
        action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        time.sleep(1)

    def remote_save_file(self,remote_folder_name,file_name):
        action = ActionChains(self.driver)
        action.key_down(Keys.CONTROL).key_down('s').key_up(Keys.CONTROL).key_up('s').perform()
        time.sleep(1)
        ele = self.driver.find_element(By.XPATH,"(//input)[3]")
        ele.clear()
        ele.send_keys(r"C:/Users/incinerator/Desktop/"+remote_folder_name+"/"+file_name)
        time.sleep(1)
        action.move_to_element(self.driver.find_element(By.XPATH,"//a[text()='OK']")).click().perform()         

    def remote_open_terminal(self):
        action = ActionChains(self.driver)         
        action.key_down(Keys.CONTROL).key_down(Keys.SHIFT).key_down('`').key_up(Keys.CONTROL).key_up(Keys.SHIFT).key_up('`').perform()
    
    def remote_write_terminal(self,command,file_name):
        action = ActionChains(self.driver)
        terminal_btn = self.driver.find_element(By.XPATH,"//a[@aria-label ='Terminal (Ctrl+`)']")
        action.move_to_element(terminal_btn).click().perform()
        time.sleep(1)
        ele = self.driver.switch_to.active_element
        ele.click()
        ele.send_keys(command + " " + file_name)
        action.key_down(Keys.ENTER).perform()

    #Keyboard Actions
    def key_enter(self):
        action = ActionChains(self.driver)
        action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        time.sleep(1)
    
    def key_backspace(self):
        action = ActionChains(self.driver)
        action.key_down(Keys.BACKSPACE).key_up(Keys.BACKSPACE).perform()   
        time.sleep(1)