import requests
from bs4 import BeautifulSoup





url = "http://202.119.210.3:8080/opac/search_adv_result.php?q0=python&sType0=any&pageSize=20&sort=score&desc=on&strText=&doctype=&strSearchType=title&displaypg=20"

def nimei():
	response  = requests.get(url)
	response.encoding = 'utf-8' 
	response_text = response.text
	
	m = BeautifulSoup(response_text,'html.parser')
	
	
	for t in m.find_all('td',bgcolor='#FFFFFF'):
		print t.text
	

if __name__ == '__main__':
	nimei()