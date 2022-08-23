from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

import csv
from lib2to3.pgen2 import driver
from operator import itemgetter
from re import template
from bs4 import BeautifulSoup

import json
import re
import pandas as pd
import requests


url = "https://www.daraz.com.bd/products/huadelai-twin-v30-35mm-i226554011-s1171026159.html?spm=a2a0e.searchlistcategory.list.6.34d93b78imSiKv&search=1"

data = (
    json.loads(
        re.search(
            r"app\.run\((.*)\);",
            requests.get(url).text,
            re.MULTILINE,
        ).group(1)
    )
)
reviews = data["data"]["root"]["fields"]["review"]

print(f'{reviews["ratings"]}\n{"-" * 800}')

ind = 0
data = []
for review in reviews["reviews"]:
    print(f'{review["reviewer"]} -> {review["reviewContent"]}\n')
    Name =  review["reviewer"]
    review = review["reviewContent"]
    data.append([Name, review])
df = pd.DataFrame(data, columns=['Name', 'review'])
#    ind=ind+1
df.to_csv('daraz_review.csv', index= False)
