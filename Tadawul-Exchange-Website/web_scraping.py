import requests
from bs4 import BeautifulSoup

# Add user agent to the request
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:132.0) Gecko/20100101 Firefox/132.0"
}
url = 'https://www.saudiexchange.sa/wps/portal/saudiexchange/newsandreports/reports-publications/annual-reports?locale=en'


# Making a GET request
response = requests.get(url=url, headers=headers)



# Parsing the HTML
soup = BeautifulSoup(response.content, 'html.parser')


for a in soup.find_all('a', href=True):
    print(a['href'])


