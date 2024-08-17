# Test 1 Link: https://ia800100.us.archive.org/28/items/test-image-1-for-download-list/Test.png

# import modules
from os.path import exists
import json
import shutil
import time
import os
import sys


# defines colors to be used
class Colors:
    red = '\033[31m'
    clear = '\033[0m'


# defines the prefixes for messages
class Pre:
    info = f'[ \033[94m INFO  \033[0m ] '
    success = f'[ \033[32mSUCCESS\033[0m ] '
    warning = f'[ \033[93mWARNING\033[0m ] '
    error = f'[ \033[31m ERROR \033[0m ] '


is_axel_installed = shutil.which("axel")
print(Pre.info + is_axel_installed)


if is_axel_installed is None:
    print(Pre.error + "Axel is not installed.")
    print(Pre.info + 'Exiting...')
    sys.exit()

print(Pre.info + 'Axel is installed.')

does_json_file_exist = exists('dl_list.json')

if does_json_file_exist is True:
    print(Pre.info + 'dl_list.json exists')

elif does_json_file_exist is False:
    print(Pre.warning + 'dl_list.json does not exist, creating...')
    with open('dl_list.json', 'w') as file:
        file.write('')

    print(Pre.info + 'Created file...')
    file_creation_success = exists('dl_list.json')

    if file_creation_success is True:
        print(Pre.success + 'Created file successfully')

    elif file_creation_success is False:
        print(Pre.error + 'Failed to create file')
        print(Pre.info + 'Exiting...')
        sys.exit()

version = '1.1.0'

# print opening message
print('Download List v' + version)

# opens the download list file
with open('dl_list.json', 'r') as dllist:
    dl_list = json.load(dllist)

# prints the download list
print('')
print(dl_list)
print('')

dll_int = int(dl_list['dll'])
dllstr = dl_list['dll']
currdl = 1

time.sleep(0.5)
prompt = True

# main downloader and command prompt
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

    if user_input == 'exit' or user_input == 'kill':
        print(Pre.info + 'Exiting...')
        sys.exit()
