import glob
from colorama import *
init(autoreset=True)

# list all log files to be read
log_files = glob.glob('queries.log*')

# initialize an empty list to store extracted elements
elements_list = []

for log_file in log_files:
    with open(log_file, 'r') as f:
        # iterate through each line in the file
        for line in f:
            # split the line by spaces into an array
            elements = line.split()
            # extract the 8th element without any parentheses, colons, or other characters
            element = elements[7].strip('():')
            # split the element by '.' and add the resulting sub-elements to the list
            sub_elements = element.split('.')
            elements_list.extend(sub_elements)

# sort the list in ascending order
sorted_list = sorted(elements_list)

# write the sorted list to a text file
with open('output.txt', 'w') as f:
    for element in sorted_list:
        f.write(element + '\n')

################################################################################
# initialize a dictionary to store word counts
word_counts = {}

# open the output file for reading
with open('output.txt', 'r') as f:
    # iterate through each line in the file
    for line in f:
        # strip leading and trailing whitespace from the line
        line = line.strip()
        # exclude words "www", "com", and more...
        if line not in ['www', 'com', 'org', 'COM', 'CO', 'IL', 'Co', 'Il', '_autodiscover', '_dmarc', 'co', 'il', 'xn--4dbrk0ce']:
            # increment the count for the word in the dictionary
            if line in word_counts:
                word_counts[line] += 1
            else:
                word_counts[line] = 1

# print the words that appear more than 10000 times
for word, count in word_counts.items():
    if count > 10000:
        print('#########################################')
        print('#########################################')
        print(Style.BRIGHT + Fore.RED + "root domain name is: ", word)
        print(Fore.RED + "Count of access to this domain: ", count)
        print('#########################################')
        print('#########################################')
#
#
#
