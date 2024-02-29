#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 03:12:24 2023

@author: ishka
"""
import requests
from bs4 import BeautifulSoup
import csv

words_file = open('/home/ishka/Coding/Python/test_input.txt', 'r') # opens the file with all the irish words

#creates a list from the file because request.get didnt like the non list format
words_list = []
for word in words_file:
    words_list.append(word.replace('\n','').replace(' ',''))
print(words_list)

#temporary words list
#words_list= ['A','á','ab']
#output_file1 = open('/home/ishka/Coding/Python/FGB_Translation_output.csv','wb')
output_file1 = open('/home/ishka/Coding/Python/FGB_Translation_output.csv', 'w')#, newline='')
output_file = csv.writer(output_file1)#, delimiter ='&')


for word in words_list:
    print('word:', word)
    url = 'https://www.teanglann.ie/en/fgb/{}'.format(word)
    #print(url)
    page = requests.get(url)  # requests network status of url, 200 is good
    #print(page)
    #gets all html data into soup
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup)
    lists = soup.find_all('span', class_='abcItem')
    print(lists)
    #print(soup.text)
    translation = soup.find('div', class_= "dir obverse exacts").text
    # Reformatting to remove unwanted stuff
    for i in range(20): # adds a space between the word and the number for words with multiple translations
        translation = translation.replace(word.lower()+str(i),' '+word.lower()+' ('+str(i)+')')
    translation = translation.replace(' m.',' masculine ').replace('(gs.','(genetive singular ').replace(' pl.',' plural ').replace('						EXACT MATCHES','').replace('						IN FOCLÓIR GAEILGE—BÉARLA','').replace('\n','').replace('\r','')
    translation = translation.replace(' f.', ' feminine ').replace(' poss.', ' possesive ').replace(' a.', ' adjective ').replace(' sg.', ' singular ').replace(' pl.', ' plural ').replace(' vn.', ' verbal noun ')
    translation = translation.replace(' gs.', ' genetive singular ').replace(' var.', ' variaton ').replace(' Lit:', ' Literatry use: ').replace(' s.', ' substantive ').replace(' int.', ' interjection ').replace(' npl.', ' nominitave plural ')
    translation = translation.split('\n\n')#.replace('\n','').replace('\r','')
    print('translation: ', translation)
    this_dict = {word:translation}
    for key, value in this_dict.items():
       output_file.writerow([key, value])
       print('key vaulue pair:', key, value)
    #output_file.writerow(this_dict.keys())
    #output_file.writerow(this_dict.values())
    
    # for line in translation:
    #     #this_dict = {word:line}
    #     line = line.replace('\n\n','').replace(',','').replace('\n','')
    #     output_file.writerow([line])
    #     print([line])
    #     #output_file.writerow([line,1])
    #     output_file.writerow(this_dict.keys())
    #     output_file.writerow(this_dict.values())
    output_file1.flush()
output_file1.close()


#put everything in try except block

# we want to collect for each word:
    # word @ <span class="fgb title">word, </span>
    # iterate for each instance of the word
        # gender @ <span title="masculine" class="fgb tip">m</span>
            # iterate for each translation and there corresponding example
                # translation <span class="diclick" onclick="window.location='/en/fgb/word'">word</span>
                # examples + examples translation
            
        # related matches words?
        
        
        
        
        
        
        
        
        
        
        
        
        
        