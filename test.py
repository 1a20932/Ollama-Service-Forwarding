import _thread
import requests
import json


# 为线程定义一个函数
def service( threadName, delay):
            print("开始线程：" + threadName)
            url = 'http://localhost:11434/api/generate'
            payload = {"model": "gemma","prompt":"Hello"}
            r = requests.post(url, json=payload)
            print(r.text)
            print(threadName+"接收到请求，处理中\n--------------------------------处理-----------------------------")
            r_a1 = str(r.text).split('\n')
            del r_a1[-1] #删除最后一个元素
            print(f"{threadName}:列表处理Step.1:\n{r_a1}")
            print(threadName+"-----------------------------------------------------------------")
            all_ans = ""
            print(threadName+"流式文本处理Step.2：")
            for i in r_a1:
                i = json.loads(i)
                all_ans=f"{all_ans}{i['response']}"
                print(i['response'],end="")
            print()
            print("---------------------------------"+threadName+"处理完成-------------------------")
            exit()

# 创建两个线程
try:
   _thread.start_new_thread( service, ("Thread-1", 2, ) )
   _thread.start_new_thread( service, ("Thread-2", 4, ) )
except:
   print ("Error: 无法启动线程")

while 1:
   pass
exit()