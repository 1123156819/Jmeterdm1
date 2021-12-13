"""
# 1创建yaml格式恩建
# 2 读取这个文件
# 3 输出这个文件
"""

# 2 读取这个文件
# 1 导入yaml包
# import yaml
#
# # 2 打开文件 encoding = "utf-8"
# with open("./data.yml", "r",encoding="utf-8") as f:
#     # 3 使用yaml读取文件
#     r = yaml.safe_load(f)
#     # 3 输出这个文件
#     print(r)


from utils.YamlUtil import YamlReader

# res = YamlReader("./data.yml").data()
res = YamlReader("./data.yml").data_all()
print(res)



