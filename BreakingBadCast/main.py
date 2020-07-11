import requests
import json

from requests import api

api_baseurl='https://www.breakingbadapi.com/api/'

def getAllCharacters():
    char_details=[]
    api_url=api_baseurl+'characters'
    try:
        api_res=requests.get(api_url)
        if api_res.status_code==200:
            api_res_json=api_res.json()
            
            for i in range(0,len(api_res_json)):
                char_id=str(api_res_json[i]['char_id'])
                char_name=api_res_json[i]['name']
                char_img=api_res_json[i]['img']
                #char_details.append(char_id)
                details={'char_name':char_name,'char_img':char_img}
                char_details.append(details)
            return char_details
        else:
            print(api_res.status_code)    

    except Exception as ex:
        print(ex)

        #print(api_url)    


if __name__=='__main__':
    getAllCharacters()