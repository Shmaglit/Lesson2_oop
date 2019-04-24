import re
from bs4 import BeautifulSoup as BS


with open('Geekbrains.htm', encoding='utf-8') as f:
    s = f.read()

#с помощью регулярных выражений
list1 =re.findall('<span class=\"total-users\">([^>]+)</span>', s)
print(list1)

#с помощью BS4
soup = BS(s, 'html.parser')
list2 = soup.find_all('span', class_='total-users')[0].get_text()
print(list2)

