from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
import logging

# 硬编码配置项
TARGET_HOST = 'localhost'
TARGET_PORT = '11434'
APP_LOG_LEVEL = 'INFO'

# 设置日志记录
logging.basicConfig(level=APP_LOG_LEVEL, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info('欢迎使用 AllForward\n开发者：刘钦宇\n著作权：刘钦宇\n版本：1.0.0')
logging.info('接下来，做一些设置！(INPUT1:STRING,INPUT2:STRING,INPUT3:NUMBER)')
logging.info(f'默认设置为转发到{TARGET_HOST}:{TARGET_PORT}')
logging.info("请问需要更改吗？(Y/N)")
if input().upper() == 'Y':
    logging.info("请输入目标服务器的IP地址：")
    TARGET_HOST = input()
    logging.info("请输入目标服务器的端口号：")
    TARGET_PORT = int(input())
    logging.info(f"配置完成，转发到{TARGET_HOST}:{TARGET_PORT}，启动服务...\n\n\n")
else:
    logging.info(f'默认设置为转发到{TARGET_HOST}:{TARGET_PORT}，不更改设置！\n\n\n')
    logging.info("启动服务...\n\n\n")

app = Flask(__name__)
CORS(app, resources=r'/*')

# 使用连接池
session = requests.Session()
session.headers.update({'User-Agent': 'Flask-Forwarder'})

@app.route('/', defaults={'path': ''},methods=['GET','POST'])
@app.route('/<path:path>',methods=['GET','POST'])
def forward_request(path):
    try:
        # 构造目标URL
        url = f'http://{TARGET_HOST}:{TARGET_PORT}/{path}'
        
        # 获取客户端请求的方法
        method = request.method
        
        # 获取客户端请求的数据
        data = request.data
        
        # 使用连接池和异常处理
        response = session.request(method, url, data=data, timeout=100)
        
        # 检查状态码
        if response.status_code >= 400:
            logging.error(f'Request to target server failed with status code: {response.status_code}')
            return jsonify({'error': 'Target server responded with an error'}), response.status_code
        
        return response.content, response.status_code
    except requests.RequestException as e:
        logging.error(f'Error while forwarding request: {e}')
        return jsonify({'error': 'Error while forwarding request'}), 500
    except Exception as e:
        logging.error(f'Unexpected error: {e}')
        return jsonify({'error': 'Unexpected error'}), 500

if __name__ == '__main__':
    app.run()