import pyautogui
from PIL import ImageGrab
import sys
import time

pyautogui.FAILSAFE = True

pyautogui.click(100, 200)
pyautogui.click(550, 730)
bbox = (70, 215, 1030, 896)
count = 0

while True:
	try:
		img = ImageGrab.grab(bbox=bbox)
		if img.getpixel((547-70, 704-215)) == (0, 123, 121, 255):
			for i in range(2):
				pyautogui.click(547, 704)
		elif img.getpixel((546-70, 722-215)) == (0, 123, 121, 255):
			for i in range(2):
				pyautogui.click(546, 722)
		else:
			for i in range(50):
				pyautogui.click(810, 583)

		count += 1

		if count == 10:
			if img.getpixel((482 -70, 680-215)) == (0, 255, 255, 255):
				for i in range(10):
					pyautogui.click(482, 602)
			if img.getpixel((482 -70, 602-215)) == (0, 255, 255, 255):
				for i in range(10):
					pyautogui.click(482, 602)
			if img.getpixel((482 -70, 520-215)) == (0, 255, 255, 255):
				for i in range(10):
					pyautogui.click(482, 520)
			if img.getpixel((482 -70, 440-215)) == (0, 255, 255, 255):
				for i in range(10):
					pyautogui.click(482, 440)
			if img.getpixel((483 -70, 363-215)) == (0, 255, 255, 255):
				for i in range(10):
					pyautogui.click(482, 363)
			count = 0
	except pyautogui.FailSafeException:
		sys.exit()