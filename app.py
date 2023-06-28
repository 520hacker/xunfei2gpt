import asyncio
import os
import json 
import websocket
from flask import Flask, Response, request

from xfws import get_ws_via_messages

app = Flask(__name__, template_folder='templates')
xfkey = os.environ.get('XF_KEY')

def actions(request):
    messages = [{"role": "system", "content": "你是系统消息提示官"}, {"role": "user", "content": "优雅的告诉我，'你发送了错误的请求'"}] 

    try:
        if request.content_type == 'application/json':
            messages = request.get_json().get('messages', None) 
    except:
        pass

    authorization = request.headers.get('Authorization')
    if authorization is None:
        authorization = 'Bearer '+ xfkey

    ws = get_ws_via_messages(authorization, messages)

    return Response(event_stream(ws), mimetype='text/event-stream')

@app.route('/api/openai/v1/chat/completions',  methods=['GET', 'POST', 'PUT', 'DELETE'])
def chat_completions():  
    return actions(request)

@app.route('/v1/chat/completions',  methods=['GET', 'POST', 'PUT', 'DELETE'])
def app_completions():  
    return actions(request)

def event_stream(ws): 
    while ws.connected:
        message = ''
        try:
            message = ws.recv()
            data = json.loads(message)
            code = data['header']['code']
            if code != 0:
                print(f'请求错误: {code}, {data}')
                ws.close()

            sse_message = data["payload"]["choices"]["text"][0]["content"]
            print(sse_message)
            
            yield sse_message

            status = data['header']['status']
            if status == 2:
                print(f'请求结束: {status}')
                ws.close()
        except websocket.WebSocketTimeoutException as ex:
            print(ex)
            print(message)
            break

    # 关闭websocket连接
    ws.close()

if __name__ == "__main__":
    if os.name == "nt":
        import asyncio

        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    app.run(host="0.0.0.0", port=5006)
