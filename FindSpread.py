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
    bidsList = bito_orderbook['bids']
    cheapest_ask = {"askprice":asksList[0]['price'],
                    'askamount':asksList[0]['amount']}

    highest_bid = {"bidprice": bidsList[0]['price'],
                    "bidamount": bidsList[0]['amount']}
    print(highest_bid)
    for  ask  in asksList:
        if  float(ask['price']) < float(cheapest_ask['askprice']) :
            cheapest_ask = {"askprice":ask['price'],
                    'askamount':ask['amount']}
    for  bid  in bidsList:
        if  float(bid['price']) < float(highest_bid['bidprice']) :
            highest_bid = {"bidprice": bidsList[0]['price'],
                           "bidamount": bidsList[0]['amount']}
    return  [cheapest_ask,highest_bid]



def  find_Max_cheapest_price(maxE_orderbook):
    cheapest_ask = {}
    highest_bid = {}
    print(maxE_orderbook)
    if maxE_orderbook[0]['side'] == "ask":
        cheapest_ask = {"askprice": maxE_orderbook[0]['price'],
                        'askamount': maxE_orderbook[0]['volume']}
        highest_bid = {"bidprice": float(maxE_orderbook[0]['price'])-10000,
                       "bidamount": maxE_orderbook[0]['volume']}
    elif  maxE_orderbook[0]['side'] == "bid":
        highest_bid = {"bidprice": maxE_orderbook[0]['price'],
                       "bidamount": maxE_orderbook[0]['volume']}
        cheapest_ask = {"askprice": float(maxE_orderbook[0]['price'])+10000,
                        'askamount': maxE_orderbook[0]['volume']}


    for  order in maxE_orderbook:
        if  order['side'] == "ask"  and  float(cheapest_ask['askprice'])  < float(order['price']):
            cheapest_ask =  {"askprice": float(order['price']) , 'askamount':order['volume']}
        elif  order['side'] == "bid"  and  float(highest_bid['bidprice'])  < float(order['price']):
            highest_bid = {"bidprice": float(order['price']), 'bidamount': order['volume']}
    return [cheapest_ask,highest_bid]

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
maxE_orderbook = maxE.get_orderbook("ethusdt",limit=40)
max_price = find_Max_cheapest_price(maxE_orderbook)
bito = BitoproExchange()
bito_orderbook = bito.get_orderbook("eth_usdt")
bito_price = find_Bito_cheapest_price(bito_orderbook)

# binance = BinanceExchange()
# binance_orderbook =  binance .get_orderbook("ETHUSDT")
# binance_price  = find_Binance_cheapest_price(binance_orderbook)



#\nBinance:{binance_price}
print(f"Max:{max_price}\nBito:{bito_price}")

