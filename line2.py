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
                
                
def searchm(id):
    
    with open('retrom.txt','r') as file:
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
                                                
            
            with open('retrom.txt','a') as file:
                file.write(f'\n{id}')            
                file.close()
                print('Записано новое событие')                
                

        


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
                if ((float(kef1) >= 1.7) and (float(kef1) <= 1.8)) or ((float(kef2) >= 1.7) and (float(kef2) <= 1.8)):
                    # print('Игроки равны')
                    id = game['I']
                    try:
                        sgi = game['SGI']
                    except:
                        pass 
                    # print(sgi)
                    # search(id) 
                    search(id)
                

                if (float(kef1) >= 2.5) or (float(kef2) >= 2.5):
                # if (float(kef1) >= 2) or (float(kef2) >= 2):
                    # print('Игроки равны'):
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
    
    
    try:
        



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
    except:
        pass
    
if __name__ == '__main__':
    main()
schedule.every(15).seconds.do(main)
while True:
 
    
    schedule.run_pending()
    time.sleep(1) 
