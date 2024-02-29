#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 02:07:20 2023

@author: ishka
"""


import requests
from bs4 import BeautifulSoup

list_of_all_words_file = open('list_of_all_words_file.txt', 'a')

ó = '%c3%b3'
á = '%c3%a1'
é = '%c3%a9'
ú = '%c3%ba'
í = '%c3%ad'
Á = '%c3%81'
Ú = '%c3%9a'
É = '%c3%89'
Í = '%c3%8d'

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
word_list = []
for letter in letters:
    url = f'https://www.teanglann.ie/en/fgb/_{letter}'
    page = requests.get(url)  #requests network status of url, 200 is good
#print(page)
    soup = BeautifulSoup(page.content, 'html.parser') # gets all html data into soup

    lists = soup.find_all('span', class_='abcItem')

    
    for element in lists:
        print(element.contents[1])
        word_scrambled = element.contents[1].get('href')
        word_scrambled = word_scrambled[8:].replace(ó,'ó').replace(á,'á').replace(é,'é').replace(ú,'ú').replace(í,'í').replace(Á,'Á').replace(Ú,'Ú').replace(É,'É').replace(Í,'Í')
        word_list.append(word_scrambled)
        list_of_all_words_file.write( word_scrambled + '\n')
    print(type(word_list[0]))
    print(word_list[len(word_list)-2])
list_of_all_words_file.close()
