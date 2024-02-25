from bs4 import BeautifulSoup
import requests

class BasicSpider():
    def __init__(self, name):
        # Each object has is own identifier
        self.name = str(name)

    def get_links(self, query):
    
        # The input query is comming from the frontend

        # Google URL, can Change to other browsers as well
        #although Google has one of the best search engines right now
        url = "https://www.google.com/search"

        # pass form (query) data and customize web page behaviour
        # add "hl":"en" to get english results
        params = {"q": str(query), "sort": "by_date"} 

        # Information about the request and response
        # User-Agent identifies the software making the request
        # It should follow robots.txt later on
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
        }
        
        # Response from the search (tags is a bs4 object)
        tags = BeautifulSoup(
            requests.get(url, params=params, headers=headers).content, "html.parser"
        )

        # Limit of returned links
        links = [a["href"] for a in tags.select("a:has(h3)")]
        
        return links


spider1 = BasicSpider("Spider1")

my_input = "guillem senabre prades"

spider1.get_links(my_input)
