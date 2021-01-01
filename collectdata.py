import pandas as pd
import requests
import json #Handling JSON Data
import boto3  # Saving into DynamoDB
import datetime as dt
import time
import threading
import apscheduler.schedulers.background as schedulers
from dateutil import parser

def save_to_dynamoDB(df):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-2',aws_access_key_id='AKIASPUVDP3PBTVXJOXH',
         aws_secret_access_key= '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')
    table = dynamodb.Table('Intraday1minTest')
    for item in df.to_dict(orient='records'):

        table.put_item(Item=item)

# def update_data(df):


def read_data():

    url = 'https://www1.nseindia.com/live_market/dynaContent/live_watch/stock_watch/niftyStockWatch.json'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
        "Upgrade-Insecure-Requests": "1", "DNT": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate"}
    cookie = {'NSE-TEST-1': '1910513674.20480.0000', 'path': '/', 'domain': 'www1.nseindia.com',
              'Expires': 'Tue, 19 Jan 2038 03:14:07 GMT'}
    # url = 'https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050'
    data = requests.get(url, headers=headers, cookies=cookie)
    return data

def parse_data(data):
    df= pd.DataFrame(data.json()['data'])
    time = parser.parse(data.json()['time'])
    # time+=dt.timedelta(minutes=i)
    # print('dt[time] ',type(dt.datetime.strftime(time,'%Y-%m-%d_%H:%M:%S')))
    df['time'] = dt.datetime.strftime(time,'%Y-%m-%d_%H:%M:%S')
    df['key']= '['+df['symbol']+']'+df['time']

    # strftime('%m-%d-%y_%H:%M:%S')
    return df[['key', 'symbol', 'time', 'high', 'low', 'ltP', 'trdVol', 'previousClose']]

def collect_data():
    # data['time'] = data.json()['time']=pd.to_datetime
    print(dt.datetime.now())
    data= parse_data(read_data())
    save_to_dynamoDB(data)
    # time.sleep(60)

collect_data()
# for i in range(200):
# scheduler = schedulers.BackgroundScheduler()
# scheduler.add_job(collect_data, 'interval', seconds=60)
# scheduler.start()
    # threading.Thread(collect_data()).start()
    # print(dt.time,i)
# threading.Thread(target=lambda: every(60, collect_data())).start()
