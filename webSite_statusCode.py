
import requests
#import urllib2
import re
from bs4 import BeautifulSoup


# page = requests.get("https://www.amazon.in/events/greatindiansale?ext_vrnc=hi&tag=googhydrabk-21&ascsubtag=_k_CjwKCAiAxp-ABhALEiwAXm6IyVxEEsg6-nyCVzhHOjbhCXbJ99UiPVe3cR2fqubVZtibSpNnat57zRoCyVUQAvD_BwE_k_&ext_vrnc=hi&gclid=CjwKCAiAxp-ABhALEiwAXm6IyVxEEsg6-nyCVzhHOjbhCXbJ99UiPVe3cR2fqubVZtibSpNnat57zRoCyVUQAvD_BwE")

# page = requests.get("https://www.amazon.com/")
# print(page.status_code)

# contents = page.content

# if page.status_code == 200:
#     print("Amazon allows web Scrapping")
#     print("Website allows webScrapping")
# else:
#     print("Amazon does not allow web Scrapping")


# page = requests.get("https://www.flipkart.com/")
# print(page.status_code)

# if page.status_code == 200:
#     print("Flipkart allows web Scrapping")
# else:
#     print("Flipkart does not allow web Scrapping")



# page = requests.get("https://www.snapdeal.com/")
# print(page.status_code)

# if page.status_code == 200:
#     print("Snapdeal allows web Scrapping")
# else:
#     print("Snapdeal does not allow web Scrapping")



# page = requests.get("https://paytm.com/shop/h/home")
# print(page.status_code)

# if page.status_code == 200:
#     print("Paytm allows web Scrapping")
# else:
#     print("Paytm does not allow web Scrapping")

# page = requests.get("https://www.ebay.com/")
# print(page.status_code)

# if page.status_code == 200:
#     print("eBay allows web Scrapping")
# else:
#     print("eBay does not allow web Scrapping")

# page = requests.get("https://www.croma.com/")
# print(page.status_code)

# if page.status_code == 200:
#     print("croma allows web Scrapping")
# else:
#     print("croma does not allow web Scrapping")


# page = requests.get("https://www.amazon.in/gp/aw/sp.html?a=B00775Q5PU&s=AF6E3O0VE0X4D")
# print(page.status_code)

# if page.status_code == 200:
#     print("Saholic allows web Scrapping")
# else:
#     print("Saholic does not allow web Scrapping")




# page = requests.get("https://www.shopclues.com/")
# print(page.status_code)

# if page.status_code == 200:
#     print("Shop Clues allows web Scrapping")
# else:
#     print("Shop Clues does not allow web Scrapping")


# page = requests.get("https://www.shopclues.com/")
# print(page.status_code)

# if page.status_code == 200:
#     print("Shop Clues allows web Scrapping")
# else:
#     print("Shop Clues does not allow web Scrapping")




# page = requests.get("http://www.ia.ooo/")
# print(page.status_code)

# if page.status_code == 200:
#     print("Infibeam allows web Scrapping")
# else:
#     print("Infibeam does not allow web Scrapping")





page = requests.get("https://www.askmebazaar.com/")
print(page.status_code)

if page.status_code == 200:
    print("AskmeBazaar allows web Scrapping")
else:
    print("AskmeBazaar does not allow web Scrapping")
