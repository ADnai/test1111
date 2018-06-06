# coding=utf-8 
import requests
import json
def write_to_file(date):
    with open('aaa','a',) as file:
        date=date.decode('ascii').encode('utf-8')
        file.write(date)
        file.write('\n')


    pass
def GetpetId():
    d = {}
    k = 0
    list = []
    for i in range(1,80):
        response = requests.get('http://xyq.cbg.163.com/cgi-bin/xyq_overall_search.py?j1li8ynr&act=overall_search_pet&page='+str(i)+'&skill=425%2C416%2C405&server_type=3&is_baobao=1',timeout=60)
        responseJson =  response.json()
        for  m  in range(len(responseJson.get('msg'))):
            skill= responseJson.get('msg')[m].get('skill')
            gongzi=int(responseJson.get('msg')[m].get('large_equip_desc').split(';')[20])
            chengzhang = int(responseJson.get('msg')[m].get('large_equip_desc').split(';')[26])
            if ('407' in skill) or (gongzi <1500) or(chengzhang<1240):
                continue
            else:
                area_name= responseJson.get('msg')[m].get('area_name')
                server_name = responseJson.get('msg')[m].get('server_name')
                price = responseJson.get('msg')[m].get('price')
                k=k+1
                w=str(k)
                d['all_name'+w]=area_name+server_name
                d['server_name'+w]=server_name
                d['skill'+w]= skill
                d['gongzi'+w] = gongzi
                d['chengzhang'+w]=chengzhang
                d['price'+w]=price
                list.append(server_name)
                
        for  t in range(len(list)):
            
            Num_a = 0
            for lll in range(1,k+1):
                ol =[]
                if list[t] in d['server_name'+str(lll)]:
                    Num_a=Num_a+1
                
            print list[t] , Num_a
            

            write_to_file(list[t])
            write_to_file(Num_a)


            
if __name__ == '__main__':
    GetpetId()