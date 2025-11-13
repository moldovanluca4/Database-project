import pandas as pd
import matplotlib.pyplot as plt
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


plt.show()