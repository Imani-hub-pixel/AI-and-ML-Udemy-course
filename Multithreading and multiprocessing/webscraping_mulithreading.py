'''
Real world example:Multithreading for I/O-bound tasks
scenario:Webscrapping-involves making numerous network requests to fetch web pages.These tasks are I/O bound
because they spend alot of time witing for respeonses from servers.Multithreading can signficantly improve the performance 
by allowing multiple web pages to be fetched concurrently

'''
'''
https://python.langchain.com/docs/introduction/

https://python.langchain.com/docs/concepts/

https://python.langchain.com/docs/tutorials/
'''

import threading
import requests
from bs4 import BeautifulSoup

urls=[
'https://python.langchain.com/docs/introduction/',

'https://python.langchain.com/docs/concepts/',

'https://python.langchain.com/docs/tutorials/'
]

def fetch_contents(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'Fetched:{len(soup.text)} characters from {url}')
threads=[]
for url in urls:
    thread=threading.Thread(target=fetch_contents,args=(url,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()

print("All web pages fetched")





