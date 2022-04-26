# 代理. 可以使用第三方的机器来代理你的请求
# 代理的弊端:
#      1. 慢.
#      2. 代理IP不好找.
import requests

# https://www.kuaidaili.com/free/intr/1/

url = "https://www.baidu.com"

# 准备代理信息
proxy = {
    "http": "http://82.156.171.147:3128",
    "https": "https://82.156.171.147:3128"
}

# proxies 代理
resp = requests.get(url, proxies=proxy)
resp.encoding = 'utf-8'
print(resp.text)
