from bs4 import BeautifulSoup
import requests
import progressbar


def get_page_url_over18(name, end):
    url_list = []
    short_url_list = []
    domain = "https://www.ptt.cc/"
    bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)
    
    for i in range(1, end + 1):
        payload = {
        'from':'/bbs/{}/index{}.html'.format(name, i),
        'yes':'yes'
        }
        rs = requests.session()
        page_url = "https://www.ptt.cc/bbs/{}/index{}.html".format(name, i)
        get_page_url = rs.post('https://www.ptt.cc/ask/over18', verify = False, data = payload)
        get_page_url = rs.get(page_url, verify = False).text
        soup = BeautifulSoup(get_page_url, "html.parser")
        bar.update(i)
        #serp title links
        title = soup.find_all("div", class_ = "title")
        for i in title:
            if i.find("a") != None:
                a = i.find("a").get("href")
                if domain in a:
                    url_list.append(a)
                else:
                    whole_a = domain + a
                    url_list.append(whole_a)
                    short_url_list.append(a)
    return(url_list, short_url_list)

def get_page_url_common(name, end):
    url_list = []
    short_url_list = []
    domain = "https://www.ptt.cc/"
    bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)
    
    for i in range(1, end + 1):
        page_url = "https://www.ptt.cc/bbs/{}/index{}.html".format(name, i)
        get_page_url = requests.get(page_url).text
        soup = BeautifulSoup(get_page_url, "html.parser")
        bar.update(i)
        #serp title links
        title = soup.find_all("div", class_ = "title")
        for i in title:
            if i.find("a") != None:
                a = i.find("a").get("href")
                if domain in a:
                    url_list.append(a)
                else:
                    whole_a = domain + a
                    url_list.append(whole_a)
                    short_url_list.append(a)
    return(url_list, short_url_list)
