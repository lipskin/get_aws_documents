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
./Get_aws.py
```

## 然后你可以在当前目录下看到一个documentation的文件夹，里面有新鲜的文档

## what next?

 - 首先，需要做一个简单的并发
 - 然后，还要加上[http://aws.amazon.com/whitepapers/](http://aws.amazon.com/whitepapers/) 和 [http://aws.amazon.com/architecture/](http://aws.amazon.com/architecture/) 的支持
 - 我打算写一个shell作为启动脚本
 - 目前的想法就是这样