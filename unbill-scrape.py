import csv
import requests
from BeautifulSoup import BeautifulSoup

url = "http://unbill.us/faq.html"
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('div', attrs={'id': 'accordion'})

list_of_rows = []
for container in table.findAll('div'):
    list_of_cells = []
    for rawTitle in container.findAll('div', attrs={'class': 'panel-heading'}):
        title = rawTitle.text[3:]
        list_of_cells.append(title)
    for rawAnswer in container.findAll('div', attrs={'role': 'tabpanel'}):
        answer = rawAnswer.text
        list_of_cells.append(answer)
    if list_of_cells:
        list_of_rows.append(list_of_cells)

outfile = open("./result.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Questin", "Answer"])
writer.writerows(list_of_rows)
