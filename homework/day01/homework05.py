# 格式化输出当前时间： 年-月-日 时:分:秒
import time
print(time.time())#时间戳
print(time.localtime(time.time())) #本地时间
print(time.strftime('%y-%m-%d',time.localtime(time.time()))) #本地时间
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))