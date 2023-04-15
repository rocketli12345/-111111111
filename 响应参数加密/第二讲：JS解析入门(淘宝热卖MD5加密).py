# -*- coding: utf-8 -*-
# @Author : 阿尔法
# @File : day11_JS解析入门.py
# @Software: PyCharm
# time : 2022/9/19
"""
课题：
    第十一讲：JS解析入门
"""
# js逆向的分类
# 请求参数的逆向
# 响应数据的逆向
# 以上操作的流程是不一样的
# token = ''
# data = ''
# i = ''
# g = ''
# aa = token + "&" + i + "&" + g + "&" + data
"""1.常规的JS文件定位的几种方法"""
# 请求参数的逆向
# 基本流程：确定加密参数sign
#           通过常规的定位方法，定位js代码sign的生成位置
# 第一种定位：通过两个搜索窗口进行搜索，搜索加密参数关键字(一般直接搜索key值：sign)
    # 观察文件类型：一般的，不是js文件类型，直接pass掉(参数的加密，大多数都是js文件生成的)
    # 在通过观察判断确定加密参数生成位置之后：需要执行js调试(进行验证)
"""搜索结果是比较多的，需要一个一个文件去观察"""

# 第二种定位方法：通过xhr断点调试包的请求生成位置：直接定位到请求的构造位置
    # xhr断点直接拿地址的特征进行操作
    # 在定位到包构造位置：如果此时此刻，你做的是请求参数的逆向，是能够观察到这个加密参数的生成原理的

# 第三种定位方法：观察标签绑定JS事件(什么标签会触发这个包的请求--从而观察什么标签的JS绑定事件)
    # 特点：通过标签触发包的请求这一特性，定位加密参数这个包，由那个标签触发，然后通过事件监听，定位js文件
    # 当前标签没有绑定js事件，就要去观察该标签的父一级标签是否有绑定的js事件

# 第四种定位方法：观察该请求的栈和堆
    # 在启动器位置，记录的是该请求由哪一个js文件触发，(该请求关联的JS文件)
    # 那个js文件显示的结果最多，先观察谁，进入js之后，直接搜索关键字，从而定位到参数加密位置
"""以上四种定位js文件方法：是如何找到加密js文件：流程都是固定的"""


"""2.解析流程"""
# c.data：请求参数data值
# g：值是固定的，为12574478
# i: 时间戳，我们可以通过time模块生成
# d.token:
# 字符串拼接：d.token + "&" + i + "&" + g + "&" + c.data
# h(d.token + "&" + i + "&" + g + "&" + c.data)
# 通过h加密字符串拼接结果
# h:是加密方法hashlib提供的md5加密

"""
爬虫进阶：大家的爬虫进阶应该不是我教大家了，
# 带领大家去接单：拓展接单渠道，让大家把学费挣回来
# 到了晚上：我会在接单群穿插上课：接单课
# 接单课：讲解接单流程，接单项目案例，更先进的技术

对应大家报名的课程
全栈接单群：对应全栈接单群网盘
高薪接单群：对应高薪接单群网盘：每一节拓展课，自己去网盘里面看回放
群里面上课的案例的区别
接单群里面上课是拓展课程(不定期更新，不定期上课，课时无限)：
接单群里面上课----微信群里面上课----微信里面上课

爬虫基础班课时时长：本周五结课
我们JS逆向的课时：
    18节：
    我们这周全部都是JS逆向：
"""

"""3.案例实战"""
"""
# 流程思路分析：淘宝热卖
    1.抓包，定位商品数据包的位置
        # 数据同步异步加载的判断----异步加载
        # xhr没有数据包显示：两个搜索窗口搜索关键字(价格，商品名称...)，定位请求包
    2.确定请求加密参数(对比，通过对比网络请求包，初步确定加密参数)----sign
    3.验证2步骤的结果：执行js调试：需要打断点：在加密参数变量位置上下随便断点
    4.刷新网页，进入调试过程
        # 1.在调试过程中，通过观察每一个变量的值(变量C和变量K):
        # 2.通过观察：确定加密参数，观察出生成原理
        # 3.模拟重现
"""
from requests_html import HTMLSession
# 创建请求对象
session = HTMLSession()
import re, time, hashlib, json, os
from urllib.parse import quote
import os, xlwt, xlrd
from xlutils.copy import copy
# cookie过期时间：过期时间大概是半小时
cookie_str = """cna=Hb66HDpxbz8BASQJiRiMyouF; xlly_s=1; _m_h5_tk=60ab90dc48ce138b0ee988a47cb493e3_1681303509336; _m_h5_tk_enc=cc7186e266b93774b19db04ed577f4ba; l=fBNyLRLPN_06q1xOBO5BPurza77OmIRb8EVzaNbMiIEGa6whtegX4NCszwr2SdtjgTfc8etr24w81dKzy3adVxDDBecuBKWOAxJ6-bpU-L5..; tfstk=cKkVBFX0iKp4d-o9J82ZzstQx_VAZL4gRTrUiFezkDMMojFciR_TqXT_4lSPSSf..; isg=BHV1IUgwfQLruZm7t1e0xRzIhPEv8ikEqrdOfveaMew7zpXAv0I51INIGJJ4uEG8"""


class TBSpider(object):

    def __init__(self):
        """准备数据"""
        # 用户输入查询关键字
        self.user_input = input('请输入你想查询的商品名称：')
        self.start_url = 'https://h5api.m.taobao.com/h5/mtop.alimama.union.xt.en.api.entry/1.0/?'
        self.headers = {
            'cookie': cookie_str,
            'referer': 'https://uland.taobao.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
        }

    def parse_start_url(self):
        """
        解析起始的地址的请求参数
        """
        # for循环模拟翻页
        for page in range(5):
            print(f'\n\n正在采集商品--------------第{page}页---------------logging！！！\n\n\n\n')
            # 请求参数data
            data = {"pNum":page,"pSize":"60","refpid":"mm_26632258_3504122_32538762","variableMap":"{\"q\":\"" + self.user_input + "\",\"navigator\":false,\"clk1\":\"3ce9496b1971f96e0984a4f5737317df\",\"union_lens\":\"recoveryid:201_33.6.195.221_13954233_1663591192826;prepvid:201_33.63.246.42_13799804_1663592125450\",\"recoveryId\":\"201_33.43.43.30_19015607_1663593670370\"}","qieId":"36308","spm":"a2e0b.20350158.31919782","app_pvid":"201_33.43.43.30_19015607_1663593670370","ctm":"spm-url:a2e0b.20350158.search.1;page_url:https%3A%2F%2Fuland.taobao.com%2Fsem%2Ftbsearch%3Fspm%3Da2e0b.20350158.search.1%26keyword%3D%25E7%2594%25B5%25E8%2584%2591%26refpid%3Dmm_26632258_3504122_32538762%26clk1%3D3ce9496b1971f96e0984a4f5737317df%26upsId%3D3ce9496b1971f96e0984a4f5737317df%26pid%3Dmm_26632258_3504122_32538762%26union_lens%3Drecoveryid%253A201_33.6.195.221_13954233_1663591192826%253Bprepvid%253A201_33.63.246.42_13799804_1663592125450"}
            # 生成时间戳: 后续有字符串的拼接：一步转换到位
            time_temp = str(int(time.time() * 1000))
            # 生成sign: 需要参数data
            sign = self.parse_sign_func(time_temp, data)
            # 一部分参数主体
            params = f"jsv=2.5.1&appKey=12574478&t={time_temp}&sign={sign}&api=mtop.alimama.union.xt.en.api.entry&v=1.0&AntiCreep=true&timeout=20000&AntiFlood=true&type=jsonp&dataType=jsonp&callback=mtopjsonp2&data="
            # 处理data字典的url转码
            data_str = quote(f"{data}")
            # 完整地址的拼接
            url = self.start_url + params + data_str
            # 发生请求，获取相应
            response = session.get(url, headers=self.headers).content.decode()
            self.parse_response_data(response)

    def parse_sign_func(self, time_temp, data):
        """
        生成sign：h(d.token + "&" + i + "&" + g + "&" + c.data)
        i: time_temp
        g: 12574478
        c.data: data
        """
        # 正则从cookie中获取token值
        token = re.findall('m_h5_tk=(.*?)_', cookie_str)[0]
        # 加密之前的字符串拼接
        sign_str = token + "&" + time_temp + "&" + '12574478' + "&" + f"{data}"
        # 执行加密
        sign = hashlib.md5(sign_str.encode('utf-8')).hexdigest()
        print(sign)
        return sign

    def parse_response_data(self, response):
        """
        解析地址的响应
        """
        json_dict_data = json.loads(response[12:-1])['data']['recommend']['resultList']
        for json_data in json_dict_data:
            # 商品名称
            itemName = json_data['itemName']
            # 商品的id
            shop_id = json_data['itemId']
            # 店铺名称
            shopTitle = json_data['shopTitle']
            # 发货城市
            provcity = json_data['provcity']
            # 商品详情页地址
            url = json_data['url']
            # 月销量
            monthSellCount = json_data['monthSellCount']
            # 商品原价
            price = json_data['price']
            # 商品的优惠价格
            promotionPrice = json_data['promotionPrice']
            data = {
                self.user_input: [shop_id, itemName, price, promotionPrice, monthSellCount, provcity, shopTitle, url]
            }
            self.parse_save_data(data)
            print(f"商品：{itemName}-----------数据保存完成！")

    def parse_save_data(self, data):
        """
        将数据保存到excel中
        """
        # 获取表的名称
        sheet_name = [i for i in data.keys()][0]
        # 创建保存excel表格的文件夹
        # os.getcwd() 获取当前文件路径
        os_mkdir_path = os.getcwd() + '/淘宝商品数据/'
        # 判断这个路径是否存在，不存在就创建
        if not os.path.exists(os_mkdir_path):
            os.mkdir(os_mkdir_path)
        # 判断excel表格是否存在           工作簿文件名称
        os_excel_path = os_mkdir_path + '数据.xls'
        if not os.path.exists(os_excel_path):
            # 不存在，创建工作簿(也就是创建excel表格)
            workbook = xlwt.Workbook(encoding='utf-8')
            """工作簿中创建新的sheet表"""  # 设置表名
            worksheet1 = workbook.add_sheet(sheet_name, cell_overwrite_ok=True)
            """设置sheet表的表头"""
            sheet1_headers = ('商品id', '商品名称', '原价', '优惠价', '月销量', '发货城市', '店铺名称', '商品详情页地址')
            # 将表头写入工作簿
            for header_num in range(0, len(sheet1_headers)):
                # 设置表格长度
                worksheet1.col(header_num).width = 2560 * 3
                # 写入表头        行,    列,           内容
                worksheet1.write(0, header_num, sheet1_headers[header_num])
            # 循环结束，代表表头写入完成，保存工作簿
            workbook.save(os_excel_path)
        """=============================已有工作簿添加新表==============================================="""
        # 打开工作薄
        workbook = xlrd.open_workbook(os_excel_path)
        # 获取工作薄中所有表的名称
        sheets_list = workbook.sheet_names()
        # 如果表名称：字典的key值不在工作簿的表名列表中
        if sheet_name not in sheets_list:
            # 复制先有工作簿对象
            work = copy(workbook)
            # 通过复制过来的工作簿对象，创建新表  -- 保留原有表结构
            sh = work.add_sheet(sheet_name)
            # 给新表设置表头
            excel_headers_tuple = ('商品id', '商品名称', '原价', '优惠价', '月销量', '发货城市', '店铺名称', '商品详情页地址')
            for head_num in range(0, len(excel_headers_tuple)):
                sh.col(head_num).width = 2560 * 3
                #               行，列，  内容，            样式
                sh.write(0, head_num, excel_headers_tuple[head_num])
            work.save(os_excel_path)
        """========================================================================================="""
        # 判断工作簿是否存在
        if os.path.exists(os_excel_path):
            # 打开工作簿
            workbook = xlrd.open_workbook(os_excel_path)
            # 获取工作薄中所有表的个数
            sheets = workbook.sheet_names()
            for i in range(len(sheets)):
                for name in data.keys():
                    worksheet = workbook.sheet_by_name(sheets[i])
                    # 获取工作薄中所有表中的表名与数据名对比
                    if worksheet.name == name:
                        # 获取表中已存在的行数
                        rows_old = worksheet.nrows
                        # 将xlrd对象拷贝转化为xlwt对象
                        new_workbook = copy(workbook)
                        # 获取转化后的工作薄中的第i张表
                        new_worksheet = new_workbook.get_sheet(i)
                        for num in range(0, len(data[name])):
                            new_worksheet.write(rows_old, num, data[name][num])
                        new_workbook.save(os_excel_path)


if __name__ == '__main__':
    t = TBSpider()
    t.parse_start_url()


