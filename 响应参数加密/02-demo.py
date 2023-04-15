from requests_html import HTMLSession

session = HTMLSession()
import time, re, hashlib
from urllib.parse import quote

cookie_str = """cna=Hb66HDpxbz8BASQJiRiMyouF; xlly_s=1; _m_h5_tk=60ab90dc48ce138b0ee988a47cb493e3_1681303509336; _m_h5_tk_enc=cc7186e266b93774b19db04ed577f4ba; l=fBNyLRLPN_06qArNKOfaFurza77OSIRYYuPzaNbMi9fP9I5B5kNlW1gPPJY6C3GVFsjwR3o-P8F6BeYBq3xonxvtNSVsr4DmndLHR35..; tfstk=cxfhBsZjJ9JC_vFRfMOQgZ8vMWeOZj2eA_5N_PIiH-WRT6fNilMZ3aaQSHEbYY1..; isg=BOXl0Zqb7dLQVAkLh2cEFSwY9KEfIpm0usc-LufKoZwr_gVwr3KphHOYiGKIW7Fs"""


class Spider():
    def __init__(self):
        self.input = input('输入你想要获取的内容：')
        self.start_url = 'https://h5api.m.taobao.com/h5/mtop.alimama.union.xt.en.api.entry/1.0/?'
        self.header = {
            'cookie': cookie_str,
            'referer': 'https://uland.taobao.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        }

    def parse_start_url(self):
        """
        t : 时间戳
        sign : j = h(d.token + "&" + i + "&" + g + "&" + c.data)
        :return:
        """
        for page in range(5):
            t = str(int(time.time() * 1000))
            data = {"pNum": page, "pSize": "60", "refpid": "mm_26632258_3504122_32538762",
                    "variableMap": "{\"q\":\"" + self.input + "\",\"navigator\":false,\"clk1\":\"f504a5aa870a7480e985f72d3ae7a4ca\",\"recoveryId\":\"201_33.7.68.244_15637036_1681291864766\"}",
                    "qieId": "36308", "spm": "a2e0b.20350158.31919782",
                    "app_pvid": "201_33.7.68.244_15637036_1681291864766",
                    "ctm": "spm-url:;page_url:https%3A%2F%2Fuland.taobao.com%2Fsem%2Ftbsearch%3Frefpid%3Dmm_26632258_3504122_32538762%26keyword%3D%25E7%25BD%2591%25E8%25B4%25AD%25E5%25B9%25B3%25E5%258F%25B0%25E6%258E%25A8%25E8%258D%2590%26clk1%3Df504a5aa870a7480e985f72d3ae7a4ca%26upsId%3Df504a5aa870a7480e985f72d3ae7a4ca"}
            sign = self.parse_sign(t, data)
            data_url = quote(f'{data}')  # 用于编码 data
            param = f'jsv=2.5.1&appKey=12574478&t={t}&sign={sign}&api=mtop.alimama.union.xt.en.api.entry&v=1.0&AntiCreep=true&timeout=20000&AntiFlood=true&type=jsonp&dataType=jsonp&callback=mtopjsonp2&data='
            url = self.start_url + param + data_url
            response = session.get(url, headers=self.header).content.decode()
            self.parse_content(response)
            print(response)

    def parse_sign(self, t, data):
        # todo sign: j = h(d.token + "&" + i + "&" + g + "&" + c.data)
        token = re.findall('_m_h5_tk=(.*?)_', cookie_str)[0]
        sign_data = token + "&" + t + "&" + '12574478' + "&" + f'{data}'
        sign = hashlib.md5(sign_data.encode('utf-8')).hexdigest()
        print(sign)
        return sign

    def parse_content(self, response):
        pass


if __name__ == '__main__':
    s = Spider()
    s.parse_start_url()
