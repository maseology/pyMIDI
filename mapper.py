# used to map midi controllers

from pygame import midi


midi.init()
print('Output ID', midi.get_default_output_id())
print('Input ID', midi.get_default_input_id())

for i in range(0, midi.get_count()): print(i, midi.get_device_info(i))

input = midi.Input(midi.get_default_input_id()) # midi.Input(3)

print('online')


try:
    while True:
        if input.poll():
            e = input.read(num_events=16)
            print(e)
            # if e[0][0][0]==146: # down press (130 release)
            #     if e[0][0][1]==37:
            #         print('zero')
except KeyboardInterrupt as err:
    print("Stopping...")

midi.quit()