import re, time, hashlib
from urllib.parse import quote

from requests_html import HTMLSession

session = HTMLSession()

cookie_str ="""cna=Hb66HDpxbz8BASQJiRiMyouF; xlly_s=1; _m_h5_tk=8f5988da92eb56e368aea65992802fdd_1681198195105; _m_h5_tk_enc=8bec96b5b3c8726ba08ab4ea21f8414c; tfstk=c6ZhBI1XpyuQ4-s81WiC05EODm7OwB7EOurabOeXci7MLpfc1F84F96i9s1eP; l=fBNyLRLPN_06qV3FBOfanurza77OSIRYDuPzaNbMi9fPOF1p5xjhW1gJg589C3hVFsSyR3o-P8F6BeYBqn4jPGKnNSVsr4DmnmOk-Wf..; isg=BL29SSoTheid-SGDP698HQTQzBm3WvGsop8Wpn8C-ZRDtt3oR6oBfItgYerwEglk"""
# cookie_str = """cna=xwOqGxUnJSkCAa8JeEvy46rh; _m_h5_tk=40ab2edad4e5137f05affd1351636fc5_1663598686307; _m_h5_tk_enc=664a440d1e61a52f8964eccea62328d4; xlly_s=1; tfstk=cAfRBvN3roqoeiyxvweDYjmrfdUcwJEpc4tn96vSpqEk_n1cX1f9kQwWRh-8k; l=eBjpqrTnTx8ClIZXBOfwourza77OSIRAguPzaNbMiOCPOI1p5T6hW6oTw5L9C3GVhsCDR3yZyToBBeYBqI2jPGKnNSVsr4Dmn; isg=BAkJZSv8jpC7P3JvOaLI-xJLGDVjVv2IQCSkFqt-hfAv8ikE86YNWPckNFbEqpXA"""


class TaoBao():
    def __init__(self):
        self.input = input("输入你要输入的内容:")
        self.url = f'https://h5api.m.taobao.com/h5/mtop.alimama.union.xt.en.api.entry/1.0/?'
        # jsv=2.5.1&appKey=12574478&t=1681123301532&sign=4a09f2ac09e6e39bbfa8e1e105636894&api=mtop.alimama.union.xt.en.api.entry&v=1.0&AntiCreep=true&timeout=20000&AntiFlood=true&type=jsonp&dataType=jsonp&callback=mtopjsonp2&data={self.input}
        self.header = {
            'cookie':  cookie_str,
            'referer': 'https://uland.taobao.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
        }


    def parse_first_url(self):
        # todo 请求参数
        data = {
            "pNum": 0, "pSize": "60", "refpid": "mm_26632258_3504122_32538762",
             "variableMap": "{\"q\":\"" + self.input +"\",\"navigator\":false,\"clk1\":\"3cc769c45e3b6ec05441e79624dabe21\",\"recoveryId\":\"201_33.5.131.176_15240984_1681123301264\"}",
             "qieId": "36308", "spm": "a2e0b.20350158.31919782", "app_pvid": "201_33.5.131.176_15240984_1681123301264",
             "ctm": "spm-url:;page_url:https%3A%2F%2Fuland.taobao.com%2Fsem%2Ftbsearch%3Frefpid%3Dmm_26632258_3504122_32538762%26keyword%3D%25E7%25BD%2591%25E8%25B4%25AD%25E5%25B9%25B3%25E5%258F%25B0%25E6%258E%25A8%25E8%258D%2590%26clk1%3D3cc769c45e3b6ec05441e79624dabe21%26upsId%3D3cc769c45e3b6ec05441e79624dabe21"}

        # todo 时间搓
        b = str(int(time.time() * 1000))
        sign = self.parse_func(b, data)
        param = f'jsv=2.5.1&appKey=12574478&t={b}&sign={sign}&api=mtop.alimama.union.xt.en.api.entry&v=1.0&AntiCreep=true&timeout=20000&AntiFlood=true&type=jsonp&dataType=jsonp&callback=mtopjsonp2&data='
        data_url = quote(f'{data}')
        url = self.url + param + data_url
        response = session.get(url, headers=self.header).content.decode()
        print(response)


    def parse_func(self, i, data):
        """
          # j = h(d.token + "&" + i + "&" + g + "&" + c.data)
        :return:
        """
        # todo 获取token
        token = re.findall('_m_h5_tk=(.*?)_', cookie_str)[0]

        sign_str = token + "&" + i + "&" + "12574478" + "&" + f'{data}'
        sign = hashlib.md5(sign_str.encode('utf-8')).hexdigest()
        print(sign)
        return sign

    def parse_response_data(self, response):
        print(response)


if __name__ == '__main__':
    a = TaoBao()
    a.parse_first_url()
