import pandas as pd
import boto3
from boto3.dynamodb.conditions import Key, Attr
from get_data import table, smyk_table, list_of_sets
from get_data_smyk import list_of_sets_smyk


def get_sum_price(aws_table, set_title, attribute_title):

    response = aws_table.scan(
        FilterExpression = Attr(attribute_title).eq(set_title)
    )

    response = response["Items"]

    counter_price = 0
    sum_price = 0

    for item in response:
        sum_price += item["Price"]
        counter_price += 1

    avg_set_price = round(sum_price / counter_price, 2)

    return avg_set_price


def get_avg_price(aws_table, list_sets, attribute_title):

    list_of_prices = []

    for item in list_sets:
        single_set_price = get_sum_price(aws_table, item, attribute_title)
        list_of_prices.append(single_set_price)

    avg_price = round(sum(list_of_prices) / len(list_of_prices), 2)

    return avg_price

# I added 3rd parameter to fuction to not create new one with new attribute_title
# Aws is case - sensitive so I need to use title and Title

def get_sum_elements(aws_table, set_title, attribute_title):

    response = aws_table.scan(
        FilterExpression = Attr(attribute_title).eq(set_title)
    )

    response = response["Items"]

    elements = response[0]['Elements']

    return elements

def get_avg_elements(aws_table, list_sets, attribute_title):
    
    list_of_elements = []

    for item in list_sets:
        single_set = get_sum_elements(aws_table, item, attribute_title)
        list_of_elements.append(single_set)

    avg_elements = round(sum(list_of_elements) / len(list_of_elements), 2)

    return avg_elements

def get_list_of_themes(aws_table):
    
    response = aws_table.scan(AttributesToGet=['Series'])
    response = response["Items"]

    list_of_themes = []

    for item in response:
        if item['Series'] not in list_of_themes:
            list_of_themes.append(item["Series"])

    return list_of_themes

def get_avg_price_theme(aws_table, theme, attribute_title):
    
    response = aws_table.scan(
        FilterExpression = Attr("Series").eq(theme)
    )

    list_of_title = []

    response = response["Items"]

    for item in response:
        if item[attribute_title] not in list_of_title:
            list_of_title.append(item[attribute_title])

    dict_of_data = {}

    for item in response:
        if item[attribute_title] in list_of_title and item[attribute_title] not in dict_of_data:
            dict_of_data[item[attribute_title]] = {"Total price": item["Price"], "Counter": 1}
        else:
            dict_of_data[item[attribute_title]]["Total price"] += item["Price"]
            dict_of_data[item[attribute_title]]["Counter"] += 1

    list_of_avg_set_price = []

    for item in dict_of_data.keys():
        avg_set_price = round(dict_of_data[item]["Total price"] / dict_of_data[item]['Counter'], 2)
        list_of_avg_set_price.append(avg_set_price)

    avg_price = round(sum(list_of_avg_set_price) / len(list_of_avg_set_price), 2)

    return avg_price

def list_avg_price_per_series(aws_table, attribute_title):

    list_of_themes = get_list_of_themes(aws_table)

    dict_of_avg_prices = {}

    for item in list_of_themes:
        dict_of_avg_prices[item] = get_avg_price_theme(aws_table, item, attribute_title)

    return dict_of_avg_prices
        

avg_price_alto = get_avg_price(table, list_of_sets, 'title')
avg_price_smyk = get_avg_price(smyk_table, list_of_sets_smyk, 'Title')

avg_price = round((avg_price_alto + avg_price_smyk) / 2, 2)

avg_elements_alto = get_avg_elements(table, list_of_sets, 'title')
avg_elements_smyk = get_avg_elements(smyk_table, list_of_sets_smyk, "Title")

avg_elements = round((avg_elements_alto + avg_elements_smyk) / 2, 0)

#print(get_avg_price_theme(smyk_table, get_list_of_themes(smyk_table)[1], 'Title'))

avg_price_series_alto = list_avg_price_per_series(table, 'title')
avg_price_series_smyk = list_avg_price_per_series(smyk_table, 'Title')
