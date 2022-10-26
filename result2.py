from datetime import datetime
import schedule
# import time
import requests
from datetime import timedelta
from telegram import send_telegram
from telegramchannel import send_channel
def igrau(resultline):
    # print(result)
    
    for period in resultline['Value']:
        try:
            cps = period['SC']['CPS']
            
        except:
            pass
        if ('4-я Партия' in cps) or ('Игра завершена' in cps): 
            idl = period['I']
            o31 = period['SC']['PS'][2]['Value']['S1']
            o32 = period['SC']['PS'][2]['Value']['S2']
            prov_result(period,idl)
            # if (cps == '3-я Партия'):
                # print('3-я Партия')
            # idlive = period['I']
                # print(idlive)
            
                
        
                
def prov_result(period,idl):
    
    liga = period['L']
    liga1 = liga.split('.')[0]
    
    with open('db.txt','r') as file:
                                
        for item in file.readlines():
            
            line = item.strip()
            print(line)
            idid = line.split('-')[0]
            print(idid)
            print(idl)
            # if ('Лига Про'== liga1) or ('Челленджер'==liga1) or ('Кубок ТТ' == liga1):  
            # print('Лига подходит')            
            if str(idl) == idid:
                print('Была сделана ставка')    
                stavka = line.split('-')[-1]
                print (stavka)
                if str(stavka) == 'P1':
                    print('Проверяем результат ТБ')
                    o31 = period['SC']['PS'][2]['Value']['S1']
                    o32 = period['SC']['PS'][2]['Value']['S2']
                    if int(o31) > int(o32):
                        print('ТБ есть. Отправляется сообщение')
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
                        message['S31'] = period['SC']['PS'][2]['Value']['S1']
                        message['S32'] = period['SC']['PS'][2]['Value']['S2']
                        message['ST'] = '3 сет: П1'
                        message['STR'] = 'Игроки равны'
                        message['RES'] = 'Ставка зашла'
                        format_message_result(message,idl,period)
                        print('Отправлено на форматирование результата') 
                    if int(o31) < int(o32):
                        print('ТБ нет. Отправляется сообщение')
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
                        message['S31'] = period['SC']['PS'][2]['Value']['S1']
                        message['S32'] = period['SC']['PS'][2]['Value']['S2']
                        message['ST'] = '3 сет: П1'
                        message['STR'] = 'Игроки равны'
                                
                        message['RES'] = 'Ставка проиграла'
                        format_message_result(message,idl,period)
                        print('Отправлено на форматирование результата') 
                        
                if str(stavka) == 'P2':
                    print('Проверяем результат ТБ')
                    o31 = period['SC']['PS'][2]['Value']['S1']
                    o32 = period['SC']['PS'][2]['Value']['S2']
                    if int(o32) > int(o31):
                        print('ТM есть. Отправляется сообщение')
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
                        message['S31'] = period['SC']['PS'][2]['Value']['S1']
                        message['S32'] = period['SC']['PS'][2]['Value']['S2']
                        message['ST'] = '3 сет: П2'
                        message['STR'] = 'Игроки равны'
                        message['RES'] = 'Ставка зашла'
                        format_message_result(message,idl,period)
                        print('Отправлено на форматирование результата') 
                    if int(o31) > int(o32):
                        print('ТM нет. Отправляется сообщение')
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
                        message['S31'] = period['SC']['PS'][2]['Value']['S1']
                        message['S32'] = period['SC']['PS'][2]['Value']['S2']
                        message['ST'] = '3 сет: П2'
                        message['STR'] = 'Игроки равны'        
                        message['RES'] = 'Ставка проиграла'
                        format_message_result(message,idl,period)
                        print('Отправлено на форматирование результата') 
                
                
                if str(stavka) == 'V1':
                    print('Проверяем результат Ф1')
                    o31 = period['SC']['PS'][2]['Value']['S1']
                    o32 = period['SC']['PS'][2]['Value']['S2']
                    if int(o31) > int(o32):
                        print('Ф1 есть. Отправляется сообщение')
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
                        message['S31'] = period['SC']['PS'][2]['Value']['S1']
                        message['S32'] = period['SC']['PS'][2]['Value']['S2']
                        message['ST'] = '3 сет: П1'
                        message['STR'] = 'Есть фаворит'
                        message['RES'] = 'Ставка зашла'
                        format_message_result(message,idl,period)
                        print('Отправлено на форматирование результата') 
                    else:
                        print('Ф1 нет. Отправляется сообщение')
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
                        message['S31'] = period['SC']['PS'][2]['Value']['S1']
                        message['S32'] = period['SC']['PS'][2]['Value']['S2']
                        message['ST'] = '3 сет: П1'
                        message['STR'] = 'Есть фаворит'        
                        message['RES'] = 'Ставка проиграла'
                        format_message_result(message,idl,period)
                        print('Отправлено на форматирование результата') 
                if str(stavka) == 'V2':
                    print('Проверяем результат Ф2')
                    o31 = period['SC']['PS'][2]['Value']['S1']
                    o32 = period['SC']['PS'][2]['Value']['S2']
                    if int(o32) > int(o31):
                        print('Ф2 есть. Отправляется сообщение')
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
                        message['S31'] = period['SC']['PS'][2]['Value']['S1']
                        message['S32'] = period['SC']['PS'][2]['Value']['S2']
                        message['ST'] = '3 сет: П2'
                        message['STR'] = 'Есть фаворит'
                        message['RES'] = 'Ставка зашла'
                        format_message_result(message,idl,period)
                        print('Отправлено на форматирование результата') 
                    else:
                        print('Ф2 нет. Отправляется сообщение')
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
                        message['S31'] = period['SC']['PS'][2]['Value']['S1']
                        message['S32'] = period['SC']['PS'][2]['Value']['S2']
                        message['ST'] = '3 сет: П2'
                        message['STR'] = 'Есть фаворит'        
                        message['RES'] = 'Ставка проиграла'
                        format_message_result(message,idl,period)
                        print('Отправлено на форматирование результата') 
                                    

def format_message_result(message,idl,period):
    with open('sr.txt','r') as file:
        list1 = []                                            
        for item in file.readlines():
            line = item.strip()
            
                                                # print(idid)
            list1.append(line)
                            # ln = int(line)
            file.close()
                                            
                                        
        print(list1)
        if str(idl) in list1:
            print('Событие уже есть ')
                
        else:
                             
            
            with open('sr.txt','a') as file:
                
                file.write(f'\n{idl}')          
                file.close()
                
                SN, L, O1, O2,S,CPS,S1,S2,S21,S22,S31,S32,ST,STR,RES = message.values()
                SP = S + 3*60*60
                Stime = datetime.fromtimestamp(SP).strftime('%d.%m %H:%M')
                if RES == 'Ставка зашла':
                    if STR == 'Игроки равны':
                        with open('sutki.txt','a') as file:
                    
                            file.write(f'\n True')          
                            file.close()
                    if STR == 'Есть фаворит':
                        with open('favorit.txt','a') as file:
                    
                            file.write(f'\n True')          
                            file.close()
                    mess = f'\U0001F3D3 {SN} - \U0001F4C6 {Stime} \n' \
                                f'\U0001F3C6 {L} \n' \
                                f'\U0001F9D1 {O1} - {O2}\U0001F9D1 \n' \
                                    f'\U0001F9FE 1- Партия:{S1} - {S2}\n' \
                                        f'\U0001F9FE 2- Партия:{S21} - {S22}\n' \
                                            f'\U0001F9FE 3- Партия:{S31} - {S32}\n' \
                                f'\n' \
                                    f'\U0001F9FE Стратегия:{STR}\n' \
                                     f'\n' \
                                    f'\U0001F4B5 Ставка: {ST} \n' \
                                        f'\U0001F4B5 Результат: {RES}  \U00002705	\U00002705 \U00002705  \n' \
                                        f'\n' \
                    
                    send_telegram(mess)
                    send_channel(mess)
                    
                    format_stat()
                    

                    # print('send')            
                    print(mess) 
                                            
                if RES == 'Ставка проиграла':
                    with open('sutki.txt','a') as file:
                
                        file.write(f'\n False')          
                        file.close()
                    mess = f'\U0001F3D3 {SN} - \U0001F4C6 {Stime} \n' \
                                f'\U0001F3C6 {L} \n' \
                                f'\U0001F9D1 {O1} - {O2}\U0001F9D1 \n' \
                                    f'\U0001F9FE 1- Партия:{S1} - {S2}\n' \
                                        f'\U0001F9FE 2- Партия:{S21} - {S22}\n' \
                                            f'\U0001F9FE 3- Партия:{S31} - {S32}\n' \
                                f'\n' \
                                   f'\U0001F9FE Стратегия:{STR}\n' \
                                     f'\n' \
                                    f'\U0001F4B5 Ставка: {ST} \n' \
                                        f'\U0001F4B5 Результат: {RES}  \U0000274C	\U0000274C \U0000274C  \n' \
                                        f'\n' \
                
                    send_telegram(mess)
                    send_channel(mess)
                    
                    format_stat()
                    

                    # print('send')            
                    print(mess)          

def format_stat():
    with open('sutki.txt','r') as file:
        struer = 0
        sfalser = 0                                          
        for item in file.readlines():
            line = item.strip()
            if 'True' in line:
                struer = struer + 1
            if 'False' in line:
                sfalser = sfalser + 1
                                                # print(idid)
            
                            # ln = int(line)
        file.close()
    with open('favorit.txt','r') as file:
        struef = 0
        sfalsef = 0                                          
        for item in file.readlines():
            line = item.strip()
            if 'True' in line:
                struef = struef + 1
            if 'False' in line:
                sfalsef = sfalsef + 1
                                                # print(idid)
            
                            # ln = int(line)
        file.close()
    format_mess_static(struer,sfalser,struef,sfalsef)
    
def format_mess_static(struer,sfalser,struef,sfalsef):
    
            
                
                
    mess = f'\U00002198 Статистика \U00002199 \n' \
        f'\n' \
        f' \U00002696 Игроки равны \U00002696 \n' \
        f' \U00002705 {struer} \n' \
            f' \U0000274C {sfalser} \n' \
                f'\n' \
                    f' \U0001F4C8 Есть фаворит \U0001F4C8  \n' \
            f' \U00002705 {struef} \n' \
                f' \U0000274C {sfalsef} \n' \
            f'\n' \

    send_telegram(mess)
    send_channel(mess)


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
        igrau(resultline)
    except:
        pass
    
if __name__ == '__main__':
    main()
schedule.every(5).seconds.do(main)
while True:
 
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    # time.sleep(1)
