import pyautogui
import time
import win32api


def find_location():
    while True:
        location = pyautogui.position()
        print(location)
        print(get_color_at_location(location))
        time.sleep(1)


def get_color_at_location(location):
    return pyautogui.pixel(location[0], location[1])


find_location()
# while (True):
#     print(get_color_at_location((903, 572)))
#     time.sleep(1)

# while (True):
#     a = win32api.GetKeyState(0x05)
#     print(a)
#     time.sleep(1)

# (518, 1089) (117, 117, 117)
# (574, 1090) (107, 107, 107)
# (628, 1090) (107, 107, 107)
# (684, 1090) (107, 107, 107)
# (735, 1089)
# (789, 1098)
# (846, 1095)
# (898, 1091)
# (970, 1099)
# (1005, 1089)
