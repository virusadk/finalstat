from datetime import datetime
import schedule
# import time
import requests
from datetime import timedelta
from telegram import send_telegram
from telegramchannel import send_channel

def format_message_fora(message,period):
    
    SN, L, O1, O2,S,CPS,S1,S2,S21,S22,ST,STR,K1,K2,KST = message.values()
    SP = S + 3*60*60
    Stime = datetime.fromtimestamp(SP).strftime('%d.%m %H:%M')

    mess = f'\U0001F3D3 {SN} - \U0001F4C6 {Stime} \n' \
            f'\U0001F3C6 {L} \n' \
            f'\U0001F9D1 {O1} - {O2}\U0001F9D1 \n' \
                f'\U0001F9FE 1- Партия:{S1} - {S2}\n' \
                    f'\U0001F9FE 2- Партия:{S21} - {S22}\n' \
            f'\n' \
                f'\U0001F9FE Стратегия:{STR}\n' \
                    f'\U0001F9FE Коэффициенты :{K1} - {K2}\n' \
                        f'\n' \
                f'\U0001F4B5 Ставка: 3-сет {ST} \U0001F4B5 Кеф: {KST}\n' \
                    f'\n' \
            
            
        


    send_telegram(mess)
    send_channel(mess)
    # print('send')            
    print(mess)
    
                          
def format_message_pred(message,period):
    
    SN, L, O1, O2,S,CPS,S1,S2,S21,S22,ST,K1,K2 = message.values()
    SP = S + 3*60*60
    Stime = datetime.fromtimestamp(SP).strftime('%d.%m %H:%M')

    if str(ST) == 'Возможно будет ставка':
        mess =  f'\U000026A0 {ST}\n' \
                f'\U0001F3D3 {SN} - \U0001F4C6 {Stime} \n' \
                f'\U0001F3C6 {L} \n' \
                f'\U0001F9D1 {O1} - {O2}\U0001F9D1 \n' \
                    f'\U0001F9FE 1- Партия:{S1} - {S2}\n' \
                        f'\U0001F9FE 2- Партия:{S21} - {S22}\n' \
                            f'\U0001F9FE Коэффициенты :{K1} - {K2}\n' \
                f'\n' \
                f'\U000026A0 \U000026A0 \U000026A0 \U000026A0 \U000026A0 \n' \
                        \
                    \
                        f'\n' \
            
            
        


        send_telegram(mess)
        send_channel(mess)
        # print('send')            
        print(mess)
        
    if str(ST) == 'Отмена. Ставки не будет':
        mess =  f'\U000026D4 {ST}\n' \
                f'\U0001F3D3 {SN} - \U0001F4C6 {Stime} \n' \
                f'\U0001F3C6 {L} \n' \
                f'\U0001F9D1 {O1} - {O2}\U0001F9D1 \n' \
                    f'\U0001F9FE 1- Партия:{S1} - {S2}\n' \
                        f'\U0001F9FE 2- Партия:{S21} - {S22}\n' \
                            f'\U0001F9FE Коэффициенты :{K1} - {K2}\n' \
                f'\n' \
               f'\U000026D4 \U000026D4 \U000026D4 \U000026D4 \U000026D4 \n' \
                        \
                    \
                        f'\n' \
            
            
        


        send_telegram(mess)
        send_channel(mess)
        # print('send')            
        print(mess)

    
   

def format_message(message,period): 
    
    
    
        SN, L, O1, O2,S,CPS,S1,S2,S21,S22,ST,STR,K1,K2,KST = message.values()
        SP = S + 3*60*60
        Stime = datetime.fromtimestamp(SP).strftime('%d.%m %H:%M')
   
        mess = f'\U0001F3D3 {SN} - \U0001F4C6 {Stime} \n' \
                f'\U0001F3C6 {L} \n' \
                f'\U0001F9D1 {O1} - {O2}\U0001F9D1 \n' \
                    f'\U0001F9FE 1- Партия:{S1} - {S2}\n' \
                        f'\U0001F9FE 2- Партия:{S21} - {S22}\n' \
                f'\n' \
                    f'\U0001F9FE Стратегия:{STR}\n' \
                        f'\U0001F9FE Коэффициенты :{K1} - {K2}\n' \
                        f'\n' \
                    f'\U0001F4B5 Ставка: 3-сет {ST} \U0001F4B5 Кеф: {KST}\n' \
                        f'\n' \
               
                
            
    
    
        send_telegram(mess)
        send_channel(mess)
        # print('send')            
        print(mess)
    
        
    
def prov_pobed(pobeda,idlive,period):
        
    
    with open('outs.txt','r') as file:
                                
        for item in file.readlines():
            line = item.strip()
                # print(line)
            idid = line.split('-')[0]
                
                
            if str(idlive) == idid:
                
                out = line.split('-')[-1]
                print(out)
                print(pobeda)
                if ((str(out) == 'out1') and (str(pobeda) == 'V1')):
                    print('Победил оутсайдер')
                        # print(totalline)
                    try:
                        listdb = []
                        with open('db.txt','r') as file:
                                                            
                                for item in file.readlines():
                                    line = item.strip()
                                    iddb = line.split('-')[0]                
                                                        # print(idid)
                                    listdb.append(iddb)
                                                        # ln = int(line)
                                    file.close()
                                    print(listdb)    
                    except:
                        print('невозможно прочитать db.txt')
                    
                
                                
                                
                    if str(idlive) in listdb:
                        print('Событие было отправлено')
                                    
                    else:
                        kef = []
                        for tot in period['E']:
                            g = tot['G']

                            if g == 1:
                                k = tot['C']
                                kef.append(k)

                        
                        # print(kef)                     
                        kef1 = kef[0]
                        kef2 = kef[1]
                        try:
                            headers = {
                                'Accept': 'application/json, text/plain, */*',
                                'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                                'Cache-Control': 'max-age=0',
                                'Connection': 'keep-alive',
                                # Requests sorts cookies= alphabetically
                                # 'Cookie': 'lng=ru; flaglng=ru; tzo=3; typeBetNames=short; auid=WNT5lGM/wTi3nUhsyj63Ag==; _ym_uid=1665122621415459923; _ym_d=1665122621; _ga=GA1.2.1498550217.1665122621; sh.session=d5016e9f-8661-4690-96a9-27aa3a14bb09; pushfree_status=canceled; right_side=right; fast_coupon=true; SESSION=178f7e31b81ce6fc219e4b43a05c475f; visit=1-f8d39eadc3a15b2b834eb0c195bed585; completed_user_settings=true; _gid=GA1.2.329207666.1666705462; _ym_isad=2; v3fr=1; coefview=0; _ym_visorc=w; _glhf=1666886418; ggru=188; _gat_gtag_UA_131611796_1=1',
                                'If-Modified-Since': 'Sat, 1 Jan 2000 00:00:00 GMT',
                                'Referer': 'https://1xstavka.ru/live/table-tennis/2064427-masters/407659157-sergey-varfolomeev-a-viktor-maly',
                                'Sec-Fetch-Dest': 'empty',
                                'Sec-Fetch-Mode': 'cors',
                                'Sec-Fetch-Site': 'same-origin',
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
                                'X-Requested-With': 'XMLHttpRequest',
                                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                            }

                            params = {
                                'id': idlive,
                                'lng': 'ru',
                                'cfview': '0',
                                'isSubGames': 'true',
                                'GroupEvents': 'true',
                                'allEventsGroupSubGames': 'true',
                                'countevents': '250',
                                'partner': '51',
                                'grMode': '2',
                                'marketType': '1',
                                'isNewBuilder': 'true',
                            }

                            response = requests.get('https://1xstavka.ru/LiveFeed/GetGameZip', params=params,  headers=headers)
                            resultgame = response.json()
                            keffchik = []
                            for igra in resultgame['SG']:
                                pn = igra['PN']
                                if '3-я Партия' in pn:
                                    for keff in igra['GE']:
                                        g = keff['G']
                                        if g == 1:
                                            k = tot['C']
                                            keffchik.append(k)



                                    # print(kef)                     
                                    kefp1 = keffchik[0]
                                    kefp2 = keffchik[1] 
                        except:
                            kefp1 = ' '
                            kefp2 = ' '
                                

                        
                        message = {}
                                        
                        message['SN'] = period['SN']
                        message['L'] = period['L']
                        message['O1'] = period['O1']
                        message['O2'] = period['O2']
                        message['S'] = period['S']
                        message['CPS'] = period['SC']['CPS']
                        message['S1'] = period['SC']['PS'][0]['Value']['S1']
                        message['S2'] = period['SC']['PS'][0]['Value']['S2']
                        
                        message['ST'] = 'П2'
                        message['STR'] = 'Есть фаворит'
                        message['K1'] = kef1
                        message['K2'] = kef2
                        message['KST'] = kefp2
                        format_message_fora(message,period)
                        print('Отправлено на форматирование') 
                        try:    
                            with open('db.txt','a') as file:
                                file.write(f'\n{idlive}-V2')            
                                file.close()
                                print('Событие записано в db.txt') 
                        except:
                            print('Невозможно записать в файл db.txt')
                            
                            
                
                if ((str(out) == 'out2') and (str(pobeda) == 'V2')):
                    print('Победил оутсайдер')
                    try:
                        listdb = []
                        with open('db.txt','r') as file:
                                                            
                                for item in file.readlines():
                                    line = item.strip()
                                    iddb = line.split('-')[0]                
                                                        # print(idid)
                                    listdb.append(iddb)
                                                        # ln = int(line)
                                    file.close()
                                    print(listdb)    
                    except:
                        print('невозможно прочитать db.txt')
                    
                
                                
                                
                    if str(idlive) in listdb:
                        print('Событие было отправлено')
                                    
                    else:
                        message = {}
                                        
                        message['SN'] = period['SN']
                        message['L'] = period['L']
                        message['O1'] = period['O1']
                        message['O2'] = period['O2']
                        message['S'] = period['S']
                        message['CPS'] = period['SC']['CPS']
                        message['S1'] = period['SC']['PS'][0]['Value']['S1']
                        message['S2'] = period['SC']['PS'][0]['Value']['S2']
                        
                        message['ST'] = 'П1'
                        message['STR'] = 'Есть фаворит'
                        message['K1'] = kef1
                        message['K2'] = kef2
                        message['KST'] = kefp1
                        format_message_fora(message,period)
                        print('Отправлено на форматирование') 
                        try:    
                            with open('db.txt','a') as file:
                                file.write(f'\n{idlive}-V1')            
                                file.close()
                                print('Событие записано в db.txt') 
                        except:
                            print('Невозможно записать в файл db.txt')        
        file.close() 
      
                            
                            
                
    

def poisk_pred_total(idlive,period,pobed):
    
    with open('retro.txt','r') as file:
                                
        for item in file.readlines():
            line = item.strip()
                # print(line)
            
                
                
            if str(idlive) == line:
                print('Событие есть в retro.txt')
                try:
                    listdb = []
                    with open('db.txt','r') as file:
                                                        
                            for item in file.readlines():
                                line = item.strip()
                                iddb = line.split('-')[0]            
                                                   # print(idid)
                                listdb.append(iddb)
                                                    # ln = int(line)
                                file.close()
                                print(listdb)    
                except:
                    print('невозможно прочитать db.txt')
                
               
                            
                            
                if str(idlive) in listdb:
                        print('Событие было отправлено')
                                
                else:
                    kef = []
                    for tot in period['E']:
                        g = tot['G']

                        if g == 1:
                            k = tot['C']
                            kef.append(k)



                    # print(kef)                     
                    kef1 = kef[0]
                    kef2 = kef[1]
                    try:
                        headers = {
                                'Accept': 'application/json, text/plain, */*',
                                'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                                'Cache-Control': 'max-age=0',
                                'Connection': 'keep-alive',
                                # Requests sorts cookies= alphabetically
                                # 'Cookie': 'lng=ru; flaglng=ru; tzo=3; typeBetNames=short; auid=WNT5lGM/wTi3nUhsyj63Ag==; _ym_uid=1665122621415459923; _ym_d=1665122621; _ga=GA1.2.1498550217.1665122621; sh.session=d5016e9f-8661-4690-96a9-27aa3a14bb09; pushfree_status=canceled; right_side=right; fast_coupon=true; SESSION=178f7e31b81ce6fc219e4b43a05c475f; visit=1-f8d39eadc3a15b2b834eb0c195bed585; completed_user_settings=true; _gid=GA1.2.329207666.1666705462; _ym_isad=2; v3fr=1; coefview=0; _ym_visorc=w; _glhf=1666886418; ggru=188; _gat_gtag_UA_131611796_1=1',
                                'If-Modified-Since': 'Sat, 1 Jan 2000 00:00:00 GMT',
                                'Referer': 'https://1xstavka.ru/live/table-tennis/2064427-masters/407659157-sergey-varfolomeev-a-viktor-maly',
                                'Sec-Fetch-Dest': 'empty',
                                'Sec-Fetch-Mode': 'cors',
                                'Sec-Fetch-Site': 'same-origin',
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
                                'X-Requested-With': 'XMLHttpRequest',
                                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                            }

                        params = {
                                'id': idlive,
                                'lng': 'ru',
                                'cfview': '0',
                                'isSubGames': 'true',
                                'GroupEvents': 'true',
                                'allEventsGroupSubGames': 'true',
                                'countevents': '250',
                                'partner': '51',
                                'grMode': '2',
                                'marketType': '1',
                                'isNewBuilder': 'true',
                            }

                        response = requests.get('https://1xstavka.ru/LiveFeed/GetGameZip', params=params,  headers=headers)
                        resultgame = response.json()
                        keffchik = []
                        for igra in resultgame['SG']:
                            pn = igra['PN']
                            if '3-я Партия' in pn:
                                for keff in igra['GE']:
                                    g = keff['G']
                                    if g == 1:
                                        k = tot['C']
                                        keffchik.append(k)



                                # print(kef)                     
                                kefp1 = keffchik[0]
                                kefp2 = keffchik[1] 
                    except:
                        kefp1 = ' '
                        kefp2 = ' '
                    if 'P1' in pobed:
                        message = {}
                                        
                        message['SN'] = period['SN']
                        message['L'] = period['L']
                        message['O1'] = period['O1']
                        message['O2'] = period['O2']
                        message['S'] = period['S']
                        message['CPS'] = period['SC']['CPS']
                        message['S1'] = period['SC']['PS'][0]['Value']['S1']
                        message['S2'] = period['SC']['PS'][0]['Value']['S2']
                        message['S21'] = period['SC']['PS'][1]['Value']['S1']
                        message['S22'] = period['SC']['PS'][1]['Value']['S2']
                        message['ST'] = 'П2'
                        message['STR'] = 'Игроки равны'
                        message['K1'] = kef1
                        message['K2'] = kef2
                        message['KST'] = kefp2
                        format_message(message,period)
                        print('Отправлено на форматирование') 
                        try:    
                            with open('db.txt','a') as file:
                                file.write(f'\n{idlive}-P2')            
                                file.close()
                                print('Событие записано в db.txt') 
                        except:
                            print('Невозможно записать в файл db.txt')
                        file.close() 
                    if 'P2' in pobed:
                        message = {}
                                        
                        message['SN'] = period['SN']
                        message['L'] = period['L']
                        message['O1'] = period['O1']
                        message['O2'] = period['O2']
                        message['S'] = period['S']
                        message['CPS'] = period['SC']['CPS']
                        message['S1'] = period['SC']['PS'][0]['Value']['S1']
                        message['S2'] = period['SC']['PS'][0]['Value']['S2']
                        message['S21'] = period['SC']['PS'][1]['Value']['S1']
                        message['S22'] = period['SC']['PS'][1]['Value']['S2']
                        message['ST'] = 'П1'
                        message['STR'] = 'Игроки равны'
                        message['K1'] = kef1
                        message['K2'] = kef2
                        message['KST'] = kefp1
                        format_message(message,period)
                        print('Отправлено на форматирование') 
                        try:    
                            with open('db.txt','a') as file:
                                file.write(f'\n{idlive}-P1')            
                                file.close()
                                print('Событие записано в db.txt') 
                        except:
                            print('Невозможно записать в файл db.txt')
                        file.close() 
            
            
    
    
def preduprezhdenie(idlive,period):
    with open('retro.txt','r') as file:
                                
        for item in file.readlines():
            line = item.strip()
                # print(line)
            
                
                
            if str(idlive) == line:
                print('Событие есть в retro.txt')
                try:
                    listdb = []
                    with open('pred.txt','r') as file:
                                                        
                            for item in file.readlines():
                                line = item.strip()
                                           
                                                   # print(idid)
                                listdb.append(line)
                                                    # ln = int(line)
                                file.close()
                                print(listdb)    
                except:
                    print('невозможно прочитать db.txt')
                
               
                            
                            
                if str(idlive) in listdb:
                        print('Предупреждение было отправлено')
                                
                else:
                    kef = []
                    for tot in period['E']:
                        g = tot['G']

                        if g == 1:
                            k = tot['C']
                            kef.append(k)



                    # print(kef)                     
                    kef1 = kef[0]
                    kef2 = kef[1]
                    message = {}
                                    
                    message['SN'] = period['SN']
                    message['L'] = period['L']
                    message['O1'] = period['O1']
                    message['O2'] = period['O2']
                    message['S'] = period['S']
                    message['CPS'] = period['SC']['CPS']
                    message['S1'] = period['SC']['PS'][0]['Value']['S1']
                    message['S2'] = period['SC']['PS'][0]['Value']['S2']
                    message['S21'] = period['SC']['PS'][1]['Value']['S1']
                    message['S22'] = period['SC']['PS'][1]['Value']['S2']
                    message['ST'] = 'Возможно будет ставка'
                    message['K1'] = kef1
                    message['K2'] = kef2
                    format_message_pred(message,period)
                    print('Отправлено на форматирование') 
                    try:    
                        with open('pred.txt','a') as file:
                            file.write(f'\n{idlive}')            
                            file.close()
                            print('Событие записано в pred.txt') 
                    except:
                        print('Невозможно записать в файл db.txt')
                    file.close() 
    

def poisk_predup(idlive,period):
    with open('pred.txt','r') as file:
                                
        for item in file.readlines():
            line = item.strip()
                # print(line)
            
                
                
            if str(idlive) == line:
                print('Событие есть в retro.txt')
                try:
                    listdb = []
                    with open('otmena.txt','r') as file:
                                                        
                            for item in file.readlines():
                                line = item.strip()
                                           
                                                   # print(idid)
                                listdb.append(line)
                                                    # ln = int(line)
                                file.close()
                                print(listdb)    
                except:
                    print('невозможно прочитать db.txt')
                
               
                            
                            
                if str(idlive) in listdb:
                        print('Отмена была отправлена')
                                
                else:
                    kef = []
                    for tot in period['E']:
                        g = tot['G']

                        if g == 1:
                            k = tot['C']
                            kef.append(k)



                    # print(kef)                     
                    kef1 = kef[0]
                    kef2 = kef[1]
                    message = {}
                                    
                    message['SN'] = period['SN']
                    message['L'] = period['L']
                    message['O1'] = period['O1']
                    message['O2'] = period['O2']
                    message['S'] = period['S']
                    message['CPS'] = period['SC']['CPS']
                    message['S1'] = period['SC']['PS'][0]['Value']['S1']
                    message['S2'] = period['SC']['PS'][0]['Value']['S2']
                    message['S21'] = period['SC']['PS'][1]['Value']['S1']
                    message['S22'] = period['SC']['PS'][1]['Value']['S2']
                    message['ST'] = 'Отмена. Ставки не будет'
                    message['K1'] = kef1
                    message['K2'] = kef2
                    format_message_pred(message,period)
                    print('Отправлено на форматирование') 
                    try:    
                        with open('otmena.txt','a') as file:
                            file.write(f'\n{idlive}')            
                            file.close()
                            print('Событие записано в pred.txt') 
                    except:
                        print('Невозможно записать в файл db.txt')
                    file.close() 
                

def get_1x2(result):
    # print(result)
    
    for period in result['Value']:
        liga = period['L']
        liga1 = liga.split('.')[0]
        try:
            
            cps = period['SC']['CPS']
            if (cps == '2-я Партия'):
                print('Проверка счета первой партии')        
                try:    
                    nf = period['SC']['PS'][0]['Value']['NF']
                except:
                    print('Нет NF')
                
                o1 = period['SC']['PS'][0]['Value']['S1']
                o2 = period['SC']['PS'][0]['Value']['S2']
                o21 = period['SC']['PS'][1]['Value']['S1']
                o22 = period['SC']['PS'][1]['Value']['S2']
                if (int(o1) > int(o2)) and (int(o21) > int(o22)) and (int(o21) >= 9):
                    print('Счет меньше 16')
                    idlive = period['I']
                    preduprezhdenie(idlive,period)
                if (int(o1) < int(o2)) and (int(o21) < int(o22)) and (int(o22) >= 9):
                    print('Счет меньше 16')
                    idlive = period['I']
                    preduprezhdenie(idlive,period)
                    
            if (cps == '3-я Партия'):
                print('Проверка счета первой партии')        
                try:    
                    nf = period['SC']['PS'][0]['Value']['NF']
                    nf2 = period['SC']['PS'][1]['Value']['NF']
                except:
                    print('Нет NF')
                
                o1 = period['SC']['PS'][0]['Value']['S1']
                o2 = period['SC']['PS'][0]['Value']['S2']
                o21 = period['SC']['PS'][1]['Value']['S1']
                o22 = period['SC']['PS'][1]['Value']['S2']
                
                if (int(o1) > int(o2)) and (int(o21) < int(o22)):
                    print('Счет меньше 16')
                    idlive = period['I']
                    
                    poisk_predup(idlive,period)
                    
                if (int(o1) < int(o2)) and (int(o21) > int(o22)):
                    print('Счет меньше 16')
                    idlive = period['I']
                    
                    poisk_predup(idlive,period)
                
                if (int(o1) > int(o2)) and (int(o21) > int(o22)):
                    print('Счет меньше 16')
                    idlive = period['I']
                    pobed = 'P1'
                    poisk_pred_total(idlive,period,pobed)
                    
                if (int(o1) < int(o2)) and (int(o21) < int(o22)):
                    print('Счет меньше 16')
                    idlive = period['I']
                    pobed = 'P2'
                    poisk_pred_total(idlive,period,pobed)
                # else:
                    # print('Счет больше 16')
                if (int(o1) > int(o2)) and (int(o21) > int(o22)):
                    print('Победил 2')
                    idlive = period['I'] 
                    pobeda = 'V1'
                    sgi = period['SGI']
                    prov_pobed(pobeda,idlive,period)
                    print('передано в пров побед')
                if (int(o1) < int(o2)) and (int(o21) < int(o22)):
                    print('Победил 1')
                    idlive = period['I'] 
                    pobeda = 'V2'
                    sgi = period['SGI']
                    prov_pobed(pobeda,idlive,period)
                    print('передано в пров побед')
           
                
        except:
            print('Нет cps')
                
        
        
            # print(o1,'-',o2)        
                
                # print('Передано на проверку')
                
                    
        # except:
            # print('Не удалось получить статус игры. Игра не может быть проверена на соответствие')
                    
            # igra_not_start(game) 
            # print('Игра не началась. Отправлена на проверку') 
        # else:
            # igra_start(game) 
            # print('Игра уже идет. Отправлена на проверку')                 
        
        
                          
        
        
            
            
        
    
    
    # print(message)
    # search_db(message)   
    # print('search_db')            
    

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
        result = response.json()
        # print(result)
        get_1x2(result)
        print('Переданы данные LIVE')
    
    except:
        pass
    
if __name__ == '__main__':
    main()
schedule.every(15).seconds.do(main)
while True:
 
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    # time.sleep(1) 
