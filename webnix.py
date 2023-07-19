import requests
from bs4 import BeautifulSoup
CRED = '\033[92m'
CEND = '\033[0m'
import os
os.system('clear')


print(CRED + ''''

     __    __     _           _      
    / / /\ \ \___| |__  _ __ (_)_  __
    \ \/  \/ / _ \ '_ \| '_ \| \ \/ /
     \  /\  /  __/ |_) | | | | |>  < 
      \/  \/ \___|_.__/|_| |_|_/_/\_\\
                                 
      
      ''' + CEND)

input_txt=input(CRED +'Put File: '+ CEND)
limit_txt=int(input(CRED +'Limit: '+ CEND))
more_export_txt=input(CRED +'More Export File: '+ CEND)
less_export_txt=input(CRED +'Less Export File: '+ CEND)
login_error_export_txt=input(CRED +'Error Facebook Account File: '+ CEND)



f = open(input_txt, "r")
import_data=f.read()

import_data=import_data.split('\n')
c=1
for import_line in import_data:
    try:
        cookie=import_line.split(' | ')[2]
        user_id=str(import_line.split(' | ')[0])
        password=str(import_line.split(' | ')[1])
    except:
        print('Format Error. Line Number:',str(c))
        continue

    headers = {
        'authority': 'mbasic.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7,he;q=0.6',
        'cache-control': 'max-age=0',
        'cookie':cookie,
        'dnt': '1',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-full-version-list': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.199", "Google Chrome";v="114.0.5735.199"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'viewport-width': '1920',
    }

    response = requests.get('https://mbasic.facebook.com/'+str(user_id)+'/friends', headers=headers)
    if(response.status_code==200):
        soup = BeautifulSoup(response.text,'html.parser')
        try:
            fnds=soup.select('#objects_container h3')[0]
            fnds=int(str(fnds).split(')')[0].split('(')[1])
            if fnds>limit_txt:
                f = open(more_export_txt, "a")
                f.write(str(user_id)+' | '+str(password)+'\n')
                f.close()
            else:
                f = open(less_export_txt, "a")
                f.write(str(user_id)+' | '+str(password)+'\n')
                f.close()
        except:
            f = open(login_error_export_txt, "a")
            f.write(import_line+'\n')
            f.close()

            print('\033[31m'+'User Cookie Is Not Correct. User ID:#'+user_id+' Line Number:'+str(c)+ CEND)
    else:
        f = open(login_error_export_txt, "a")
        f.write(import_line+'\n')
        f.close()

        print('\033[31m'+'Facebook Error. User ID:#'+user_id+' Line Number:'+str(c)+ CEND)

        
    print(CRED +'Account Checked '+str(c)+'/'+str(len(import_data))+', Remains:'+str(len(import_data)-c)+ CEND)
    c+=1
