#!/usr/bin/python
# -*-  coding: utf-8 -*-
import requests
import json
class PeTcollections(object):
    """docstring for PeTcollections"""
    def __init__(self, available_pet):
        
        self.available_pet = available_pet


    @property
    def select_pets(self):
        for raw_pet in self.available_pet['msg']:
            skill = raw_pet['skill']
            gongzi=raw_pet['large_equip_desc'].split(';')[20]
            chengzhang = raw_pet['large_equip_desc'].split(';')[26]
            if (407 in skill) or (gongzi <1500) or(chengzhang<1240):
                continue
            else:
                information_pet=[raw_pet['area_name'].encode('utf-8'),
                                 raw_pet['price'],
                                 skill,
                                 gongzi,
                                 chengzhang,
                                 raw_pet['large_equip_desc'].split(';')[0],
                                ]
            yield  information_pet


    def write_to_file(self):
        with open('aaa','a') as file:
            for  infor_pet in self.select_pets: 
                file.write(str(infor_pet))
                file.write('\n')
        
def run_code():
    for i in range(1,80):
        url='http://xyq.cbg.163.com/cgi-bin/xyq_overall_search.py?j1li8ynr&act=overall_search_pet&page='+str(i)+'&skill=425%2C416%2C405&server_type=3&is_baobao=1'
        r = requests.get(url,verify=False)
      
        available_pet = r.json()
        PeTcollections(available_pet).write_to_file()
if __name__ == '__main__':
    run_code()