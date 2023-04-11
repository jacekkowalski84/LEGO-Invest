import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.by import By
  

LEGO_ID = "41916"


def get_amazon_url (lego_id:str)->str:
    query = {'k': f"lego {lego_id}"}
    query_encoded = urllib.parse.urlencode(query)
    url = f"https://www.amazon.com/s?{query_encoded}&ref=nb_sb_ss_recent_1_0_recent"
    return url


def define_title_with_lego_id (titles: list, lego_id: str):
    for t in titles:
        if lego_id in t.text:
            title_with_lego_id = t
            return title_with_lego_id


def scrap_price_whole (url: str, lego_id: str)->str:
    driver = webdriver.Chrome()
    driver.get(url)
    titles = driver.find_elements(By.XPATH, r'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div/div/div/div/div/div[2]')
    title_with_lego_id = define_title_with_lego_id (titles, lego_id)
    price_element = title_with_lego_id.find_elements(By.XPATH, r'.//*[@class="a-price"]')
    price_whole = price_element[0].text
    driver.quit
    return price_whole


def string_to_float (text: str)->float:
    digits = '1234567890'
    for t in text:
        if t not in digits:
            text = text.replace (t,'')
    price = float (f"{text[:-2]}.{text[-2:]}")
    return price


def main(lego_id:str)->None:
    url = get_amazon_url(lego_id)
    price_whole = scrap_price_whole (url, lego_id)
    amazon_current_price = string_to_float (price_whole) 
    print (amazon_current_price)


if __name__ == "__main__":
    main(LEGO_ID)