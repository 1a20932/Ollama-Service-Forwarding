# Ollama Service Forwarding
 Ollama的转发服务(顺带处理了流式数据)
## 处理数据的内核文件
`get_answer`是一个我自制的内核文件
用法：命令
```shell
>>> get_answer {您的问题}
{答案}
```
本服务需要Ollama运行在`Windows` 环境下的 `localhost:11434`并且是`gemma`模型，目前不支持`Linux`,`Mac`

::: warning 尝试其他模型
> 如果您真的想使用其他模型，我们只能提醒您，我们只对了gemma进行适配，其他模型可能无法使用，后果自行承担
`get_answer --model {模型名称} {您的问题}`
:::