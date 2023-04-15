from Crypto.Cipher import AES
from requests_html import HTMLSession

session = HTMLSession()


class Spider():
    def __init__(self):
        self.url = 'https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/comp/list?complexname=%E5%9B%9B%E5%B7%9D&pg=0&pgsz=15&total=0'
        self.header = {
            'Cookie': 'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c=1681205031,1681284994,1681285199; Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c=1681286491',
            'Host': 'jzsc.mohurd.gov.cn',
            'Referer': 'https://jzsc.mohurd.gov.cn/data/company?complexname=%E5%9B%9B%E5%B7%9D',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        }

        self.key = 'jo8j9wGw%6HbxfFn'
        self.v = '0123456789ABCDEF'

    def parse_url_start(self):
        """用第三方模块来模拟解密"""
        # todo 密钥key 跟 偏移量v 操作encode 用于解决 源代码中js加密过程
        #  key = d.a.enc.Utf8.parse("jo8j9wGw%6HbxfFn")
        #  v = d.a.enc.Utf8.parse("0123456789ABCDEF");
        key = self.key.encode()
        v = self.v.encode()
        response = session.get(self.url, headers=self.header).content.decode()
        # 先用python的bytes 模块来进行数据分析 Hex加密的数据
        text = bytes.fromhex(response)
        # todo 模拟解密new(密钥， 解密方式， 偏移量)
        aes = AES.new(key, AES.MODE_CBC, v)
        result = aes.decrypt(text).decode()
        print(result)


if __name__ == '__main__':
    s = Spider()
    s.parse_url_start()
