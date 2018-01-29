import logging,sys



logger = logging.getLogger()#获取logger对象
formatter = logging.Formatter('%(asctime)s -%(levelname)-8s: %(message)s')#设置格式
file_handler = logging.FileHandler("test512.log")
file_handler.setFormatter(formatter)#指定输出格式
# 控制台日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.formatter = formatter  # 也可以直接给formatter赋值
# 为logger添加的日志处理器
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 指定日志的最低输出级别，默认为WARN级别
logger.setLevel(logging.INFO)

