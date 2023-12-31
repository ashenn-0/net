import time
import requests

message_list = []  # 保存提问过的问题
saved_time = -1  # 用来保存一个对话发起的时间，超出一定时间后删除提过的问题
saved_length = 5  # 对话保存的分钟数


def get_access_token():
    access_token_url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {
        "grant_type": "client_credentials",
        "client_id": "GOBgFrUPwFg7j3NihGUh1rey",
        "client_secret": "5sqNHtFbXjXT2Epn51k3R7FTnp4cVvCh"
    }
    response = requests.post(access_token_url, params)
    r = response.json()
    access_token = r['access_token']
    return access_token


def check_time():
    global saved_time, saved_length, message_list

    if saved_time == -1:
        saved_time = time.time()
        return
    ctime = time.time()
    stime = saved_time + saved_length * 60
    if stime < ctime:
        message_list = []


def add_to_message_list(name, words):
    message = {
        "role": name,
        "content": words
    }
    message_list.append(message)


def talk(_content):  # 与文心一言交互
    check_time()  # 检查保存的对话是否过期
    access_token = get_access_token()  # 获取access_token

    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"
    params = {
        "access_token": access_token
    }
    add_to_message_list('user', _content)
    body = {
        "messages": message_list
    }
    response = requests.post(url, params=params, json=body)  # 与文心一言交互
    res = response.json()
    words = res["result"]  # 提取回复中的信息
    add_to_message_list('assistant', words)
    print('==baidu==')
    print(message_list)
    print('=baidu end=')
    return words


