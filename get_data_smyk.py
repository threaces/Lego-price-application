import boto3
import time
from boto3.dynamodb.conditions import Key, Attr
import pandas as pd
from get_data import smyk_table

dynamodb = boto3.resource('dynamodb', 
                        aws_access_key_id = 'XXXXX',
                        aws_secret_access_key = 'XXXXXXX',
                        region_name = 'us-east-2')

def get_set_title(amazon_table):

    items = amazon_table.scan(AttributesToGet=['Title'])
    items = items['Items']

    list_of_set_title = []

    for item in items:
        item = item['Title']

        if item not in list_of_set_title:
            list_of_set_title.append(item)

    return list_of_set_title


def get_smyk_price_df(amazon_table, set_title):
    
    response = amazon_table.scan(
        FilterExpression = Attr('Title').eq(set_title)
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


# calling a functions
list_of_sets_smyk = get_set_title(smyk_table)
