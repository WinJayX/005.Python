import requests


def get_ip():
    while 1:  # 反复提取代理IP
        # 有待完善. 如果代理ip都用完了. 怎么办????
        url = "https://dev.kdlapi.com/api/getproxy/?orderid=962349361442245&num=100&protocol=2&method=1&an_tr=1&quality=1&format=json&sep=1"
        resp = requests.get(url)
        ips = resp.json()
        if ips['code'] == 0:
            for ip in ips['data']['proxy_list']:  # 拿到每一个ip
                yield ip   # 一个一个返回代理ip
            print("所有IP已经用完, 即将更新!")  # for循环结束. 继续提取新IP
        else:
            print("获取代理IP出现异常. 重新获取!")



def spider():
    url = "https://www.baidu.com"
    while 1:
        try:
            proxy_ip = next(gen)  # 拿到代理ip
            proxy = {
                "http": "http://" + proxy_ip,
                "https": "https://" + proxy_ip,
            }
            resp = requests.get(url, proxies=proxy)
            resp.encoding = "utf-8"
            return resp.text
        except :
            print("报错了. ")


if __name__ == '__main__':
    gen = get_ip()  #  gen就是代理ip的生成器
    for i in range(10):
        spider()
