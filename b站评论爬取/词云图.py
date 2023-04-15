from PIL import Image
import stylecloud

# 使用前只需要将数据用过big_list.append() 将数据传入即可
big_list = []
big_list.append()


def parse_c_y_img(self):
    """生成词云图"""
    data = ''.join(big_list)
    stylecloud.gen_stylecloud(text=data,
                              font_path=r"C:\Users\Administrator\Desktop\UDDigiKyokashoN-B.ttc")  # 生词词云图路径用r转化
    Image.open("stylecloud.png")
