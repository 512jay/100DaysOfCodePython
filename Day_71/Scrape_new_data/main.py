import csv
import requests
from bs4 import BeautifulSoup

url1 = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"

response = requests.get(url1)
data = response.text
soup = BeautifulSoup(data, 'html.parser')


majors = soup.find_all('span', class_="data-table__value")
rows, row = [], []
count = 0
for major in majors:
    row.append(major.text)
    count += 1
    if count % 6 == 0:
        rows.append(row)
        row = []
        count = 0


categories = ["Rank", "Major", "Degree", "Start", "Mid", "Spread"]
with open('eggs.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(categories)
    writer.writerows(rows)
