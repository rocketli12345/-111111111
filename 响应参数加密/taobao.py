# todo 变化数据 t sign
from requests_html import HTMLSession

session = HTMLSession()
import time, re, hashlib
from urllib.parse import quote
cookie_str = """cna=Hb66HDpxbz8BASQJiRiMyouF; _m_h5_tk=5522d231ffe4021027932707635da6cd_1681292881606; _m_h5_tk_enc=63fe9fadf23cd1084d416c0096d3a0b3; xlly_s=1; tfstk=cOohBiOfp2zC4rt-1XZB0xzsMXLOwlTUO0oZbdhGtUoAQOfc1N7qFp9g9IOFP; l=fBNyLRLPN_06q-sFKOfaFurza77OSIRYYuPzaNbMi9fPO2CB5SbAW1gz9LT6C3GVFsjwR3o-P8F6BeYBq3xonxvtNSVsr4DmndLHR35..; isg=BDMz57b3U-wLdB89BR1qW86iwjddaMcq2O1IeOXQj9KJ5FOGbThXepFynhQKgB8i"""


class TaoBao():
    def __init__(self):
        self.input = input('输入你要获取的内容关键词：')
        self.url = 'https://h5api.m.taobao.com/h5/mtop.alimama.union.xt.en.api.entry/1.0/?'
        # jsv=2.5.1&appKey=12574478&t=1681189256612&sign=d04547d1f946006a9b110aeee22a8151&api=mtop.alimama.union.xt.en.api.entry&v=1.0&AntiCreep=true&timeout=20000&AntiFlood=true&type=jsonp&dataType=jsonp&callback=mtopjsonp2&data=
        self.header = {
            'cookie': cookie_str,
            'referer': 'https://uland.taobao.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        }

    def parse_url(self):
        """

        :return:
        """
        data = {"pNum": 0, "pSize": "60", "refpid": "mm_26632258_3504122_32538762",
                "variableMap": "{\"q\":\"" + self.input + "\",\"navigator\":false,\"clk1\":\"09dac7ac1ab94813640a7ec8f45e31af\",\"recoveryId\":\"201_33.7.72.85_15393149_1681189256546\"}",
                "qieId": "36308", "spm": "a2e0b.20350158.31919782", "app_pvid": "201_33.7.72.85_15393149_1681189256546",
                "ctm": "spm-url:;page_url:https%3A%2F%2Fuland.taobao.com%2Fsem%2Ftbsearch%3Frefpid%3Dmm_26632258_3504122_32538762%26keyword%3D%25E7%25BD%2591%25E8%25B4%25AD%25E5%25B9%25B3%25E5%258F%25B0%25E6%258E%25A8%25E8%258D%2590%26clk1%3D09dac7ac1ab94813640a7ec8f45e31af%26upsId%3D09dac7ac1ab94813640a7ec8f45e31af"}

        t = str(int(time.time() * 1000))
        sign = self.parse_sign(t, data)
        data_url = quote(f'{data}')
        param = f'jsv=2.5.1&appKey=12574478&t={t}&sign={sign}&api=mtop.alimama.union.xt.en.api.entry&v=1.0&AntiCreep=true&timeout=20000&AntiFlood=true&type=jsonp&dataType=jsonp&callback=mtopjsonp2&data='
        url = self.url + param + data_url
        response = session.get(url, headers=self.header).content.decode()
        print(response)

    def parse_sign(self, t, data):
        """
         todo 数据sign构成元素 j = h(d.token + "&" + i + "&" + g + "&" + c.data)
         t:构成元素是时间戳
         sign : d04547d1f946006a9b110aeee22a8151
        :return:
        """
        token = re.findall('_m_h5_tk=(.*?)_', cookie_str)[0]

        sign_content = token + "&" + t + "&" + '12574478' + "&" + f'{data}'
        sign = hashlib.md5(sign_content.encode('utf-8')).hexdigest()
        print(sign)
        return sign


if __name__ == '__main__':
    a = TaoBao()
    a.parse_url()