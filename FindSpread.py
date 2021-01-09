from  DigExchangeLib.BitoproExchange import BitoproExchange
from  DigExchangeLib.MaxExchange import MaxExchange
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
def  find_Bito_cheapest_price(asksList):
    cheapestinfo = {"price":asksList[0]['price'],'amount':asksList[0]['amount']}
    for  ask  in asksList:
        if  float(ask['price']) < float(cheapestinfo['price']) :
            cheapestinfo = ask
    print(cheapestinfo)
    return  cheapestinfo



def  find_Max_cheapest_price(maxE_orderbook):
    cheapestinfo = {"price": maxE_orderbook[0]['price'], 'amount':maxE_orderbook[0]['volume']}
    for  order in maxE_orderbook:
        if  order['side'] == "ask"  and  float(cheapestinfo['price'])  < float(order['price']):
            cheapestinfo =  {"price": float(order['price']) , 'amount':order['volume']}
    print(cheapestinfo)
    return cheapestinfo

"""Max:
 btc/eth/ltc/bch/mith/xrp/max/usdt  twd  
 eth  btc
btc/eth/ltc/bch/mith/xrp/max/sand       usdt 
 """


maxE = MaxExchange()
maxE_orderbook = maxE.get_orderbook("ethusdt",limit=4)
find_Max_cheapest_price(maxE_orderbook)
bito = BitoproExchange()
bito_orderbook = bito.get_orderbook("eth_usdt")
find_Bito_cheapest_price(bito_orderbook['asks'])


