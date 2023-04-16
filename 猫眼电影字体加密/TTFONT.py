# from fontTools.ttLib import TTFont
#
# font_data = TTFont("文件名称")
# font_data.saveXML("文件名称")
# gly_list = font_data.getGlyphOrder()
# 得到数据
# 得到的密文数据前三个不要通过列表下滑[3:] 如demo 所示

from fontTools.ttLib import TTFont

font_data = TTFont("e3dfe524.woff")
font_data.saveXML("e3dfe524.woff")
gly_list = font_data.getGlyphOrder()
print(gly_list)
# ['glyph00000', 'x', 'uniEB92', 'uniE8D7', 'uniF7FF', 'uniF85E', 'uniE99C', 'uniF1FC', 'uniF726', 'uniE8EE', 'uniE9EA', 'uniECDC']