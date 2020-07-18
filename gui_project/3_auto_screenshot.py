# Python Project

# Title : ScreenShot Program
# Date : 2020-07-18
# Creator : tunealog

import time
from PIL import ImageGrab

# Wait 5seconds
time.sleep(5)

# Screen Capture
for i in range(1, 11):
    img = ImageGrab.grab()
    img.save("image{}.png".format(i))
    time.sleep(2)
