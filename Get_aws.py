#! /usr/local/bin/python3
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import os
import urllib
import pdb

def get_document():
    if not os.path.exists('documentation'):
        os.mkdir('documentation')
    os.chdir('documentation')
    document_url = 'https://aws.amazon.com/documentation/'
    document_page = requests.get(document_url).content
    document_soup = BeautifulSoup(document_page, "lxml").find('ul', class_='content-wrapper')
    services_name = [ x.text.strip() for x in document_soup.find_all('h4') ][1:-1]
    for service_name in services_name:
        if not os.path.exists(service_name):
            os.mkdir(service_name)
        os.chdir(service_name)
        services_tag = document_soup.find('h4',id=service_name).parent.parent.parent.parent.find_all('a')[1:-1]
        for service_subname in services_tag:
            if not os.path.exists(service_subname.text):
                os.mkdir(service_subname.text)
            os.chdir(service_subname.text)
            service_url = urllib.parse.urljoin('https://aws.amazon.com', service_subname['href'])
            service_page = requests.get(service_url).text
            service_soup = BeautifulSoup(service_page, 'lxml')
            pdf_urls = [ x['href'] for x in service_soup.find_all('a',text='PDF')]
            for pdf_url in pdf_urls:
                os.system('curl -O ' + pdf_url + ' &')
            os.chdir('..')
        os.chdir('..')
    os.chdir('..')

if __name__ == '__main__':
    get_document()

