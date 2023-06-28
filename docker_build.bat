docker build -t odinluo/xunfei2gpt .
docker push odinluo/xunfei2gpt
docker save -o xunfei2gpt.tar odinluo/xunfei2gpt:latest
move xunfei2gpt.tar xunfei2gpt.tar