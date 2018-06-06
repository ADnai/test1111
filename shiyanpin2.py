import requests
from bs4  import BeautifulSoup
def laa():
    response = requests.get("http://www.hq88.com/lms/member/course/exam_studyExamPre?courseUuid=510a9046-f8ea-11e3-a4fb-24b6fdf8cd6c&examUuid=72f452d2-f8ea-11e3-a4fb-24b6fdf8cd6c")
    
    response_text = response.text
    m = BeautifulSoup(response_text,"html.parser")
    print m
    for t in m.find_all('div' , id= "imagegallery"):
        try: 
            print t.text
        except NameError: 
    	    print 'NameError'
if __name__ == '__main__':
	laa()