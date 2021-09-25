#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests

html_doc = """
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>
<h3><b id='boldest'>Lebron James</b></h3>
<p> Salary: $ 92,000,000 </p>
<h3> Stephen Curry</h3>
<p> Salary: $85,000, 000 </p>
<h3> Kevin Durant </h3>
<p> Salary: $73,200, 000</p>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, "html5lib")


# Children, parents, and siblings
tag_object = soup.h3
tag_child = tag_object.b
parent_tag = tag_child.parent
tag_object.parent

sibling_1 = tag_object.next_sibling
sibling_2 = sibling_1.next_sibling


# Html attributes

tag_child["id"]

tag_child.attrs

tag_child.get("id")

table = """
<table>
  <tr>
    <td id='flight' >Flight No</td>
    <td>Launch site</td>
    <td>Payload mass</td>
   </tr>
  <tr>
    <td>1</td>
    <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a></td>
    <td>300 kg</td>
  </tr>
  <tr>
    <td>2</td>
    <td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td>
    <td>94 kg</td>
  </tr>
  <tr>
    <td>3</td>
    <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td>
    <td>80 kg</td>
  </tr>
</table>"""


table_bs = BeautifulSoup(table, "html5lib")

# Fina_all()
table_rows = table_bs.find_all("tr")
# print(table_rows)

# Iterate through the list

for i, row in enumerate(table_rows):
    "row", i
    cells = row.find_all("td")
    for j, cell in enumerate(cells):
        "column", j, "cell", cell


# If use a list we can match against any item in that list

list_input = table_bs.find_all(name=["tr", "td"])
table_bs.find_all(href=False)

# search with attri
table_bs.find_all(id="boldest")

# search with string
table_bs.find_all(string="Florida")


# Find : If you are looking for one element you can use the `find()`


two_tables = """
<h3>Rocket Launch </h3>

<p>
<table class='rocket'>
  <tr>
    <td>Flight No</td>
    <td>Launch site</td> 
    <td>Payload mass</td>
  </tr>
  <tr>
    <td>1</td>
    <td>Florida</td>
    <td>300 kg</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Texas</td>
    <td>94 kg</td>
  </tr>
  <tr>
    <td>3</td>
    <td>Florida </td>
    <td>80 kg</td>
  </tr>
</table>
</p>
<p>

<h3>Pizza Party  </h3>
  
    
<table class='pizza'>
  <tr>
    <td>Pizza Place</td>
    <td>Orders</td> 
    <td>Slices </td>
   </tr>
  <tr>
    <td>Domino's Pizza</td>
    <td>10</td>
    <td>100</td>
  </tr>
  <tr>
    <td>Little Caesars</td>
    <td>12</td>
    <td >144 </td>
  </tr>
  <tr>
    <td>Papa John's </td>
    <td>15 </td>
    <td>165</td>
  </tr>

"""
# Create a BeautifulSoup object

two_tables_bs = BeautifulSoup(two_tables, "html5lib")

# we can find te first table

first_table = two_tables_bs.find("table")


# filter the class attribute to find the second table

first_table_with_class_pizza = two_tables_bs.find("table", class_="pizza")


# Downloading and Scrapping the content of a web page

# we download the contents of the webpage
url = "https://www.ibm.com"

data = requests.get(url).text

# create a beautiful soup object

soup = BeautifulSoup(data, "html5lib")

# scrape all links

for link in soup.find_all("a", href=True):
    link.get("href")

# scrape all images Tags

for link in soup.find_all("img"):
    link
    link.get("src")


# Scrape Data from HTML table

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

data = requests.get(url).text

soup = BeautifulSoup(data, "html5lib")

table = soup.find("table")

# Get all the rows in the table

for row in table.find_all("tr"):
    # Get all column in each row
    col = row.find_all("td")
    color_name = col[2].string  # Store the calue in column 3 as color_name
    color_code = col[3].string  # Store the value in column 4 as color_code
    print(f"{color_name} ----> {color_code}")
