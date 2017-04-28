from bs4 import BeautifulSoup
import requests
import progressbar
from datetime import datetime
from common_and_over18 import get_page_url_over18
from get_text import get_meta_text


url_list, short_url_list = get_page_url_over18("Gossiping", 23175) #board name, end-page

text_list = []
for i in range(0, len(url_list)):
    text_data = get_meta_text(i)
    text_list.append(text_data)
    
for text in text_list:
  print(text)
