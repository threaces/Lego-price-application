import boto3
import time
from boto3.dynamodb.conditions import Key, Attr
import pandas as pd

dynamodb = boto3.resource('dynamodb', 
                        aws_access_key_id = 'XXXXXX',
                        aws_secret_access_key = 'XXXXXXXXX',
                        region_name = 'us-east-2')

def amazon_database(name):
    amazon_table = dynamodb.Table(name)

    return amazon_table

table = amazon_database("Lego")
smyk_table = amazon_database("Lego_smyk")

def get_set_title(amazon_table):

    items = amazon_table.scan(AttributesToGet=['title'])
    items = items['Items']

    list_of_set_title = []

    for item in items:
        item = item['title']

        if item not in list_of_set_title:
            list_of_set_title.append(item)

    return list_of_set_title

list_of_sets = get_set_title(table)
#list_of_sets_smyk = get_set_title(smyk_table)

def get_price_df(amazon_table, set_title):
    
    response = amazon_table.scan(
        FilterExpression = Attr('title').eq(set_title)
    )

    response = response['Items']

    list_of_modified_items = []

    for item in response:
        tuple_single_item = tuple()

        tuple_single_item = (item['Date'], item['Price'])

        list_of_modified_items.append(tuple_single_item)

    df = pd.DataFrame(list_of_modified_items, columns=['Date', 'Price'])
    df['Price'] = pd.to_numeric(df['Price'])

    df = df.drop_duplicates(subset=['Date'])
    df = df.sort_values(by='Date')
    df = df.reset_index()
    df = df.drop(['index'], axis=1)

    return df

def get_min_price(df):
    filtered_df = df[df['Price'] == df['Price'].min()]
    filtered_df = filtered_df.reset_index()
    filtered_df = filtered_df.drop(['index'], axis=1)

    if len(filtered_df) > 1:
        min_price = filtered_df['Price'].min()
        first_date = filtered_df['Date'][0]
        last_date = filtered_df['Date'][len(filtered_df) - 1]

        return min_price, first_date, last_date
    else:
        min_price = filtered_df['Price'].min()
        historical_min = filtered_df["Date"][0]

        return min_price, historical_min

    #return filtered_df


    


