
from datetime import datetime
import schedule
import time
import requests
from datetime import timedelta
from telegram import send_telegram
from telegramchannel import send_channel


def main():
    
    with open('sutki.txt','r') as file:
        struer = 0
        sfalser = 0
        struerligapro = 0
        sfalserligapro = 0  
        struerligaprominsk = 0
        sfalserligaprominsk = 0
        struerligaprocheh = 0
        sfalserligaprocheh = 0 
        struerkuboktt = 0
        sfalserkuboktt = 0 
        struerkubokttg = 0
        sfalserkubokttg = 0  
        struerkuboktti = 0
        sfalserkuboktti = 0
        struerkubokttl = 0
        sfalserkubokttl = 0 
        struerkubokttp = 0
        sfalserkubokttp = 0
        struerkuboktts = 0
        sfalserkuboktts = 0  
        struerkubokttch = 0
        sfalserkubokttch = 0  
        struerkuboktte = 0
        sfalserkuboktte = 0   
        struermasters = 0
        sfalsermasters = 0 
        struermastersz = 0
        sfalsermastersz = 0 
        struersk = 0
        sfalsersk = 0 
        struerskz = 0
        sfalserskz = 0  
        struerskch = 0
        sfalserskch = 0 
        struerchbittcup = 0
        sfalserchbittcup = 0
        struerchsittcup = 0
        sfalserchsittcup = 0 
        struerac = 0
        sfalserac = 0 
        struerpss = 0
        sfalserpss = 0   
        struerpssz = 0
        sfalserpssz = 0
        struervc = 0
        sfalservc = 0 
        struervcz = 0
        sfalservcz = 0   
        struerkchr = 0
        sfalserkchr = 0 
        struerkchrz = 0
        sfalserkchrz = 0
        struerkm = 0
        sfalserkm = 0  
        struerkmz = 0
        sfalserkmz = 0                                 
        for item in file.readlines():
            line = item.strip()
            liga = line.split('-')[0]
            zn = line.split('-')[-1]
            if 'Лига Про' in liga:
                if 'True' in zn:
                    struerligapro = struerligapro + 1
                if 'False' in zn:
                    sfalserligapro = sfalserligapro + 1
                    
            
            if 'Лига Про. Минск' in liga:
                if 'True' in zn:
                    struerligaprominsk = struerligaprominsk + 1
                if 'False' in zn:
                    sfalserligaprominsk = sfalserligaprominsk + 1
                    
            if 'Лига Про. Чехия' in liga:
                if 'True' in zn:
                    struerligaprocheh = struerligaprocheh + 1
                if 'False' in zn:
                    sfalserligaprocheh = sfalserligaprocheh + 1
                    
            if 'Кубок ТТ' in liga:
                if 'True' in zn:
                    struerkuboktt = struerkuboktt + 1
                if 'False' in zn:
                    sfalserkuboktt = sfalserkuboktt + 1
                    
            if 'Кубок ТТ. Германия' in liga:
                if 'True' in zn:
                    struerkubokttg = struerkubokttg + 1
                if 'False' in zn:
                    sfalserkubokttg = sfalserkubokttg + 1
                    
            if 'Кубок ТТ. Испания' in liga:
                if 'True' in zn:
                    struerkuboktti = struerkuboktti + 1
                if 'False' in zn:
                    sfalserkuboktti = sfalserkuboktti + 1
                    
            if 'Кубок ТТ. Латвия' in liga:
                if 'True' in zn:
                    struerkubokttl = struerkubokttl + 1
                if 'False' in zn:
                    sfalserkubokttl = sfalserkubokttl + 1
                    
            if 'Кубок ТТ. Польша' in liga:
                if 'True' in zn:
                    struerkubokttp = struerkubokttp + 1
                if 'False' in zn:
                    sfalserkubokttp = sfalserkubokttp + 1
                    
            if 'Кубок ТТ. США' in liga:
                if 'True' in zn:
                    struerkuboktts = struerkuboktts + 1
                if 'False' in zn:
                    sfalserkuboktts = sfalserkuboktts + 1
                    
            if 'Кубок ТТ. Чехия' in liga:
                if 'True' in zn:
                    struerkubokttch = struerkubokttch + 1
                if 'False' in zn:
                    sfalserkubokttch = sfalserkubokttch + 1
                    
            if 'Кубок ТТ. Эстония' in liga:
                if 'True' in zn:
                    struerkuboktte = struerkuboktte + 1
                if 'False' in zn:
                    sfalserkuboktte = sfalserkuboktte + 1
                    
            if 'Мастерс' in liga:
                if 'True' in zn:
                    struermasters = struermasters + 1
                if 'False' in zn:
                    sfalsermasters = sfalsermasters + 1
                    
            if 'Мастерс. Женщины' in liga:
                if 'True' in zn:
                    struermastersz = struermastersz + 1
                if 'False' in zn:
                    sfalsermastersz = sfalsermastersz + 1
                    
            if 'Сетка Кап' in liga:
                if 'True' in zn:
                    struersk = struersk + 1
                if 'False' in zn:
                    sfalsersk = sfalsersk + 1
                    
            if 'Сетка Кап. Женщины' in liga:
                if 'True' in zn:
                    struerskz = struerskz + 1
                if 'False' in zn:
                    sfalserskz = sfalserskz + 1
                    
            if 'Сетка Кап. Чехия' in liga:
                if 'True' in zn:
                    struerskch = struerskch + 1
                if 'False' in zn:
                    sfalserskch = sfalserskch + 1
                    
            if 'Чемпионат Болгарии. ИТТ Кап' in liga:
                if 'True' in zn:
                    struerchbittcup = struerchbittcup + 1
                if 'False' in zn:
                    sfalserchbittcup = sfalserchbittcup + 1
                    
            if 'Чемпионат Словакии. ИТТ Кап' in liga:
                if 'True' in zn:
                    struerchsittcup = struerchsittcup + 1
                if 'False' in zn:
                    sfalserchsittcup = sfalserchsittcup + 1
                    
            if 'ART Cup' in liga:
                if 'True' in zn:
                    struerac = struerac + 1
                if 'False' in zn:
                    sfalserac = sfalserac + 1
                    
            if 'Pro Spin Series' in liga:
                if 'True' in zn:
                    struerpss = struerpss + 1
                if 'False' in zn:
                    sfalserpss = sfalserpss + 1
                    
            if 'Pro Spin Series. Женщины' in liga:
                if 'True' in zn:
                    struerpssz = struerpssz + 1
                if 'False' in zn:
                    sfalserpssz = sfalserpssz + 1
                    
            if 'Вин Кап' in liga:
                if 'True' in zn:
                    struervc = struervc + 1
                if 'False' in zn:
                    sfalservc = sfalservc + 1
                    
            if 'Вин Кап. Женщины' in liga:
                if 'True' in zn:
                    struervcz = struervcz + 1
                if 'False' in zn:
                    sfalservcz = sfalservcz + 1
                    
                    
            if 'Командный чемпионат России' in liga:
                if 'True' in zn:
                    struerkchr = struerkchr + 1
                if 'False' in zn:
                    sfalserkchr = sfalserkchr + 1
                    
            if 'Командный чемпионат России. Женщины' in liga:
                if 'True' in zn:
                    struerkchrz = struerkchrz + 1
                if 'False' in zn:
                    sfalserkchrz = sfalserkchrz + 1
                    
            if 'Кубок Мира' in liga:
                if 'True' in zn:
                    struerkm = struerkm + 1
                if 'False' in zn:
                    sfalserkm = sfalserkm + 1
                    
            if 'Кубок Мира. Женщины' in liga:
                if 'True' in zn:
                    struerkmz = struerkmz + 1
                if 'False' in zn:
                    sfalserkmz = sfalserkmz + 1
                    
            if 'True' in zn:
                struer = struer + 1
            if 'False' in zn:
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
    format_mess_static(struerligapro,sfalserligapro,struerligaprominsk,sfalserligaprominsk,struerligaprocheh,sfalserligaprocheh,struerkuboktt,sfalserkuboktt,struerkubokttg,sfalserkubokttg,struerkuboktti,sfalserkuboktti,struerkubokttl,sfalserkubokttl,struerkubokttp,sfalserkubokttp,struerkuboktts,sfalserkuboktts,struerkubokttch,sfalserkubokttch,struerkuboktte,sfalserkuboktte,struermasters,sfalsermasters,struermastersz,sfalsermastersz,struersk,sfalsersk,struerskz,sfalserskz,struerskch,sfalserskch,struerchbittcup,sfalserchbittcup,struerchsittcup,sfalserchsittcup,struerac,sfalserac,struerpss,sfalserpss,struerpssz,sfalserpssz,struervcz,sfalservcz,struerkchr,sfalserkchr,struerkchrz,sfalserkchrz,struerkm,sfalserkm,struerkmz,sfalserkmz,struef,sfalsef,struervc,sfalservc,struer,sfalser)
    
def format_mess_static(struerligapro,sfalserligapro,struerligaprominsk,sfalserligaprominsk,struerligaprocheh,sfalserligaprocheh,struerkuboktt,sfalserkuboktt,struerkubokttg,sfalserkubokttg,struerkuboktti,sfalserkuboktti,struerkubokttl,sfalserkubokttl,struerkubokttp,sfalserkubokttp,struerkuboktts,sfalserkuboktts,struerkubokttch,sfalserkubokttch,struerkuboktte,sfalserkuboktte,struermasters,sfalsermasters,struermastersz,sfalsermastersz,struersk,sfalsersk,struerskz,sfalserskz,struerskch,sfalserskch,struerchbittcup,sfalserchbittcup,struerchsittcup,sfalserchsittcup,struerac,sfalserac,struerpss,sfalserpss,struerpssz,sfalserpssz,struervcz,sfalservcz,struerkchr,sfalserkchr,struerkchrz,sfalserkchrz,struerkm,sfalserkm,struerkmz,sfalserkmz,struef,sfalsef,struervc,sfalservc,struer,sfalser):
    
            
                
                
    mess = f'\U00002198 Статистика \U00002199 \n' \
        \
        f'\n' \
            f'\U00002198 Общий результат \U00002199 \n' \
            f' \U00002705 {struer} \n' \
                f' \U0000274C {sfalser} \n' \
                    f'\n' \
                        f'\U00002198 Роспись по лигам \U00002199 \n' \
        f' \U00002696 Игроки равны \U00002696 \n' \
        f' \U0001F3C6 Лига Про \U00002705 {struerligapro} \U0000274C {sfalserligapro}\n'\
        f' \U0001F3C6 Лига Про. Минск \U00002705 {struerligaprominsk} \U0000274C {sfalserligaprominsk}\n'\
        f' \U0001F3C6 Лига Про. Чехия \U00002705 {struerligaprocheh} \U0000274C {sfalserligaprocheh}\n'\
        f' \U0001F3C6 Кубок ТТ \U00002705 {struerkuboktt} \U0000274C {sfalserkuboktt}\n'\
        f' \U0001F3C6 Кубок ТТ. Германия \U00002705 {struerkubokttg} \U0000274C {sfalserkubokttg}\n'\
        f' \U0001F3C6 Кубок ТТ. Италия \U00002705 {struerkuboktti} \U0000274C {sfalserkuboktti}\n'\
        f' \U0001F3C6 Кубок ТТ. Латвия \U00002705 {struerkubokttl} \U0000274C {sfalserkubokttl}\n'\
        f' \U0001F3C6 Кубок ТТ. Польша \U00002705 {struerkubokttp} \U0000274C {sfalserkubokttp}\n'\
        f' \U0001F3C6 Кубок ТТ. США \U00002705 {struerkuboktts} \U0000274C {sfalserkuboktts}\n'\
        f' \U0001F3C6 Кубок ТТ. Чехия \U00002705 {struerkubokttch} \U0000274C {sfalserkubokttch}\n'\
        f' \U0001F3C6 Кубок ТТ. Эстония \U00002705 {struerkuboktte} \U0000274C {sfalserkuboktte}\n'\
        f' \U0001F3C6 Мастерс \U00002705 {struermasters} \U0000274C {sfalsermasters}\n'\
        f' \U0001F3C6 Мастерс. Женщины \U00002705 {struermastersz} \U0000274C {sfalsermastersz}\n'\
        f' \U0001F3C6 Сетка Кап \U00002705 {struersk} \U0000274C {sfalsersk}\n'\
        f' \U0001F3C6 Сетка Кап. Женщины \U00002705 {struerskz} \U0000274C {sfalserskz}\n'\
        f' \U0001F3C6 Сетка Кап. Чехия \U00002705 {struerskch} \U0000274C {sfalserskch}\n'\
        f' \U0001F3C6 Чемп.Болгарии ITT Cup \U00002705 {struerchbittcup} \U0000274C {sfalserchbittcup}\n'\
        f' \U0001F3C6 Чемп.Словакии ITT Cup \U00002705 {struerchsittcup} \U0000274C {sfalserchsittcup}\n'\
        f' \U0001F3C6 Art Cup \U00002705 {struerac} \U0000274C {sfalserac}\n'\
        f' \U0001F3C6 Pro Spin Series \U00002705 {struerpss} \U0000274C {sfalserpss}\n'\
        f' \U0001F3C6 Pro Spin Series. Женщины \U00002705 {struerpssz} \U0000274C {sfalserpssz}\n'\
        f' \U0001F3C6 Вин Кап \U00002705 {struervc} \U0000274C {sfalservc}\n'\
        f' \U0001F3C6 Вин Кап. Женщины \U00002705 {struervcz} \U0000274C {sfalservcz}\n'\
        f' \U0001F3C6 Ком.ч.России \U00002705 {struerkchr} \U0000274C {sfalserkchr}\n'\
        f' \U0001F3C6 Ком.ч.России.Женщины \U00002705 {struerkchrz} \U0000274C {sfalserkchrz}\n'\
        f' \U0001F3C6 Кубок Мира \U00002705 {struerkm} \U0000274C {sfalserkm}\n'\
        f' \U0001F3C6 Кубок Мира. Женщины \U00002705 {struerkmz} \U0000274C {sfalserkmz}\n'\
        \
                f'\n' \
                    f' \U0001F4C8 Есть фаворит \U0001F4C8  \n' \
            f' \U00002705 {struef} \n' \
                f' \U0000274C {sfalsef} \n' \
            f'\n' \

    send_telegram(mess)
    send_channel(mess)    
    
    
if __name__ == '__main__':
    main()
schedule.every(60).minutes.do(main)
while True:
 
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1) 
