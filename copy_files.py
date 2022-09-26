import os
import shutil
from termcolor import colored

print(colored('Welcome to my search program.', 'green', attrs=['bold']))
source_dir = input('Please wright here the source folder: ')
target_dir = input('Please wright here the destination folder: ')
print('\n')
print(colored('Now, please insert file extension that you want to find. For example', 'green'), '.pdf')
file_type = input('Please wright here the file extinction: ')
print('###############################################################')
for root, dirs, files in os.walk(source_dir):
    for file in files:
        if file.endswith(file_type):
            print(os.path.join(root, file))
print('###############################################################')

for path, subdirs, files in os.walk(source_dir):
    for file in files:
        if file.endswith(file_type):
            filename = os.path.join(path, file)
            shutil.copy2(filename, target_dir)

print(colored('List files in your target:', 'green'))
for root, dirs, files in os.walk(target_dir):
    for file in files:
        if file.endswith(file_type):
            print(os.path.join(root, file))
print('###############################################################')
print(colored('Finish', 'green', attrs=['bold']))
