import requests
from bs4 import BeautifulSoup
import datetime

def get_web_data(url: str):
  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
  link_to_lego = requests.get(url, headers=headers)

  soup1 = BeautifulSoup(link_to_lego.content, 'html.parser')
  soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')


  title = soup2.find(class_="sc-1bker4h-4 hMQkuz").get_text()
  cleaned_title = title.strip().split(' ')

  dict_of_information = {}

  if cleaned_title[1] == 'Star':
    dict_of_information['Series'] = cleaned_title[1] + ' ' + cleaned_title[2]
    dict_of_information['Serial Number'] = cleaned_title[3]
    dict_of_information['Title'] = (' ').join(cleaned_title[4: ])
  elif cleaned_title[1] == 'Speed':
    dict_of_information['Series'] = cleaned_title[1] + ' ' + cleaned_title[2]
    dict_of_information['Serial Number'] = cleaned_title[3]
    dict_of_information['Title'] = (' ').join(cleaned_title[4: ])
  elif cleaned_title[1] == 'Harry':
    dict_of_information['Series'] = cleaned_title[1] + ' ' + cleaned_title[2]
    dict_of_information['Serial Number'] = cleaned_title[3]
    dict_of_information['Title'] = (' ').join(cleaned_title[4: ])
  else:
    dict_of_information['Series'] = cleaned_title[1]
    dict_of_information['Serial Number'] = cleaned_title[2]
    dict_of_information['Title'] = (' ').join(cleaned_title[3: ])

  element_amount = soup2.find_all(class_ ="sc-p7lf0n-3 eRnmRi")[-1]
  converted_elements = str(element_amount).replace(' ', '')
  remove_n_elements = converted_elements.replace('\n', '')

  if remove_n_elements[-11] == '>':
    dict_of_information['Elements'] = int(remove_n_elements[-10:-7])
  elif remove_n_elements[-11].isdigit():
    dict_of_information['Elements'] = int(remove_n_elements[-11:-7])

  input_date = datetime.datetime.now()
  formatted_date = input_date.strftime("%Y-%m-%d")

  dict_of_information['Date'] = formatted_date

  price = soup2.find('span', attrs = {'class': "sc-fzoant kanfxU"}).get_text()
  price = price.strip()
  price = price[:-3]
  price = price.replace(",", ".")
  price = price.replace(" ", "")
  
  dict_of_information['Price'] = float(price)

  price_per_element = round(dict_of_information['Price'] / dict_of_information['Elements'], 2)

  dict_of_information['Price per Element'] = price_per_element

  return dict_of_information


