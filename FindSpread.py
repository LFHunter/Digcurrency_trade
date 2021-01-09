from  DigExchangeLib.BitoproExchange import BitoproExchange
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
def  find_cheapest_price(asksList):
    cheapestinfo = {"price":asksList[0]['price']}
    for  ask  in asksList:
        if  float(ask['price']) < float(cheapestinfo['price']) :
            cheapestinfo = ask
    print(cheapestinfo)
    return  cheapestinfo

bito = BitoproExchange()
bito_orderbook = bito.get_orderbook("yfi_usdt")
find_cheapest_price(bito_orderbook['asks'])