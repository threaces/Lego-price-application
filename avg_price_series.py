from general_summary_cards import avg_price_series_alto, avg_price_series_smyk
import pandas as pd

technic = (((avg_price_series_alto["Technic™"] * 1 + avg_price_series_alto["Technic"] * 21) / 22) + avg_price_series_smyk["Technic"]) / 2
star_wars = (((avg_price_series_alto["Star Wars"] * 15 + avg_price_series_alto["Star Wars™"] * 1) / 16) + avg_price_series_smyk["Star"]) / 2

list_of_dict_series = [{"Art": (avg_price_series_alto["Art"] + avg_price_series_smyk["Art"]) / 2},
                       {"Speed Champions": (avg_price_series_alto["Speed Champions"] + avg_price_series_smyk["Speed"]) / 2},
                       {"Icons" : (avg_price_series_alto["Icons"] + avg_price_series_smyk["Icons"]) / 2},
                       {"Harry Potter" : avg_price_series_alto["Harry Potter"]},
                       {"Technic" : round(technic, 2)},
                       {"Star Wars": round(star_wars, 2)},
                       {"Super Mario": (avg_price_series_alto["Super Mario"] + avg_price_series_smyk["Super"]) / 2},
                       {"Marvel": avg_price_series_smyk["Marvel"]},
                       {"Creator Expert": avg_price_series_smyk["Creator"]},
                       {"Ideas": avg_price_series_smyk["Ideas"]},
                       {"DC": avg_price_series_smyk["Dc"]}]

merged_data = {}

for item in list_of_dict_series:
    merged_data.update(item)

avg_price_series_df = pd.DataFrame(list(merged_data.items()), columns=["Series", "Avg Price"])

avg_price_series_df = avg_price_series_df.sort_values(by="Avg Price", ascending=True)

