from bs4 import BeautifulSoup
import requests

class BasicSpider():
    def __init__(self, name):
        # Each spider has is own identifier
        self.name = str(name)

        # Google URL, can Change to other browsers as well
        #although Google has one of the best search engines right now
        self.url = "https://www.google.com/search"

    def get_data(self):

        query = input("Input query: ")
        
        response_tree = self._get_response(self.url, query)
        links_and_h3 = self._get_links_and_headers(response_tree)

        #links = [a["href"] for a in website_tree.select("a:has(h3)") if "href" in a.attrs]
        print(links_and_h3)
        return "finished"

    def _get_response(self, url, query):
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
        website_tree = BeautifulSoup(
            requests.get(url, params=params, headers=headers).content, "html.parser"
        )

        return website_tree


    def _get_links_and_headers(self, response):
        # Dictionary to store header3 and the href link
        links_and_h3 =  {}

        # This counter is needed since the not all anchors contain 'href' or 'h3'
        index = 0

        # Loops over all anchors
        for anchor in response.find_all('a'):
            
            # Extracts only the anchors that contain href AND h3
            if anchor.find_all('h3') and "href" in anchor.attrs:

                # Builds the dictionary with the extracted data
                links_and_h3[f"pair{index}"] = anchor.find('h3').text.strip(), anchor['href']
                
                index += 1

        return links_and_h3

