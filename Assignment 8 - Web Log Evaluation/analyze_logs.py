import csv
import re

path_to_log_files = "/var/log/apache2/access_log"
path_to_error_log_files = "/var/log/apache2/error_log"


csv_file_access_logs = open('statistics_access.csv', 'wb')
writer = csv.writer(csv_file_access_logs, quoting=csv.QUOTE_ALL)
writer.writerow(['IP Address', 'Timeline','Page Accessed','Browser'])

csv_file_error_logs = open('statistics_error.csv', 'wb')
writer_error = csv.writer(csv_file_error_logs, quoting=csv.QUOTE_ALL)
writer_error.writerow(['IP Address', 'Timeline','Error Message'])

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


with open(path_to_error_log_files, 'r') as error_log_file:
    for line in error_log_file:
        if '/home/lmoldovan/public_html/The-flask-app' in line:
            match_error = re.search(r'\[(.*?)\] \[.*?\] \[client (.*?)\] (.*)', line)
            if match_error:
                timeline_error = match_error.group(1)
                ip_address_error = match_error.group(2)
                error_message = match_error.group(3)
                writer_error.writerow([ip_address_error, timeline_error, error_message])
            else:
                match_error_alt = re.search(r'\[(.*?)\] \[.*?\] (.*)', line)
                if match_error_alt:
                    timeline_error = match_error_alt.group(1)
                    error_message = match_error_alt.group(2)
                    writer_error.writerow(['N/A', timeline_error, error_message])