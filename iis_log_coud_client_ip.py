import os.path
import smtplib
from email.message import EmailMessage
from tabulate import tabulate

log_file_name = "_filename_.log"

if not os.path.isfile(log_file_name):
    print('###################################################################')
    print("# Log file not founded. Please add log file to project directory. #")
    print('###################################################################')
    exit()

# Read block 11 values and sort them
with open(log_file_name, "r", encoding="utf-8") as file:
    block11_list = []
    for line in file:
        blocks = line.split(" ")
        block11_list.append(blocks[10])
    sorted_block11_list = sorted(block11_list)

# Write sorted block 11 values to output file
with open("output.txt", "w") as output_file:
    for block11 in sorted_block11_list:
        output_file.write(block11 + "\n")

# Count occurrences of each block 11 value in output file
count_dict = {}
with open("output.txt", "r") as input_file:
    for line in input_file:
        block11 = line.strip()
        count_dict[block11] = count_dict.get(block11, 0) + 1

# Create table of block 11 values and counts
table = []
for block11, count in count_dict.items():
    if block11 != "10.217.0.1" and count > 1000:
        table.append([block11, count])

# Print and send email with table
headers = ["IP", "Count"]
print(tabulate(table, headers=headers))

# Write block 11 values and counts to temp file
with open("temp.txt", "w") as temp_file:
    temp_file.write(tabulate(table, headers=headers))

# Send email with output file attached
msg = EmailMessage()
msg['From'] = 'FROM@DOMAIN.COM'
msg['To'] = 'TO@DOMAIN.COM'
msg['Subject'] = 'IIS log IP count'

with open('temp.txt', 'r') as f:
    file_data = f.read()

msg.set_content(file_data)

with smtplib.SMTP('X.X.X.X') as smtp:
    smtp.send_message(msg)
###############################################################################
