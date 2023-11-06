from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#import fake_useragent
from selenium.webdriver.chrome.options import Options
import random
from time import sleep
from multiprocessing import Pool


options = Options()
#options.add_argument(f'UserAgent = {fake_useragent.UserAgent().random}')
options.add_extension('23.10.16.1_0.crx')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)


def sui_flip(dat):
    try:
        sleep(10)
        sui_window = driver.window_handles[2]
        driver.switch_to.window(sui_window)
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[1]/div[4]/a').click()
        driver.implicitly_wait(10)
        driver.find_element(by=By.XPATH, value='//*[@id="overlay-portal-container"]/div/div[2]/div/section[2]/a[1]').click()
        driver.implicitly_wait(10)
        for i in range(0,12):
            driver.find_element(by=By.XPATH, value=f'//*[@id="recoveryPhrase.{i}"]').send_keys(dat[i])
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[1]/div[3]/form/div[2]/div/button[2]').click()
        for i in range(1,3):
            driver.find_element(by=By.XPATH, value=f'//*[@id="root"]/div/div[1]/div[3]/form/div[{i}]/label/div[2]/input').send_keys(dat[12])
        driver.find_element(by=By.XPATH, value='//*[@id="acceptedTos"]').click()
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[1]/div[3]/form/div[5]/div[2]/button[2]').click()
        driver.implicitly_wait(10)
        driver.get('https://desuicoinflip.io')
        driver.implicitly_wait(10)
        driver.find_element(by=By.XPATH, value='/html/body/div[4]/div/div/div/div/div/a/button').click()
        driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div[1]/main/main/div/div[1]/button').click()
        driver.find_element(by=By.XPATH, value='//*[@id="radix-:Rsl36:"]/div/div[2]/div/div[2]').click()
        sleep(2)
        sui_valid = driver.window_handles[3]
        flip_window = driver.window_handles[2]
        driver.switch_to.window(sui_valid)
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[1]/div/div/main/div/div[2]/div/button[2]').click()
        driver.switch_to.window(flip_window)
        for i in range(300):
            i = random.randint(1,2)
            driver.find_element(by=By.XPATH, value=f'//*[@id="__next"]/div[1]/main/div/div/div/div[2]/div[1]/button[{i}]').click()
            driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div[1]/main/div/div/div/div[2]/div[2]/button[1]').click()
            driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div[1]/main/div/div/div/div[3]').click()
            sleep(2)
            driver.switch_to.window(driver.window_handles[3])
            driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[1]/div/div/main/div/div[2]/div/button[2]').click()
    except Exception as err:
        print(err)
    finally:
        driver.close()
        driver.quit()


with open('psrf.txt') as f:
    str = f.read().split()

k = len(str)//13
pases = []
for i in range(1, k+1):
    if i == 1:
        pases.append(str[i-1:i*13])
    else:
        pases.append(str[(i-1)*13:i*13])


if __name__ == '__main__':
    with Pool(k) as p:
        p.map(sui_flip, pases)
