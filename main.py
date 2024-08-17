# Test 1 Link: https://ia800100.us.archive.org/28/items/test-image-1-for-download-list/Test.png

# import modules
import json
import time
import os
import sys

# print opening message
print('Download List v1.0.0')

#
with open('dl_list.json', 'r') as dllist:
    dl_list = json.load(dllist)

print('')
print(dl_list)
print('')

dll_int = int(dl_list['dll'])
dllstr = dl_list['dll']
currdl = 1
time.sleep(4)
prompt = True


while prompt is True:
    user_input = input(']')

    if user_input == 'run download':
        while not (currdl > dll_int):
            currdlstr = str(currdl)
            dl_link = dl_list['dl' + currdlstr]

            print('Download Link: ' + dl_link)
            print('Download ID: ' + currdlstr)

            os.system('axel ' + dl_link)

            currdl += 1
    if user_input == 'exit':
        sys.exit()
