#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 16:55:15 2023

@author: ishka
"""

import googletrans
from pprint import pprint



translator = googletrans.Translator()


# Basic Translate
output_file = open("output_file.txt","a")
irish_lines_list = open('/home/ishka/Downloads/New Folder/irishwordlist.txt').read().splitlines()
irish_lines_translated = []
for word in irish_lines_list:
    results = translator.translate(word, dest='en',src='ga')
    translation = results.text
    irish_lines_translated.append(results.text + '\n')
    print(round((len(irish_lines_translated) / len(irish_lines_list)) * 100, 2))
    output_file.write( translation + '\n')
    output_file.flush()
    #print(word)
    #print(results.text)
#print(list2)
# newlist = []
# for word in list2:
#     word = word + '\n'
#     newlist.append(word)
    
#print(list2)
#print(newlist)

#output_file.writelines(newlist)
output_file.close()