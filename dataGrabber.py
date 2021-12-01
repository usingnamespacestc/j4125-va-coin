import json
import requests

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
headers = {'Content-Type': 'application/json', 'X-CMC_PRO_API_KEY': '4fed23b2-234d-4578-843b-2d70a5ddb644'}
params = {
    'symbol': 'BTC,ETH,XRP,DOT,GALA,ADA,LUNA,SOL,FTM,AVAX,ENJ,MANA,CHZ,CRV,DYDX'
}


def grab_data():
    response = requests.get(url=url, headers=headers, params=params)
    coin_data = json.loads(response.text)['data']
    return coin_data


if __name__ == '__main__':
    test_response = requests.get(url=url, headers=headers, params=params)
    test_coinData = json.loads(test_response.text)['data']
