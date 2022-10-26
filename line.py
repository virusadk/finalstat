
from datetime import datetime
import schedule
import time
import requests
from datetime import timedelta
from telegram import send_telegram
def search1(id,kef1,kef2):
    
    with open('outs.txt','r') as file:
        list1 = []                                            
        for item in file.readlines():
            line = item.strip()
            idid = line.split('-')[0]
                                                # print(idid)
            list1.append(idid)
                            # ln = int(line)
            file.close()
                                            
                                        
        # print(list1)
        if str(id) in list1:
            print('Событие уже есть 111 ')
                
        else:
                                                
            
            with open('outs.txt','a') as file:
                if float(kef1) > float(kef2):
                    file.write(f'\n{id}-out1') 
                if float(kef2) > float(kef1):
                    file.write(f'\n{id}-out2')           
                file.close()
                

def search(id):
    
    with open('retro.txt','r') as file:
        list1 = []                                            
        for item in file.readlines():
            line = item.strip()
            
                                                # print(idid)
            list1.append(line)
                            # ln = int(line)
            file.close()
                                            
                                        
        # print(list1)
        if str(id) in list1:
            print('Событие уже есть ')
                
        else:
                                                
            
            with open('retro.txt','a') as file:
                file.write(f'\n{id}')            
                file.close()
                print('Записано новое событие')
                
def stat(sgi,game):
    try:

    

        headers = {
            'authority': 'eventsstat.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'referer': 'https://eventsstat.com/statisticpopup/game/10/6347c72ff75a663f6947def9/main?hs=1&fh=1&ln=ru&w=899&rtl=0&r=51&g=44&tz=3&geo=22&mh=200',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'x-statistic-api': '1',
        }

        params = {
            'gameId': sgi,
            'ln': 'ru',
            'partner': '51',
            'geo': '22',
        }

        response = requests.get('https://eventsstat.com/sf/Game', params=params, headers=headers)
    except:
        pass
    game_stat = response.json()
    # print(game_stat)
    static(game_stat,game)
    
    
def static(game_stat,game):
    try:
        for gs in game_stat['RTS']:
            TT = gs['TT']
            if TT == 'Рейтинг в день игры':
                RDIV1 = gs['V1']
                RDIV2 = gs['V2']
                print(TT,RDIV1,RDIV2)
            if TT == 'Процент выигрыша своей подачи':
                PVSPV1 = gs['V1']
                PVSPV2 = gs['V2']
                print(TT,PVSPV1,PVSPV2)
            if TT == 'История личных встреч':
                ILVV1 = gs['V1']
                ILVV2 = gs['V2']
                print(TT,ILVV1,ILVV2)
        # print(gs)
        # print (V1,'-',V2) 
    except:
        pass                               
    sravnenie(RDIV1,RDIV2,PVSPV1,PVSPV2,ILVV1,ILVV2,game)
    
def sravnenie(RDIV1,RDIV2,PVSPV1,PVSPV2,ILVV1,ILVV2,game):
    if (abs(int(RDIV1) - int(RDIV2 )) <=50) and (abs(int(ILVV1) - int(ILVV2 )) <= 5):
        id = game['I']
        search(id)

def igra(resultline):
    
    
    for game in resultline['Value']:
        try:
            
            liga = game['L']
            liga1 = liga.split('.')[0]
            nf = game['SC']['PS'][0]['Value']['NF']
        except:
            pass
            # print('Не удалось получить NF')
            
        try: 
            # if ('Лига Про'== liga1) or ('Челленджер'==liga1) or ('Кубок ТТ' == liga1):  
            if (nf == '1-я Партия') and ((game['SC']['PS'][0]['Value']['S1'] not in game['SC']['PS'][0]['Value']) or (game['SC']['PS'][0]['Value']['S2'] not in game['SC']['PS'][0]['Value'])):


                kef = []
                for tot in game['E']:
                    g = tot['G']

                    if g == 1:
                        k = tot['C']
                        kef.append(k)



                # print(kef)                     
                kef1 = kef[0]
                kef2 = kef[1]
                # print(kef1,'-',kef2)              
                if (float(kef1) >= 1.5) and (float(kef2) >= 1.5):
                    # print('Игроки равны')
                    id = game['I']
                    try:
                        sgi = game['SGI']
                    except:
                        pass 
                    # print(sgi)
                    # search(id) 
                    stat(sgi,game)
                else:
                    pass
                    # print('Есть аутсайдер') 

                if (float(kef1) >= 6) or (float(kef2) >= 6):
                    # print('Игроки равны')
                    id = game['I'] 

                    # print(id)
                    search1(id,kef1,kef2) 
                else:
                    pass
                    # print('Есть аутсайдер')                  
        except:
            pass
            # print('нечего сравнивать')
                    
    



def main():
    
    
    



    params = {
    'sports': '10',
    'count': '50',
    'antisports': '188',
    'mode': '4',
    'country': '22',
    'partner': '51',
    'getEmpty': 'true',
    'noFilterBlockEvent': 'true',
    }

    
   
    response = requests.get('https://1xstavka.ru/LiveFeed/Get1x2_VZip', params=params)
    resultline = response.json()
    # print(result)
    igra(resultline)
    
    
if __name__ == '__main__':
    main()
schedule.every(15).seconds.do(main)
while True:
 
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1) 
