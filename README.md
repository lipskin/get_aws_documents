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

 - 由于`curl`并不十分可靠，并且在python中并没有很好的方式通过curl的返回值判断文件下载的完整性和正确性，所以将在下一个版本改用python来处理字节流，保存为pdf文件。
 - 另外，并发的效果没有测试。。鉴于爬取动作返回值的问题，并发的可用性应该不高。。另外如果要使用纯python进行并发处理，爬虫的结构应该会有较大改变。。很多变量都能这样存，可以单独写一个类用于下载，放到一个子进程里面，用一个loop管理进程，但是这样的话文件保存路径的规则也得变，不能用系统切换路径的方式，而要在处理文件流的时候带上文件路径参数。恩，目前看来这样就没什么问题了。