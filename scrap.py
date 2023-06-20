import requests
import pandas as pd
from bs4 import BeautifulSoup

url="https://webscraper.io/test-sites/e-commerce/allinone/phones"
r=requests.get(url)
soup= BeautifulSoup(r.content,"html.parser")
name=soup.find_all("a",class_="title")
product_list=[]
for i in name:
    name=i.text
    product_list.append(name)
#print(product_list)
header=soup.find_all("h4",class_="pull-right price")
price_list=[]
for i in header:
    name=i.text
    price_list.append(name)
#print(price_list)
desc=soup.find_all("p",class_="description")
description_list=[]
for i in desc:
    name=i.text
    description_list.append(name)
#print(description_list)
revi=soup.find_all("p",class_="pull-right")
review_list=[]
for i in revi:
    name=i.text
    review_list.append(name)
#print(review_list)
data=pd.DataFrame({"productName":product_list,"prices":price_list,"Description":description_list,"reviews":review_list})
print(data)

