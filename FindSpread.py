from  DigExchangeLib.BitoproExchange import BitoproExchange
from  DigExchangeLib.MaxExchange import MaxExchange
from  DigExchangeLib.BinanceExchange import BinanceExchange
"""

'bids': [{'amount': '0.00657471',
           'count': 1,
           'price': '32704',
           'total': '0.00657471'}

'asks': [{'amount': '0.0016',
           'count': 1,
           'price': '38723.41',
           'total': '0.0016'}}
"""
def  find_Bito_cheapest_price(bito_orderbook):
    asksList = bito_orderbook['asks']
    cheapestinfo = {"price":asksList[0]['price'],'amount':asksList[0]['amount']}
    for  ask  in asksList:
        if  float(ask['price']) < float(cheapestinfo['price']) :
            cheapestinfo = ask
    return  cheapestinfo



def  find_Max_cheapest_price(maxE_orderbook):
    cheapestinfo = {"price": maxE_orderbook[0]['price'], 'amount':maxE_orderbook[0]['volume']}
    for  order in maxE_orderbook:
        if  order['side'] == "ask"  and  float(cheapestinfo['price'])  < float(order['price']):
            cheapestinfo =  {"price": float(order['price']) , 'amount':order['volume']}
    return cheapestinfo

def find_Binance_cheapest_price(binance_orderbook):
    """
            {'lastUpdateId': 4725681499,
             'bids': [['1226.05000000', '30.00000000'], ['1225.84000000', '1.65491000'], ['1225.82000000', '5.20000000'],
                      ['1225.79000000', '0.16309000'], ['1225.78000000', '5.14245000']],
             'asks': [['1226.28000000', '1.56131000'], ['1226.29000000', '32.80000000'], ['1226.30000000', '32.81681000'],
                      ['1226.31000000', '0.13522000'], ['1226.32000000', '0.58248000']]}
            """
    cheapestinfo = {"price": binance_orderbook['asks'][0][0], 'amount': binance_orderbook['asks'][0][1]}
    for order in binance_orderbook['asks']:
        if float(cheapestinfo['price']) < float(order[0]):
            cheapestinfo = {"price": float(order[0]), 'amount': order[1]}
    return cheapestinfo

"""Max:
 btc/eth/ltc/bch/mith/xrp/max/usdt  twd  
 eth  btc
btc/eth/ltc/bch/mith/xrp/max/sand       usdt 
 """


maxE = MaxExchange()
maxE_orderbook = maxE.get_orderbook("ethusdt",limit=4)
max_price = find_Max_cheapest_price(maxE_orderbook)
bito = BitoproExchange()
bito_orderbook = bito.get_orderbook("eth_usdt")
bito_price = find_Bito_cheapest_price(bito_orderbook)

binance = BinanceExchange()
binance_orderbook =  binance .get_orderbook("ETHUSDT")
binance_price  = find_Binance_cheapest_price(binance_orderbook)

print(f"Max:{max_price}\nBito:{bito_price}\nBinance:{binance_price}")

