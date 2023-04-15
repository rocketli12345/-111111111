# a = input('输入你要输入的内容：')
import re
import time
from urllib.parse import quote
b = int(time.time() * 1000)
data = {"pNum": 0, "pSize": "60", "refpid": "mm_26632258_3504122_32538762", ' \
                      '"variableMap": "{\"q\":\" 网购\",\"navigator\":false,\"clk1\":\"09dac7ac1ab94813640a7ec8f45e31af\",\"recoveryId\":\"201_33.7.72.85_15393149_1681189256546\"}",
        "qieId": "36308", "spm": "a2e0b.20350158.31919782", "app_pvid": "201_33.7.72.85_15393149_1681189256546",
        "ctm": "spm-url:;page_url:https%3A%2F%2Fuland.taobao.com%2Fsem%2Ftbsearch%3Frefpid%3Dmm_26632258_3504122_32538762%26keyword%3D%25E7%25BD%2591%25E8%25B4%25AD%25E5%25B9%25B3%25E5%258F%25B0%25E6%258E%25A8%25E8%258D%2590%26clk1%3D09dac7ac1ab94813640a7ec8f45e31af%26upsId%3D09dac7ac1ab94813640a7ec8f45e31af"}

cookie_str = """cna=Hb66HDpxbz8BASQJiRiMyouF; xlly_s=1; _m_h5_tk=8f5988da92eb56e368aea65992802fdd_1681198195105; _m_h5_tk_enc=8bec96b5b3c8726ba08ab4ea21f8414c; l=fBNyLRLPN_06qr2hKOfaFurza77OSIRYYuPzaNbMi9fP_JCB5LCPW1gJdbT6C3GVFsjwR3o-P8F6BeYBq3xonxvtNSVsr4DmndLHR35..; tfstk=cnofBgql1sffuXtGmS9rVAkK2bZ1wkd7EENxhIRzzA33sW1cvMPC8VuGZlyTF; isg=BLGxbbDkcXTWSt1n02sIcbDcwD1LniUQlgOKApPGrXiXutEM2-414F_c3E7cQr1I"""
token = re.findall('_m_h5_tk=(.*?)_', cookie_str)[0]
print(token)
data_url = quote(f'{data}')
print(data_url)

