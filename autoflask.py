import pyautogui as page
import time


def autogrind():
    try:
        while True:
            marble_loc = page.locateOnScreen('resources/marble.png', confidence=0.9)
            page.moveTo(page.center(marble_loc))
            # Click inside crowfall
            page.mouseDown(button='left')
            page.mouseUp(button='left')

            page.mouseDown(button='right')
            page.mouseUp(button='right')

            # Click Assemble
            assemble_loc = page.locateOnScreen('resources/assemble.png', confidence=0.9)
            page.moveTo(page.center(assemble_loc))
            page.mouseDown(button='left')
            page.mouseUp(button='left')
            time.sleep(1)

            # Click Make Item
            make_loc = page.locateOnScreen('resources/make_item.png', confidence=0.9)
            page.moveTo(page.center(make_loc))
            page.mouseDown(button='left')
            page.mouseUp(button='left')
            time.sleep(1)

            # Click Take Item
            take_loc = page.locateOnScreen('resources/take.png', confidence=0.9)
            page.moveTo(page.center(take_loc))
            page.mouseDown(button='left')
            page.mouseUp(button='left')
            time.sleep(1)
    except Exception:
        pass


def autoflask():
    try:
        while True:
            # Click Powder
            powder_loc = page.locateOnScreen('resources/powder.png', confidence=0.9)
            page.moveTo(page.center(powder_loc))

            # Click inside crowfall first
            page.mouseDown()
            page.mouseUp()

            page.mouseDown(button='right')
            page.mouseUp(button='right')

            page.mouseDown(button='right')
            page.mouseUp(button='right')

            # Click Dust
            dust_loc = page.locateOnScreen('resources/dust.png', confidence=0.9)
            page.moveTo(page.center(dust_loc))
            page.mouseDown(button='right')
            page.mouseUp(button='right')

            # Click Assemble
            assemble_loc = page.locateOnScreen('resources/assemble.png', confidence=0.9)
            page.moveTo(page.center(assemble_loc))
            page.mouseDown(button='left')
            page.mouseUp(button='left')
            time.sleep(1)

            # Click Make Item
            make_loc = page.locateOnScreen('resources/make_item.png', confidence=0.9)
            page.moveTo(page.center(make_loc))
            page.mouseDown(button='left')
            page.mouseUp(button='left')
            time.sleep(1)

            # Click Take Item
            take_loc = page.locateOnScreen('resources/take.png', confidence=0.9)
            page.moveTo(page.center(take_loc))
            page.mouseDown(button='left')
            page.mouseUp(button='left')
            time.sleep(1)
    except Exception:
        pass


if __name__ == '__main__':
    autogrind()
    autoflask()
