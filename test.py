#!/usr/bin/env python
# coding: utf-8
# Created on: 09.02.2016
# Author: Roman Miroshnychenko aka Roman V.M.
# E-mail: romanvm@yandex.ua

from selenium.webdriver import Chrome, ChromeOptions


def test_headless_chrome():
    print('Starting Headless Chrome test...')
    options = ChromeOptions()
    options.add_argument('headless')
    options.add_argument('disable-gpu')
    # options.add_argument('remote-debugging-port=9222')
    browser = Chrome(chrome_options=options)
    browser.get('http://example.com/')
    h1 = browser.find_element_by_tag_name('h1')
    assert h1.text == 'Example Domain'
    print('Test passed OK')


if __name__ == '__main__':
    test_headless_chrome()
