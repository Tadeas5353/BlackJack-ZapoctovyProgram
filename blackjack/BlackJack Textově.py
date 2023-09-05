import random
import time
import tkinter as tk

Okno = tk.Tk()
Okno.geometry("800x800")
ikona=tk.PhotoImage(file="Ikona.png")
Okno.title("BlackJack")
Okno.iconphoto(True, ikona)
Okno.geometry("1020x560")
Nadpis=tk.Label(Okno,text="BLACKJACK",font=("Arial",40,"bold"),fg="#c94024",bg="black",relief="raised",bd=10)
Nadpis.pack()

Text_ZadejtePocetHracu = tk.Label(Okno, text="Nastavte počet hráčů:")
Text_ZadejtePocetHracu.pack()

Posuvnik_ZadejtePocetHracu = tk.Scale(Okno, from_=1, to=5, orient="horizontal", length=200, sliderlength=20, showvalue=True)
Posuvnik_ZadejtePocetHracu.pack()

Text_ZadejtePocetHracu = tk.Label(Okno, text="Nastavte počet balíčků:")
Text_ZadejtePocetHracu.pack()

Posuvnik_ZadejtePocetBalicku = tk.Scale(Okno, from_=1, to=8, orient="horizontal", length=200, sliderlength=20, showvalue=True)
Posuvnik_ZadejtePocetBalicku.pack()

class Karta:
    def __init__(self, barva, typ, hodnota):
        self.barva=barva
        self.typ=typ
        self.hodnota=int(hodnota)

class Balicek:
    def __init__(self):
        self.balicek=[]
    def Zamichat(self):
        random.shuffle(self.balicek)
    def Vytvor_novy(self):
        self.balicek.clear()
        for i in range (Pocet_balicku):
            self.balicek.append(Srdcova_dvojka)
            self.balicek.append(Srdcova_trojka)
            self.balicek.append(Srdcova_ctyrka)
            self.balicek.append(Srdcova_petka)
            self.balicek.append(Srdcova_sestka)
            self.balicek.append(Srdcova_sedmicka)
            self.balicek.append(Srdcova_osmicka)
            self.balicek.append(Srdcova_devitka)
            self.balicek.append(Srdcova_desitka)
            self.balicek.append(Srdcovy_spodek)
            self.balicek.append(Srdcova_kralovna)
            self.balicek.append(Srdcovy_kral)
            self.balicek.append(Srdcove_eso)
            self.balicek.append(Karova_dvojka)
            self.balicek.append(Karova_trojka)
            self.balicek.append(Karova_ctyrka)
            self.balicek.append(Karova_petka)
            self.balicek.append(Karova_sestka)
            self.balicek.append(Karova_sedmicka)
            self.balicek.append(Karova_osmicka)
            self.balicek.append(Karova_devitka)
            self.balicek.append(Karova_desitka)
            self.balicek.append(Karovy_spodek)
            self.balicek.append(Karova_kralovna)
            self.balicek.append(Karovy_kral)
            self.balicek.append(Karove_eso)
            self.balicek.append(Pikova_dvojka)
            self.balicek.append(Pikova_trojka)
            self.balicek.append(Pikova_ctyrka)
            self.balicek.append(Pikova_petka)
            self.balicek.append(Pikova_sestka)
            self.balicek.append(Pikova_sedmicka)
            self.balicek.append(Pikova_osmicka)
            self.balicek.append(Pikova_devitka)
            self.balicek.append(Pikova_desitka)
            self.balicek.append(Pikovy_spodek)
            self.balicek.append(Pikova_kralovna)
            self.balicek.append(Pikovy_kral)
            self.balicek.append(Pikove_eso)
            self.balicek.append(Listova_dvojka)
            self.balicek.append(Listova_trojka)
            self.balicek.append(Listova_ctyrka)
            self.balicek.append(Listova_petka)
            self.balicek.append(Listova_sestka)
            self.balicek.append(Listova_sedmicka)
            self.balicek.append(Listova_osmicka)
            self.balicek.append(Listova_devitka)
            self.balicek.append(Listova_desitka)
            self.balicek.append(Listovy_spodek)
            self.balicek.append(Listova_kralovna)
            self.balicek.append(Listovy_kral)
            self.balicek.append(Listove_eso)
        self.Zamichat()                               
    def Lizni_Kartu(self):
        if len(self.balicek)==0:
            self.Vytvor_novy()
        return self.balicek.pop()

class Hrac():
    def __init__ (self, jmeno, uroven, rozpocet, sazka, karty, blackjack, pojistka, jedenactkova_esa, skore, split, SKarty1, SKarty2, SSkore1, SSkore2, SBJ1, SBJ2, S11E1, S11E2):
        self.jmeno=jmeno
        self.uroven=int(uroven)
        self.rozpocet=int(rozpocet)
        self.sazka=int(sazka)
        self.karty=karty
        self.blackjack=blackjack
        self.pojistka=pojistka
        self.jedenactkova_esa=int(jedenactkova_esa)
        self.skore=int(skore)
        self.split=split
        self.SKarty1=SKarty1
        self.SKarty2=SKarty2
        self.SSkore1=SSkore1
        self.SSkore2=SSkore2
        self.SBJ1=SBJ1
        self.SBJ2=SBJ2
        self.S11E1=S11E1
        self.S11E2=S11E2
    def Rozhodovaci_Funkce_Prvni_Tah(self, dealer):
        Ta_Druha_K_Esu=0
        par=False
        if self.karty[0].hodnota==self.karty[1].hodnota:
            par=True
        eso=False
        if self.karty[0].typ=="A" or self.karty[1].typ=="A":
            eso=True
            if self.karty[0].typ=="A":
                Ta_Druha_K_Esu=self.karty[1].hodnota
            else:
                Ta_Druha_K_Esu=self.karty[0].hodnota

        if self.uroven==5:
            if par:
                tah=str(input("Zadej svůj další tah! Stand - Hit - Double - Split ")).lower()
                while tah != "hit" and tah!= "stand" and tah!= "double" and tah!= "split":
                    print("Neplatný vstup!")
                    tah=str(input("Zadej svůj další tah! Stand - Hit - Double - Split ")).lower()
            else:
                tah=str(input("Zadej svůj další tah! Stand - Hit - Double ")).lower()
                while tah != "hit" and tah!= "stand" and tah!= "double" and tah!= "split":
                    print("Neplatný vstup!")
                    tah=str(input("Zadej svůj další tah! Stand - Hit - Double ")).lower()                
            if tah == "stand":
                return "Stand"
            elif tah == "double":
                return "Double"
            elif tah == "split":
                return "Split"
            else:
                return "Hit"                

        if self.uroven==4:
            if par:
                if eso or self.karty[0].typ=="8":
                    return "Split"
                elif self.karty[0].typ=="10":
                    return "Stand"
                elif self.karty[0].typ=="9":
                    if dealer==7 or dealer==10 or dealer==11:
                        return "Stand"
                    else:
                        return "Split"
                elif self.karty[0].typ=="7":
                    if dealer > 7:
                        return "Hit"
                    else:
                        return "Split"
                elif self.karty[0].typ=="6":
                    if dealer > 6 or dealer==2:
                        return "Hit"
                    else:
                        return "Split"
                elif self.karty[0].typ=="5":
                    if dealer > 5:
                        return "Hit"
                    else:
                        return "Double"
                elif self.karty[0].typ=="4":
                    return "Hit"
                else:
                    if dealer < 3 or dealer > 7:
                        return "Hit"
                    else:
                        return "Split"
                    
            elif eso:
                if Ta_Druha_K_Esu>8:
                    return "Stand"
                elif Ta_Druha_K_Esu==7:
                    if dealer==2 or dealer==7 or dealer==8:
                        return "Stand"
                    elif dealer > 2 and dealer < 7:
                        return "Double"
                    else:
                        return "Hit"
                elif Ta_Druha_K_Esu==6:
                    if dealer>2 and dealer<7:
                        return "Double"
                    else:
                        return "Hit"
                elif Ta_Druha_K_Esu==5 or Ta_Druha_K_Esu==4:
                    if dealer > 3 and dealer<7:
                        return "Double"
                    else:
                        return "Hit"
                else:
                    if dealer==5 or dealer==6:
                        return "Double"
                    else:
                        return "Hit"
                    
            else:
                if self.skore>16:
                    return "Stand"
                elif self.skore>12 and self.skore<17:
                    if dealer>6:
                        return "Hit"
                    else:
                        return "Stand"
                elif self.skore==12:
                    if dealer>3 and dealer<7:
                        return "Stand"
                    else:
                        return "Hit"
                elif self.skore==11:
                    return "Double"
                elif self.skore==10:
                    if dealer>9:
                        return "Hit"
                    else:
                        return "Double"
                elif self.skore==9:
                    if dealer>2 and dealer<8:
                        return "Double"
                    else: 
                        return "Hit"
                else:
                    return "Hit"                

        elif self.uroven==3:
            if par:
                if eso:
                    return "Split"
                elif self.karty[0].typ=="8":
                    return random.choice(["Split","Split","Split","Stand","Split"])
                elif self.karty[0].typ=="10":
                    return "Stand"
                elif self.karty[0].typ=="9":
                    if dealer>7:
                        return random.choice(["Split","Stand"])
                    else:
                        return "Split"
                elif self.karty[0].typ=="7":
                    if dealer > 7:
                        return "Hit"
                    else:
                        return "Split"
                elif self.karty[0].typ=="6":
                    if dealer > 6:
                        return "Hit"
                    else:
                        return "Split"
                elif self.karty[0].typ=="5":
                    if dealer > 5 and dealer < 8:
                        return random.choice(["Hit", "Split", "Double"])
                    else:
                        return "Double"
                elif self.karty[0].typ=="4":
                    return random.choice(["Hit","Hit","Hit","Hit","Hit","Hit","Hit","Hit","Hit","Split"])
                else:
                    if dealer < 3 or dealer > 8:
                        return "Hit"
                    else:
                        return "Split"
                    
            elif eso:
                if Ta_Druha_K_Esu>8:
                    return "Stand"
                elif Ta_Druha_K_Esu==7:
                    if dealer>2 and dealer<8:
                        return random.choice(["Double","Stand"])
                    else:
                        return "Hit"
                elif Ta_Druha_K_Esu==6:
                    if dealer>2 and dealer<8:
                        return "Double"
                    else:
                        return "Hit"
                elif Ta_Druha_K_Esu==5 or Ta_Druha_K_Esu==4:
                    if dealer > 2 and dealer<7:
                        return "Double"
                    else:
                        return "Hit"
                else:
                    if dealer==5 or dealer==6:
                        return "Double"
                    else:
                        return "Hit"
                    
            else:
                if self.skore>17:
                    return "Stand"
                elif self.skore>12 and self.skore<17:
                    if dealer>5:
                        return "Hit"
                    elif dealer<8:
                        return "Stand"
                    else:
                        return random.choice(["Stand","Hit"])
                elif self.skore==12:
                    if dealer<7:
                        return "Stand"
                    else:
                        return "Hit"
                elif self.skore==11:
                    return random.choice(["Double","Double","Double","Double","Double","Double","Hit"])
                elif self.skore==10:
                    if dealer>8:
                        return "Hit"
                    else:
                        return "Double"
                elif self.skore==9:
                    if dealer>2 and dealer<9:
                        return "Double"
                    else: 
                        return "Hit"
                else:
                    return "Hit"

        elif self.uroven==2:
            if par:
                if eso:
                    return random.choice(["Split","Split","Split","Double","Hit"])
                elif self.karty[0].typ=="8":
                    return random.choice(["Split","Split","Split","Stand","Stand"])
                elif self.karty[0].typ=="10":
                    return random.choice(["Stand","Split","Split","Split","Split"])
                elif self.karty[0].typ=="9":
                    if dealer>6:
                        return random.choice(["Split","Stand"])
                    else:
                        return "Split"
                elif self.karty[0].typ=="7":
                    if dealer > 6:
                        return "Hit"
                    else:
                        return "Split"
                elif self.karty[0].typ=="6":
                    if dealer > 6:
                        return random.choice(["Split","Hit","Double"])
                    else:
                        return "Split"
                elif self.karty[0].typ=="5":
                    if dealer > 5 and dealer < 9:
                        return random.choice(["Hit", "Split", "Double"])
                    else:
                        return "Double"
                elif self.karty[0].typ=="4":
                    return random.choice(["Hit","Split"])
                else:
                    return random.choice(["Split","Hit"])
                    
            elif eso:
                if Ta_Druha_K_Esu>8:
                    return random.choice(["Stand","Stand","Stand","Hit"])
                elif Ta_Druha_K_Esu==7:
                    if dealer>2 and dealer<8:
                        return random.choice(["Double","Stand"])
                    else:
                        return "Hit"
                elif Ta_Druha_K_Esu==6:
                    if dealer>2 and dealer<9:
                        return "Double"
                    else:
                        return "Hit"
                else:
                    return random.choice(["Double","Hit"])
                    
            else:
                if self.skore>18:
                    return "Stand"
                elif self.skore==17:
                    return random.choice(["Stand","Stand","Stand","Stand","Stand","Hit"])
                elif self.skore>11 and self.skore<17:
                    return random.choice(["Stand","Hit"])
                elif self.skore==11:
                    return random.choice(["Double","Hit","Stand","Double","Hit"])
                elif self.skore<11 and self.skore>6:
                    return random.choice(["Hit","Double"])
                else:
                    return "Hit"

        else:
            if par:
                return random.choice(["Stand","Hit","Double","Split"])
            else:
                return random.choice(["Stand","Hit","Double"])             
        
    def pojistovaci_funkce(self):
        if self.uroven==5:
            pojistka=str(input("Dealer má eso. Chceš se pojistit proti BlackJacku? Ano - Ne ")).lower()
            while pojistka!="ano" and pojistka!="ne":
                print("Odpověz Ano-ne! ")
                pojistka=str(input("Dealer má eso. Chceš se pojistit? Ano - Ne ")).lower()
        elif self.uroven==4:
            pojistka="ne"
        elif self.uroven==3:
            pojistka=random.choice(["ne","ne","ne","ne","ano"])
        elif self.uroven==2:
            pojistka=random.choice(["ano","ne","ne"])
        else:
            pojistka=random.choice(["ano","ne"])
        if pojistka=="ano":
            return True
        else:
            return False
                   

def Dealeruv_tah():
    skore=Dealerovy_karty[0].hodnota+Dealerovy_karty[1].hodnota
    esa=0
    if Dealerovy_karty[0].typ=="A":
        esa+=1
    if Dealerovy_karty[1].typ=="A":
        esa+=1
    while esa>0 and skore>21:
        skore+=-10
        esa+=-1
    print("Dealerovy karty jsou "+Dealerovy_karty[0].barva+" "+Dealerovy_karty[0].typ+ " a "+Dealerovy_karty[1].barva+" "+Dealerovy_karty[1].typ)
    time.sleep(1)
    print("Dealerovo skore je: "+str(skore))
    while skore<17:
        Dealerovy_karty.append(Hraci_balicek.Lizni_Kartu())
        skore=skore+Dealerovy_karty[-1].hodnota
        if Dealerovy_karty[-1].typ=="A":
            esa+=1
        while esa>0 and skore>21:
            esa+=-1
            skore+=-10
        time.sleep(1)            
        print("Dealer si líznul: "+Dealerovy_karty[-1].barva+" "+Dealerovy_karty[-1].typ)
        time.sleep(0.5)
        print("Dealerovo skore je: "+str(skore))
    if skore>21:
        time.sleep(1)
        print("Dealer má bust!")
    else:
        time.sleep(1)
        print("Dealer skončil svůj tah!")
    return skore

def vyhodnoceni(hrac, dealer, sazka, Pojisten, BlackJack, Dealeruv_BlackJack, jmeno):
    if BlackJack and Dealeruv_BlackJack:
        time.sleep(1)        
        if Pojisten:
            print("Dealer i "+jmeno+" mají oba BlackJack! Sázka se vrací."+jmeno+" zaplatil pojistku, takže dostává navíc výši své sázky!")
            return sazka*2
        else:
            print("Dealer i "+jmeno+" mají oba BlackJack! Sázka se vrací.")
            return sazka        
    if BlackJack:
        time.sleep(1)
        print(jmeno+" vyhrává díky BlackJacku.")
        return sazka*2+sazka//2
    if dealer==hrac and not Dealeruv_BlackJack:
        time.sleep(1)
        print(jmeno+" i dealer mají "+str(hrac)+" bodů! Je to remíza! Sázka se vrací.")
        return sazka
    if (dealer<hrac or dealer>21) and hrac<=21:
        time.sleep(1)
        print(jmeno+" má "+str(hrac)+" bodů. Dealer má "+str(dealer)+" bodů. "+jmeno+ " vyhrává")
        return sazka*2
    else:
        time.sleep(1)
        print(jmeno+" má "+str(hrac)+" bodů. Dealer má "+str(dealer)+" bodů. Dealer vyhrál!")
        if Pojisten and Dealeruv_BlackJack:
            time.sleep(0.8)
            print(jmeno+" zaplatil pojistku a Dealer má BlackJack, takže se vrací sázka!")
            return sazka
        return 0

def Rozhodovaci_funkce(uroven,skore,dealer):
    if uroven==5:
        tah=str(input("Zadej svůj další tah! Stand - Hit " )).lower()
        while tah != "hit" and tah!= "stand":
            print("Neplatný vstup!")
            tah=str(input("Zadej svůj další tah! Stand - Hit " )).lower()
        if tah == "stand":
            return "Stand"
        else:
            return "Hit"
    if uroven==4:
        if skore>16:
            return "Stand"
        elif skore>12 and skore<17:
            if dealer>6:
                return "Hit"
            else:
                return "Stand"
        elif skore==12:
            if dealer>3 and dealer<7:
                return "Stand"
            else:
                return "Hit"
        else:
            return "Hit"
        
    elif uroven==3:
        if skore>17:
            return "Stand"
        elif skore>12 and skore<17:
            if dealer>5:
                return "Hit"
            elif dealer<8:
                return "Stand"
            else:
                return random.choice(["Stand","Hit"])
        elif skore==12:
            if dealer<7:
                return "Stand"
            else:
                return "Hit"
        elif skore==11:
            return "Hit" 
    elif uroven==2:
        if skore>18:
            return "Stand"
        elif skore==17:
            return random.choice(["Stand","Stand","Stand","Stand","Stand","Hit"])
        elif skore>11 and skore<17:
            return random.choice(["Stand","Hit"])
        elif skore==11 or skore==10:
            return random.choice(["Hit","Stand","Hit"])
        elif skore<10 and skore>6:
            return "Hit"
        
    else:
        return random.choice(["Stand","Hit"])

Okno.mainloop()

Srdcova_dvojka=Karta("Srdce","2",2)
Srdcova_trojka=Karta("Srdce","3",3)
Srdcova_ctyrka=Karta("Srdce","4",4)
Srdcova_petka=Karta("Srdce","5",5)
Srdcova_sestka=Karta("Srdce","6",6)
Srdcova_sedmicka=Karta("Srdce","7",7)
Srdcova_osmicka=Karta("Srdce","8",8)
Srdcova_devitka=Karta("Srdce","9",9)
Srdcova_desitka=Karta("Srdce","10",10)
Srdcovy_spodek=Karta("Srdce","J",10)
Srdcova_kralovna=Karta("Srdce","Q",10)
Srdcovy_kral=Karta("Srdce","K",10)
Srdcove_eso=Karta("Srdce","A",11)

Karova_dvojka=Karta("Kary","2",2)
Karova_trojka=Karta("Kary","3",3)
Karova_ctyrka=Karta("Kary","4",4)
Karova_petka=Karta("Kary","5",5)
Karova_sestka=Karta("Kary","6",6)
Karova_sedmicka=Karta("Kary","7",7)
Karova_osmicka=Karta("Kary","8",8)
Karova_devitka=Karta("Kary","9",9)
Karova_desitka=Karta("Kary","10",10)
Karovy_spodek=Karta("Kary","J",10)
Karova_kralovna=Karta("Kary","Q",10)
Karovy_kral=Karta("Kary","K",10)
Karove_eso=Karta("Kary","A",11)

Pikova_dvojka=Karta("Piky","2",2)
Pikova_trojka=Karta("Piky","3",3)
Pikova_ctyrka=Karta("Piky","4",4)
Pikova_petka=Karta("Piky","5",5)
Pikova_sestka=Karta("Piky","6",6)
Pikova_sedmicka=Karta("Piky","7",7)
Pikova_osmicka=Karta("Piky","8",8)
Pikova_devitka=Karta("Piky","9",9)
Pikova_desitka=Karta("Piky","10",10)
Pikovy_spodek=Karta("Piky","J",10)
Pikova_kralovna=Karta("Piky","Q",10)
Pikovy_kral=Karta("Piky","K",10)
Pikove_eso=Karta("Piky","A",11)

Listova_dvojka=Karta("Listy","2",2)
Listova_trojka=Karta("Listy","3",3)
Listova_ctyrka=Karta("Listy","4",4)
Listova_petka=Karta("Listy","5",5)
Listova_sestka=Karta("Listy","6",6)
Listova_sedmicka=Karta("Listy","7",7)
Listova_osmicka=Karta("Listy","8",8)
Listova_devitka=Karta("Listy","9",9)
Listova_desitka=Karta("Listy","10",10)
Listovy_spodek=Karta("Listy","J",10)
Listova_kralovna=Karta("Listy","Q",10)
Listovy_kral=Karta("Listy","K",10)
Listove_eso=Karta("Listy","A",11)

Jmena={"Marek", "Jan", "Petr", "Šimon", "Lukáš", "Zuzana", "Klára", "Roman", "Denis", "Vojta", "Adam", "Alexandr", "Kryštof", "Barbora", "Karel", "Anna", "Eliška", "Jiří", "Pankrác", "Josefína", "Bertrúda", "Kazimír", "Prokop", "Řehoř", "Ondřej", "Soňa", "Mirek", "Jiřina", "Věnceslav", "Tomáš", "Oliver", "Chrudoš", "Vavřinec", "Bernard", "Augustýn", "Spytihněv", "Karolína", "Štěpán", "Filip", "Norbert", "František", "Přemysl", "Luboš", "David", "Servác", "Bonifác", "Bohuslava", "Celestýna"} 

while True:
    try:
        Pocet_hracu = int(input("Zadej v kolika hráčích chceš hrát! Rozmezí jedna až pět! "))
        while Pocet_hracu < 1 or Pocet_hracu > 5:
            print("Počet botů musí být v rozsahu jedna a pět!")
            Pocet_hracu = int(input("Zadej správné číslo! "))
        break
    except ValueError:
        print("Neplatný vstup. Zadej prosím číslo.")

Hraci=[]
time.sleep(0.5)

for i in range (Pocet_hracu):
    while True:
        try:
            Hracova_uroven = int(input("Zadej úroveň hráče "+str(i+1)+"! 5-Manuální ovládání, 4-Profesionál, 3-Dobrý hráč, 2-Začátečník, 1-Hráč opilec "))
            while Hracova_uroven < 1 or Hracova_uroven > 5:
                print("Úroveň hráče musí být v rozmezí jedna až pět")
                Hracova_uroven = int(input("Zadej správné číslo! 5-Manuální ovládání 4-Profesionál, 3-Dobrý hráč, 2-Začátečník, 1-Hráč opilec "))
            break
        except ValueError:
            print("Neplatný vstup. Zadej prosím číslo.")
    if Hracova_uroven==5:
        Jmeno=str(input("Zadejte přezdívku pro hráče "+str(i+1)+"! "))
    else:
        Jmeno=random.choice(list(Jmena))
        Jmena.remove(Jmeno)
    if i==0:
        Hrac_1=Hrac(Jmeno,Hracova_uroven,0,0,[],False,False,False,0,False,[],[],0,0,False,False,False,False)
        Hraci.append(Hrac_1)
    elif i==1:
        Hrac_2=Hrac(Jmeno,Hracova_uroven,0,0,[],False,False,False,0,False,[],[],0,0,False,False,False,False)
        Hraci.append(Hrac_2)
    elif i==2:
        Hrac_3=Hrac(Jmeno,Hracova_uroven,0,0,[],False,False,False,0,False,[],[],0,0,False,False,False,False)
        Hraci.append(Hrac_3)
    elif i==3:
        Hrac_4=Hrac(Jmeno,Hracova_uroven,0,0,[],False,False,False,0,False,[],[],0,0,False,False,False,False)
        Hraci.append(Hrac_4)
    elif i==4:
        Hrac_5=Hrac(Jmeno,Hracova_uroven,0,0,[],False,False,False,0,False,[],[],0,0,False,False,False,False)
        Hraci.append(Hrac_5)        
    time.sleep(1)

while True:
    try:
        Pocet_balicku = int(input("Zadej s kolika balíčky chceš hrát! "))
        while Pocet_balicku < 1 or Pocet_balicku > 8:
            print("Počet balíčků musí být v rozsahu jedna a osm!")
            Pocet_balicku = int(input("Zadej správné číslo! "))
        break
    except ValueError:
        print("Neplatný vstup. Zadej prosím číslo.")

Hraci_balicek=Balicek()
Hraci_balicek.Vytvor_novy()

while True:
    try:
        Rozpocet=int(input("Zadej vstupní kapitál! "))
        while Rozpocet<100:
            print("Vstupní peníze musí být alespoň sto korun.")
            Rozpocet=int(input("Zadej vstupní kapitál znovu! "))
        break
    except ValueError:
        print("Neplatný vstup. Zadej prosím číslo.")

for hrac in Hraci:
    hrac.rozpocet=Rozpocet

Dalsi_Hra=True

while Dalsi_Hra:

    for hrac in Hraci:
        if hrac.uroven<5:
            hrac.sazka=random.randint(1,int(0.4*hrac.rozpocet-1))
            print (hrac.jmeno+" sází "+str(hrac.sazka)+" korun!")
            hrac.rozpocet=hrac.rozpocet-hrac.sazka
            time.sleep(1.5)
        else:
            while True:
                Dalsi_Hra=False
                try:
                    hrac.sazka=int(input("Kolik korun chceš vsadit? "))
                    while hrac.sazka<1 or hrac.sazka>hrac.rozpocet*0.4:
                        print("Sázka musí být alespoň jedna koruna a nemůže být větší než 40% rozpočtu!")
                        hrac.sazka=int(input())
                    break
                except ValueError:
                    print("Neplatný vstup! Zadej delé číslo.")
            hrac.rozpocet=hrac.rozpocet-hrac.sazka
            print(hrac.jmeno+" sází "+str(hrac.sazka)+" korun!")
            time.sleep(1.5)

    Dealerovy_karty=[]
    Dealerovo_skore=0
    Dealeruv_BlackJack=False

    for hrac in Hraci:
        hrac.karty=[]
        hrac.blackjack=False
        hrac.split=False
        hrac.pojistka=False
        hrac.jedenactkova_esa=0
        hrac.skore=0
        hrac.SSkore1=0
        hrac.SSkore2=0
        hrac.SKarty1=[]
        hrac.SKarty2=[]
        hrac.SBJ1=False
        hrac.SBJ2=False
        hrac.S11E1=0
        hrac.S11E2=0

    for kolo in range(2):
        for i in range(Pocet_hracu+1):
            if i==Pocet_hracu:
                Dealerovy_karty.append(Hraci_balicek.Lizni_Kartu())
            else:
                Hraci[i].karty.append(Hraci_balicek.Lizni_Kartu())

    for hrac in Hraci:
        for karta in hrac.karty:
            if karta.typ=="A":
                hrac.jedenactkova_esa+=1

    for hrac in Hraci:
        hrac.skore=hrac.karty[0].hodnota+hrac.karty[1].hodnota
        if hrac.skore>21:
            hrac.skore+=-10
            hrac.jedenactkova_esa+=-1

    if Dealerovy_karty[0].hodnota+Dealerovy_karty[1].hodnota==21:
        Dealeruv_BlackJack=True
        Dealerovo_skore=21


    time.sleep(1)
    print("Dealerova první karta je: "+Dealerovy_karty[0].barva+" "+Dealerovy_karty[0].typ)
    time.sleep(1)
    for hrac in Hraci:

        print(hrac.jmeno+" Má v ruce: "+hrac.karty[0].barva+" "+hrac.karty[0].typ+" a "+hrac.karty[1].barva+" "+hrac.karty[1].typ)
        time.sleep(0.5)
        print("Hodnota těchto karet je: "+str(hrac.skore))
        time.sleep(1)
    
        if Dealerovy_karty[0].typ=="A":
            hrac.pojistka=hrac.pojistovaci_funkce()
            if hrac.pojistka:
                print(hrac.jmeno+" se pojistil!")
                hrac.rozpocet-=hrac.sazka//2
            else:
                print(hrac.jmeno+" se nepojistil!")
            time.sleep(1)
        if hrac.skore==21:
            print(hrac.jmeno.upper()+" MÁ BLACKJACK!")
            hrac.blackjack=True
            time.sleep(0.8)
            print(hrac.jmeno+" končí svůj tah!")

        else:
            tah=hrac.Rozhodovaci_Funkce_Prvni_Tah(Dealerovy_karty[0].hodnota)

            if tah=="Split":
                print(hrac.jmeno+" hraje Split!")
                hrac.split=True
                hrac.rozpocet=hrac.rozpocet-hrac.sazka
                hrac.SKarty1=[hrac.karty[0]]
                hrac.SKarty2=[hrac.karty[1]]
                hrac.SKarty1.append(Hraci_balicek.Lizni_Kartu())
                hrac.SKarty2.append(Hraci_balicek.Lizni_Kartu())
                hrac.SSkore1=hrac.SKarty1[0].hodnota+hrac.SKarty1[1].hodnota
                hrac.SSkore2=hrac.SKarty2[0].hodnota+hrac.SKarty2[1].hodnota
                hrac.SBJ1=False
                hrac.SBJ2=False
                hrac.S11E1=0
                hrac.S11E2=0
                for karta in hrac.SKarty1:
                    if karta.typ=="A":
                        hrac.S11E1+=1
                while hrac.SSkore1>21 and hrac.S11E1>0:
                    hrac.SSkore1+=-10
                    hrac.S11E1+=-1
                time.sleep(1)
                print(hrac.jmeno+" má v první várce tyto karty: "+hrac.SKarty1[0].barva+" "+hrac.SKarty1[0].typ+" a "+hrac.SKarty1[1].barva+" "+hrac.SKarty1[1].typ)
                time.sleep(0.8)
                print("Skóre těchto karet je: "+str(hrac.SSkore1))
                time.sleep(1)
                for karta in hrac.SKarty2:
                    if karta.typ=="A":
                        hrac.S11E2+=1
                while hrac.SSkore2>21 and hrac.S11E2>0:
                    hrac.SSkore2+=-10
                    hrac.S11E2+=-1              
                print(hrac.jmeno+" má v druhé várce tyto karty: "+hrac.SKarty2[0].barva+" "+hrac.SKarty2[0].typ+" a "+hrac.SKarty2[1].barva+" "+hrac.SKarty2[1].typ)
                time.sleep(0.8)
                print("Skóre těchto karet je: "+str(hrac.SSkore2))
                time.sleep(1)
                if hrac.SSkore1!=21:
                    print(hrac.jmeno+" hraje s první várkou!")    
                    tah=Rozhodovaci_funkce(hrac.uroven,hrac.SSkore1,Dealerovy_karty[0].hodnota)
                    while tah=="Hit":
                        print(hrac.jmeno+" si líže další kartu!")
                        hrac.SKarty1.append(Hraci_balicek.Lizni_Kartu())
                        print(hrac.jmeno+" má novou kartu a tou je "+hrac.SKarty1[-1].barva+" "+hrac.SKarty1[-1].typ)
                        if hrac.SKarty1[-1].typ=="A":
                            hrac.S11E1+=1
                        hrac.SSkore1=hrac.SSkore1+hrac.SKarty1[-1].hodnota
                        while hrac.S11E1>0 and hrac.SSkore1>21:
                            hrac.S11E1+=-1
                            hrac.SSkore1+=-10
                        time.sleep(1)
                        print(hrac.jmeno+" má skóre "+str(hrac.SSkore1))
                        if hrac.SSkore1>21:
                            time.sleep(1)
                            print("Bust!")
                            time.sleep(0.5)
                            break
                        tah=Rozhodovaci_funkce(hrac.uroven,hrac.SSkore1,Dealerovy_karty[0].hodnota)
                        time.sleep(1)
                    print(hrac.jmeno+" ukončil tah s první várkou!")
                else:
                    print(hrac.jmeno+" má v první várce BlackJack!")
                    hrac.SBJ1=True
                time.sleep(1)
                if hrac.SSkore2!=21:
                    print(hrac.jmeno+" hraje s druhou várkou!")                 
                    tah=Rozhodovaci_funkce(hrac.uroven,hrac.SSkore2,Dealerovy_karty[0].hodnota)
                    while tah=="Hit":
                        print(hrac.jmeno+" si líže další kartu!")
                        hrac.SKarty2.append(Hraci_balicek.Lizni_Kartu())
                        print(hrac.jmeno+" má novou kartu a tou je "+hrac.SKarty2[-1].barva+" "+hrac.SKarty2[-1].typ)
                        if hrac.SKarty2[-1].typ=="A":
                            hrac.S11E2+=1
                        hrac.SSkore2=hrac.SSkore2+hrac.SKarty2[-1].hodnota
                        while hrac.S11E2>0 and hrac.SSkore2>21:
                            hrac.S11E2+=-1
                            hrac.SSkore2+=-10
                        time.sleep(1)
                        print(hrac.jmeno+" má skóre "+str(hrac.SSkore2))
                        if hrac.SSkore2>21:
                            time.sleep(1)
                            print("Bust!")
                            time.sleep(0.5)
                            break
                        tah=Rozhodovaci_funkce(hrac.uroven,hrac.SSkore2,Dealerovy_karty[0].hodnota)
                        time.sleep(1)
                    print(hrac.jmeno+" ukončil tah s druhou várkou!")
                else:
                    print(hrac.jmeno+" má v druhé várce BlackJack!")
                    hrac.SBJ2=True
                time.sleep(1)
                print(hrac.jmeno+" končí svůj tah!")
    
            elif tah=="Double":
                print(hrac.jmeno+" hraje Double!")
                time.sleep(1)
                hrac.rozpocet=hrac.rozpocet-hrac.sazka
                hrac.sazka=hrac.sazka*2
                hrac.karty.append(Hraci_balicek.Lizni_Kartu())
                print("Nová karta je "+hrac.karty[2].barva+" "+hrac.karty[2].typ)
                hrac.skore=hrac.skore+hrac.karty[2].hodnota
                if hrac.karty[2].typ=="A":
                    hrac.jedenactkova_esa+=1
                while hrac.skore>21 and hrac.jedenactkova_esa>0:
                    hrac.skore+=-10
                    hrac.jedenactkova_esa+=-1                        
                time.sleep(0.8)
                print(hrac.jmeno+" má skóre "+str(hrac.skore))
                if hrac.skore>21:
                    time.sleep(1)
                    print("Bust!")
                    time.sleep(0.5)
                time.sleep(1)
                print(hrac.jmeno+" končí svůj tah!")
    
            else:
                while tah=="Hit":
                    print(hrac.jmeno+" si líže další kartu!")
                    hrac.karty.append(Hraci_balicek.Lizni_Kartu())
                    time.sleep(1)
                    print(hrac.jmeno+" má novou kartu a tou je "+hrac.karty[-1].barva+" "+hrac.karty[-1].typ)
                    if hrac.karty[-1].typ=="A":
                        hrac.jedenactkova_esa+=1
                    hrac.skore=hrac.skore+hrac.karty[-1].hodnota
                    while hrac.jedenactkova_esa>0 and hrac.skore>21:
                        hrac.jedenactkova_esa+=-1
                        hrac.skore+=-10
                    time.sleep(0.8)
                    print(hrac.jmeno+" má skóre "+str(hrac.skore))
                    if hrac.skore>21:
                        time.sleep(1)
                        print("Bust!")
                        time.sleep(0.5)
                        break
                    tah=Rozhodovaci_funkce(hrac.uroven,hrac.skore,Dealerovy_karty[0].hodnota)
                    time.sleep(1)
                print(hrac.jmeno+" končí svůj tah!")
                time.sleep(2)

    Dealerovo_skore=Dealeruv_tah()
    
    for hrac in Hraci:
        vyhra=0
        vyhra1=0
        vyhra2=0
        if hrac.split:
            print(hrac.jmeno+" rozdělil svou sázku, takže se vyhodnocuje ve dvou vlnách!")
            time.sleep(1)
            print("Vyhodnocování první várky.")
            vyhra1=vyhodnoceni(hrac.SSkore1,Dealerovo_skore,hrac.sazka,hrac.pojistka,hrac.SBJ1,Dealeruv_BlackJack,hrac.jmeno)
            time.sleep(1)
            print(hrac.jmeno+" získává v první várce "+str(vyhra1)+ " korun!")
            hrac.rozpocet+=vyhra1
            time.sleep(1)
            print("Vyhodnodnocování druhé várky!")
            vyhra2=vyhodnoceni(hrac.SSkore2,Dealerovo_skore,hrac.sazka,hrac.pojistka,hrac.SBJ2,Dealeruv_BlackJack,hrac.jmeno)
            time.sleep(1)
            print(hrac.jmeno+" získává v druhé várce "+str(vyhra2)+ " korun!")
            hrac.rozpocet+=vyhra2                
        else:
            vyhra=vyhodnoceni(hrac.skore,Dealerovo_skore,hrac.sazka,hrac.pojistka,hrac.blackjack,Dealeruv_BlackJack,hrac.jmeno)
            time.sleep(1)
            print(hrac.jmeno+" získává "+str(vyhra)+" korun!")
            hrac.rozpocet+=vyhra

    time.sleep(1)
    for hrac in Hraci:
        print(hrac.jmeno+" má momentálně "+str(hrac.rozpocet)+" korun!")
        time.sleep(0.8)
        if hrac.rozpocet<10:
            time.sleep(1.3)
            print(hrac.jmeno+" má bohužel příliš málo peněz na to, aby mohl nadále pokračovat ve hře. Hra pro něj končí!")
            Hraci.remove(hrac)
            Pocet_hracu+=-1
    time.sleep(0.8)
    
    if Pocet_hracu>0:
        print("Chceš dát další hru?")
        Nova_hra=str(input()).upper()
        while Nova_hra!="ANO" and Nova_hra!="NE":
            print("Musíš odpovědět Ano nebo ne.")
            Nova_hra=str(input()).upper()
        if Nova_hra=="ANO":
            Dalsi_Hra=True
        else:
            Dalsi_Hra=False
            time.sleep(1)
    else:
        print("Všichni hráči zkrachovali.")
        Dalsi_Hra=False

time.sleep(2)
print("Konec hry!")   
time.sleep(5)             