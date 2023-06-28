# 讯飞API 转 GPT

![img](https://memosfile.qiangtu.com/picgo/assets/2023/06/28202306_28235526.png)

这是一个为了让讯飞api兼容GPT而做的一个半成品。

前2天通过了讯飞的测试申请，准备在商用前稍微测试一下，但是目前大家的界面都是针对GPT开发的，所以会存在需要兼容GPT的情况，于是写了一个转GPT的例子，仅供参考。

有疑问可以来留言 https://memos.qiangtu.com/m/1028

## 已实现内容

- 实现了一个聊天的API, 将Websocket 转换成了 OPENAI 的 SSE
- 结合我关联项目[xunfei2ui](https://github.com/520hacker/xunfei2ui) ， 就能够把对话走起来，效果：https://xunfei.qiangtu.com/
- 提供了docker部署，填自己的key就能跑起来

## 部署指东

- pull 我提供的image   odinluo/xunfei2gpt
- 创建容器，设置环境变量 XF_KEY , 格式为  appid$appsec$appkey 
- 设置端口，本程序暴露端口为5006，请自己按照自己的喜欢进行映射
- 运行
- 安装 [xunfei2ui](https://github.com/520hacker/xunfei2ui) ， 从前台访问

## 探索方向

- 认真读一下sdk文档，研究下哪些可以进行深度拓展一下

## 怎么申请讯飞的KEY

​			这个貌似是要靠工单手动支持你接入的

-  https://console.xfyun.cn/app/create?redirect=%2Fapp%2Fmyapp 创建应用
-  https://console.xfyun.cn/services/cbm 获得APPID
-  https://xinghuo.xfyun.cn/ 页面底部点 合作咨询
-  填写表单 申请接入能力。

## 感谢2位AI在写代码的时候答疑

- OPENAI GPT
- BING

# iFlytek2GPT

This is a semi-finished product designed to make iFlytek API compatible with GPT.

After passing iFlytek's test application two days ago, I am planning to do a brief test before commercialization. However, currently everyone's interface is developed for GPT, so there may be a need to make it compatible with GPT. Therefore, I wrote an example for converting to GPT, for reference only.

If you have any questions, you can leave a message [here](https://memos.qiangtu.com/m/1028).

## Implemented Features

- Implemented a chat API that converts WebSocket to OPENAI's SSE.
- Combined with my associated project [xunfei2ui](https://github.com/520hacker/xunfei2ui), we can start a conversation. Here is an example: [https://xunfei.qiangtu.com/](https://xunfei.qiangtu.com/).
- Docker deployment is provided, just fill in your own key to run.

## Deployment Instructions

- Pull the image I provided `odinluo/xunfei2gpt`.
- Create a container and set the environment variable `XF_KEY` in the format `appid$appsec$appkey`.
- Set the port. This program exposes port 5006. Please map it according to your preference.
- Run the program.
- Install [xunfei2ui](https://github.com/520hacker/xunfei2ui) and access it from the front end.

## Exploration Direction

- Carefully read the SDK documentation and explore which areas can be further expanded.

## How to Apply for iFlytek's Key

It seems that this needs to be manually supported through a work order.

- [Create an application](https://console.xfyun.cn/app/create?redirect=%2Fapp%2Fmyapp)
- Obtain the APPID from [here](https://console.xfyun.cn/services/cbm)
- At the bottom of the [page](https://xinghuo.xfyun.cn/), click on "合作咨询" (Cooperation Consultation)
- Fill out the form to apply for access capabilities.

## Special Thanks to the Two AIs for Answering Questions During Code Writing

- OPENAI GPT
- BING
