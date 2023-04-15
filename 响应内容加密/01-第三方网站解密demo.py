from requests_html import HTMLSession

session = HTMLSession()


#  通过第三方工具获取信息

class Spider():
    def __init__(self):
        self.url = 'https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/comp/list?complexname=%E5%9B%9B%E5%B7%9D&pg=0&pgsz=15&total=0'
        self.header = {
            'Cookie': 'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c=1681205031,1681284994,1681285199; Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c=1681286491',
            'Host': 'jzsc.mohurd.gov.cn',
            'Referer': 'https://jzsc.mohurd.gov.cn/data/company?complexname=%E5%9B%9B%E5%B7%9D',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        }
        self.url1 = 'http://tool.chacuo.net/cryptaes'
        self.header1 = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': '__yjs_duid=1_114c0f09f1aef3511c5de2afe2d747501681287196795; Hm_lvt_ef483ae9c0f4f800aefdf407e35a21b3=1681287196; __bid_n=1877486af88d11caed4207; FPTOKEN=dOfSyMZUMsSgG/l586MF4fKJhM7EAN1AVxu7y4RYZjruy/WsNzCy5y4NuoUxgGDhwg9W6GBr6JkjZ1EgMuctmVWooLQFYOZSYyzfSUUhDdAhuaLzd/Btk2loAM+A9ope8pNY1AC/5zPrxzMQDWkXWIFYmHO6TU1QCnvUxo/vpeOqz5A39CPCRueWQGOY7nXHTXWT8Iw4ESUx1jqdcR9Wtol64jBEScYUKVI0S+Yy6jbVo9+BjEPUKzntkg32vpioQJn9e0+Jq8mlfGlbXOvKcFKlT7uW9JBtSf+VvK2C67e3qqx4B6JfCcJGB61CmIefxAvCXWXTHR9rpkuSFtR+qM8c3RM0vHTh1mZlAjw6cz2Y201tuLOSTzOmtD22QK+NFb/uZvUZuSO9bomapc+daQ==|wz2KPm7D4APzSpJw5ve3pXS6TYGLl565mXBsJeuS2Fc=|10|fdc0f6506dd0fad3cb4441d642576b39; __gads=ID=0a1957ec44a6e30c-225bece42cdd0042:T=1681287198:RT=1681287198:S=ALNI_MbzsKu9pVkU8wsGpj0Bk4HaWw1CsA; __gpi=UID=00000bf2d6115fb3:T=1681287198:RT=1681287198:S=ALNI_MY2FbZc9wRBA84X1DzzhxW1pmyF-Q; Hm_lpvt_ef483ae9c0f4f800aefdf407e35a21b3=1681287833',
            'Referer': 'http://tool.chacuo.net/cryptaes',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        }

    def parse_url_start(self):
        response = session.get(self.url, headers=self.header).content.decode()
        data = {
            'data': response,
            'type': 'aes',
            'arg': 'm=cbc_pad=pkcs7_block=128_p=jo8j9wGw%6HbxfFn_i=0123456789ABCDEF_o=1_s=utf-8_t=1'
        }
        json_parse = session.post(self.url1, headers=self.header1, data=data).json()
        print(json_parse)


if __name__ == '__main__':
    s = Spider()
    s.parse_url_start()
