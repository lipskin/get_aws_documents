# 这个是用来爬AWS文档的
文档来自[https://aws.amazon.com/documentation/](https://aws.amazon.com/documentation/)

## 准备环境

你的电脑可以是Linux，也可以是Mac；Windows环境尚未测试。
对于这一版本，不管你的电脑是什么系统，一定得有`curl`
然后
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
**说明：**
并行其实也没有测试，可能会比较**辣眼睛**。。一不小心就会`根本停不下来`。。另外，一个在测试中已知的一个问题是“Connection reset by peer“并不会导致程序终止，但会导致单个文件不能正常下载。。也是curl的原因导致的偶然失败。
另外，AWS的文档并不是每一个都有PDF版本，所以空文件夹是由于该内容没有PDF版本导致的。
以上问题将在下一个版本修复。。欢迎大家帮忙测试并行的效果

## 然后你可以在当前目录下看到一个documentation的文件夹，里面有新鲜的文档

## what next?

 - 由于`curl`并不十分可靠，并且在python中并没有很好的方式通过curl的返回值判断文件下载的完整性和正确性，所以将在下一个版本改用python来处理字节流，保存为pdf文件。
 - 另外，并发的效果没有测试。。鉴于爬取动作返回值的问题，并发的可用性应该不高。。另外如果要使用纯python进行并发处理，爬虫的结构应该会有较大改变。。很多变量都能这样存，可以单独写一个类用于下载，放到一个子进程里面，用一个loop管理进程，但是这样的话文件保存路径的规则也得变，不能用系统切换路径的方式，而要在处理文件流的时候带上文件路径参数。恩，目前看来这样就没什么问题了。