
import base64
import datetime
import hashlib
import hmac
import json
import time
from datetime import datetime
from time import mktime
from urllib.parse import urlencode, urlparse
from wsgiref.handlers import format_date_time

import websocket


xunfeiurl = "ws://spark-api.xf-yun.com/v1.1/chat" 

class Ws_Param(object):
    # 初始化
    def __init__(self, APPID, APIKey, APISecret, gpt_url):
        self.APPID = APPID
        self.APIKey = APIKey
        self.APISecret = APISecret
        self.host = urlparse(gpt_url).netloc
        self.path = urlparse(gpt_url).path
        self.gpt_url = gpt_url

    # 生成url
    def create_url(self):
        # 生成RFC1123格式的时间戳
        now = datetime.now()
        date = format_date_time(mktime(now.timetuple()))

        # 拼接字符串
        signature_origin = "host: " + self.host + "\n"
        signature_origin += "date: " + date + "\n"
        signature_origin += "GET " + self.path + " HTTP/1.1"

        # 进行hmac-sha256进行加密
        signature_sha = hmac.new(self.APISecret.encode('utf-8'), signature_origin.encode('utf-8'),
                                 digestmod=hashlib.sha256).digest()

        signature_sha_base64 = base64.b64encode(signature_sha).decode(encoding='utf-8')

        authorization_origin = f'api_key="{self.APIKey}", algorithm="hmac-sha256", headers="host date request-line", signature="{signature_sha_base64}"'

        authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')

        # 将请求的鉴权参数组合为字典
        v = {
            "authorization": authorization,
            "date": date,
            "host": self.host
        }
        # 拼接鉴权参数，生成url
        url = self.gpt_url + '?' + urlencode(v)
        # 此处打印出建立连接时候的url,参考本demo的时候可取消上方打印的注释，比对相同参数时生成的url与自己代码生成的url是否一致
        return url

def gen_params_via_messages(appid, messages):
    """
    通过appid和用户的提问来生成请参数
    """
    data = {
        "header": {
            "app_id": appid,
            "uid": "1234"
        },
        "parameter": {
            "chat": {
                "domain": "general",
                "random_threshold": 0.7,
                "max_tokens": 2048,
                "auditing": "default"
            }
        },
        "payload": {
            "message": {
                "text": messages
            }
        }
    }
    return data

def gen_params(appid, question):
    """
    通过appid和用户的提问来生成请参数
    """
    data = {
        "header": {
            "app_id": appid,
            "uid": "1234"
        },
        "parameter": {
            "chat": {
                "domain": "general",
                "random_threshold": 0.7,
                "max_tokens": 2048,
                "auditing": "default"
            }
        },
        "payload": {
            "message": {
                "text": [
                    {"role": "user", "content": question}
                ]
            }
        }
    }
    return data

def gen_response(answer):
    data = {
        "id": int(time.time()),
        "object": "chat.completion",
        "created": int(time.time()),
        "choices": [{
            "index": 0,
            "message": {
            "role": "assistant",
            "content": answer,
            },
            "finish_reason": "stop"
        }],
        "usage": {
            "prompt_tokens": 20,
            "completion_tokens": 60,
            "total_tokens": 80
        }
    }
    return data


def get_ws(authorization, question):
    authorization = authorization.replace("Bearer ", "")
    auth_parts = authorization.split('$')
    appid, api_secret, api_key = auth_parts
  
    wsParam = Ws_Param(appid, api_key, api_secret, xunfeiurl)
    wsUrl = wsParam.create_url()
    ws = websocket.create_connection(wsUrl, 60)
    data = json.dumps(gen_params(appid=appid, question=question))
    ws.send(data)
    return ws


def get_ws_via_messages(authorization, messages):
    authorization = authorization.replace("Bearer ", "")
    auth_parts = authorization.split('$')
    appid, api_secret, api_key = auth_parts
  
    wsParam = Ws_Param(appid, api_key, api_secret, xunfeiurl)
    wsUrl = wsParam.create_url()
    ws = websocket.create_connection(wsUrl, 60)
    data = json.dumps(gen_params_via_messages(appid=appid, messages=messages))
    ws.send(data)
    return ws