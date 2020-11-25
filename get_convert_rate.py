import csv
import argparse
import requests
import pandas as pd
import datetime as dt

description = "This file is used to retrieve the convert rate of ETH to USD and input this in the target pickle file. Remember to pass the argument --key with your Nomics API key."

parser = argparse.ArgumentParser(description=description)
parser.add_argument("-V", "--version", help="Show program version", action="store_true")
parser.add_argument("-K", "--key", help="Nomics API key", action="store", type=str)
args = parser.parse_args()

def convert_to_rfc(block_timestamp):
    date = block_timestamp.date().isoformat()+"T00%3A00%3A00Z"
    return date 

if __name__ == "__main__":
    if(args.version):
        print("This is get_convert_rate version 0.1.")
    
    if(not args.key):
        print("Please insert your Nomics API key with the --key argument.")
    else:
        df  = pd.read_pickle('./uniswap_events.pickle')
        try:
            df.drop(columns=['convert_ETH_rate', 'convert_DAI_rate'], inplace=True)
        except:
            pass
        df['block_date'] = df.apply(lambda row: convert_to_rfc(row.block_timestamp), axis=1)
        start = df.iloc[0].block_date
        end = df.iloc[-1].block_date
        coin="ETH"
        api_request = f"https://api.nomics.com/v1/exchange-rates/history?key={args.key}&currency={coin}&start={start}&end={end}&format=csv"

        with requests.Session() as s:
            download = s.get(api_request)

            decoded_content = download.content.decode('utf-8')

            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            my_list = list(cr)
            eth_rate_df = pd.DataFrame(my_list, columns=['date', 'convert_ETH_rate'])


        print(start, end)
        coin="DAI"
        api_request = f"https://api.nomics.com/v1/exchange-rates/history?key={args.key}&currency={coin}&start={start}&end={end}&format=csv"

        with requests.Session() as s:
            download = s.get(api_request)

            decoded_content = download.content.decode('utf-8')

            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            my_list = list(cr)
            dai_rate_df = pd.DataFrame(my_list, columns=['date', 'convert_DAI_rate'])
            dai_rate_df.to_csv('test.csv')

    df['block_date'] = pd.to_datetime(df['block_timestamp']).dt.strftime('%Y-%m-%d')
    eth_rate_df['date'] = pd.to_datetime(eth_rate_df['date']).dt.strftime('%Y-%m-%d')
    dai_rate_df['date'] = pd.to_datetime(dai_rate_df['date']).dt.strftime('%Y-%m-%d')

    df['block_date'] = pd.to_datetime(df['block_timestamp']).dt.strftime('%Y-%m-%d')
    df = df.set_index('block_date').join(eth_rate_df.set_index('date')).reset_index(drop=True)
    df['block_date'] = pd.to_datetime(df['block_timestamp']).dt.strftime('%Y-%m-%d')
    df = df.set_index('block_date').join(dai_rate_df.set_index('date')).reset_index(drop=True)
    df['convert_ETH_rate'] = df['convert_ETH_rate'].astype(float)
    df['convert_DAI_rate'] = df['convert_DAI_rate'].astype(float)
    df.to_pickle('./uniswap_events.pickle')