from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

import os
import requests
import shutil


def download_chapters(base_path, urls: list):
    i = 1
    for n, url in enumerate(urls):
        driver.get(url)
        driver.minimize_window()

        if n == 0:
            title = driver.title[:20]
            path = os.path.join(base_path, title)
            if not os.path.exists(path):
                os.mkdir(path)
                print("Directory created")
                os.chdir(path)
            else:
                print("Path already exists")

        cur_page_numb = int(driver.find_element(By.CLASS_NAME, "current").text)
        max_page_numb = int(driver.find_element(By.CLASS_NAME, "num-pages").text)

        while cur_page_numb <= max_page_numb:
            img = driver.find_element(By.ID, "image-container").find_element(By.TAG_NAME, "img")
            img_src = img.get_attribute('src')
            page_name = str(i)

            # Generating the name for the page
            filename = page_name + '.jpg'
            # Downloading the Image
            request = requests.get(img_src, stream=True)
            if request.status_code == 200:
                with open(filename,'wb') as f:
                    shutil.copyfileobj(request.raw, f)
                print(f"Page {i} downloaded")
                i += 1

                if cur_page_numb == max_page_numb:
                    print("Download Complete")
                    break
                driver.find_element(By.CLASS_NAME, "next").click()
                cur_page_numb = int(driver.find_element(By.CLASS_NAME, "current").text)
            else:
                driver.refresh()
                continue
    else:
        driver.quit()


options = Options()
driver = webdriver.Firefox(options=options)

# safe images at this path
b_path = "C:\D\BILDER\Iwas\Bilder\Comics\Selenium"
link = [
    ""
]

download_chapters(b_path, link)





