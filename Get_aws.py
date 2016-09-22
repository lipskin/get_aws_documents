#! /usr/bin/env python3
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import re
import os
import urllib
from Bcolor import bcolors
import pdb

def get_document(flag, retry_times=3):
    if not os.path.exists('documentation'):
        os.mkdir('documentation')
    os.chdir('documentation')
    print(bcolors.BOLD + '开始爬取(' + os.getcwd() +') 况且况且。。。' + bcolors.ENDC)
    document_url = 'https://aws.amazon.com/documentation/'
    document_page = requests.get(document_url).content
    document_soup = BeautifulSoup(document_page, "lxml").find('ul', class_='content-wrapper')
    services_name = [ x.text.strip() for x in document_soup.find_all('h4') ][1:-1]
    # 遍历documentation 路径下的server组
    for service_name in services_name:
        if not os.path.exists(service_name):
            os.mkdir(service_name)
        os.chdir(service_name)
        print(bcolors.YELLOW + '创建文件夹:' + os.getcwd() + bcolors.ENDC)
        services_tag = document_soup.find('h4',id=service_name.replace(' ', '_')).parent.parent.parent.next_sibling.next_sibling.find_all('a')
        # 进入到每一个server的url下面爬去pdf文档
        for service_subname in services_tag:
            service_subname = re.search('\/documentation\/(.+)\/', service_subname).group(1) if service_subname == '' else service_subname # 处理一个隐藏的文档
            service_subname_folder = service_subname.text.replace('/', ':') # 处理一个名称带"/"的文档
            if not os.path.exists(service_subname_folder):
                os.mkdir(service_subname_folder)
            os.chdir(service_subname_folder)
            print(bcolors.YELLOW + '文件夹:' + os.getcwd() + bcolors.ENDC)
            try:
                service_url = urllib.parse.urljoin('https://aws.amazon.com', service_subname['href'])
                service_page = requests.get(service_url).text
                service_soup = BeautifulSoup(service_page, 'lxml')
                pdf_urls = [ x['href'] for x in service_soup.find_all('a',text='PDF')]
                # 使用curl爬取当页所有pdf，如果爬取失败，retry 4次
                for pdf_url in pdf_urls:
                    for i in range(retry_times+1):
                        try:
                            print(bcolors.GREEN + pdf_url + bcolors.ENDC)
                            os.system('curl -O ' + pdf_url + ' %s'%flag)
                        except:
                            print(bcolors.PURPLE + 'retry: %s times'%i + bcolors.ENDC)
                            continue
                        if i == retry_times:
                            print(bcolors.RED + '爬取失败！%s'%pdf_url)
                        break
            except:
                pass
            os.chdir('..')
        os.chdir('..')
    os.chdir('..')
    return True

if __name__ == '__main__':
    input_str = input(bcolors.BOLD + '是否并行？(y/n)（将占用最大带宽）:\n' + bcolors.ENDC)
    flag = '1>>/dev/null &' if input_str == 'y' else ''
    if get_document(flag):
        print(bcolors.GREEN + "爬取完成!" + bcolors.ENDC)
