
import requests
import time
from fake_useragent import UserAgent
import logging

from tqdm import trange    
from bs4 import BeautifulSoup
from random import *


logging.captureWarnings(True)

def check_requests(url):
    ua = UserAgent()
    headers={"User-Agent":ua.firefox} # to diversify the header information
    t1 = time.time() # to calculate the speed
    
    try:
        r = requests.get(url,headers=headers,verify=False, timeout = 20)
        
    except requests.exceptions.ConnectTimeout: 
        print( '超时！')
        r = False
        
    except requests.exceptions.ConnectionError:
        print('无效地址！')
        r = False
    except requests.exceptions.ChunkedEncodingError:
        r = False
        print('连接失败！')
    except requests.adapters.ReadTimeout:
        r =False
        print('连接超时！')
    except requests.adapters.InvalidProxyURL:
        r =False
        print('代理无效！')
        
    t2 = time.time()
    print("时间差:" , (t2 - t1))
    return r


def get_text(page_url):
    
    results = []
    for i in trange(len(page_url)):
        print('page {0} starts.'.format(str(i)))
        r = check_requests(page_url[i])  
        c = 0
        while True:
        
            if r:
                soup = BeautifulSoup(r.text, "lxml") 
                try:
                    title = soup.find('title').get_text().replace(': 지식iN', '').strip()
                except:
                    title = ''
                    print('title is not found.') 
                try:
                    question_text = soup.find('div', attrs={"class": 'c-heading__content'}).get_text().strip().replace('\n', '')
                except:
                    try:
                        question_text = soup.find(attrs={"property":"og:description"})['content']
                    except:
                        question_text = ""
                        print('question is not found.')
                try:
                    answers_text = soup.find_all('div', attrs={"class": '_endContentsText c-heading-answer__content-user'})
                    answers_text = [x.get_text().strip() for x in answers_text]
                    answers_text = [x.replace('\n', '') for x in answers_text]
                except:
                    answers_text  =[]
                    print("answers is not found.")
                try:
                    user_info = soup.find_all('span', attrs = {'class': 'c-userinfo__info'})
                    user_info = [x.get_text() for x in user_info]
                    views = user_info[-1].strip().split(' ')[-1].replace(',', '')    
                    date = user_info[0].strip().replace('작성일', '')    
                except:
                    views = 0
                    date = ''
                    print("views or date is not found.")
            
                results.append({'title': title, 'question_text': question_text, 'answers_text': answers_text, 'views':views, 'date': date})
                break
    
            elif c < 5:
                time.sleep(randrange(5,8))
                print('start again')
                c += 1
                r = check_requests(page_url[i])
        
            else:
                results.append({'url': page_url[i]})
                print('page {0} is not found.'.format(str(i)))
                break
           
        print('page {0} ends.'.format(str(i)))
        time.sleep(randrange(1,4))
        
    return results


###############################################################################
if __name__ == '__main__':
    with open(r'./result/url_list_keyword.txt', 'r') as f:
        page_url = [line.strip() for line in f.readlines()]
    
    results = get_text(page_url)
    
    import pickle
    with open(r'.\keyword_results.txt', 'wb') as f:
        pickle.dump(results, f)

