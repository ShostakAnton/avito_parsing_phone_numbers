from selenium import webdriver
from time import sleep
from PIL import Image  # библиотека для работы с изображениями
from pytesseract import image_to_string
import base64


class Bot:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.navigate()

    def take_screenshot(self):
        self.driver.save_screenshot('avito_screenshot.png')

    def tel_recon(self):
        image = Image.open('tel.gif')
        print(image_to_string(image))

    def crop(self, location, size):
        x = location['x']
        y = location['y']
        width = size['width']
        height = size['height']

        image = Image.open('avito_screenshot.png')
        image.crop((x, y, x + width, y + height)).save('tel.gif')

        self.tel_recon()

    def navigate(self):
        self.driver.get('https://www.avito.ru/moskva/telefony/htc_sensation_z710e_1843910601')

        button = self.driver.find_element_by_xpath(
            '//button[@class="button-button-2Fo5k button-size-l-3LVJf button-primary-1RhOG width-width-12-2VZLz"]')
        button.click()

        sleep(3)

        self.take_screenshot()

        image = self.driver.find_element_by_xpath('//img[@class="contacts-phone-3KtSI"]')

        location = image.location  # dict    {'x': 2343, 'y': 23423}
        size = image.size  # dict    {'width': 234, 'height': 234}

        self.crop(location, size)



def main():
    a = Bot()


if __name__ == '__main__':
    main()
