from Crypto.Cipher import AES
from requests_html import HTMLSession

session = HTMLSession()


class Spider():
    def __init__(self):
        self.url = 'https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/comp/list?complexname=%E5%9B%9B%E5%B7%9D&pg=0&pgsz=15&total=0'
        self.header = {
            'Cookie': 'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c=1681284994,1681285199,1681296162,1681367076; Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c=1681367463',
            'Host': 'jzsc.mohurd.gov.cn',
            'Referer': 'https://jzsc.mohurd.gov.cn/data/company?complexname=%E5%9B%9B%E5%B7%9D',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        }
        self.key = 'jo8j9wGw%6HbxfFn'
        self.v = '0123456789ABCDEF'

    def parse_url(self):
        """
        通过python内置函数来实现转化
        :return:
        """
        # 首先通过对密钥跟偏移量进行加码
        key = self.key.encode()
        v = self.v.encode()
        text = session.get(self.url, headers=self.header).content.decode()
        # 用内置函数来解码hex的加密
        response = bytes.fromhex(text)
        # 然后还原方法
        aes = AES.new(key, AES.MODE_CBC, v)
        result = aes.decrypt(response).decode()
        print(result)


if __name__ == '__main__':
    s = Spider()
    s.parse_url()