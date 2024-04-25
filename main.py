"""
本项目仅限于SLSChatAnyWhere合作方、SLSChatAnyWhere开发者使用，禁
止商业用途。商业用途单独审批许可证，当团队/企业拿到本文件时，默认拥有
一个月的商业用途许可证，在合作方停止合作后一个月，证书默认取消！

------------------------------------------------------------
|            SLSChatAnyWhere API 2.0.6(紧急恢复版)           |
------------------------------------------------------------
|         1个月的长期商业用途许可证，可无限次使用，可商用。     |
------------------------------------------------------------
"""
'''
API LINK

GET API
---------------------------------------
/AI/v3-get/xfxh?content={content}
/AI/v3-get/chatgpt?content={content}
/AT/CORS?url={url}
---------------------------------------

POST API
----------------------------------------

'''


from flask import Flask, request, jsonify, render_template
import requests
from flask_cors import CORS
import json
import random
import _thread
import _thread
import requests
import json
import flask
from flask_cors import CORS
#from os import system
from os import popen

ap = 13518062036
qq = 2295326064
ae = "liu_qinyu@outlook.com"

request_error = {}

#Flask与CORS初始化
app = Flask(__name__)
CORS(app,resources=r'/*')

#==========================ETool==========================#
class ETool:
    '''
    # EasyTool函数v1.0.0\n
    ### 需要Random库
    '''
    def a(text_a:str):
        '''
        Yes/No选择
        '''
        tdata_a = input(f"{text_a}(y/n)?")
        if tdata_a.lower() == 'y':
            return True
        else:
            return False

    def b(text_b):
        '''
        相当于INPUT
        '''
        tdata_b = input(f"{text_b}:")
        return tdata_b
    
    def c(num,gs:list):
        '''
        gs是列表，分别指 0-num 指什么。num指的是输出选项数量
        返回e表示选择有问题
        返回 数字 则正常

        nz_themes = []
        '''
        print("选择")
        for i in range(0,num):
            print(f"[{i}]{gs[i]}")
        ans = int(input("选择："))
        if ans > num:
            return 'e'
        if ans <= num:
            return ans+1

    def d(list_dt:list):
        '''
        # Random的choice优化版\n
        ## 需要Random库提供支持
        ### :P
        '''
        sysr = random.SystemRandom()
        return sysr.choice(list_dt)
    
    def ePassword(long:int,tszf:bool):
        '''
        # EasyPassword v1.0
        # 快速的生成密码
        ### 参数详解
        long 密码长度,INT\n
        tszf 是否有特殊字符,Bool
        '''
        sysr = random.SystemRandom()
        random.seed(0x1010)  # 设置随机种子数
        # 设置种子选择空间
        #带特殊字符
        s_dtszf = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
        #不带特殊字符
        s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        if tszf:
            s = s_dtszf
        ls = []  # 存取密码的列表
        FirstPsw = ""  # 存取第一个密码的字符

        while len(ls) < 20:  # 十个随机密码
            pwd = ""
            for i in range(long):
                pwd += s[random.randint(0, len(s) - 1)]
            if pwd[0] in FirstPsw:
                continue
            else:
                ls.append(pwd)
                FirstPsw += pwd[0]
        return sysr.choice(ls)
#=======================================ETool========================================#

def system(command):
    # 定义命令模板，用 {} 占位符表示需要替换的内容
    command_template = command

    # 使用 os.popen() 执行命令并获取命令输出的文件对象
    with popen(command_template) as process:
        # 读取命令输出并返回
        output = process.read().strip()

    return output

task_list = []
run_data = {}
def run_command(threadName, delay,task_id,content):
    print('RUNNING'+threadName)
    run_data[task_id] = system(f'get_answer {content}')
    print('\n\n')

# 定义创建任务函数
def create_task(content):
    # 创建随机数对象
    sysr = random.SystemRandom()
    # 创建当前任务
    now_task = ETool.ePassword(long=8,tszf=False)
    # 判断当前任务是否重复
    if now_task in task_list:
        # 如果重复，重新创建任务
        create_task()
    else:
        # 否则将当前任务添加到任务列表中
        task_list.append(now_task)
        run_data[now_task] = None
        _thread.start_new_thread( run_command, ("Thread-"+now_task, 2, now_task, content) )#run_command(now_task,content)
        return now_task
    

@app.route('/ctask', methods=['GET','POST'])
def ctask():
    try:
        if request.method == "GET":
            content = request.args.get('content')
            return {
                "code": 200,
                "msg": "success",
                "data": {
                    "status": "ok",
                    "task": create_task(content)
                }
            }
        else:
            return {
                "code": 403,
                "msg": "error:禁止用POST请求",
                "data": {
                    "status": "error",
                    "task": "error"
                }
            }
    except:
        return f"Error:请联系管理员：[email]{ae},[Phone]{ap},[QQ]{qq}"

@app.route('/get_task', methods=['GET','POST'])
def gtask():
    try:
        if request.method == "GET":
            task = request.args.get('task')
            if run_data[task] != None:
                return {
                    "code": 200,
                    "msg": "success",
                    "data": {
                        "status": "ok",
                        "task": run_data[task]
                    }
                }
            else:
                return {
                    "code": 404,
                    "msg": "Task not found/Creating",
                    "data": {
                        "status": "error",
                        "task": "error"
                    }
                }
        else:
            return {
                "code": 403,
                "msg": "error:禁止用POST请求",
                "data": {
                    "status": "error",
                    "task": "error"
                }
            }
    except:
        return f"Error:请联系管理员：[email]{ae},[Phone]{ap},[QQ]{qq}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)