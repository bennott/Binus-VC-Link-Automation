from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import yaml
import time as tm

def wait(x):
    tm.sleep(x)

config = yaml.load(open('login.yml'))
binusUsername = config['binusUser']['username']
binusPassword = config['binusUser']['password']

driver = webdriver.Chrome(executable_path="C:\\Users\\Bennett\\OneDrive\\Desktop\\Bennett\\Work\\VSCode\\3rd-Party\\chromedriver.exe")
driver.get("https://myclass.apps.binus.ac.id/Auth")

def login(usernameId, username, passwordId, password, submitButtonId):
    driver.find_element_by_id(usernameId).send_keys(username)
    wait(0.5)
    driver.find_element_by_id(passwordId).send_keys(password)
    wait(0.5)
    driver.find_element_by_id(submitButtonId).click()
    wait(5)

wait(2)
login("Username", binusUsername, "Password", binusPassword, "btnSubmit")

driver.get("https://myclass.apps.binus.ac.id/Home/Index")
    
wait(2)
temp = driver.find_elements_by_class_name("iDate.not-center")
dates = []
for element in temp:
    if len(element.text) > 0:
        dates.append(element.text)

wait(2)
temp = driver.find_elements_by_class_name("iTime")
times = []
for element in temp:
    if len(element.text) > 0:
        times.append(element.text)

wait(2)
temp = driver.find_elements_by_class_name("iCourse.not-center")
courses = []
for element in temp:
    if len(element.text) > 0:
        courses.append(element.text)

wait(2)
temp = driver.find_elements_by_class_name("iAction")
links = []
for element in temp:
    properties = element.find_elements_by_tag_name("a")
    for property in properties:
        links.append(property.get_attribute("href"))

index = 0
while index < len(dates):
    print("Date\t: " + dates[index])
    print("Time\t: " + times[index])
    print("Course\t: " + courses[index])
    if index < len(links):
        print("Link\t: " + links[index])
    else:
        print("GSLC")
    print("")
    index+=1

wait(2)
driver.quit()