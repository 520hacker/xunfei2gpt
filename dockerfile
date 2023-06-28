# 使用官方的python镜像作为基础
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录下的所有文件到工作目录
COPY *.py .
 
# 安装构建所需依赖项
RUN pip install --no-cache-dir asyncio flask websocket-client

# 设置环境变量
ENV XF_KEY=your_key

# 暴露端口
EXPOSE 5006

# 运行主文件
CMD ["python", "app.py"]
