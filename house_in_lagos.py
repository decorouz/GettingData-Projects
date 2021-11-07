from bs4 import BeautifulSoup
import datetime
import requests
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import time
import random
import re

sns.set()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
}

house_for_sale = "https://nigeriapropertycentre.com/for-sale/houses/lagos/ikeja/showtype"

doc = requests.get(house_for_sale, headers=headers).text

# Time to make some soup

house_data = BeautifulSoup(doc, "html5lib")


def date_formatter(item, date):
    date = item.find_all("span", class_="added-on")[0].text
    new_date = date.replace("Added", "").replace("on", "").strip()

    if new_date.lower() == "today":
        return datetime.date.today().strftime("%d %b %Y")
    elif new_date.lower() == "yesterday":
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        return yesterday.strftime("%d %b %Y")
    else:
        return new_date


# # setting up the lists that will form our dataframe with all the results
titles = []
created = []
prices = []
sizes = []
locations = []
documents = []
descriptions = []
urls = []
thumbnails = []

page_text = house_data.find(class_="pagination pagination-style-2 pagination-lg")
pages = int(str(page_text.find_all("li")[-2].text))

for page in range(1, pages + 1):
    house_for_sale = f"https://nigeriapropertycentre.com/for-sale/houses/lagos/ikeja/showtype?page={page}"

    page = requests.get(house_for_sale, headers=headers).text
    doc = BeautifulSoup(page, "html5lib")

    house_containers = doc.find_all("div", class_="wp-block property list")

    if house_containers != []:
        for container in house_containers:

            # Title
            title = container.find_all("h4", class_="content-title")[0].text
            titles.append(title)

            # Location
            location = container.find_all("address")[0].text.strip()
            zone = location[location.find(",") + 2 :]
            locations.append(zone)

            # Price
            price = container.find_all("span", class_="pull-sm-left")[0].text
            prices.append(price)

            # Created Date
            date = container.find_all("span", class_="added-on")[0].text
            date = date_formatter(container, date)
            created.append(date)

            # url
            link = "https://nigeriapropertycentre.com/" + container.find_all("a")[0].get(
                "href"
            )
            urls.append(link)

            # Size

            # size = container.find_all("span")[9]
            # sizes.append(size)

            # Description
            description = container.find_all("p")[0].text
            descriptions.append(description[:10])

            # Documents
            doc = "c of".lower()
            doc_2 = "certificate of occupancy".lower()
            if re.search(doc, description.lower()) or re.search(
                doc_2, description.lower()
            ):
                documents.append("C-of-O")
            else:
                documents.append("c-of-o not indicated")

    else:
        break
    time.sleep(random.randint(1, 2))


cols = ["Title", "Location", "Price", "Documents", "Date", "URL", "Description"]

lagos = pd.DataFrame(
    {
        "Title": titles,
        "Location": locations,
        "Price": prices,
        "Documents": documents,
        "Date": created,
        "URL": urls,
        "Description": descriptions,
    }
)[cols]

lagos.to_excel("data/ikeja_raw.xls")

