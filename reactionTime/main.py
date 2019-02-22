import pyautogui
from PIL import ImageGrab
import sys
import time

bbox = (645, 210, 646, 211)

pyautogui.click(300, 300)

while True:
	try:
		img = ImageGrab.grab(bbox=bbox)
		pixels = img.getdata()
		width, height = img.size
		for x in range(width):
			for y in range(height):
				if img.getpixel((x, y)) == (0, 232, 107, 255):
					pyautogui.click(645 + x, 210 + y)
					print("hi")
					time.sleep(2)



	except (pyautogui.FailSafeException, KeyboardInterrupt):
		sys.exit()