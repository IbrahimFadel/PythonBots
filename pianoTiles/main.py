import pyautogui
from PIL import ImageGrab
import sys

pyautogui.FAILSAFE = True

pyautogui.click(100, 200)

while True:
	try:
		img = ImageGrab.grab()
		px = img.load()	
		left = px.__getitem__((570, 601))
		leftMid = px.__getitem__((670, 601))
		rightMid = px.__getitem__((770, 601))
		right = px.__getitem__((870, 601))

		if left == (17, 17, 17, 255):
			pyautogui.click(570, 601)
		elif leftMid == (17, 17, 17, 255):
			pyautogui.click(670, 601)
		elif rightMid == (17, 17, 17, 255):
			pyautogui.click(770, 601)
		elif right == (17, 17, 17, 255):
			pyautogui.click(870, 601)
	except pyautogui.FailSafeException:
		sys.exit()