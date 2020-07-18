# Python Project

# Title : Advanced ScreenShot Program
# Date : 2020-07-18
# Creator : tunealog

import time
import keyboard
from PIL import ImageGrab

# Check : MacOs Catalina -> Segmentation fault: 11
# Go to Settings -> Security and Privacy -> Privacy Tab -> Accessibility
# And finally check your terminal


def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))


keyboard.add_hotkey("a", screenshot)

keyboard.wait("esc")
