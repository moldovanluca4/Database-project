import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np


df = pd.read_csv('statistics_access.csv', on_bad_lines='skip')


accesses_october = df[df['Timeline'].str.contains('/Oct/2025')].shape[0]
accesses_november = df[df['Timeline'].str.contains('/Nov/2025')].shape[0]

print(df.head())

plt.figure(figsize=(8, 6))
months = ['October 2025', 'November 2025']
counts = [accesses_october, accesses_november]
colors = ['#007ACC', '#FFA500']

plt.bar(months, counts, color=colors)
plt.title('Web Accesses per Month (Oct/Nov 2025)', fontsize=16)
plt.ylabel('Number of Accesses', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
for i, count in enumerate(counts):
    plt.text(i, count + 0.5, str(count), ha='center', va='bottom', fontsize=12, fontweight='bold')



browser_counts = df['Browser'].value_counts()
print(browser_counts)

plt.figure(figsize=(12, 8))
browser_counts.sort_values().plot(kind='barh', color='green')
plt.title('Browser Usage Distribution', fontsize=16)
plt.xlabel('Number of Accesses', fontsize=12)
plt.ylabel('Browser', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()



ip_counts = df['IP Address'].value_counts().head(10)
print(ip_counts)

plt.figure(figsize=(12, 7))
ip_counts.sort_values().plot(kind='barh', color='purple')
plt.title('Top 10 IP Addresses by Access Count', fontsize=16)
plt.xlabel('Number of Accesses', fontsize=12)
plt.ylabel('IP Address', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()


dif = pd.read_csv('statistics_error.csv', on_bad_lines='skip')

dif['Timestamp'] = pd.to_datetime(dif['Timeline'], format='%a %b %d %H:%M:%S.%f %Y', errors='coerce')

dif = dif.dropna(subset=['Timestamp']).sort_values(by='Timestamp')

if not dif.empty:
    plt.figure(figsize=(12, 8))
    
    (markerline, stemlines, _) = plt.stem(dif['Timestamp'], [0] * len(dif), orientation='horizontal', basefmt=' ')
    plt.setp(markerline, 'marker', 'o', 'color', 'red', 'markersize', 8, 'zorder', 3)
    plt.setp(stemlines, 'color', 'darkgray', 'linestyle', ':', 'linewidth', 1.5)

    for _, row in dif.iterrows():
        message_summary = row['Error Message'].split(':')[0].strip()
        
        label = f"{row['IP Address']} | {message_summary}"
        
        plt.text(row['Timestamp'], 0.015, label, va='center', ha='left', fontsize=9, alpha=0.9)

    plt.title('Error Timeline: Originator (IP), Error Summary, and Time', fontsize=16, pad=15)
    
    ax = plt.gca()
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d %H:%M'))
    plt.xticks(rotation=30, ha='right')
    ax.yaxis.set_visible(False)
    ax.spines[['left', 'top', 'right']].set_visible(False)
    plt.grid(axis='x', linestyle='--', alpha=0.4)
    plt.tight_layout()
else:
    print("No valid timestamps found in error data for plotting.")
    
plt.show()