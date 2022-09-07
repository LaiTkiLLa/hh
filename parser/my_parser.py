from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36")

driver = webdriver.Chrome(
    executable_path="C:\\Program Files\\Selenium\\chromedriver.exe",
    options = options
)


try:
    driver.get('https://prodavay.sel-be.ru/core?signin')
    time.sleep(5)

    name = driver.find_element(By.NAME,"username")
    name.clear()
    name.send_keys('m.strelchuk@solber.ru')
    time.sleep(0.3)

    password = driver.find_element(By.NAME,'password')
    password.clear()
    password.send_keys('jXi23uh(A*E29')
    time.sleep(0.3)
    password.send_keys(Keys.ENTER)
    time.sleep(5)

    trade = driver.get('https://prodavay.sel-be.ru/core/supplier/registry#?category=100&category=39322&category=39323&category=39324&category=39325&category=44924')
    time.sleep(10)

    SCROLL_PAUSE_TIME = 10

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height




    companies_href = driver.find_elements(By.CSS_SELECTOR,'.medium span a')
    companies_name = driver.find_elements(By.CSS_SELECTOR, '.medium span a')
    for company_name in companies_name:
        info_1 = company_name.text
        print(company_name.text)
    for company_href in companies_href:
        print(company_href.get_attribute('href'))
        info_2 = company_href.get_attribute('href')






except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


