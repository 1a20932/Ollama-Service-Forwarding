import requests
import json

url = 'http://localhost:11434/api/generate'
payload = {"model": "gemma","prompt":input("USER >>> ")}
r = requests.post(url, json=payload)
print(r.text)
print("--------------------------------处理-----------------------------")
r_a1 = str(r.text).split('\n')
del r_a1[-1] #删除最后一个元素
print(f"列表处理Step.1:\n{r_a1}")
print("-----------------------------------------------------------------")

print("流式文本处理Step.2：")
for i in r_a1:
    i = json.loads(i)
    print(i['response'],end="")
print()
print("---------------------------------处理完成-------------------------")