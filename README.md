# 这个是用来爬AWS文档的
文档来自[https://aws.amazon.com/documentation/](https://aws.amazon.com/documentation/)

## 准备环境

```
brew install python3
pip3 install requests python-bs4 lxml 
```
 
## 使用

```
git clone https://github.com/lipskin/get_aws_documents.git
cd get_aws_documents
./run.sh
```

## 然后你可以在当前目录下看到一个documentation的文件夹，里面有新鲜的文档

## what next?

 - 并发的支持还不是很好，因为无法获取os.system('command')中command的返回值，无法判断爬取是否成功，，如果失败无法retry
