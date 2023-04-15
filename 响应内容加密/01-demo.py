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
        self.url1 = 'http://tool.chacuo.net/cryptaes'
        self.header1 = {
            'Cookie': '__yjs_duid=1_114c0f09f1aef3511c5de2afe2d747501681287196795; __bid_n=1877486af88d11caed4207; __gads=ID=0a1957ec44a6e30c-225bece42cdd0042:T=1681287198:RT=1681287198:S=ALNI_MbzsKu9pVkU8wsGpj0Bk4HaWw1CsA; Hm_lvt_ef483ae9c0f4f800aefdf407e35a21b3=1681287196,1681296502,1681368406; Hm_lpvt_ef483ae9c0f4f800aefdf407e35a21b3=1681368406; FPTOKEN=h7ZxEw/UXZLXYD12We4HMMlLmQTs6ziNiMaZvMMl7j6Fmls+O9yPmZ7Q6yzTjlkm0x1ctGkhi1pBHbYPePxbw3kymOsq3NOuHprcdnQmKEO/M1vr4tK/bGQuBpmkkMVRUVU0l72tiuCJOaI/tKbzp+VrmatBk0dYjROzJIaznMk8IljXhi/IF2otqSG+W0oqJfEu6RzAh42yJ583L+pQg9nh3bz3r2zR0IwLIbpuEYuIY8pWLQUrr0W0bi9npv8gC6FrUXm8KgQjvBH5xiKZezW9Sib4lwVs+Sy36AXg8eYFYVuVJIFCUQZkpgLpEKdGTNUDPRjWxaBN1yXgs7/SApShqT/V3tmM68PQAy6aweRB39lXsXGn7fpnetizSHVH0BMiLHo6p6GlwUwPA2OQ4w==|ynRgflepba9zwoigg3VjE6gqd+WL3QfoDwUP7M9aiyk=|10|d2b77c1160a7bc0b7a000a019e491ade; __gpi=UID=00000bf2d6115fb3:T=1681287198:RT=1681368406:S=ALNI_MY2FbZc9wRBA84X1DzzhxW1pmyF-Q',
            'Referer': 'http://tool.chacuo.net/cryptaes',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        }

    def parse_get(self):
        """
        主要逻辑是用过第三方软件进行解密然后通过访问数据得出
        :return:
        """
        # .content.decode()是解决乱码问题
        response = session.get(self.url, headers=self.header).content.decode()
        # 因为要通过post请求获取信息
        data = {
            'data': response,
            'type': 'aes',
            'arg': 'm=cbc_pad=pkcs7_block=128_p=jo8j9wGw%6HbxfFn_i=0123456789ABCDEF_o=1_s=utf-8_t=1'
        }
        # 当遇到json数据时候 用.json()来解决解码问题
        text = session.post(self.url1, headers=self.header1, data=data).json()
        print(text)


if __name__ == '__main__':
    s = Spider()
    s.parse_get()