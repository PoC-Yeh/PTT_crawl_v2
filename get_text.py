from bs4 import BeautifulSoup
import requests
from datetime import datetime

    
def get_meta_text(num):    
    text_page_url = url_list[num]
    payload = {
        'from':short_url_list[num],
        'yes':'yes'
        }
    rs = requests.session()
    get_page_url = rs.post('https://www.ptt.cc/ask/over18', verify = False, data = payload)
    get_page_url = rs.get(text_page_url, verify = False).text
    soup = BeautifulSoup(get_page_url, "html.parser")
    
    #get meta data
    text = soup.find("div", class_="bbs-screen bbs-content").text
    meta = soup.find_all("span", class_="article-meta-value")
    meta_text = []  #author, category, title, time
    for item in meta:
        meta_text.append(item.text)
    #print(meta_text)
    
    #deal with datetime format
    datetime_object = datetime.strptime( meta_text[3], '%a %b %d %H:%M:%S %Y')
    extract_date = "".join(("".join(list(str(datetime_object))[:10])).split("-"))
    
    #list of meta data in order
    final_text = [extract_date]  #date
    final_text.append("PTT")  #PTT
    final_text.append(meta_text[1]) #board
    final_text.append(meta_text[2]) #title
    final_text.append(meta_text[0]) #author
    text_join = "; ".join(final_text)
    return(text_join)
