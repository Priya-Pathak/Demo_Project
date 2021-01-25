import requests
#import urllib2
import re
from bs4 import BeautifulSoup


html_page = requests.get("http://imgur.com")
# #page = requests.get("https://www.amazon.in/events/greatindiansale?ext_vrnc=hi&tag=googhydrabk-21&ascsubtag=_k_CjwKCAiAxp-ABhALEiwAXm6IyVxEEsg6-nyCVzhHOjbhCXbJ99UiPVe3cR2fqubVZtibSpNnat57zRoCyVUQAvD_BwE_k_&ext_vrnc=hi&gclid=CjwKCAiAxp-ABhALEiwAXm6IyVxEEsg6-nyCVzhHOjbhCXbJ99UiPVe3cR2fqubVZtibSpNnat57zRoCyVUQAvD_BwE")
# print(page.status_code)

# contents = page.content


# soup = BeautifulSoup(contents, 'html.parser')
# results = soup.find_all('img')

# for result in results :
#     if len(result.attrs) == 1 :
#         print(result)
# print('this is running')


# html_page = urllib2.urlopen("http://imgur.com")
soup = BeautifulSoup(html_page)

images = []

for img in soup.findAll('img'):
    images.append(img.get('src'))

print(images)