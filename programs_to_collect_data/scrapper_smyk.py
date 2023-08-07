import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import datetime

def get_website_content(website_link):

  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

  req = Request(website_link, headers=headers)
  web = urlopen(req).read()

  soup1 = BeautifulSoup(web, 'html.parser')
  soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

  return soup2

def get_data(website_content, website_link):

  elements = website_content.find_all('span', class_= 'box-attributes-list__atribute--L')

  element = ''

  for item in elements:
    item = item.get_text()
    item = item.replace('\n', '')
    item = item.strip()

    if item.isdigit():
      element = int(item)

  list_of_elements = website_link.split('-')
  list_of_elements = list_of_elements[1:-1]

  title = ' '.join(list_of_elements[1: -1])
  title = title.title()

  series = list_of_elements[0].title()
  serial_number = list_of_elements[-1]

  price = website_content.find('span', class_ = 'price__new').get_text()
  price = price.replace('\n', '').replace('  ', '').replace(',', '.')
  price = price.strip()
  price = float(price[:-3])

  date = datetime.datetime.now()
  date = date.strftime('%Y-%m-%d')

  price_per_element = round(price / element, 2)

  dict_of_information = {
      'Serial Number': serial_number,
      'Series': series,
      'Title': title,
      'Date': date,
      'Price': price,
      'Elements': element,
      'Price per element': price_per_element
  }

  return dict_of_information

list_of_links = [
    "https://www.smyk.com/p/lego-technic-bugatti-bolide-agile-blue-42162-i7503457",
    'https://www.smyk.com/p/lego-speed-champions-koenigsegg-jesko-76900-i6949371',
    "https://www.smyk.com/p/lego-speed-champions-nissan-skyline-gt-r-r34-z-filmu-za-szybcy-za-wsciekli-76917-i7376346",
    "https://www.smyk.com/p/lego-marvel-samochod-spider-mana-i-doc-ock-10789-i7405515",
    "https://www.smyk.com/p/lego-speed-champions-lamborghini-countach-76908-i7091838",
    "https://www.smyk.com/p/lego-technic-jeep-wrangler-42122-i6835749",
    "https://www.smyk.com/p/lego-speed-champions-fast--furious-1970-dodge-charger-rt-76912-i7242946",
    "https://www.smyk.com/p/lego-technic-mclaren-senna-gtr-42123-i6835750",
    "https://www.smyk.com/p/lego-speed-champions-ferrari-812-competizione-76914-i7405507",
    "https://www.smyk.com/p/lego-star-wars-mysliwiec-x-wing-lukea-skywalkera-75301-i6837331",
    "https://www.smyk.com/p/lego-ideas-chatka-w-ksztalcie-litery-a-21338-i7481783",
    "https://www.smyk.com/p/lego-speed-champions-toyota-gr-supra-76901-i6949372",
    "https://www.smyk.com/p/lego-speed-champions-007-aston-martin-db5-76911-i7242947",
    "https://www.smyk.com/p/lego-technic-ford-mustang-shelbygt500-42138-i7089272",
    "https://www.smyk.com/p/lego-speed-champions-aston-martin-valkyrie-amr-pro-i-aston-martin-vantage-gt3-76910-i7091839",
    "https://www.smyk.com/p/lego-technic-bolid-bugatti-42151-i7376259",
    "https://www.smyk.com/p/lego-speed-champions-lotus-evija-76907-i7091837",
    "https://www.smyk.com/p/lego-technic-peugeot-9x8-24h-le-mans-hybrid-hypercar-42156-i7405527",
    "https://www.smyk.com/p/lego-ideas-sredniowieczna-kuznia-21325-i6933264",
    "https://www.smyk.com/p/lego-icons-optimus-prime-10302-i7253708",
    "https://www.smyk.com/p/lego-speed-champions-pagani-utopia-76915-i7405508",
    "https://www.smyk.com/p/lego-marvel-helm-star-lorda-76251-i7441359",
    "https://www.smyk.com/p/lego-technic-ford-gt-wersja-z-2022-roku-42154-i7405495",
    "https://www.smyk.com/p/lego-star-wars-dziecko-75318-i6840721",
    "https://www.smyk.com/p/lego-speed-champions-porsche-963-76916-i7405509",
    "https://www.smyk.com/p/lego-icons-posterunek-policji-10278-i6933259",
    "https://www.smyk.com/p/lego-star-wars-mandalorianin-i-dziecko-75317-i6725229",
    "https://www.smyk.com/p/lego-marvel-kwatera-straznikow-galaktyki-76253-i7405524",
    "https://www.smyk.com/p/lego-technic-nowy-chevrolet-camaro-zl1-z-serii-nascar-42153-i7405494",
    "https://www.smyk.com/p/lego-technic-samochod-wyscigowy-mclaren-formula-1-42141-i7089501",
    "https://www.smyk.com/p/lego-star-wars-helm-mrocznego-szturmowca-75343-i7090425",
    "https://www.smyk.com/p/lego-star-wars-maszyna-kroczaca-at-te-75337-i7253712",
    "https://www.smyk.com/p/lego-technic-doms-dodge-charger-42111-i6681176",
    "https://www.smyk.com/p/lego-technic-lamborghini-huracn-tecnica-42161-i7501782",
    "https://www.smyk.com/p/lego-icons-porsche-911-10295-i6933261",
    "https://www.smyk.com/p/lego-speed-champions-1970-ferrari-512-m-76906-i7091836",
    "https://www.smyk.com/p/lego-technic-ferrari-daytona-sp3-42143-i7253711",
    "https://www.smyk.com/p/lego-speed-champions-mclaren-solus-gt-i-mclaren-f1-lm-76918-i7405510",
    "https://www.smyk.com/p/lego-technic-ciezki-samochod-pomocy-drogowej-42128-i6949501",
    "https://www.smyk.com/p/lego-marvel-super-heroes-venom-76187-i6943456",
    "https://www.smyk.com/p/lego-star-wars-sokol-millennium-75192-i6213153",
    "https://www.smyk.com/p/lego-creator-expert-ford-mustang-10265-i6636742",
    "https://www.smyk.com/p/lego-technic-the-batman---batmobil-42127-i7089267",
    "https://www.smyk.com/p/lego-star-wars-helm-kapitana-rexa-75349-i7405520",
    "https://www.smyk.com/p/lego-star-wars-helm-mandalorianina-75328-i7089493",
    "https://www.smyk.com/p/lego-star-wars-justifier-75323-i7253713",
    "https://www.smyk.com/p/lego-star-wars-helm-dartha-vadera-75304-i6943457",
    "https://www.smyk.com/p/lego-icons-wahadlowiec-discovery-nasa-10283-i6933260",
    "https://www.smyk.com/p/lego-star-wars-helm-lukea-skywalkera---czerwony-piec-75327-i7089494",
    "https://www.smyk.com/p/lego-technic-ferrari-488-gte-af-corse-51-42125-i6835752",
    "https://www.smyk.com/p/lego-technic-bmw-m-1000-rr-42130-i7091960",
    "https://www.smyk.com/p/lego-super-heroes-sanctum-sanctorum-76218-i7256155",
    "https://www.smyk.com/p/lego-marvel-statek-straznikow-76193-i6950562",
    "https://www.smyk.com/p/lego-creator-expert-plac-zgromadzen-10255-i6213148",
    "https://www.smyk.com/p/lego-technic-lamborghini-sin-fkp-37-42115-i6725791",
    "https://www.smyk.com/p/lego-creator-expert-horizon-forbidden-west-zyraf-76989-i7091729",
    "https://www.smyk.com/p/lego-star-wars-helm-dowodcy-klonow-codyego-75350-i7405521",
    "https://www.smyk.com/p/lego-dc-comics-super-heroes-batmobil-tumbler-76240-i7016603",
    "https://www.smyk.com/p/lego-technic-formula-e-porsche-99x-electric-42137-i7089271",
    "https://www.smyk.com/p/lego-technic-helikopter-ratunkowy-airbus-h175-42145-i7253705",
    "https://www.smyk.com/p/lego-star-wars-mysliwiec-x-wing-75355-i7501884",
    "https://www.smyk.com/p/lego-technic-pojazd-terenowy-42139-i7089505",
    "https://www.smyk.com/p/lego-art-batman-jima-lee---kolekcja-31205-i7091723",
    "https://www.smyk.com/p/lego-star-wars-helm-boby-fetta-75277-i6681181",
    "https://www.smyk.com/p/lego-icons-ecto-1-pogromcow-duchow-10274-i6933257",
    "https://www.smyk.com/p/lego-technic-sterowany-przez-aplikacje-buldozer-cat-d11-42131-i7016616",
    "https://www.smyk.com/p/lego-super-mario-potezny-bowser-71411-i7304229",
    "https://www.smyk.com/p/lego-art-niesamowity-spider-man-31209-i7501763",
    "https://www.smyk.com/p/lego-technic-yamaha-mt-10-sp-42159-i7501780"
]

for item in list_of_links:
  print(get_data(get_website_content(item), item))