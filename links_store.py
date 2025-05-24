from pprint import pprint
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def links_online_store(first_page_link:str,
                       store_name:str) -> list[str] | None:
    
    """
    Function to create automaticlly links to all pages which contain LEGO offers.
    Links are created for one store.
    Args:
        - first_page_link (str); Link to first page with lego offers in online store.
        - store_name (str); Store name
    Returns:
        - list_of_pages (list[str]); List with all pages from online reseller about Lego
    """

    list_of_pages = [first_page_link]

    if store_name.lower() == 'smyk':
        for number_page in range(2, 20):
            new_link = first_page_link + f"?p={number_page}"
            list_of_pages.append(new_link)
    elif store_name.lower() == 'alto':
        for number_page in range(2, 22):
            new_link = first_page_link + f"?page={number_page}"
            list_of_pages.append(new_link)

    return list_of_pages

def get_website_content(website_link):

  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

  req = Request(website_link, headers=headers)
  web = urlopen(req).read()

  soup1 = BeautifulSoup(web, 'html.parser')
  soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

  return soup2

def collect_links(website_content,
                  store_name:str) -> list | None:

    """
    Function to collect all of links from one page.
    Args:
        - website_content; Website content collected through scrapping process
        - store_name (str); parameter to control which part of function is 'working'
    Returns:
        - lego_set_links (list); list of links to lego sets collected from one_page of store
    """

    lego_set_links = []

    
    for link in website_content.find_all('a', href=True):
        link = str(link['href'])
        if store_name.lower() == 'alto':
            if "/p/" in link and link.startswith('/p/', 0, 3) and "#Opinie" not in link:
                modified_link = "al.to" + link
                lego_set_links.append(modified_link)
        elif store_name.lower() == 'smyk':
            if "/p/lego" in link:
                modified_link = 'https://www.smyk.com' + link
                lego_set_links.append(modified_link)
        
    return list(set(lego_set_links))

smyk_links = links_online_store("https://www.smyk.com/zabawki-gry/klocki/lego.html", "smyk")
alto_links = links_online_store("https://www.al.to/g-63/c/2073-klocki-lego.html", "alto")

smyk_contents = [get_website_content(link) for link in smyk_links]
alto_contents = [get_website_content(link) for link in alto_links]

smyk_lego_sets = [collect_links(content, 'smyk') for content in smyk_contents]
alto_lego_sets = [collect_links(content, 'alto') for content in alto_contents]
     
sample_link = smyk_lego_sets[0][0]
#pprint(collect_links(smyk_content, 'smyk'))
    