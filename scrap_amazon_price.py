"""
Usage:
python scrap_amazon_price.py <lego_id>
"""

import click
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import urllib.parse


def get_amazon_url (lego_id:str)->str:
    query = {'k': f"lego {lego_id}"}
    query_encoded = urllib.parse.urlencode(query)
    url = f"https://www.amazon.com/s?{query_encoded}&ref=nb_sb_ss_recent_1_0_recent"
    return url


def define_titles_containing_id (titles: list, lego_id: str)->list:
    titles_containing_id = [t for t in titles 
                            if str(lego_id) in t.text]
    if len(titles_containing_id) == 0:
        titles_containing_id = []
    return titles_containing_id


def remove_duplicate_prices (price_element: str)-> str:
    while price_element.count('$')>1:
        price_element.rsplit ('$', maxsplit=1)
    return price_element

def price_str_to_float (price_element: str)->float:
    digits = '1234567890'
    for t in price_element:
        if t not in digits:
            price_element = price_element.replace (t,'')
    price = float (f"{price_element[:-2]}.{price_element[-2:]}")
    return price


def define_amazon_price (titles_containing_id: list)-> float:
    price_elements = [price_element  
                      for title in titles_containing_id
                      for price_element in title.find_elements(By.XPATH, r'.//*[@class="a-price"]')]
    if len(price_elements) == 0:
        amazon_price = ''
    else:
        amazon_prices = [price_str_to_float(remove_duplicate_prices(pe.text))
                         for pe in price_elements]
        amazon_price = sum(amazon_prices) / len(amazon_prices)
    return amazon_price

def scrap_amazon_price (lego_id: str):
    url = get_amazon_url (lego_id)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    titles = driver.find_elements(By.XPATH, r'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div/div/div/div/div/div')
    titles_containing_id = define_titles_containing_id (titles, lego_id)
    if titles_containing_id == []:
        amazon_price = ''
    else:
        amazon_price = define_amazon_price (titles_containing_id)
    driver.quit()
    return amazon_price

@click.command()
@click.argument ('lego_id')
def main(lego_id:str)->None:
    amazon_current_price = scrap_amazon_price (lego_id)  
    print (amazon_current_price)


if __name__ == "__main__":
    main()