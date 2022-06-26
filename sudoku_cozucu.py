# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 00:14:47 2022
@author: feth
"""
import numpy as np
import pandas as pd
from sudoku_resmi_oku import resmi_listeye_cevir
print("")
print("")
print("****************************************************")
print("Lütfen sudokunun ismini girin. örn: sudoku.jpeg  ")
print("=")
sudokuInput=input()
numpyArray=resmi_listeye_cevir(sudokuInput)

ListeMatris=[[[],[],[],[],[],[],[],[],[]],
             [[],[],[],[],[],[],[],[],[]],
             [[],[],[],[],[],[],[],[],[]],
             [[],[],[],[],[],[],[],[],[]],
             [[],[],[],[],[],[],[],[],[]],
             [[],[],[],[],[],[],[],[],[]],
             [[],[],[],[],[],[],[],[],[]],
             [[],[],[],[],[],[],[],[],[]],
             [[],[],[],[],[],[],[],[],[]]]

dataFrame=pd.DataFrame(numpyArray)
dataFrameBaslangic=pd.DataFrame(numpyArray)
olmazMatris=pd.DataFrame(ListeMatris)
olurMatris=pd.DataFrame(ListeMatris)
ruMetodOlamazMatris=pd.DataFrame(ListeMatris)

bulunanDeger=int()
oncekiBulunanDeger=0
turSayisi=int()

def calistir():
    global bulunanDeger
    global oncekiBulunanDeger
    global turSayisi
    
    while True :
        for x in list(range(9)):
            for y in list(range(9)):
                olamazMatrisineOlamazListesiniYaz(x,y)
                olabilirListesiniOlabilirMatrisineYaz(x,y)              
                kesinDegeriBulVeYaz(x,y)
        yeniMetod()        
        ruMetod()
        print(f"bulunan sayı adedi= {bulunanDegerSay()[0]} kalan boşluk= {bulunanDegerSay()[1]}")
        print(f"hata var mı? = {hataKontrolu()}")
        turSayisi+=1
        print("tur sayisi= " + str(turSayisi))
        print("*********************************************")
        bulunanDeger=bulunanDegerSay()[0]
        if bulunanDeger==oncekiBulunanDeger:
            break
        else:
            oncekiBulunanDeger=bulunanDeger
               
def hangiBolumBul(x=int(),y=int()):
    bolum=int()
    matrisBolum=pd.DataFrame()
    olamazMatrisBolum=pd.DataFrame()
    olurMatrisBolum=pd.DataFrame()
    
    if   y<3 and x<3:
        bolum=1
        olamazMatrisBolum=pd.DataFrame(olmazMatris.loc[0:2,0:2])
        matrisBolum=dataFrame.loc[0:2,0:2]
        olurMatrisBolum=olurMatris.loc[0:2,0:2]
    elif y<6 and x<3:
        bolum=2
        olamazMatrisBolum=pd.DataFrame(olmazMatris.loc[0:2,3:5])
        matrisBolum=dataFrame.loc[0:2,3:5]
        olurMatrisBolum=olurMatris.loc[0:2,3:5]
    elif y<9 and x<3:
        bolum=3
        olamazMatrisBolum=pd.DataFrame(olmazMatris.loc[0:2,6:8])
        matrisBolum=dataFrame.loc[0:2,6:8]
        olurMatrisBolum=olurMatris.loc[0:2,6:8]
    elif y<3 and x<6:
        bolum=4
        olamazMatrisBolum=pd.DataFrame(olmazMatris.loc[3:5,0:2])
        matrisBolum=dataFrame.loc[3:5,0:2]
        olurMatrisBolum=olurMatris.loc[3:5,0:2]
    elif y<6 and x<6:
        bolum=5
        olamazMatrisBolum=pd.DataFrame(olmazMatris.loc[3:5,3:5])
        matrisBolum=dataFrame.loc[3:5,3:5]
        olurMatrisBolum=olurMatris.loc[3:5,3:5]
    elif y<9 and x<6:
        bolum=6
        olamazMatrisBolum=pd.DataFrame(olmazMatris.loc[3:5,6:8])
        matrisBolum=dataFrame.loc[3:5,6:8]
        olurMatrisBolum=olurMatris.loc[3:5,6:8]
    elif y<3 and x<9:
        bolum=7
        olamazMatrisBolum=pd.DataFrame(olmazMatris.loc[6:8,0:2])
        matrisBolum=dataFrame.loc[6:8,0:2]
        olurMatrisBolum=olurMatris.loc[6:8,0:2]
    elif y<6 and x<9:
        bolum=8
        olamazMatrisBolum=pd.DataFrame(olmazMatris.loc[6:8,3:5])
        matrisBolum=dataFrame.loc[6:8,3:5]
        olurMatrisBolum=olurMatris.loc[6:8,3:5]
    elif y<9 and x<9:
        bolum=9
        olamazMatrisBolum=pd.DataFrame(olmazMatris.loc[6:8,6:8])
        matrisBolum=dataFrame.loc[6:8,6:8]
        olurMatrisBolum=olurMatris.loc[6:8,6:8]
        
    return bolum,matrisBolum,olamazMatrisBolum,olurMatrisBolum

def yatayOlamazDegerleri(x_kordinat=int()):
    yatayda_olamazlar=list(set(list(dataFrame.iloc[x_kordinat])))
    if 0 in yatayda_olamazlar:
        yatayda_olamazlar.remove(0)
    return yatayda_olamazlar

def dikeyOlamazDegerleri(y_kordinat=int()):
    dikeyde_olamazlar=list(set(list(dataFrame[y_kordinat])))
    if 0 in dikeyde_olamazlar:
        dikeyde_olamazlar.remove(0)
    return dikeyde_olamazlar

def karedeOlamazDegerleri(x=int(),y=int()):
    karede_olamazlar=list()
    kare_sutunlari=list()
    karedeki_tum_degerler=list()
    
    matrisBolum=hangiBolumBul(x,y)[1]
    
    matrisBolum=matrisBolum.to_numpy()
    matrisBolum=pd.DataFrame(matrisBolum)
   
    for e in list(range(3)):
        kare_sutunlari=list(matrisBolum[e])
        karedeki_tum_degerler.extend(kare_sutunlari)
        karedeki_tum_degerler=list(set(karedeki_tum_degerler))
        if 0 in karedeki_tum_degerler:
            karedeki_tum_degerler.remove(0)
        karede_olamazlar=karedeki_tum_degerler    
    return karede_olamazlar

def takasFonksiyonu(liste=list()):
    birdenDokuzaListe=list(range(1,10))
    cevapListe=list()
    for eleman in liste:
        birdenDokuzaListe.remove(eleman)
    cevapListe=birdenDokuzaListe
    return cevapListe   

def olamazDegerlerListesi(x=int(),y=int()):
    konumDegeri=dataFrame.iloc[x][y]
    tumOlamazListesi=list()
    tumOlamazListesi.extend(yatayOlamazDegerleri(x))
    tumOlamazListesi.extend(dikeyOlamazDegerleri(y))
    tumOlamazListesi.extend(karedeOlamazDegerleri(x,y))
    tumOlamazListesi.extend(ruMetodOlamazMatris.iloc[x][y])
   
    if konumDegeri!=0:
        tumOlamazListesi=takasFonksiyonu([konumDegeri])
    else:
        tumOlamazListesi=list(set(tumOlamazListesi)) 
    return tumOlamazListesi

def olamazMatrisineOlamazListesiniYaz(x=int(),y=int()):
    tumOlamazElemanlar=list()
    tumOlamazElemanlar=olamazDegerlerListesi(x,y)
    olmazMatris.iloc[x][y]=tumOlamazElemanlar
                   
def olabilirDegerlerListesi(x=int(),y=int()):
    olabilir_listesi=takasFonksiyonu(olamazDegerlerListesi(x,y)) 
    return olabilir_listesi

def olabilirListesiniOlabilirMatrisineYaz(x=int(),y=int()):
    olurMatris.iloc[x][y]=olabilirDegerlerListesi(x,y)

def kesinDegeriBulVeYaz(x=int(),y=int()):
    if dataFrame.iloc[x][y]==0:
        if len(list(olabilirDegerlerListesi(x,y)))==1:
            dataFrame.iloc[x][y]=olabilirDegerlerListesi(x,y)[0]
            
def yeniMetod():
    
    for x in list(range(9)):
        for y in list(range(9)):
            
    
            olamazDegerler=[]
            elemanSayisi=0   
            olamazMatrisBolum=hangiBolumBul(x,y)[2]
            olamazMatrisBolum=olamazMatrisBolum.to_numpy()
            olamazMatrisBolum=pd.DataFrame(olamazMatrisBolum)    
            for a in list(range(3)):
                for b in list(range(3)):
                    olamazDegerler.extend(olamazMatrisBolum[a][b])
            for eleman in range(1,10):
                if eleman not in olmazMatris.iloc[x][y]:
                    if len(olmazMatris.iloc[x][y])!=8:
                        elemanSayisi=olamazDegerler.count(eleman)
                        if elemanSayisi==8 and dataFrame.iloc[x][y]==0 :
                            dataFrame.iloc[x][y]=eleman
                           
            if x==y:
        
                dikey=list(olmazMatris[x])
                yatay=list(olmazMatris.iloc[x])
                dikey_toplam=list()
                yatay_toplam=list()
                
                for eklenecek in dikey:
                    dikey_toplam.extend(eklenecek)
                    
                for eklenecek in yatay:
                    yatay_toplam.extend(eklenecek)
                    
                
                for e in [1,2,3,4,5,6,7,8,9]:
                    if dikey_toplam.count(e)==8:
                        for index,eleman in enumerate(dikey):
                            if e not in eleman:
                                if dataFrame.iloc[index][x]==0:
                                    dataFrame.iloc[index][x]=e

                                
                for e in [1,2,3,4,5,6,7,8,9]:
                    if yatay_toplam.count(e)==8:
                        for index,eleman in enumerate(yatay): 
                            if e not in eleman:
                                if dataFrame.iloc[x][index]==0:
                                    dataFrame.iloc[x][index]=e
   
def bulunanDegerSay():
    saymaListesi=list()
    saymaListesi2=list()
    for x in list(range(9)):
        for y in list(range(9)):
            saymaListesi.append(int(dataFrame[x][y])) 
            saymaListesi2.append(int(dataFrameBaslangic[x][y]))
    df1SıfırSayisi=saymaListesi.count(0)
    df2SıfırSayisi=saymaListesi2.count(0)
    bulunanVeriSayisi=df2SıfırSayisi-df1SıfırSayisi
    kalanBoslukSayisi=df1SıfırSayisi
 
    return bulunanVeriSayisi,kalanBoslukSayisi
    
def ruMetod():
    for x1 in [0,3,6]:
        for y1 in [0,3,6]:
            sifirdanSekizeListe=[0,1,2,3,4,5,6,7,8]
            tumToplam=list() 
            olurMatrisBolum=hangiBolumBul(x1,y1)[3]
            
            Indexler=list(olurMatrisBolum.index)
            Basliklar=list(olurMatrisBolum.columns)
            
            yazilacakIndexler=list()
            yazilacakBasliklar=list()
            
            for eleman in Indexler:
                sifirdanSekizeListe.remove(eleman)
            yazilacakIndexler = sifirdanSekizeListe
            
            sifirdanSekizeListe=[0,1,2,3,4,5,6,7,8] #listeyi yeniden doldurmak
            
            for eleman in Basliklar:
                sifirdanSekizeListe.remove(eleman)
            yazilacakBasliklar=sifirdanSekizeListe
            
            olurMatrisBolum=olurMatrisBolum.to_numpy()
            olurMatrisBolum=pd.DataFrame(olurMatrisBolum)
            
            for x2 in [0,1,2]:
                for y2 in [0,1,2]:
                    tumToplam.extend(olurMatrisBolum.iloc[x2][y2])

            for xVy in [0,1,2]:
                sutununToplam=list()
                satirToplam=list()
               
                for i in [0,1,2]:
                    
                    sutununToplam.extend(olurMatrisBolum.iloc[i][xVy])  #sutun topla
                    for e1 in list(set(sutununToplam)):#sutun yaz
                        if sutununToplam.count(e1)>1:
                            if tumToplam.count(e1)==sutununToplam.count(e1):
                                for index in yazilacakIndexler:
                                    if e1 not in ruMetodOlamazMatris.iloc[index][Basliklar[xVy]]:
                                        ruMetodOlamazMatris.iloc[index][Basliklar[xVy]].extend([e1])
                    
                    satirToplam.extend(olurMatrisBolum.iloc[xVy][i])  #satır topla
                    for e2 in list(set(satirToplam)):#satır yaz
                        if satirToplam.count(e2)>1:
                            if tumToplam.count(e2)==satirToplam.count(e2):
                                for baslik in yazilacakBasliklar:
                                    if e2 not in ruMetodOlamazMatris.iloc[Indexler[xVy]][baslik]:
                                        ruMetodOlamazMatris.iloc[Indexler[xVy]][baslik].extend([e2])
                                     
def hataKontrolu():
    sonuc=1
    sonucStr=str()
    for i in [0,1,2,3,4,5,6,7,8]:
        dikey=list(dataFrame[i])
        yatay=list(dataFrame.iloc[i])
        dikey_toplam=list()
        yatay_toplam=list()
    
        for eklenecek in dikey:
            dikey_toplam.append(eklenecek)
            
        for eklenecek in yatay:
            yatay_toplam.append(eklenecek)
            
        if sonuc==1:
            for d in [1,2,3,4,5,6,7,8,9]:
                if dikey_toplam.count(d)>1:
                    sonuc=0
                    break
                else:
                    sonuc=1
               
        if sonuc==1:  
            for y in [1,2,3,4,5,6,7,8,9]:
                if yatay_toplam.count(y)>1:
                    sonuc=0
                    break
                else:
                    sonuc=1
                    
        if sonuc==1:
            for x in [0,2,8]:
                    for y in [0,2,8]:
                        bolumunElemanlari=list()                      
                        matrisBolum=hangiBolumBul(x,y)[1]                     
                        matrisBolum=matrisBolum.to_numpy()
                        matrisBolum=pd.DataFrame(matrisBolum)
                        if sonuc==1:
                            for i in [0,1,2]:
                                    bolumunElemanlari.extend(list(matrisBolum[i]))
                             
                            
                            for k in [1,2,3,4,5,6,7,8,9]:
                                if bolumunElemanlari.count(k)>1:
                                    sonuc=0
                                    break
                                else:
                                    sonuc=1
                        else:
                            break                           
        else:
            sonuc=0
            break
    
    if sonuc==0:
        sonucStr="ÇÖZÜM HATALI!"
    else:
        sonucStr="hata yok"
    return sonucStr                                                 

calistir()


sonuc=dataFrame.values.tolist()
sonuc=np.array(sonuc)
print("")
print("###SONUÇ###")
print(sonuc)

from datetime import datetime
belgeZamani=datetime.now().strftime("%d%m%Y%H%M%S")
belgeIsmi="sudokuSonucu"+str(belgeZamani)+".txt"
belge=open(belgeIsmi,"w")
print(sonuc,file=belge)
print("",file=belge)
print(f"bulunan sayı adedi= {bulunanDegerSay()[0]} kalan boşluk= {bulunanDegerSay()[1]}",file=belge)
print(f"hata var mı? = {hataKontrolu()}",file=belge)
print("tur sayisi= " + str(turSayisi),file=belge)
belge.close()








