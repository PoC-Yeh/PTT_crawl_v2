from bs4 import BeautifulSoup
import requests
import progressbar
from datetime import datetime
from get_url import get_page_url_over18
from get_url import get_page_url_common
from get_text import get_meta_text_over18
from get_text import get_meta_text_common



#####pages for adults only
over18_url_list, over18_short_url_list = get_page_url_over18("Gossiping", 23175) #board name, end-page
#output1 = pickle.dump(over18_url_list, open("Gossiping_url_list.txt", "wb"))
#output2 = pickle.dump(over18_short_url_list, open("Gossiping_short_url_list.txt", "wb"))
#over18_url_list = pickle.load(open("Gossiping_url_list.txt", 'rb'))
#over18_short_url_list = pickle.load(open("Gossiping_short_url_list.txt", 'rb'))
over18_text_list = []
for i in range(0, len(over18_url_list)):
    text_data = get_meta_text_over18(i, over18_url_list, over18_short_url_list)
    over18_text_list.append(text_data)
    
for text_a in over18_text_list:
    print(text_a)

    
#####common pages
common_url_list, common_short_url_list = get_page_url_common("Makeup", 2566)
#output = pickle.dump(common_url_list, open("Gossiping_url_list.txt", "wb"))
#common_url_list = pickle.load(open("Gossiping_url_list.txt", 'rb'))
common_text_list = []
for i in range(0, len(common_url_list)):
    text_data = get_meta_text_common(i, common_url_list)
    common_text_list.append(text_data)
    
for text_c in common_text_list:
    print(text_C)
