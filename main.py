from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from secrets import username, pw
import sys

class QueueBot:
    def __init__(self, username, pw, course_id, location, comment, wants_to_present):
        self.username = username
        self.pw = pw
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://queue.csc.kth.se/Queue/{}".format(course_id))
        sleep(1)
        # Login button
        self.driver.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/div[1]/div/div").click()
        sleep(2)
        self._log_in()
        sleep(2)
        self._join_queue(location, comment, wants_to_present)
        sleep(5)
    
    # Handle login after KTH auth redirect
    def _log_in(self):
        self.driver.find_element_by_xpath("//input[@id=\"username\"]")\
            .send_keys(self.username)
        self.driver.find_element_by_xpath("//input[@id=\"password\"]")\
            .send_keys(self.pw)
        self.driver.find_element_by_xpath("//input[@type=\"submit\" and @value=\"Logga in\"]").click()
    
    # Fill in form and join queue
    def _join_queue(self, location, comment, wants_to_present):
        self.driver.find_element_by_xpath("//input[@name=\"location\"]")\
            .send_keys(location)
        self.driver.find_element_by_xpath("//input[@name=\"comment\"]")\
            .send_keys(comment)
        radio_btns = self.driver.find_elements_by_xpath("//input[@type=\"radio\"]")
        radio_btns[wants_to_present].click()
        sleep(2)
        # Wait until Queue is open, timeout after 20 mins
        join_queue_btn = WebDriverWait(self.driver, 20*60).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"root\"]/div/div[2]/div[1]/div[4]")))
        join_queue_btn.click()


if(len(sys.argv) != 5):
    print("Run: python main.py <course_id> <location> <comment> <want to present = 1 or 0>")
    print("Eg:  python main.py Cprog zoom lab4 1")
    print("Note that <course_id> is case sensitive and has to match the actual queque name")
else:
    course_id, location, comment = sys.argv[1], sys.argv[2], sys.argv[3]
    wants_to_present = 1 if sys.argv[4] == '1' else 0
    queue_bot = QueueBot(username, pw, course_id, location, comment, wants_to_present)
