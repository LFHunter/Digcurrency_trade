import  requests
import  pprint
class  MaxExchange:
    def __init__(self):
        self.domain = "https://max-api.maicoin.com"
        self.request =   requests.Session()
        self.cookie = ''

    def  get_orderbook(self,coinpair,limit=10):
        #https://max-api.maicoin.com/api/v2/trades?market=btctwd&order_by=desc&pagination=true&page=1&limit=5&offset=0
        url = f"{self.domain}/api/v2/trades?market={coinpair}&order_by=desc&pagination=true&page=1&limit={limit}&offset=0"
        print(url)
        headers = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                   "accept-encoding": "gzip, deflate, br",
                   "accept-language": "en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7,ja;q=0.6",
                   "cache-control": "max-age=0",
                   "cookie": "_fbp=fb.1.1606834828218.887065729; _hjid=e5254de7-cf42-4f44-b67d-c2241a192437; _hjTLDTest=1; _gid=GA1.2.385297035.1610183138; _hjAbsoluteSessionInProgress=0; _ga_V0KCMFFN8F=GS1.1.1610200849.6.1.1610201624.0; _ga=GA1.1.1087359578.1606834828",
                   "upgrade-insecure-requests": "1",
                   "user-agent": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
                   }

        resp = self.request.get(url=url, allow_redirects=True, headers=headers, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            #print(data)
            return data

if __name__ == '__main__':
    bt = MaxExchange()
    bt.get_orderbook("btcusdt",limit=5)
    # 'price': '1140373.1',
    #'volume': '0.00182733'
