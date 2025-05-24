from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import datetime
import re

def get_website_content(website_link):

  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

  req = Request(website_link, headers=headers)
  web = urlopen(req).read()

  soup1 = BeautifulSoup(web, 'html.parser')
  soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

  return soup2

def get_elements_lego(website_content, 
                      class_website: str) -> int:
  
  # 'box-attributes-list__atribute--L'

  """
  Function to retrive amount of elements in lego set from website.

  Args:
    - website_content;
    - class_website (str);
  Returns:
    - lego_elements (int); Lego pieces in checked set
  """

  elements = website_content.find_all('span', class_= class_website)

  lego_elements = ''

  for item in elements:
    item = item.get_text()
    item = item.replace('\n', '')
    item = item.strip()

    if item.isdigit():
      lego_elements = int(item)

  return lego_elements

def get_series(website_link: str) -> list:

  """
  Function to retrive a data from the link to online reseller.

  Args:
    - website_link (str); Link to reseller offer (Lego set)
  Returns:

  """
  list_of_elements = website_link.split('-')
  list_of_elements = list_of_elements[1:-1]

  title = ' '.join(list_of_elements[1: -1])
  title = title.title()

  series = list_of_elements[0].title()

  if series == "Speed":
    series = "Speed Champions"
    title = title.replace("Champions", "").lstrip()
  elif "3 W 1" in title or "3W1" in title:
    series = "Creator 3W1"
    title = re.sub(r"3\s*W\s*1", "", title,flags=re.IGNORECASE).lstrip()
  elif series == "Star":
    series = "Star Wars"
    title = title.replace("Wars", "")
  elif series == "Super":
    series = "Super Mario"
    title = title.replace("Mario", "").lstrip()

  serial_number = list_of_elements[-1]

  return [title, series, serial_number]

def get_price(website_content,
              class_name: str) -> float | str:
  
  """
  Function to retrive lego set price from website content

  Args:
    - website_content; 
    - class_name (str);
  Returns:
    - price (float); Lego set price
  """
  # 'price__new'

  price = website_content.find('span', class_ = class_name)

  if price:
    price = price.get_text()
    price = price.replace('\n', '').replace('  ', '').replace(',', '.')
    price = price.strip()
    price = float(price[:-3])
  else:
    price = "Brak ceny"

  return price

def get_data(website_link: str):

  """
  Function to combine a data into dictionary and add a timestamp

  Returns:
    - dict_of_information (dict); Dict with all of informations about Lego sets
  """

  website_content = get_website_content(website_link)

  lego_elements = get_elements_lego(website_content, 'box-attributes-list__atribute--L')
  title, series, serial_number = get_series(website_link)
  price = get_price(website_content, 'price__new')

  date = datetime.datetime.now()
  date = date.strftime('%Y-%m-%d')

  if isinstance(lego_elements, int) and isinstance(price, float):
    price_per_element = round(price / lego_elements, 2)

    dict_of_information = {
        'Serial Number': serial_number,
        'Series': series,
        'Title': title,
        'Date': date,
        'Price': price,
        'Elements': lego_elements,
        'Price per element': price_per_element
    }
  else:
        dict_of_information = {
        'Serial Number': serial_number,
        'Series': series,
        'Title': title,
        'Date': date,
        'Price': price,
        'Elements': lego_elements,
    }

  return dict_of_information

    
