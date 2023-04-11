import urllib.parse
import requests
from lxml.html import fromstring


LEGO_ID = "41916"

def getting_amazon_url(lego_id: str)->str:
    query = {'k': f"lego {lego_id}"}
    query_encoded = urllib.parse.urlencode(query)
    url = f"https://www.amazon.com/s?{query_encoded}&ref=nb_sb_ss_recent_1_0_recent"
    return url

def extract_amazon_current_price (html:str):
    dom = fromstring (html)
    xpath = r'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div[2]/div[3]/div/a/span/span[2]/span[2]'
    elements = dom.xpath (xpath)
    amazon_current_price = [e.text_content() for e in elements]
    return amazon_current_price


def main(lego_id):
    url = getting_amazon_url(lego_id)
    response = requests.get(url)
    html = response.text
    print (extract_amazon_current_price (html))
    
if __name__ == "__main__":
    main(LEGO_ID)