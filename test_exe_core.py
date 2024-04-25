import _thread
import requests
import json
import flask
from flask_cors import CORS
import os


# 为线程定义一个函数
def service( threadName, delay, content):
            os.system(f'get_answer {content}')

# 创建两个线程
try:
   _thread.start_new_thread( service, ("Thread-1", 2, input()) )
   _thread.start_new_thread( service, ("Thread-2", 4, input()) )
except:
   print ("Error: 无法启动线程")

while 1:
   pass
exit()