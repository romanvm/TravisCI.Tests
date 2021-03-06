#!/usr/bin/env python
# coding: utf-8
# Created on: 09.02.2016
# Author: Roman Miroshnychenko aka Roman V.M.
# E-mail: romanvm@yandex.ua

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def test_headless_chrome():
    print('Starting Headless Chrome test...')
    capabilities = DesiredCapabilities.CHROME
    capabilities['loggingPrefs'] = {'browser': 'ALL'}
    options = ChromeOptions()
    options.add_argument('headless')
    options.add_argument('disable-gpu')
    browser = Chrome(chrome_options=options, desired_capabilities=capabilities)
    browser.get('http://example.com/')
    h1 = browser.find_element_by_tag_name('h1')
    print(h1.text)
    assert h1.text == 'Example Domain'
    print('Test passed OK')


if __name__ == '__main__':
    test_headless_chrome()
