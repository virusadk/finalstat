from datetime import datetime
import schedule
# import time
import requests
from datetime import timedelta
from telegram import send_telegram
from telegramchannel import send_channel

def format_message_fora(message,period):
    
    SN, L, O1, O2,S,CPS,S1,S2,S21,S22,ST,STR = message.values()
    SP = S + 3*60*60
    Stime = datetime.fromtimestamp(SP).strftime('%d.%m %H:%M')

    mess = f'\U0001F3D3 {SN} - \U0001F4C6 {Stime} \n' \
            f'\U0001F3C6 {L} \n' \
            f'\U0001F9D1 {O1} - {O2}\U0001F9D1 \n' \
                f'\U0001F9FE 1- Партия:{S1} - {S2}\n' \
                f'\U0001F9FE 2- Партия:{S21} - {S22}\n' \
            f'\n' \
                f'\U0001F9FE Стратегия:{STR}\n' \
                        f'\n' \
                f'\U0001F4B5 Ставка: 3-сет {ST}\n' \
                    f'\n' \
            
            
        


    send_telegram(mess)
    send_channel(mess)
    # print('send')            
    print(mess)
    
                          
def format_message_pred(message,period):
    
    SN, L, O1, O2,S,CPS,S1,S2,S21,S22,ST = message.values()
    SP = S + 3*60*60
    Stime = datetime.fromtimestamp(SP).strftime('%d.%m %H:%M')

    if str(ST) == 'Возможно будет ставка':
        mess =  f'\U000026A0 {ST}\n' \
                f'\U0001F3D3 {SN} - \U0001F4C6 {Stime} \n' \
                f'\U0001F3C6 {L} \n' \
                f'\U0001F9D1 {O1} - {O2}\U0001F9D1 \n' \
                    f'\U0001F9FE 1- Партия:{S1} - {S2}\n' \
                        f'\U0001F9FE 2- Партия:{S21} - {S22}\n' \
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
    
    
    
        SN, L, O1, O2,S,CPS,S1,S2,ST,STR = message.values()
        SP = S + 3*60*60
        Stime = datetime.fromtimestamp(SP).strftime('%d.%m %H:%M')
   
        mess = f'\U0001F3D3 {SN} - \U0001F4C6 {Stime} \n' \
                f'\U0001F3C6 {L} \n' \
                f'\U0001F9D1 {O1} - {O2}\U0001F9D1 \n' \
                    f'\U0001F9FE 1- Партия:{S1} - {S2}\n' \
                f'\n' \
                    f'\U0001F9FE Стратегия:{STR}\n' \
                        f'\n' \
                    f'\U0001F4B5 Ставка: 3-сет {ST}\n' \
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
                        message['STR'] = 'Есть фаворит'
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
                        message['S21'] = period['SC']['PS'][1]['Value']['S1']
                        message['S22'] = period['SC']['PS'][1]['Value']['S2']
                        message['ST'] = 'П1'
                        message['STR'] = 'Есть фаворит'
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
