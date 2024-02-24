from bs4 import BeautifulSoup
import requests

url = "https://www.google.com/search"
params = {"q": "boring stuff"}  # add "hl":"en" to get english results
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
}
tags = BeautifulSoup(
    requests.get(url, params=params, headers=headers).content, "html.parser"
)

num_links = 5

for index in range(num_links):
    a = tags.select("a:has(h3)")[index]
    print(a["href"])