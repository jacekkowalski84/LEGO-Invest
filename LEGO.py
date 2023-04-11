import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.by import By
  

LEGO_ID = "41916"


def text_preprocessing_remove_nondigits (text: str)->str:
    digits = '123456789'
    for t in text:
        if t not in digits:
            text = text.replace (t,'')
    return text


def getting_amazon_url (lego_id:str)->str:
    query = {'k': f"lego {lego_id}"}
    query_encoded = urllib.parse.urlencode(query)
    url = f"https://www.amazon.com/s?{query_encoded}&ref=nb_sb_ss_recent_1_0_recent"
    return url


def scrapping_price_element (url: str)->str:
    driver = webdriver.Chrome()
    driver.get(url)
    elements_by_class = driver.find_elements(By.XPATH, f'//*[@class="a-price"]')
    elements = [e.text for e in elements_by_class]
    price_element = elements[0]
    driver.quit()
    return price_element


def extract_amazon_current_price(price_element: str)->float:
    price_whole = text_preprocessing_remove_nondigits(price_element)
    amazon_price = float (f"{price_whole[:-2]}.{price_whole[-2:]}")
    return amazon_price


def main(lego_id:str)->None:
    url = getting_amazon_url(lego_id)
    price_element = scrapping_price_element(url)
    amazon_current_price = extract_amazon_current_price (price_element)
    print(amazon_current_price)


if __name__ == "__main__":
    main(LEGO_ID)