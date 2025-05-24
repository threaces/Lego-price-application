from programs_to_collect_data.scrapper_smyk import get_data
from links_store import smyk_lego_sets
from pprint import pprint

details = [get_data(web_page) for web_page in smyk_lego_sets[0]]

pprint(details)