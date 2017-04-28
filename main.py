from bs4 import BeautifulSoup
import requests
import progressbar
from datetime import datetime
from common_and_over18 import get_page_url_over18
from common_and_over18 import get_page_url_common
from get_text import get_meta_text

#pages for adults only
over18_url_list, over18_short_url_list = get_page_url_over18("Gossiping", 23175) #board name, end-page

over18_text_list = []
for i in range(0, len(over18_url_list)):
    text_data = get_meta_text(i)
    over18_text_list.append(text_data)
    
for text_a in over18_text_list:
    print(text_a)

    
#common pages
common_url_list, common_short_url_list = get_page_url_common("Makeup", 2566)
common_text_list = []
for i in range(0, len(common_url_list)):
    text_data = get_meta_text(i)
    common_text_list.append(text_data)
    
for text_c in common_text_list:
    print(text_C)
