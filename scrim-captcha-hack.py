#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: sahildua2305
# @Date:   2016-01-25 20:21:45
# @Last Modified by:   sahildua2305
# @Last Modified time: 2016-01-25 21:17:57


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from time import sleep
import unittest


SCRIM_URL = "http://scr.im/fake"


"""
sub-class of unittest.TestCase for testing the automated hack

https://docs.python.org/2/library/unittest.html#unittest.TestCase
"""
class HackTest(unittest.TestCase):

	"""
	Instructions that will be executed before the test case
	
	https://docs.python.org/2/library/unittest.html#unittest.TestCase.setUp
	"""
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.get(SCRIM_URL)

	"""
	Main method that will be executed and tested
	"""
	def test_hack_captcha(self):
		driver = self.driver

		# find all the options available for captcha
		optionsXPath = "(//ul//li)"
		options = WebDriverWait(driver, 20).until(lambda driver: driver.find_elements(By.XPATH, optionsXPath))
		print "%d total captcha options found!" % len(options)

		while True:

			# randomly select any option
			# Intentionally chosen the middle one to increase probability of getting email as soon as possible
			selectedOption = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(optionsXPath+"[5]"))
			selectedOption.click()

			try:
				# check if email has been revealed
				emailElementId = "mailto"
				emailElement = WebDriverWait(driver, 2).until(lambda driver: driver.find_element_by_id(emailElementId))

			except TimeoutException:
				# if email isn't revealed, let it try again
				print "Email not found!"
				pass

			else:
				# reveal email
				emailId = emailElement.get_attribute("innerHTML")
				print emailId
				break

			# Find try again button and click, if email hasn't been already revealed
			tryAgainButtonText = "try again"
			tryAgainButton = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_link_text(tryAgainButtonText))
			tryAgainButton.click()

	"""
	Instructions that will be executed after the test case

	https://docs.python.org/2/library/unittest.html#unittest.TestCase.tearDown
	"""
	def tearDown(self):
		sleep(2)
		self.driver.quit()


# run all the unit test cases written
unittest.main()
