# used to map midi controllers

from pygame import midi
import pyautogui


midi.init()
# print('Output ID', midi.get_default_output_id())
# print('Input ID', midi.get_default_input_id())
# for i in range(0, midi.get_count()): print(i, midi.get_device_info(i))
input = midi.Input(midi.get_default_input_id())
print('midi-numpad enabled')


try:
    while True:
        if input.poll():
            e = input.read(num_events=16)
            if e[0][0][0]==146: # down press (130 release)
                if e[0][0][1]==37: pyautogui.keyDown('0')
                if e[0][0][1]==40: pyautogui.keyDown('1')
                if e[0][0][1]==41: pyautogui.keyDown('2')
                if e[0][0][1]==42: pyautogui.keyDown('3')
                if e[0][0][1]==44: pyautogui.keyDown('4')
                if e[0][0][1]==45: pyautogui.keyDown('5')
                if e[0][0][1]==46: pyautogui.keyDown('6')
                if e[0][0][1]==48: pyautogui.keyDown('7')
                if e[0][0][1]==49: pyautogui.keyDown('8')
                if e[0][0][1]==50: pyautogui.keyDown('9')

                if e[0][0][1]==38: pyautogui.keyDown('.')
                if e[0][0][1]==39: pyautogui.keyDown('enter')

except KeyboardInterrupt as err:
    print("Stopping...")

midi.quit()