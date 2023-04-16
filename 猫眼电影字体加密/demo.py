str = ' .9241536807'
font = ['glyph00000', 'x', 'uniEB19', 'uniE3EC', 'uniF7D2', 'uniED30', 'uniF3E8', 'uniF11C', 'uniEA60', 'uniEF28', 'uniEA6F', 'uniE3DF']

dic = {}
for a, b in zip(str, font):
    dic[b[3:]] = a
print(dic)

# {'ph00000': ' ', '': '.', 'EB92': '7', 'E8D7': '3', 'F7FF': '6', 'F85E': '1', 'E99C': '2', 'F1FC': '8', 'F726': '0', 'E8EE': '4', 'E9EA': '9', 'ECDC': '5'}
#
# ['\ue8ee\ue8ee\uf85e\uf726.\uf726', '\ue8ee\uecdc\ue8d7\ueb92.\uf726', '\ue99c\uf1fc\uf1fc\ue8ee.\uf726', '\uf85e.\ue8d7\ue8d7', '\ue99c\uecdc\ue8ee\uf1fc.\uf726', '\ue99c\uecdc\ue8ee\uf1fc.\uf726', '\uf85e\uf7ff\ue99c\ue99c.\uf726', '\uecdc.\ue8d7\uf7ff', '\uf85e\uecdc\uecdc\uf85e.\uf726', '\ue8d7.\uf7ff\ue8d7', '\ue9ea\uf85e\ue8d7.\uf726', '\ue8ee\ue9ea\uecdc\uf726.\uf726', '\ue8ee\ue99c\uecdc.\uf726', '\uecdc\ue8d7\ue99c.\uf726', '\ue8d7\uf1fc\uecdc.\uf726', '\ue8ee\ue8d7\ue99c\uf726.\uf726', '\ue8d7\ue99c\ue99c.\uf726', '\ue8d7\uf7ff\uf7ff\ue9ea.\uf726', '\ue99c\ue9ea\uf85e.\uf726', '\uf85e.\ue8d7\ue99c']
