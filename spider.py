from bs4 import BeautifulSoup
import requests

def crawl_data():

  # Dyanimc query
  query = input(f"Crawl data from: ")

  # Google URL, can Change to other browsers as well
  url = "https://www.google.com/search"

  # input parameters (query, ...)
  params = {"q": str(query)}  # add "hl":"en" to get english results

  headers = {
      "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
  }
  
  # Response from the search (tags is a bs4 object)
  tags = BeautifulSoup(
      requests.get(url, params=params, headers=headers).content, "html.parser"
  )

  # Limit of returned links
  num_links = 5

  # loop to retrieve the link from the <a> tag
  for index in range(num_links):
      a = tags.select("a:has(h3)")[index]
      print(a["href"])  
  
  return "Search completed!"

if __name__=="__main__":
   crawl_data()

