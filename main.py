import concurrent.futures
import pyautogui as pag
import time
import win32api


class KnightCombat:
    priorities = [9, 7, 5, 4, 6]
    previous_ability = None
    # Constant for triggering combos
    combo_color = (255, 255, 255)
    combo_location = (903, 572)
    block_slotted_color = (236, 197, 73)

    block_skill_position = (959, 528)
    dodge_skill_position = (963, 476)
    rmb_skill_position = (944, 799)
    block_slotted_position = (1136, 1091)

    def swap_dodge(self, skills_on_cd):
        if not skills_on_cd[11]:
            if pag.pixelMatchesColor(self.block_slotted_position[0],
                                     self.block_slotted_position[1], self.block_slotted_color):
                pag.press('k')
                pag.moveTo(self.dodge_skill_position)
                pag.dragTo(self.rmb_skill_position, duration=0.2, button='left')
                pag.press('esc')
            else:
                pag.press('k')
                pag.moveTo(self.block_skill_position)
                pag.dragTo(self.rmb_skill_position, duration=0.2, button='left')
                pag.press('esc')

    def run_combat(self, skills_on_cd):
        if pag.pixelMatchesColor(self.combo_location[0], self.combo_location[1], self.combo_color):
            if self.previous_ability:
                pag.press(str(self.previous_ability))
                return
        for priority in self.priorities:
            if not skills_on_cd[priority - 1]:
                if priority < 10:
                    pag.press(str(priority))
                elif priority == 10:
                    pag.press('0')
                self.previous_ability = priority
                return

        if self.previous_ability < 9:
            pag.press(str(self.previous_ability))
        elif self.previous_ability == 10:
            pag.press('0')


def process_skills() -> list:
    cooldown_list = list()
    cooldown_locations = [
        (537, 1063),  # 1 - Headbutt
        (592, 1063),  # 2 - Free Action
        (645, 1063),  # 3 - Pursuit
        (699, 1063),  # 4 - Retribution Strike
        (754, 1064),  # 5 - Dazzling Blades
        (808, 1063),  # 6 - Blood Strike
        (862, 1062),  # 7 - Retribution Strike
        (916, 1063),  # 8 - Chain
        (969, 1063),  # 9 - Shield Swipe
        (1023, 1063),  # 0 - Gestault
        (1099, 1063),  # LMB - Basic Attack
        (1154, 1063)  # RMB - Dodge / Block
    ]

    deactivated_locations = [
        (518, 1089),  # 1 - Headbutt
        (574, 1087),  # 2 - Free Action
        (628, 1090),  # 3 - Pursuit
        (684, 1090),  # 4 - Blood Strike
        (735, 1089),  # 5 - Dazzling Blades
        (789, 1098),  # 6 - Retribution Strike
        (846, 1095),  # 7 - Noble Blood
        (898, 1091),  # 8 - Chain
        (954, 1083),  # 9 - Shield Swipe
        (1005, 1089),  # 0 - Gestault
        (1091, 1076),  # LMB - Basic Attack
        (1137, 1089)  # RMB - Blockw
    ]

    timer_1_locations = [
        None,  # - Unused
        None,  # 2 - Shield Swipe
        None,  # - Unused
        (688, 1138),  # 4 - Noble Blood
        None,  # - Unused
        (850, 1138),  # 6 - Blood Strike
        None,  # - Unused
        None,  # - Unused
        (958, 1138),  # - Unused
        None,  # - Unused
        None,  # - Unused
        None  # - Unused
    ]

    timer_2_locations = [
        None,  # - Unused
        None,  # - Unused
        None,  # - Unused
        None,  # - Unused
        None,  # - Unused
        (796, 1162),  # 6 - Blood Strike
        None,  # - Unused
        None,  # - Unused
        None,  # - Unused
        None,  # - Unused
        None,  # - Unused
        None  # - Unused
    ]

    # Constant for the blue color on the cooldown arrow
    cooldown_color = (134, 153, 179)
    # (125, 142, 166)
    # Constant for gray border around skill
    deactivated_color = (107, 107, 107)
    # Constant for red arrow on timer 1 CD
    timer_1_color = (171, 28, 22)
    # Constant for yellow arrow on timer 2 CD
    timer_2_color = (255, 154, 0)

    # Optimize checking only things that are needed
    cooldown_checks = [9, 7, 5, 4, 6, 12]
    deactivated_checks = []
    timer_1_checks = [9, 6, 4]
    timer_2_checks = [6]

    for skill in range(1, 13):
        skill_on_cd = False
        if not skill_on_cd and skill in timer_2_checks:
            if pag.pixelMatchesColor(timer_2_locations[skill - 1][0], timer_2_locations[skill - 1][1], timer_2_color,
                                     tolerance=5):
                skill_on_cd = True
        if not skill_on_cd and skill in timer_1_checks:
            if pag.pixelMatchesColor(timer_1_locations[skill - 1][0], timer_1_locations[skill - 1][1], timer_1_color,
                                     tolerance=5):
                skill_on_cd = True
        if not skill_on_cd and skill in cooldown_checks:
            if pag.pixelMatchesColor(cooldown_locations[skill - 1][0], cooldown_locations[skill - 1][1],
                                     cooldown_color, tolerance=5):
                skill_on_cd = True
        if not skill_on_cd and skill in deactivated_checks:
            if pag.pixelMatchesColor(deactivated_locations[skill - 1][0], deactivated_locations[skill - 1][1],
                                     deactivated_color, tolerance=5):
                skill_on_cd = True

        cooldown_list.append(skill_on_cd)

    return cooldown_list


if __name__ == '__main__':
    # Read in the skills from the resource directory

    combat = KnightCombat()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        while True:
            start = time.perf_counter()
            # If Caps Lock is pressed
            # if win32api.GetKeyState(0x14) < 0:
            #     skills_available = executor.submit(process_skills)
            #     combat.swap_dodge(skills_available.result())
            # If Mouse 4 is pressed
            if win32api.GetKeyState(0x05) < 0:
                skills_available = executor.submit(process_skills)
                combat.run_combat(skills_available.result())
            end = time.perf_counter()
            time.sleep(0.05)
