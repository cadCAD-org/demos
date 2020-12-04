import csv
import argparse
import requests
import pandas as pd
import datetime as dt

def get_convert_rate(API_key):
  df  = pd.read_pickle('../uniswap_events.pickle')
  try:
      df.drop(columns=['convert_ETH_rate', 'convert_DAI_rate'], inplace=True)
  except:
      pass
  df['block_date'] = df.apply(lambda row: convert_to_rfc(row.block_timestamp), axis=1)
  start = df.iloc[0].block_date
  end = df.iloc[-1].block_date
  coin="ETH"
  api_request = f"https://api.nomics.com/v1/exchange-rates/history?key={API_key}&currency={coin}&start={start}&end={end}&format=csv"

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
  df.to_pickle('../uniswap_events.pickle')