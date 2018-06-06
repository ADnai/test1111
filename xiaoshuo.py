import requests
from bs4  import BeautifulSoup



url = "http://www.23us.com/html/64/64886/"

def Url_paqu(url_1):
    response = requests.get(url_1)
    response.encoding = "gb18030"
    response_text = response.text
    m = BeautifulSoup(response_text,"html.parser")
    list_2 = []
    for t in m.find_all(dd , id= "contenes")
        print t.string
    pass






def Get_url():
    response = requests.get(url)
    response.encoding= 'gb18030'
    response_text = response.text
    k =  BeautifulSoup(response_text,"html.parser")
    href_list = []
    for i in  k.find_all('td',class_='L'):
        
        try:
            t = i.a.get('href')
            href_list.append(t)
            
        except AttributeError:
            print 'NoneType object has no attribute get'
    print href_list
def list_change(list):
    for i in range(len(list)):
        url_change= url + list[i]

    pass
if __name__ == '__main__':
    xiaoshuo()