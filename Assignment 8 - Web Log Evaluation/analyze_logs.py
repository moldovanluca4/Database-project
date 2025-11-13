import csv
import re

path_to_log_files = "/var/log/apache2/access_log"

csv_file = open('statistics.csv', 'wb')
writer = csv.writer(csv_file)
writer.writerow(['IP Address', 'Timeline','Page Accessed','Browser'])

with open(path_to_log_files, 'r') as log_file:
    for line in log_file:
        if 'http://10.60.36.1/~lmoldovan/' in line:
            match = re.search(r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(\S+ (\S+) \S+)" \d+ \S+ ".*?" "(.*?)" "(.*?)"', line)
            if match:
                ip_address = match.group(1)
                timeline = match.group(2)
                page_accessed = match.group(4)
                browser = match.group(6)
                writer.writerow([ip_address, timeline, page_accessed,browser])