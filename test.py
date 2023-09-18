from bs4 import BeautifulSoup
import pandas as pd
import requests

start_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

#page request
page = requests.get(start_url)

soup = BeautifulSoup(page.text, "html.parser")
table = soup.find("table")

#empty list
temp_list = []

tr_tags = table.find_all("tr")

#get all tr tags
for tr_tag in tr_tags:
    td_tags = tr_tag.find_all("td")
    row = [i.text.rstrip() for i in td_tags]
    temp_list.append(row)

name = []
distance = []
mass = []
radius = []

for i in range(1, len(temp_list)):
    name.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])

df = pd.DataFrame(list(zip(name, distance, mass, radius)), columns=["name", "distance", "mass", "radius"])
df.to_csv("stars_data.csv")