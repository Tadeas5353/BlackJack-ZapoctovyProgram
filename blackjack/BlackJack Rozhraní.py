import random
import sys
import tkinter as tk

class Karta:
    def __init__(self, barva, typ, hodnota):
        self.barva=barva
        self.typ=typ
        self.hodnota=int(hodnota)
    def nazev(self):
        Nazev=(self.barva+" "+self.typ)
        return Nazev

class Balicek:
    def __init__(self):
        self.balicek=[]
    def Zamichat(self):
        random.shuffle(self.balicek)

# Tato funkce vytváří nový balíček pomocí všech kombincí barev a typů karet.
    def Vytvor_novy(self):
        self.balicek.clear()
        for i in range (Pocet_balicku):
            for barva in (["Srdce", "Listy", "Piky", "Káry"]):
                for typ in ([("2",2),("3",3),("4",4),("5",5),("6",6),("7",7),("8",8),("9",9),("10",10),("J",10),("Q",10),("K",10),("A",11)]):
                    self.balicek.append(Karta(barva,typ[0],typ[1]))
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

# Funkce sloužící k rozhodnutí prvního tahu hráče na základě údaje o jeho kartách, skóre a kartě dealera. Jsou rozlišeny speciální případy, kdy hráč má dvojici 
# karet stejné hodnoty a kdy hráč má v ruce eso.  Rozhodování probíhá v závislosti na hráčově úrovni.

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

# Funkce která u hráčů rozhoduje, zda se pojistí, či nikoliv. V závislosti na jejich úrovni. 

    def pojistovaci_funkce(self):
        if self.uroven==4:
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

def vyhodnoceni(hrac, dealer, sazka, Pojisten, BlackJack, Dealeruv_BlackJack):
    if BlackJack and Dealeruv_BlackJack:      
        if Pojisten:
            return sazka*2
        else:
            return sazka        
    if BlackJack:
        return sazka*2+sazka//2
    if dealer==hrac and not Dealeruv_BlackJack:
        return sazka
    if (dealer<hrac or dealer>21) and hrac<=21:
        return sazka*2
    else:
        if Pojisten and Dealeruv_BlackJack:
            return sazka
        return 0

# Funkce, která rozhoduje o tazích hráče v závislosti na jeho skóre a Dealerově kartě. Pro každého hráče rozhoduje zvlášť.

def Rozhodovaci_funkce(uroven,skore,dealer):

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

# Funkce vrátí barvu framu hráče, který byl jako poslední na tahu. Též zavře tlačítko, které spustilo tuto funkci. Dále hra buď nechá proběhnout dealerův tah
# nebo nastaví hodnotu dealeruv_blackjack na True

def Dealeruv_tah():

    Spustit_vyhodnocovani.place(relx=1.0, rely=1.0, anchor="se",x=-10, y=-10)
    Zacit_dealeruv_tah.place_forget()
    Ukazatel_BlackJacku.pack_forget()

    if Pocet_hracu==1:
        Okno_hrac_1.config(bg="#eddd72")
        Jmeno_hrac_1.config(bg="#eddd72")
        Zobrazeni_karet_hrace_1.config(bg="#eddd72")
        Zobrazeni_sazky_hrce_1.config(bg="#eddd72")
        Zobrazeni_rozpoctu_hrace_1.config(bg="#eddd72")
        Zobrazeni_skore_hrace_1.config(bg="#eddd72")
    elif Pocet_hracu==2:
        Okno_hrac_2.config(bg="#eddd72")
        Jmeno_hrac_2.config(bg="#eddd72")
        Zobrazeni_karet_hrace_2.config(bg="#eddd72")
        Zobrazeni_sazky_hrce_2.config(bg="#eddd72")
        Zobrazeni_rozpoctu_hrace_2.config(bg="#eddd72")
        Zobrazeni_skore_hrace_2.config(bg="#eddd72")  
    elif Pocet_hracu==3:
        Okno_hrac_3.config(bg="#eddd72")
        Jmeno_hrac_3.config(bg="#eddd72")
        Zobrazeni_karet_hrace_3.config(bg="#eddd72")
        Zobrazeni_sazky_hrce_3.config(bg="#eddd72")
        Zobrazeni_rozpoctu_hrace_3.config(bg="#eddd72")
        Zobrazeni_skore_hrace_3.config(bg="#eddd72") 
    elif Pocet_hracu==4:
        Okno_hrac_4.config(bg="#eddd72")
        Jmeno_hrac_4.config(bg="#eddd72")
        Zobrazeni_karet_hrace_4.config(bg="#eddd72")
        Zobrazeni_sazky_hrce_4.config(bg="#eddd72")
        Zobrazeni_rozpoctu_hrace_4.config(bg="#eddd72")
        Zobrazeni_skore_hrace_4.config(bg="#eddd72") 
    else:
        Okno_hrac_5.config(bg="#eddd72")
        Jmeno_hrac_5.config(bg="#eddd72")
        Zobrazeni_karet_hrace_5.config(bg="#eddd72")
        Zobrazeni_sazky_hrce_5.config(bg="#eddd72")
        Zobrazeni_rozpoctu_hrace_5.config(bg="#eddd72")
        Zobrazeni_skore_hrace_5.config(bg="#eddd72") 

    global Dealerovy_karty
    global Hraci_balicek
    global Dealerovo_skore

    if Dealeruv_BlackJack:
        Ukazatel_BlackJacku.config(text="Dealer má BLACKJACK!")
        Ukazatel_BlackJacku.pack()
        Zobrazeni_dealerovych_karet.config(text="Karty: "+konvertor_balicku(Dealerovy_karty))
        Zobrazeni_dealerova_skore.config(text="Skóre: 21")
    else:
        Dealerova_11_esa=0
        Dealerovo_skore=Dealerovy_karty[0].hodnota+Dealerovy_karty[1].hodnota
        if Dealerovy_karty[0].typ=="A":
            Dealerova_11_esa+=1
        if Dealerovy_karty[1].typ=="A":
            Dealerova_11_esa+=1
        while Dealerova_11_esa>0 and Dealerovo_skore>21:
            Dealerovo_skore+=-10
            Dealerova_11_esa+=-1
        Zobrazeni_dealerovych_karet.config(text="Karty: "+konvertor_balicku(Dealerovy_karty))
        Dealerovo_skore=Dealerovy_karty[0].hodnota+Dealerovy_karty[1].hodnota
        Zobrazeni_dealerova_skore.config(text="Skóre: "+str(Dealerovo_skore))
        while Dealerovo_skore<17:
            Dealerovy_karty.append(Hraci_balicek.Lizni_Kartu())
            Dealerovo_skore=Dealerovo_skore+Dealerovy_karty[-1].hodnota
            if Dealerovy_karty[-1].typ=="A":
                Dealerova_11_esa+=1
            while Dealerova_11_esa>0 and Dealerovo_skore>21:
                Dealerova_11_esa+=-1
                Dealerovo_skore+=-10
            Zobrazeni_dealerovych_karet.config(text="Karty: "+konvertor_balicku(Dealerovy_karty))
            Zobrazeni_dealerova_skore.config(text="Skóre: "+str(Dealerovo_skore))

# Funkce na kontrolu rozpočtu. Volána ve widgetech na řádku 1907 a 1908

def Kontrala_rozpoctu(vstup):
    if vstup == "": 
        return True
    if vstup.isdigit() and int(vstup)<=1000000:
        return True
    else:
        return False

# Funkce rozmístí widgety pro zadání úrovní hráčů a zavře widgety z první stránky (která se otevírá v hlavním porgramu).

def Nastaveni_hracu_zobrazit():
    Zadavani_urovne_nadpis.pack()
    Frame_na_urovne.pack()
    Frame_urovne_1.pack(side="left")

    if Pocet_hracu>1:
        Frame_urovne_2.pack(side="left")
        if Pocet_hracu>2:
            Frame_urovne_3.pack(side="left")
            if Pocet_hracu>3:
                Frame_urovne_4.pack(side="left")
                if Pocet_hracu>4:
                    Frame_urovne_5.pack(side="left")

    Uroven_prvniho_hrace_nadpis.pack()
    Uroven_prvniho_hrace_vyber.pack()
    Vyber_prvni_urovne.pack()

    if Pocet_hracu>1:
        Uroven_druheho_hrace_nadpis.pack()
        Uroven_druheho_hrace_vyber.pack()
        Vyber_druhe_urovne.pack()

        if Pocet_hracu>2:
            Uroven_tretiho_hrace_nadpis.pack()
            Uroven_tretiho_hrace_vyber.pack()
            Vyber_treti_urovne.pack()

            if Pocet_hracu>3:
                Uroven_ctvrteho_hrace_nadpis.pack()
                Uroven_ctvrteho_hrace_vyber.pack()
                Vyber_ctvrte_urovne.pack()

                if Pocet_hracu>4:
                    Uroven_pateho_hrace_nadpis.pack()
                    Uroven_pateho_hrace_vyber.pack()
                    Vyber_pate_urovne.pack() 

    Potvrzeni_urovni.place(relx=1.0, rely=1.0, anchor="se",x=-10, y=-10)

#Funkce nastaví hodnoty proměnných a zároveň a v příapdě, že rozpočet byl zadán správně, posunu hru vpřed. Navíc zavře již nepotřebné widgety.

def Potvrdit_zaklad():
    global Rozpocet
    global Pocet_balicku
    global Pocet_hracu
    global Hraci_balicek
    
    Rozpocet=Nastaveni_rozpoctu.get()
    Pocet_balicku=Posuvnik_ZadejtePocetBalicku.get()
    Pocet_hracu=Posuvnik_ZadejtePocetHracu.get()
    Hraci_balicek.Vytvor_novy()

    if Rozpocet!="" and int(Rozpocet)>=100:
        Rozpocet=int(Rozpocet)
        Text_ZadejtePocetHracu.pack_forget()
        Text_ZadejtePocetBalicku.pack_forget()
        Text_ZadejteRozpocet.pack_forget()
        Posuvnik_ZadejtePocetBalicku.pack_forget()
        Posuvnik_ZadejtePocetHracu.pack_forget()
        Nastaveni_rozpoctu.pack_forget()
        Potvrdit_zakladni_vstup.place_forget()
        Spatny_Rozpocet.pack_forget()
        Nastaveni_hracu_zobrazit()
    else:
        Spatny_Rozpocet.pack()

#Následující funkce kontrolují, zda hráč nezvolil u hráče manuální ovládání a pokud ano, otevřou políčko pro zadání jména.

def Vypsani_urovne_1(event):
    vybrana_uroven = Uroven_prvniho_hrace_vyber.curselection()
    if vybrana_uroven:
        Uroven_pro_1.set(Uroven_prvniho_hrace_vyber.get(vybrana_uroven[0]))
        if Uroven_prvniho_hrace_vyber.get(Uroven_prvniho_hrace_vyber.curselection()) == "Manuální ovládání":
            Zadani_jmena_1.pack()
        else:
            Zadani_jmena_1.pack_forget()

def Vypsani_urovne_2(event):
    vybrana_uroven = Uroven_druheho_hrace_vyber.curselection()
    if vybrana_uroven:
        Uroven_pro_2.set(Uroven_druheho_hrace_vyber.get(vybrana_uroven[0]))
        if Uroven_druheho_hrace_vyber.get(Uroven_druheho_hrace_vyber.curselection()) == "Manuální ovládání":
            Zadani_jmena_2.pack()
        else:
            Zadani_jmena_2.pack_forget()        

def Vypsani_urovne_3(event):
    vybrana_uroven = Uroven_tretiho_hrace_vyber.curselection()
    if vybrana_uroven:
        Uroven_pro_3.set(Uroven_tretiho_hrace_vyber.get(vybrana_uroven[0]))
        if Uroven_tretiho_hrace_vyber.get(Uroven_tretiho_hrace_vyber.curselection()) == "Manuální ovládání":
            Zadani_jmena_3.pack()
        else:
            Zadani_jmena_3.pack_forget()

def Vypsani_urovne_4(event):
    vybrana_uroven = Uroven_ctvrteho_hrace_vyber.curselection()
    if vybrana_uroven:
        Uroven_pro_4.set(Uroven_ctvrteho_hrace_vyber.get(vybrana_uroven[0]))
        if Uroven_ctvrteho_hrace_vyber.get(Uroven_ctvrteho_hrace_vyber.curselection()) == "Manuální ovládání":
            Zadani_jmena_4.pack()
        else:
            Zadani_jmena_4.pack_forget()

def Vypsani_urovne_5(event):
    vybrana_uroven = Uroven_pateho_hrace_vyber.curselection()
    if vybrana_uroven:
        Uroven_pro_5.set(Uroven_pateho_hrace_vyber.get(vybrana_uroven[0]))
        if Uroven_pateho_hrace_vyber.get(Uroven_pateho_hrace_vyber.curselection()) == "Manuální ovládání":
            Zadani_jmena_5.pack()
        else:
            Zadani_jmena_5.pack_forget()

def Kontrola_urovni():

    Vsude_uroven = True

    if Vyber_prvni_urovne.cget("text") =="":
        Vsude_uroven = False

    if Pocet_hracu>1 and Vsude_uroven:
        if Vyber_druhe_urovne.cget("text") =="":
            Vsude_uroven = False

    if Pocet_hracu>2 and Vsude_uroven:
        if Vyber_treti_urovne.cget("text") =="":
            Vsude_uroven = False

    if Pocet_hracu>3 and Vsude_uroven:
        if Vyber_ctvrte_urovne.cget("text") =="":
            Vsude_uroven = False

    if Pocet_hracu>4 and Vsude_uroven:
        if Vyber_pate_urovne.cget("text") =="":
            Vsude_uroven = False

    if Vsude_uroven:
        Potvrdit_urovne()
    else:
        Spatne_urovne.pack(side="bottom")

#Funkce, ve které se vytváří hráči. Jelikož předem neznáme počet hráčů a jelikož pro každého hráče můme různé proměnné, je tento kód poměrně dlouhý, přestože se v něm
#většinou opakuje to stejné dokola. Tato sitauce se v celém kódu objevuje častěji ze stejného důvodu.

def Potvrdit_urovne():
    global Hraci
    global Jmena

    for i in range (1,Pocet_hracu+1):
        if i==1:
            Hracova_uroven=Vyber_prvni_urovne.cget("text")
            if Hracova_uroven:
                Hracova_uroven=Konvertor_urovni(Hracova_uroven)
                if Hracova_uroven==0:
                    Jmeno=Zadani_jmena_1.get()
                    if Jmeno=="":
                        Jmeno="Ignotus Primus"                    
                else:
                    Jmeno=random.choice(list(Jmena))
                    Jmena.remove(Jmeno)
                Hrac_1=Hrac(Jmeno,Hracova_uroven,Rozpocet,0,[],False,False,False,0,False,[],[],0,0,False,False,False,False)
                Hraci.append(Hrac_1)
        if i==2:
            Hracova_uroven=Vyber_druhe_urovne.cget("text")
            if Hracova_uroven:
                Hracova_uroven=Konvertor_urovni(Hracova_uroven)
                if Hracova_uroven==0:
                    Jmeno=Zadani_jmena_2.get()
                    if Jmeno=="":
                        Jmeno="Ignotus Secundus"                    
                else:
                    Jmeno=random.choice(list(Jmena))
                    Jmena.remove(Jmeno)
                Hrac_2=Hrac(Jmeno,Hracova_uroven,Rozpocet,0,[],False,False,False,0,False,[],[],0,0,False,False,False,False)
                Hraci.append(Hrac_2)
        if i==3:
            Hracova_uroven=Vyber_treti_urovne.cget("text")
            if Hracova_uroven:
                Hracova_uroven=Konvertor_urovni(Hracova_uroven)
                if Hracova_uroven==0:
                    Jmeno=Zadani_jmena_3.get()
                    if Jmeno=="":
                        Jmeno="Ignotus Tertius"                    
                else:
                    Jmeno=random.choice(list(Jmena))
                    Jmena.remove(Jmeno)
                Hrac_3=Hrac(Jmeno,Hracova_uroven,Rozpocet,0,[],False,False,False,0,False,[],[],0,0,False,False,False,False)
                Hraci.append(Hrac_3)
        if i==4:
            Hracova_uroven=Vyber_ctvrte_urovne.cget("text")
            if Hracova_uroven:
                Hracova_uroven=Konvertor_urovni(Hracova_uroven)
                if Hracova_uroven==0:
                    Jmeno=Zadani_jmena_4.get()
                    if Jmeno=="":
                        Jmeno="Ignotus Quartus"                    
                else:
                    Jmeno=random.choice(list(Jmena))
                    Jmena.remove(Jmeno)
                Hrac_4=Hrac(Jmeno,Hracova_uroven,Rozpocet,0,[],False,False,False,0,False,[],[],0,0,False,False,False,False)
                Hraci.append(Hrac_4)
        if i==5:
            Hracova_uroven=Vyber_pate_urovne.cget("text")
            if Hracova_uroven:
                Hracova_uroven=Konvertor_urovni(Hracova_uroven)
                if Hracova_uroven==0:
                    Jmeno=Zadani_jmena_5.get()
                    if Jmeno=="":
                        Jmeno="Ignotus Quintius"
                else:
                    Jmeno=random.choice(list(Jmena))
                    Jmena.remove(Jmeno)
                Hrac_5=Hrac(Jmeno,Hracova_uroven,Rozpocet,0,[],False,False,False,0,False,[],[],0,0,False,False,False,False)
                Hraci.append(Hrac_5)

    Frame_na_urovne.pack_forget()
    Potvrzeni_urovni.place_forget()
    Zadavani_urovne_nadpis.pack_forget()
    Spatne_urovne.pack_forget()

    Zacatek_kola()

def Konvertor_urovni(Uroven):
    return Urovne.index(Uroven)

# Funkce, která primárne nastaví základní rozhraní. Tato funkce je volána i v případě, že uživatel se na konci kola rozhodne pro další hru. Celé rozhraní je pro každé kolo
# přenastavováno z toho důvodu, že na konci kola mohl někdo zkrachovat.

def Zacatek_kola():

    global Dealerovy_karty
    global Dealeruv_BlackJack
    global Dealerovo_okno
    global Napis_Dealer
    global Zobrazeni_dealerova_skore
    global Zobrazeni_dealerovych_karet
    global Okno_hracu
    global Sazkovy_frame
    global Okno_hrac_1
    global Okno_hrac_2
    global Okno_hrac_3
    global Okno_hrac_4
    global Okno_hrac_5
    global Jmeno_hrac_1
    global Jmeno_hrac_2
    global Jmeno_hrac_3
    global Jmeno_hrac_4
    global Jmeno_hrac_5
    global Zobrazeni_karet_hrace_1
    global Zobrazeni_karet_hrace_2
    global Zobrazeni_karet_hrace_3
    global Zobrazeni_karet_hrace_4
    global Zobrazeni_karet_hrace_5
    global Zobrazeni_rozpoctu_hrace_1
    global Zobrazeni_rozpoctu_hrace_2
    global Zobrazeni_rozpoctu_hrace_3
    global Zobrazeni_rozpoctu_hrace_4
    global Zobrazeni_rozpoctu_hrace_5
    global Zobrazeni_sazky_hrce_1
    global Zobrazeni_sazky_hrce_2
    global Zobrazeni_sazky_hrce_3
    global Zobrazeni_sazky_hrce_4
    global Zobrazeni_sazky_hrce_5
    global Zobrazeni_skore_hrace_1
    global Zobrazeni_skore_hrace_2
    global Zobrazeni_skore_hrace_3
    global Zobrazeni_skore_hrace_4
    global Zobrazeni_skore_hrace_5
    global Sazka_hrace_1
    global Sazka_hrace_1_napis
    global Sazka_hrace_2
    global Sazka_hrace_2_napis
    global Sazka_hrace_3
    global Sazka_hrace_3_napis
    global Sazka_hrace_4
    global Sazka_hrace_4_napis
    global Sazka_hrace_5
    global Sazka_hrace_5_napis
    global Potvrdit_sazky
    global Jen_boti

    Dealerovy_karty=[]
    Dealerovo_skore=0
    Dealeruv_BlackJack=False

    Dealerovo_okno = tk.Frame(Okno,bg="#5fb9fa")
    Napis_Dealer = tk.Label(Dealerovo_okno,text="DEALER",justify="center",font=("Comic Sans MS",20),fg="black",bg="#5fb9fa")
    Zobrazeni_dealerovych_karet = tk.Label(Dealerovo_okno,text="Tady budou dealerovy karty",bg="#5fb9fa")
    Zobrazeni_dealerova_skore = tk.Label(Dealerovo_okno,text="Skóre: "+str(Dealerovo_skore),bg="#5fb9fa")

    Okno_hracu = tk.Frame(Okno,bg="#eddd72")

    Sazkovy_frame = tk.Frame(Okno,pady=10)  

    Jen_boti = True

    Okno_hrac_1 = tk.Frame(Okno_hracu,bg="#eddd72")
    Jmeno_hrac_1 = tk.Label(Okno_hrac_1,bg="#eddd72",text=Hraci[0].jmeno,font=("Comic Sans MS",20),fg="black")
    Zobrazeni_karet_hrace_1 = tk.Label(Okno_hrac_1,bg="#eddd72",text="Tady budou karty hráče 1")
    Zobrazeni_skore_hrace_1 = tk.Label(Okno_hrac_1,bg="#eddd72",text="Skóre: ")
    Zobrazeni_rozpoctu_hrace_1 = tk.Label(Okno_hrac_1,bg="#eddd72",text="Rozpočet: "+str(Hraci[0].rozpocet))
    Zobrazeni_sazky_hrce_1 = tk.Label(Okno_hrac_1,bg="#eddd72",text="Sázka: "+str(Hraci[0].sazka))
    Sazka_hrace_1_napis = tk.Label(Sazkovy_frame,text=Hraci[0].jmeno+" sází!",font=("Arial",12))
    Sazka_hrace_1 = tk.Scale(Sazkovy_frame,from_=1,to=Hraci[0].rozpocet*0.4,orient="horizontal", length=200, sliderlength=20, showvalue=True)
    if Hraci[0].uroven==0:
        Jen_boti = False

    Potvrdit_sazky = tk.Button(Okno, text="Potvrdit sázky", command=PotvrditSazky, font=("Arial",10))

    Spustit_novou_hru.pack_forget()
    
    if Pocet_hracu>1:

        Okno_hrac_2 = tk.Frame(Okno_hracu,bg="#eddd72")
        Jmeno_hrac_2 = tk.Label(Okno_hrac_2,bg="#eddd72",text=Hraci[1].jmeno,font=("Comic Sans MS",20),fg="black")
        Zobrazeni_karet_hrace_2 = tk.Label(Okno_hrac_2,bg="#eddd72",text="Tady budou karty hráče 2")
        Zobrazeni_skore_hrace_2 = tk.Label(Okno_hrac_2,bg="#eddd72",text="Skóre: ")
        Zobrazeni_rozpoctu_hrace_2 = tk.Label(Okno_hrac_2,bg="#eddd72",text="Rozpočet: "+str(Hraci[1].rozpocet))
        Zobrazeni_sazky_hrce_2 = tk.Label(Okno_hrac_2,bg="#eddd72",text="Sázka: "+str(Hraci[1].sazka))
        Sazka_hrace_2_napis = tk.Label(Sazkovy_frame,text=Hraci[1].jmeno+" sází!",font=("Arial",12))
        Sazka_hrace_2 = tk.Scale(Sazkovy_frame,from_=1,to=Hraci[1].rozpocet*0.4,orient="horizontal", length=200, sliderlength=20, showvalue=True)
        if Hraci[1].uroven==0:
            Jen_boti = False

        if Pocet_hracu>2:

            Okno_hrac_3 = tk.Frame(Okno_hracu,bg="#eddd72")
            Jmeno_hrac_3 = tk.Label(Okno_hrac_3,bg="#eddd72",text=Hraci[2].jmeno,font=("Comic Sans MS",20),fg="black")
            Zobrazeni_karet_hrace_3 = tk.Label(Okno_hrac_3,bg="#eddd72",text="Tady budou karty hráče 3")
            Zobrazeni_skore_hrace_3 = tk.Label(Okno_hrac_3,bg="#eddd72",text="Skóre: ")
            Zobrazeni_rozpoctu_hrace_3 = tk.Label(Okno_hrac_3,bg="#eddd72",text="Rozpočet: "+str(Hraci[2].rozpocet))
            Zobrazeni_sazky_hrce_3 = tk.Label(Okno_hrac_3,bg="#eddd72",text="Sázka: "+str(Hraci[2].sazka))
            Sazka_hrace_3_napis = tk.Label(Sazkovy_frame,text=Hraci[2].jmeno+" sází!",font=("Arial",12))
            Sazka_hrace_3 = tk.Scale(Sazkovy_frame,from_=1,to=Hraci[2].rozpocet*0.4,orient="horizontal", length=200, sliderlength=20, showvalue=True)
            if Hraci[2].uroven==0:
                Jen_boti = False

            if Pocet_hracu>3:

                Okno_hrac_4 = tk.Frame(Okno_hracu,bg="#eddd72")
                Jmeno_hrac_4 = tk.Label(Okno_hrac_4,bg="#eddd72",text=Hraci[3].jmeno,font=("Comic Sans MS",20),fg="black")
                Zobrazeni_karet_hrace_4 = tk.Label(Okno_hrac_4,bg="#eddd72",text="Tady budou karty hráče 4")
                Zobrazeni_skore_hrace_4 = tk.Label(Okno_hrac_4,bg="#eddd72",text="Skóre: ")
                Zobrazeni_rozpoctu_hrace_4 = tk.Label(Okno_hrac_4,bg="#eddd72",text="Rozpočet: "+str(Hraci[3].rozpocet))
                Zobrazeni_sazky_hrce_4 = tk.Label(Okno_hrac_4,bg="#eddd72",text="Sázka: "+str(Hraci[3].sazka))
                Sazka_hrace_4_napis = tk.Label(Sazkovy_frame,text=Hraci[3].jmeno+" sází!",font=("Arial",12))
                Sazka_hrace_4 = tk.Scale(Sazkovy_frame,from_=1,to=Hraci[3].rozpocet*0.4,orient="horizontal", length=200, sliderlength=20, showvalue=True)
                if Hraci[3].uroven==0:
                    Jen_boti = False

                if Pocet_hracu>4:
                
                    Okno_hrac_5 = tk.Frame(Okno_hracu,bg="#eddd72")
                    Jmeno_hrac_5 = tk.Label(Okno_hrac_5,bg="#eddd72",text=Hraci[4].jmeno,font=("Comic Sans MS",20),fg="black")
                    Zobrazeni_karet_hrace_5 = tk.Label(Okno_hrac_5,bg="#eddd72",text="Tady budou karty hráče 5")
                    Zobrazeni_skore_hrace_5 = tk.Label(Okno_hrac_5,bg="#eddd72",text="Skóre: ")
                    Zobrazeni_rozpoctu_hrace_5 = tk.Label(Okno_hrac_5,bg="#eddd72",text="Rozpočet: "+str(Hraci[4].rozpocet))
                    Zobrazeni_sazky_hrce_5 = tk.Label(Okno_hrac_5,bg="#eddd72",text="Sázka: "+str(Hraci[4].sazka))
                    Sazka_hrace_5_napis = tk.Label(Sazkovy_frame,text=Hraci[4].jmeno+" sází!",font=("Arial",12))
                    Sazka_hrace_5 = tk.Scale(Sazkovy_frame,from_=1,to=Hraci[4].rozpocet*0.4,orient="horizontal", length=200, sliderlength=20, showvalue=True)
                    if Hraci[4].uroven==0:
                        Jen_boti = False

    Dealerovo_okno.pack(side="right")
    Napis_Dealer.pack(side="top")
    Zobrazeni_dealerovych_karet.pack(side="left")
    Zobrazeni_dealerova_skore.pack(side="left")

    Okno_hracu.pack(side="left")
    Okno_hrac_1.pack(side="top")
    Jmeno_hrac_1.pack(side="top")    
    Zobrazeni_karet_hrace_1.pack(side="left")
    Zobrazeni_skore_hrace_1.pack(side="left")
    Zobrazeni_rozpoctu_hrace_1.pack(side="left")
    Zobrazeni_sazky_hrce_1.pack(side="left")

    Sazkovy_frame.pack()

    if Hraci[0].uroven==0:
        Sazka_hrace_1_napis.pack()
        Sazka_hrace_1.pack()

    if Pocet_hracu>1:
        Okno_hrac_2.pack(side="top")
        Jmeno_hrac_2.pack(side="top")    
        Zobrazeni_karet_hrace_2.pack(side="left")
        Zobrazeni_skore_hrace_2.pack(side="left")
        Zobrazeni_rozpoctu_hrace_2.pack(side="left")
        Zobrazeni_sazky_hrce_2.pack(side="left")
        if Hraci[1].uroven==0:
            Sazka_hrace_2_napis.pack()
            Sazka_hrace_2.pack()

        if Pocet_hracu>2:
            Okno_hrac_3.pack(side="top")
            Jmeno_hrac_3.pack(side="top")    
            Zobrazeni_karet_hrace_3.pack(side="left")
            Zobrazeni_skore_hrace_3.pack(side="left")
            Zobrazeni_rozpoctu_hrace_3.pack(side="left")
            Zobrazeni_sazky_hrce_3.pack(side="left")
            if Hraci[2].uroven==0:
                Sazka_hrace_3_napis.pack()
                Sazka_hrace_3.pack()

            if Pocet_hracu>3:
                Okno_hrac_4.pack(side="top")
                Jmeno_hrac_4.pack(side="top")    
                Zobrazeni_karet_hrace_4.pack(side="left")
                Zobrazeni_skore_hrace_4.pack(side="left")
                Zobrazeni_rozpoctu_hrace_4.pack(side="left")
                Zobrazeni_sazky_hrce_4.pack(side="left")
                if Hraci[3].uroven==0:
                    Sazka_hrace_4_napis.pack()
                    Sazka_hrace_4.pack()

                if Pocet_hracu>4:
                    Okno_hrac_5.pack(side="top")
                    Jmeno_hrac_5.pack(side="top")    
                    Zobrazeni_karet_hrace_5.pack(side="left")
                    Zobrazeni_skore_hrace_5.pack(side="left")
                    Zobrazeni_rozpoctu_hrace_5.pack(side="left")
                    Zobrazeni_sazky_hrce_5.pack(side="left")
                    if Hraci[4].uroven==0:
                        Sazka_hrace_5_napis.pack()
                        Sazka_hrace_5.pack()

    if Jen_boti:
        PotvrditSazky()
    else:
        Potvrdit_sazky.place(relx=1.0, rely=1.0, anchor="se",x=-10, y=-10)

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

# Funcke rozdává karty a přepíše informace v rozhraní.

def Rozdej_karty():

    global Dealeruv_BlackJack
    global Dealerovo_skore

    Rozdavani_karet_napis.pack_forget()

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
        if hrac.skore==21:
            hrac.blackjack=True

    if Dealerovy_karty[0].hodnota+Dealerovy_karty[1].hodnota==21:
        Dealeruv_BlackJack=True
        Dealerovo_skore = 21

    Zobrazeni_dealerovych_karet.config(text="Karty : " + Dealerovy_karty[0].nazev()+ ", ?")
    Zobrazeni_dealerova_skore.config(text="Skóre: "+str(Dealerovy_karty[0].hodnota))

    for i in range (Pocet_hracu):
        if i == 0:
            Zobrazeni_karet_hrace_1.config(text="Karty: " + Hraci[0].karty[0].nazev() + ", " + Hraci[0].karty[1].nazev())
            Zobrazeni_skore_hrace_1.config(text="Skóre: "+str(Hraci[0].skore))
        if i == 1:
            Zobrazeni_karet_hrace_2.config(text="Karty: " + Hraci[1].karty[0].nazev() + ", " + Hraci[1].karty[1].nazev())
            Zobrazeni_skore_hrace_2.config(text="Skóre: "+str(Hraci[1].skore))
        if i == 2:
            Zobrazeni_karet_hrace_3.config(text="Karty: " + Hraci[2].karty[0].nazev() + ", " + Hraci[2].karty[1].nazev())
            Zobrazeni_skore_hrace_3.config(text="Skóre: "+str(Hraci[2].skore))
        if i == 3:
            Zobrazeni_karet_hrace_4.config(text="Karty: " + Hraci[3].karty[0].nazev() + ", " + Hraci[3].karty[1].nazev())
            Zobrazeni_skore_hrace_4.config(text="Skóre: "+str(Hraci[3].skore))
        if i == 4:
            Zobrazeni_karet_hrace_5.config(text="Karty: " + Hraci[4].karty[0].nazev() + ", " + Hraci[4].karty[1].nazev())
            Zobrazeni_skore_hrace_5.config(text="Skóre: "+str(Hraci[4].skore))

    if Dealerovy_karty[0].typ == "A":
        pojistovani()
    else:
        hrat.place(relx=1.0, rely=1.0, anchor="se",x=-10, y=-10)

def PotvrditSazky():

    global Pocet_hracu

    for i in range(1,Pocet_hracu+1):

        if i == 1:
            if Hraci[0].uroven==0:
                Hraci[0].sazka=Sazka_hrace_1.get()
            else:
                Hraci[0].sazka=random.randint(1,int(0.4*Hraci[0].rozpocet-1))
            Hraci[0].rozpocet-=Hraci[0].sazka
            Zobrazeni_sazky_hrce_1.config(text="Sázka: "+str(Hraci[0].sazka))
            Zobrazeni_rozpoctu_hrace_1.config(text="Rozpočet: "+str(Hraci[0].rozpocet))

        if i == 2:
            if Hraci[1].uroven==0:
                Hraci[1].sazka=Sazka_hrace_2.get()
            else:
                Hraci[1].sazka=random.randint(1,int(0.4*Hraci[1].rozpocet-1))
            Hraci[1].rozpocet-=Hraci[1].sazka
            Zobrazeni_sazky_hrce_2.config(text="Sázka: "+str(Hraci[1].sazka))
            Zobrazeni_rozpoctu_hrace_2.config(text="Rozpočet: "+str(Hraci[1].rozpocet))

        if i == 3:
            if Hraci[2].uroven==0:
                Hraci[2].sazka=Sazka_hrace_3.get()
            else:
                Hraci[2].sazka=random.randint(1,int(0.4*Hraci[2].rozpocet-1))
            Hraci[2].rozpocet-=Hraci[2].sazka
            Zobrazeni_sazky_hrce_3.config(text="Sázka: "+str(Hraci[2].sazka))
            Zobrazeni_rozpoctu_hrace_3.config(text="Rozpočet: "+str(Hraci[2].rozpocet))

        if i == 4:
            if Hraci[3].uroven==0:
                Hraci[3].sazka=Sazka_hrace_4.get()
            else:
                Hraci[3].sazka=random.randint(1,int(0.4*Hraci[3].rozpocet-1))
            Hraci[3].rozpocet-=Hraci[3].sazka
            Zobrazeni_sazky_hrce_4.config(text="Sázka: "+str(Hraci[3].sazka))
            Zobrazeni_rozpoctu_hrace_4.config(text="Rozpočet: "+str(Hraci[3].rozpocet))

        if i == 5:
            if Hraci[4].uroven==0:
                Hraci[4].sazka=Sazka_hrace_5.get()
            else:
                Hraci[4].sazka=random.randint(1,int(0.4*Hraci[4].rozpocet-1))
            Hraci[4].rozpocet-=Hraci[4].sazka
            Zobrazeni_sazky_hrce_5.config(text="Sázka: "+str(Hraci[4].sazka))
            Zobrazeni_rozpoctu_hrace_5.config(text="Rozpočet: "+str(Hraci[4].rozpocet))       

    Sazkovy_frame.pack_forget()
    Potvrdit_sazky.place_forget()

    Rozdavani_karet_napis.pack()
    Okno.after(3000, Rozdej_karty)

# Funkce pojišťování se volá v případě, že ve hře je hráč ovládaný manuálně. Funkce využívá booleanvar díky čemu se rychle získává údaj TRUE/FALSE z checkbuttonu.

def pojistovani():

    global Pojistovani_1
    global Pojistovani_2
    global Pojistovani_3
    global Pojistovani_4
    global Pojistovani_5
    global Pojisten_1
    global Pojisten_2
    global Pojisten_3
    global Pojisten_4
    global Pojisten_5
    global Pojistovaci_frame
    global Potvrzeni_pojisteni

    Pojistovaci_frame = tk.Frame(Okno,bg="#c5cf9b")
    Pojistovaci_frame.place(x=500,y=250)

    for i in range(Pocet_hracu):

        if i == 0:
            if Hraci[0].uroven==0:
                Pojisten_1 = tk.BooleanVar()
                Pojistovani_1 = tk.Checkbutton(Pojistovaci_frame,text="Chce se "+Hraci[0].jmeno+" pojistit?",variable=Pojisten_1,bg="#c5cf9b")
                Pojistovani_1.pack()         
        if i == 1:
            if Hraci[1].uroven==0:
                Pojisten_2 = tk.BooleanVar()
                Pojistovani_2 = tk.Checkbutton(Pojistovaci_frame,text="Chce se "+Hraci[1].jmeno+" pojistit?",variable=Pojisten_2,bg="#c5cf9b")
                Pojistovani_2.pack()  
        if i == 2:
            if Hraci[2].uroven==0:
                Pojisten_3 = tk.BooleanVar()                          
                Pojistovani_3 = tk.Checkbutton(Pojistovaci_frame,text="Chce se "+Hraci[2].jmeno+" pojistit?",variable=Pojisten_3,bg="#c5cf9b")
                Pojistovani_3.pack()  
        if i == 3:
            if Hraci[3].uroven==0:          
                Pojisten_4 = tk.BooleanVar()  
                Pojistovani_4 = tk.Checkbutton(Pojistovaci_frame,text="Chce se "+Hraci[3].jmeno+" pojistit?",variable=Pojisten_4,bg="#c5cf9b")
                Pojistovani_4.pack()  
        if i == 4:
            if Hraci[4].uroven==0:          
                Pojisten_5 = tk.BooleanVar()
                Pojistovani_5 = tk.Checkbutton(Pojistovaci_frame,text="Chce se "+Hraci[4].jmeno+" pojistit?",variable=Pojisten_5,bg="#c5cf9b")
                Pojistovani_5.pack()    
    
    if Jen_boti:
        vyhodnoceni_pojisteni()
    else:
        Potvrzeni_pojisteni = tk.Button(Okno, text="Pokračovat", command=vyhodnoceni_pojisteni, font=("Arial",10))
        Potvrzeni_pojisteni.place(relx=1.0, rely=1.0, anchor="se",x=-10, y=-10)

# Funkce vypíše, zda se hráči pojistili, či nikoliv. Opět se jedná o dlouhou funkci, ve které se většinou opakuje podobný text. Je to z důvodu rozdílných proměnných
# pro hráče a faktu, že počet hráčů je proměnlivý.

def vyhodnoceni_pojisteni():

    global zaznamy_pojistek
    global hrat

    zaznamy_pojistek = tk.Frame(Okno)
    zaznamy_pojistek.place(x=420,y=250)
    hrat.place(relx=1.0, rely=1.0, anchor="se",x=-10, y=-10)

    for i in range(Pocet_hracu):
        
        if i == 0:
            jmeno_pojistence_1 = tk.Label(zaznamy_pojistek,text=Hraci[0].jmeno,font=("arial",20))
            if Hraci[0].uroven!=0:
                Hraci[0].pojistka = Hraci[0].pojistovaci_funkce()
            else:
                Hraci[0].pojistka = Pojisten_1.get()
            jmeno_pojistence_1.pack()
            if Hraci[0].pojistka:
                jmeno_pojistence_1.config(text=Hraci[0].jmeno+" uzavírá pojistku!")
                jmeno_pojistence_1.config(fg="#24d129")
                Hraci[0].rozpocet-=Hraci[0].sazka//2
                Zobrazeni_rozpoctu_hrace_1.config(text="Rozpočet "+str(Hraci[0].rozpocet))
            else:
                jmeno_pojistence_1.config(text=Hraci[0].jmeno+" se nepojišťije!")
                jmeno_pojistence_1.config(fg="#b5262d")

    
        if i == 1:
            jmeno_pojistence_2 = tk.Label(zaznamy_pojistek,text=Hraci[1].jmeno,font=("arial",20))
            if Hraci[1].uroven!=0:
                Hraci[1].pojistka = Hraci[1].pojistovaci_funkce()
            else:
                Hraci[1].pojistka = Pojisten_2.get()
            jmeno_pojistence_2.pack()
            if Hraci[1].pojistka:
                jmeno_pojistence_2.config(text=Hraci[1].jmeno+" uzavírá pojistku!")
                jmeno_pojistence_2.config(fg="#24d129")
                Hraci[1].rozpocet-=Hraci[1].sazka//2
                Zobrazeni_rozpoctu_hrace_2.config(text="Rozpočet "+str(Hraci[1].rozpocet))
            else:
                jmeno_pojistence_2.config(text=Hraci[1].jmeno+" se nepojišťije!")
                jmeno_pojistence_2.config(fg="#b5262d")


        if i == 2:
            jmeno_pojistence_3 = tk.Label(zaznamy_pojistek,text=Hraci[2].jmeno,font=("arial",20))
            if Hraci[2].uroven!=0:
                Hraci[2].pojistka = Hraci[2].pojistovaci_funkce()
            else:
                Hraci[2].pojistka = Pojisten_3.get()
            jmeno_pojistence_3.pack()
            if Hraci[2].pojistka:
                jmeno_pojistence_3.config(text=Hraci[2].jmeno+" uzavírá pojistku!")
                jmeno_pojistence_3.config(fg="#24d129")
                Hraci[2].rozpocet-=Hraci[2].sazka//2
                Zobrazeni_rozpoctu_hrace_3.config(text="Rozpočet "+str(Hraci[2].rozpocet))
            else:
                jmeno_pojistence_3.config(text=Hraci[2].jmeno+" se nepojišťije!")
                jmeno_pojistence_3.config(fg="#b5262d")


        if i == 3:
            jmeno_pojistence_4 = tk.Label(zaznamy_pojistek,text=Hraci[3].jmeno,font=("arial",20))
            if Hraci[3].uroven!=0:
                Hraci[3].pojistka = Hraci[3].pojistovaci_funkce()
            else:
                Hraci[3].pojistka = Pojisten_4.get()
            jmeno_pojistence_4.pack()
            if Hraci[3].pojistka:
                jmeno_pojistence_4.config(text=Hraci[3].jmeno+" uzavírá pojistku!")
                jmeno_pojistence_4.config(fg="#24d129")
                Hraci[3].rozpocet-=Hraci[3].sazka//2
                Zobrazeni_rozpoctu_hrace_4.config(text="Rozpočet "+str(Hraci[3].rozpocet))
            else:
                jmeno_pojistence_4.config(text=Hraci[3].jmeno+" se nepojišťije!")
                jmeno_pojistence_4.config(fg="#b5262d")


        if i == 4:
            jmeno_pojistence_5 = tk.Label(zaznamy_pojistek,text=Hraci[4].jmeno,font=("arial",20))
            if Hraci[4].uroven!=0:
                Hraci[4].pojistka = Hraci[4].pojistovaci_funkce()
            else:
                Hraci[4].pojistka = Pojisten_5.get()
            jmeno_pojistence_5.pack()
            if Hraci[4].pojistka:
                jmeno_pojistence_5.config(text=Hraci[4].jmeno+" uzavírá pojistku!")
                jmeno_pojistence_5.config(fg="#24d129")
                Hraci[4].rozpocet-=Hraci[4].sazka//2
                Zobrazeni_rozpoctu_hrace_5.config(text="Rozpočet "+str(Hraci[4].rozpocet))
            else:
                jmeno_pojistence_5.config(text=Hraci[4].jmeno+" se nepojišťije!")
                jmeno_pojistence_5.config(fg="#b5262d")

    Pojistovaci_frame.place_forget()
    if not Jen_boti:
        Potvrzeni_pojisteni.place_forget()

def konvertor_balicku(balicek):
    string = ""
    for karta in balicek:
        string += karta.nazev() + ', '
    return string[:-2] 

# Následující funkce zavolají buďto tah bota nebo tah hráče. Zároveň zvýrazňují hráče, který je na tahu.

def hra_1():

    if Dealerovy_karty[0].typ=="A":
        zaznamy_pojistek.place_forget()
    hrat.place_forget()

    Okno_hrac_1.config(bg="#7aeffa")
    Jmeno_hrac_1.config(bg="#7aeffa")
    Zobrazeni_karet_hrace_1.config(bg="#7aeffa")
    Zobrazeni_sazky_hrce_1.config(bg="#7aeffa")
    Zobrazeni_rozpoctu_hrace_1.config(bg="#7aeffa")
    Zobrazeni_skore_hrace_1.config(bg="#7aeffa")

    if Hraci[0].blackjack:
        Ukazatel_BlackJacku.config(text=Hraci[0].jmeno+" má BLACKJACK!")
        Ukazatel_BlackJacku.pack()
        if Pocet_hracu>1:
            Zacit_tah_2.place(relx=1.0, rely=1.0, anchor="se",x=-10, y=-10)
        else:
            Zacit_dealeruv_tah.place(relx=1.0, rely=1.0, anchor="se",x=-10, y=-10)

    else:
        if Hraci[0].uroven!=0:
            tah_bota(Hraci[0], Zobrazeni_skore_hrace_1, Zobrazeni_sazky_hrce_1, Zobrazeni_rozpoctu_hrace_1, Zobrazeni_karet_hrace_1)
            if Pocet_hracu>1:
                Zacit_tah_2.place(relx=1.0, rely=1.0, anchor="se",x=-10, y=-10)
            else:
                Zacit_dealeruv_tah.place(relx=1.0, rely=1.0, anchor="se",x=-10, y=-10)
        else:
            tah_hrace(Hraci[0], Zobrazeni_skore_hrace_1, Zobrazeni_sazky_hrce_1, Zobrazeni_rozpoctu_hrace_1, Zobrazeni_karet_hrace_1)

def hra_2():

    Ukazatel_BlackJacku.pack_forget()
    Zacit_tah_2.place_forget()

    Okno_hrac_2.config(bg="#7aeffa")
    Jmeno_hrac_2.config(bg="#7aeffa")
    Zobrazeni_karet_hrace_2.config(bg="#7aeffa")
    Zobrazeni_sazky_hrce_2.config(bg="#7aeffa")
    Zobrazeni_rozpoctu_hrace_2.config(bg="#7aeffa")
    Zobrazeni_skore_hrace_2.config(bg="#7aeffa")

    Okno_hrac_1.config(bg="#eddd72")
    Jmeno_hrac_1.config(bg="#eddd72")
    Zobrazeni_karet_hrace_1.config(bg="#eddd72")
    Zobrazeni_sazky_hrce_1.config(bg="#eddd72")
    Zobrazeni_rozpoctu_hrace_1.config(bg="#eddd72")
    Zobrazeni_skore_hrace_1.config(bg="#eddd72")

    if Hraci[1].blackjack:
        Ukazatel_BlackJacku.config(text=Hraci[1].jmeno+" má BLACKJACK!")
        Ukazatel_BlackJacku.pack()
        if Pocet_hracu>2:
            Zacit_tah_3.place(relx=1.0, rely=1.0, anchor="se",x=-10, y=-10)
        else:
            Zacit_dealeruv_tah.place(relx=1.0, rely=1.0, anchor="se",x=-10, y=-10)

    else:
        if Hraci[1].uroven!=0:
            tah_bota(Hraci[1], Zobrazeni_skore_hrace_2, Zobrazeni_sazky_hrce_2, Zobrazeni_rozpoctu_hrace_2, Zobrazeni_karet_hrace_2)
            if Pocet_hracu>2:
                Zacit_tah_3.place(relx=1.0, rely=1.0, anchor="se",x=-10, y=-10)
            else:
                Zacit_dealeruv_tah.place(relx=1.0, rely=1.0, anchor="se",x=-10, y=-10)
        else:
            tah_hrace(Hraci[1], Zobrazeni_skore_hrace_2, Zobrazeni_sazky_hrce_2, Zobrazeni_rozpoctu_hrace_2, Zobrazeni_karet_hrace_2)

def hra_3():

    Ukazatel_BlackJacku.pack_forget()
    Zacit_tah_3.place_forget()

    Okno_hrac_3.config(bg="#7aeffa")
    Jmeno_hrac_3.config(bg="#7aeffa")
    Zobrazeni_karet_hrace_3.config(bg="#7aeffa")
    Zobrazeni_sazky_hrce_3.config(bg="#7aeffa")
    Zobrazeni_rozpoctu_hrace_3.config(bg="#7aeffa")
    Zobrazeni_skore_hrace_3.config(bg="#7aeffa")
    
    Okno_hrac_2.config(bg="#eddd72")
    Jmeno_hrac_2.config(bg="#eddd72")
    Zobrazeni_karet_hrace_2.config(bg="#eddd72")
    Zobrazeni_sazky_hrce_2.config(bg="#eddd72")
    Zobrazeni_rozpoctu_hrace_2.config(bg="#eddd72")
    Zobrazeni_skore_hrace_2.config(bg="#eddd72")

    if Hraci[2].blackjack:
        Ukazatel_BlackJacku.config(text=Hraci[2].jmeno+" má BLACKJACK!")
        Ukazatel_BlackJacku.pack()
        if Pocet_hracu>3:
            Zacit_tah_4.place(relx=1.0, rely=1.0, anchor="se",x=-10, y=-10)
        else:
            Zacit_dealeruv_tah.place(relx=1.0, rely=1.0, anchor="se",x=-10, y=-10)

    else:
        if Hraci[2].uroven!=0:
            tah_bota(Hraci[2], Zobrazeni_skore_hrace_3, Zobrazeni_sazky_hrce_3, Zobrazeni_rozpoctu_hrace_3, Zobrazeni_karet_hrace_3)
            if Pocet_hracu>3:
                Zacit_tah_4.place(relx=1.0, rely=1.0, anchor="se",x=-10, y=-10)
            else:
                Zacit_dealeruv_tah.place(relx=1.0, rely=1.0, anchor="se",x=-10, y=-10)
        else:
            tah_hrace(Hraci[2], Zobrazeni_skore_hrace_3, Zobrazeni_sazky_hrce_3, Zobrazeni_rozpoctu_hrace_3, Zobrazeni_karet_hrace_3)

def hra_4():

    Ukazatel_BlackJacku.pack_forget()
    Zacit_tah_4.place_forget()

    Okno_hrac_4.config(bg="#7aeffa")
    Jmeno_hrac_4.config(bg="#7aeffa")
    Zobrazeni_karet_hrace_4.config(bg="#7aeffa")
    Zobrazeni_sazky_hrce_4.config(bg="#7aeffa")
    Zobrazeni_rozpoctu_hrace_4.config(bg="#7aeffa")
    Zobrazeni_skore_hrace_4.config(bg="#7aeffa")

    Okno_hrac_3.config(bg="#eddd72")
    Jmeno_hrac_3.config(bg="#eddd72")
    Zobrazeni_karet_hrace_3.config(bg="#eddd72")
    Zobrazeni_sazky_hrce_3.config(bg="#eddd72")
    Zobrazeni_rozpoctu_hrace_3.config(bg="#eddd72")
    Zobrazeni_skore_hrace_3.config(bg="#eddd72")

    if Hraci[3].blackjack:
        Ukazatel_BlackJacku.config(text=Hraci[3].jmeno+" má BLACKJACK!")
        Ukazatel_BlackJacku.pack()
        if Pocet_hracu>4:
            Zacit_tah_5.place(relx=1.0, rely=1.0, anchor="se",x=-10, y=-10)
        else:
            Zacit_dealeruv_tah.place(relx=1.0, rely=1.0, anchor="se",x=-10, y=-10)

    else:
        if Hraci[3].uroven!=0:
            tah_bota(Hraci[3], Zobrazeni_skore_hrace_4, Zobrazeni_sazky_hrce_4, Zobrazeni_rozpoctu_hrace_4, Zobrazeni_karet_hrace_4)
            if Pocet_hracu>4:
                Zacit_tah_5.place(relx=1.0, rely=1.0, anchor="se",x=-10, y=-10)
            else:
                Zacit_dealeruv_tah.place(relx=1.0, rely=1.0, anchor="se",x=-10, y=-10)
        else:
            tah_hrace(Hraci[3], Zobrazeni_skore_hrace_4, Zobrazeni_sazky_hrce_4, Zobrazeni_rozpoctu_hrace_4, Zobrazeni_karet_hrace_4)

def hra_5():

    Ukazatel_BlackJacku.pack_forget()
    Zacit_tah_5.place_forget()

    Okno_hrac_5.config(bg="#7aeffa")
    Jmeno_hrac_5.config(bg="#7aeffa")
    Zobrazeni_karet_hrace_5.config(bg="#7aeffa")
    Zobrazeni_sazky_hrce_5.config(bg="#7aeffa")
    Zobrazeni_rozpoctu_hrace_5.config(bg="#7aeffa")
    Zobrazeni_skore_hrace_5.config(bg="#7aeffa")

    Okno_hrac_4.config(bg="#eddd72")
    Jmeno_hrac_4.config(bg="#eddd72")
    Zobrazeni_karet_hrace_4.config(bg="#eddd72")
    Zobrazeni_sazky_hrce_4.config(bg="#eddd72")
    Zobrazeni_rozpoctu_hrace_4.config(bg="#eddd72")
    Zobrazeni_skore_hrace_4.config(bg="#eddd72")

    if Hraci[4].blackjack:
        Ukazatel_BlackJacku.config(text=Hraci[4].jmeno+" má BLACKJACK!")
        Ukazatel_BlackJacku.pack()
        Zacit_dealeruv_tah.place(relx=1.0, rely=1.0, anchor="se",x=-10, y=-10)

    else:
        if Hraci[4].uroven!=0:
            tah_bota(Hraci[4], Zobrazeni_skore_hrace_5, Zobrazeni_sazky_hrce_5, Zobrazeni_rozpoctu_hrace_5, Zobrazeni_karet_hrace_5)
            Zacit_dealeruv_tah.place(relx=1.0, rely=1.0, anchor="se",x=-10, y=-10)
        else:
            tah_hrace(Hraci[4], Zobrazeni_skore_hrace_5, Zobrazeni_sazky_hrce_5, Zobrazeni_rozpoctu_hrace_5, Zobrazeni_karet_hrace_5)

# Funkce určí první tah dle Rozhodovaci_funkce_prvni_tah a dle něj následně pokračuje dle typů jednotlivých tahů. 

def tah_bota(hrac, ukazatel_skore, ukazatel_sazky, ukazatel_rozpoctu, ukazatel_karet):

    tah=hrac.Rozhodovaci_Funkce_Prvni_Tah(Dealerovy_karty[0].hodnota)

    if tah=="Split":

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

        for karta in hrac.SKarty2:
            if karta.typ=="A":
                hrac.S11E2+=1
        while hrac.SSkore2>21 and hrac.S11E2>0:
            hrac.SSkore2+=-10
            hrac.S11E2+=-1   
                   
        ukazatel_karet.config(text="Karty: "+hrac.SKarty1[0].nazev()+" "+hrac.SKarty1[1].nazev()+" | "+hrac.SKarty2[0].nazev()+", "+hrac.SKarty2[1].nazev())

        ukazatel_skore.config(text="Skóre: "+str(hrac.SSkore1)+" | "+str(hrac.SSkore2))
        if hrac.SSkore1!=21:    
            tah=Rozhodovaci_funkce(hrac.uroven,hrac.SSkore1,Dealerovy_karty[0].hodnota)
            while tah=="Hit":
                hrac.SKarty1.append(Hraci_balicek.Lizni_Kartu())
                ukazatel_karet.config(text="Karty: "+konvertor_balicku(hrac.SKarty1)+" | "+hrac.SKarty2[0].nazev()+", "+hrac.SKarty2[1].nazev())
                if hrac.SKarty1[-1].typ=="A":
                    hrac.S11E1+=1
                hrac.SSkore1=hrac.SSkore1+hrac.SKarty1[-1].hodnota
                while hrac.S11E1>0 and hrac.SSkore1>21:
                    hrac.S11E1+=-1
                    hrac.SSkore1+=-10
                ukazatel_skore.config(text="Skóre: "+str(hrac.SSkore1)+" | "+str(hrac.SSkore2))
                if hrac.SSkore1>21:
                    break
                tah=Rozhodovaci_funkce(hrac.uroven,hrac.SSkore1,Dealerovy_karty[0].hodnota)
        else:
            hrac.SBJ1=True

        ukazatel_skore.config(text="Skóre: "+str(hrac.SSkore1)+" | "+str(hrac.SSkore2))
        if hrac.SSkore2!=21:               
            tah=Rozhodovaci_funkce(hrac.uroven,hrac.SSkore2,Dealerovy_karty[0].hodnota)
            while tah=="Hit":
                hrac.SKarty2.append(Hraci_balicek.Lizni_Kartu())
                ukazatel_karet.config(text="Karty: "+konvertor_balicku(hrac.SKarty1)+", "+konvertor_balicku(hrac.SKarty2))
                if hrac.SKarty2[-1].typ=="A":
                    hrac.S11E2+=1
                hrac.SSkore2=hrac.SSkore2+hrac.SKarty2[-1].hodnota
                while hrac.S11E2>0 and hrac.SSkore2>21:
                    hrac.S11E2+=-1
                    hrac.SSkore2+=-10
                ukazatel_skore.config(text="Skóre: "+str(hrac.SSkore1)+" | "+str(hrac.SSkore2))
                if hrac.SSkore2>21:
                    break
                tah=Rozhodovaci_funkce(hrac.uroven,hrac.SSkore2,Dealerovy_karty[0].hodnota)
        else:
            hrac.SBJ2=True

    elif tah=="Double":
        hrac.rozpocet=hrac.rozpocet-hrac.sazka
        hrac.sazka=hrac.sazka*2
        ukazatel_sazky.config(text="Sázka: "+str(hrac.sazka))
        ukazatel_rozpoctu.config(text="Rozpočet: "+str(hrac.rozpocet))
        hrac.karty.append(Hraci_balicek.Lizni_Kartu())
        ukazatel_karet.config(text="Karty: "+konvertor_balicku(hrac.karty))
        hrac.skore=hrac.skore+hrac.karty[2].hodnota
        if hrac.karty[2].typ=="A":
            hrac.jedenactkova_esa+=1
        while hrac.skore>21 and hrac.jedenactkova_esa>0:
            hrac.skore+=-10
            hrac.jedenactkova_esa+=-1                        
        ukazatel_skore.config(text="Skóre: "+str(hrac.skore))

    else:
        while tah=="Hit":
            hrac.karty.append(Hraci_balicek.Lizni_Kartu())
            ukazatel_karet.config(text="Karty: "+konvertor_balicku(hrac.karty))
            if hrac.karty[-1].typ=="A":
                hrac.jedenactkova_esa+=1
            hrac.skore=hrac.skore+hrac.karty[-1].hodnota

# Zde je viděn příklad toho, kterak dochází k využívání proměnné jedenáctková esa.

            while hrac.jedenactkova_esa>0 and hrac.skore>21:
                hrac.jedenactkova_esa+=-1
                hrac.skore+=-10
            ukazatel_skore.config(text="Skóre: "+str(hrac.skore))
            if hrac.skore>21:
                break
            tah=Rozhodovaci_funkce(hrac.uroven,hrac.skore,Dealerovy_karty[0].hodnota)

# Funkce otevře tlačítka pro první tah, podle toho, které uživatel zmáčkne, tím směrem se hra bude vyvíjet.

def tah_hrace(Hrac, Ukazatel_skore, Ukazatel_sazky, Ukazatel_rozpoctu, Ukazatel_karet):

    global Prvni_hit_Tlacitko
    global Double_Tlacitko
    global Prvni_stand_Tlacitko
    global Split_Tlacitko

    Prvni_hit_Tlacitko = tk.Button(Frame_na_prvni_akci, text="HIT", command=lambda:Hit(Hrac, Ukazatel_karet, Ukazatel_skore), font=("Arial",10), bg="#80acbf")
    Prvni_stand_Tlacitko = tk.Button(Frame_na_prvni_akci, text="STAND", command=lambda:Stand(Hrac), font=("Arial",10), bg="#80acbf")
    Double_Tlacitko = tk.Button(Frame_na_prvni_akci, text="DOUBLE", command=lambda:Double(Hrac, Ukazatel_sazky, Ukazatel_rozpoctu, Ukazatel_karet, Ukazatel_skore), font=("Arial",10), bg="#80acbf")
    Split_Tlacitko = tk.Button(Frame_na_prvni_akci, text="SPLIT", command=lambda:Split(Hrac, Ukazatel_sazky, Ukazatel_rozpoctu, Ukazatel_karet, Ukazatel_skore), font=("Arial",10),  bg="#80acbf")

    Frame_na_prvni_akci.pack(side="bottom")
    Prvni_tah_napis.pack(side="top")
    Prvni_hit_Tlacitko.pack(side="left")
    Double_Tlacitko.pack(side="left")
    if Hrac.karty[0].hodnota==Hrac.karty[1].hodnota:
        Split_Tlacitko.pack(side="left")
    Prvni_stand_Tlacitko.pack(side="right")

def Double(hrac, ukazatel_sazky, ukazatel_rozpoctu, ukazatel_karet, ukazatel_skore):

    Frame_na_akci.pack_forget()
    Prvni_tah_napis.pack_forget
    Prvni_stand_Tlacitko.pack_forget()
    Prvni_hit_Tlacitko.pack_forget()
    Split_Tlacitko.pack_forget()
    Double_Tlacitko.pack_forget()

    hrac.rozpocet=hrac.rozpocet-hrac.sazka
    hrac.sazka=hrac.sazka*2
    ukazatel_sazky.config(text="Sázka: "+str(hrac.sazka))
    ukazatel_rozpoctu.config(text="Rozpočet: "+str(hrac.rozpocet))
    hrac.karty.append(Hraci_balicek.Lizni_Kartu())
    ukazatel_karet.config(text="Karty: "+konvertor_balicku(hrac.karty))
    hrac.skore=hrac.skore+hrac.karty[2].hodnota
    if hrac.karty[2].typ=="A":
        hrac.jedenactkova_esa+=1
    while hrac.skore>21 and hrac.jedenactkova_esa>0:
        hrac.skore+=-10
        hrac.jedenactkova_esa+=-1                        
    ukazatel_skore.config(text="Skóre: "+str(hrac.skore))
    Stand(hrac)

def Stand(hrac):

    global HS_otevreno

    Frame_na_prvni_akci.pack_forget()
    Prvni_tah_napis.pack_forget
    Prvni_stand_Tlacitko.pack_forget()
    Prvni_hit_Tlacitko.pack_forget()
    Split_Tlacitko.pack_forget()
    Double_Tlacitko.pack_forget()
    Frame_na_akci.pack_forget()
    Tah_napis.pack_forget()

    if HS_otevreno:
        Hit_tlacitko.pack_forget()
        Stand_tlacitko.pack_forget()
        HS_otevreno = False

    Index=Hraci.index(hrac)

    if Index+1==Pocet_hracu:
        Zacit_dealeruv_tah.place(relx=1.0, rely=1.0, anchor="se",x=-10, y=-10)
    else:
        if Index==0:
            Zacit_tah_2.place(relx=1.0, rely=1.0, anchor="se",x=-10, y=-10)
        elif Index==1:
            Zacit_tah_3.place(relx=1.0, rely=1.0, anchor="se",x=-10, y=-10)
        elif Index==2:
            Zacit_tah_4.place(relx=1.0, rely=1.0, anchor="se",x=-10, y=-10)
        else:
            Zacit_tah_5.place(relx=1.0, rely=1.0, anchor="se",x=-10, y=-10)

def Hit(hrac, ukazatel_karet, ukazatel_skore):

    global Hit_tlacitko
    global Stand_tlacitko
    global HS_otevreno

    Frame_na_prvni_akci.pack_forget()
    Prvni_tah_napis.pack_forget
    Prvni_stand_Tlacitko.pack_forget()
    Prvni_hit_Tlacitko.pack_forget()
    Split_Tlacitko.pack_forget()
    Double_Tlacitko.pack_forget()

    Frame_na_akci.pack(side="bottom")
    Tah_napis.pack(side="top")

    hrac.karty.append(Hraci_balicek.Lizni_Kartu())
    ukazatel_karet.config(text="Karty: "+konvertor_balicku(hrac.karty))
    if hrac.karty[-1].typ=="A":
        hrac.jedenactkova_esa+=1
    hrac.skore=hrac.skore+hrac.karty[-1].hodnota
    while hrac.jedenactkova_esa>0 and hrac.skore>21:
        hrac.jedenactkova_esa+=-1
        hrac.skore+=-10
    ukazatel_skore.config(text="Skóre: "+str(hrac.skore))
    if hrac.skore>21:
        Stand(hrac)
    else:
        if not HS_otevreno:
            Hit_tlacitko = tk.Button(Frame_na_akci, text="HIT", command=lambda:Hit(hrac, ukazatel_karet, ukazatel_skore), font=("Arial",10), bg="#80acbf")
            Stand_tlacitko = tk.Button(Frame_na_akci, text="STAND", command=lambda:Stand(hrac), font=("Arial",10), bg="#80acbf")     
            Hit_tlacitko.pack(side="left")        
            Stand_tlacitko.pack(side="right")
            HS_otevreno = True

def Split(hrac, ukazatel_sazky, ukazatel_rozpoctu, ukazatel_karet, ukazatel_skore):

    Frame_na_prvni_akci.pack_forget()
    Prvni_tah_napis.pack_forget
    Prvni_stand_Tlacitko.pack_forget()
    Prvni_hit_Tlacitko.pack_forget()
    Split_Tlacitko.pack_forget()
    Double_Tlacitko.pack_forget()

    hrac.split=True
    hrac.rozpocet=hrac.rozpocet-hrac.sazka
    ukazatel_sazky.config(text="Sázka: "+str(hrac.sazka))
    ukazatel_rozpoctu.config(text="Rozpočet: "+str(hrac.rozpocet))
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
    for karta in hrac.SKarty2:
        if karta.typ=="A":
            hrac.S11E2+=1
    while hrac.SSkore2>21 and hrac.S11E2>0:
        hrac.SSkore2+=-10
        hrac.S11E2+=-1   
               
    ukazatel_karet.config(text="Karty: "+hrac.SKarty1[0].nazev()+" "+hrac.SKarty1[1].nazev()+" | "+hrac.SKarty2[0].nazev()+", "+hrac.SKarty2[1].nazev())
    ukazatel_skore.config(text="Skóre: "+str(hrac.SSkore1)+" | "+str(hrac.SSkore2))
    if hrac.SSkore1!=21:
        Frame_na_prvni_split_akce.pack(side="bottom")
        Prvni_split_napis.pack(side="top")
        Hit_S1 = tk.Button(Frame_na_prvni_split_akce, text="HIT", command=lambda:Split_hit_1(hrac, ukazatel_karet, ukazatel_skore), font=("Arial",10), bg="#80acbf")
        Stand_S1 = tk.Button(Frame_na_prvni_split_akce, text="STAND", command=lambda:Split_stand_1(hrac, ukazatel_karet, ukazatel_skore), font=("Arial",10), bg="#80acbf")
        Hit_S1.pack(side="left")
        Stand_S1.pack(side="right")
    else:
        hrac.SBJ1=True
        Split_stand_1(hrac, ukazatel_karet, ukazatel_skore)
    ukazatel_skore.config(text="Skóre: "+str(hrac.SSkore1)+" | "+str(hrac.SSkore2))

def Split_hit_1(hrac, ukazatel_karet, ukazatel_skore):

    hrac.SKarty1.append(Hraci_balicek.Lizni_Kartu())
    ukazatel_karet.config(text="Karty: "+konvertor_balicku(hrac.SKarty1)+" | "+hrac.SKarty2[0].nazev()+", "+hrac.SKarty2[1].nazev())
    if hrac.SKarty1[-1].typ=="A":
        hrac.S11E1+=1
    hrac.SSkore1=hrac.SSkore1+hrac.SKarty1[-1].hodnota
    while hrac.S11E1>0 and hrac.SSkore1>21:
        hrac.S11E1+=-1
        hrac.SSkore1+=-10
    ukazatel_skore.config(text="Skóre: "+str(hrac.SSkore1)+" | "+str(hrac.SSkore2))
    if hrac.SSkore1>21:
        Split_stand_1(hrac, ukazatel_karet, ukazatel_skore)
    
def Split_stand_1(hrac, ukazatel_karet, ukazatel_skore):

    Frame_na_prvni_split_akce.pack_forget()

    if hrac.SSkore2!=21:
        Frame_na_druhy_split_akce.pack(side="bottom")
        Druhy_split_napis.pack(side="top")
        Hit_S2 = tk.Button(Frame_na_druhy_split_akce, text="HIT", command=lambda:Split_hit_2(hrac, ukazatel_karet, ukazatel_skore), font=("Arial",10), bg="#80acbf")
        Stand_S2 = tk.Button(Frame_na_druhy_split_akce, text="STAND", command=lambda:Split_stand_2(hrac), font=("Arial",10), bg="#80acbf")
        Hit_S2.pack(side="left")
        Stand_S2.pack(side="right")
    else:
        hrac.SBJ2=True
        Split_stand_2(hrac)

def Split_hit_2(hrac, ukazatel_karet, ukazatel_skore):

    hrac.SKarty2.append(Hraci_balicek.Lizni_Kartu())
    ukazatel_karet.config(text="Karty: "+konvertor_balicku(hrac.SKarty1)+", "+konvertor_balicku(hrac.SKarty2))
    if hrac.SKarty2[-1].typ=="A":
        hrac.S11E2+=1
    hrac.SSkore2=hrac.SSkore2+hrac.SKarty2[-1].hodnota
    while hrac.S11E2>0 and hrac.SSkore2>21:
        hrac.S11E2+=-1
        hrac.SSkore2+=-10
    ukazatel_skore.config(text="Skóre: "+str(hrac.SSkore1)+" | "+str(hrac.SSkore2))
    if hrac.SSkore2>21:
        Split_stand_2(hrac)

def Split_stand_2(hrac):

    Frame_na_druhy_split_akce.pack_forget()
    Stand(hrac)

# Funkce ukazuje konečné zisky hráčů. 

def ukazka_vyhodnoceni():

    global vysledky
    global vysledky_1
    global vysledky_2
    global vysledky_3
    global vysledky_4
    global vysledky_5

    vysledky = tk.Frame(Okno)
    vysledky.place(x=420,y=250)
    Spustit_vyhodnocovani.place_forget()
    Spustit_zaverecku.place(relx=1.0, rely=1.0, anchor="se",x=-10, y=-10)
    Ukazatel_BlackJacku.pack_forget()

    for i in range(Pocet_hracu):
        
        if i == 0:
            vysledky_1 = tk.Label(vysledky,text=Hraci[0].jmeno,font=("arial",20))
            vysledky_1.pack()    
        if i == 1:
            vysledky_2 = tk.Label(vysledky,text=Hraci[1].jmeno,font=("arial",20))
            vysledky_2.pack()
        if i == 2:
            vysledky_3 = tk.Label(vysledky,text=Hraci[2].jmeno,font=("arial",20))
            vysledky_3.pack()
        if i == 3:
            vysledky_4 = tk.Label(vysledky,text=Hraci[3].jmeno,font=("arial",20))
            vysledky_4.pack()
        if i == 4:
            vysledky_5 = tk.Label(vysledky,text=Hraci[4].jmeno,font=("arial",20))
            vysledky_5.pack()

    for hrac in Hraci:
        i=Hraci.index(hrac)
        vyhra=0
        vyhra1=0
        vyhra2=0

        if hrac.split:
            vyhra1=vyhodnoceni(hrac.SSkore1,Dealerovo_skore,hrac.sazka,hrac.pojistka,hrac.SBJ1,Dealeruv_BlackJack,hrac.jmeno)
            vyhra2=vyhodnoceni(hrac.SSkore2,Dealerovo_skore,hrac.sazka,hrac.pojistka,hrac.SBJ2,Dealeruv_BlackJack,hrac.jmeno)
            vyhra=vyhra1+vyhra2              
        else:
            vyhra=vyhodnoceni(hrac.skore,Dealerovo_skore,hrac.sazka,hrac.pojistka,hrac.blackjack,Dealeruv_BlackJack,hrac.jmeno)

        hrac.rozpocet+=vyhra
        if i == 0:
            vysledky_1.config(text=Hraci[0].jmeno+" získává "+str(vyhra)+" korun!")
            Zobrazeni_rozpoctu_hrace_1.config(text="Rozpočet: "+str(Hraci[0].rozpocet))        
        elif i == 1:
            vysledky_2.config(text=Hraci[1].jmeno+" získává "+str(vyhra)+" korun!")
            Zobrazeni_rozpoctu_hrace_2.config(text="Rozpočet: "+str(Hraci[1].rozpocet))
        elif i == 2:
            vysledky_3.config(text=Hraci[2].jmeno+" získává "+str(vyhra)+" korun!")
            Zobrazeni_rozpoctu_hrace_3.config(text="Rozpočet: "+str(Hraci[2].rozpocet))
        elif i == 3:
            vysledky_4.config(text=Hraci[3].jmeno+" získává "+str(vyhra)+" korun!")
            Zobrazeni_rozpoctu_hrace_4.config(text="Rozpočet: "+str(Hraci[3].rozpocet))
        elif i == 4:
            vysledky_5.config(text=Hraci[4].jmeno+" získává "+str(vyhra)+" korun!")
            Zobrazeni_rozpoctu_hrace_5.config(text="Rozpočet: "+str(Hraci[4].rozpocet))

def zaverecka():

    global zkrachovale_existence
    global Pocet_hracu

    vysledky.place_forget()    
     
    Spustit_zaverecku.place_forget()
    zkrachovale_existence=[]

    for i in range(Pocet_hracu):
        if i == 0:
            Okno_hrac_1.pack_forget()
            vysledky_1.pack_forget()
        if i == 1:
            Okno_hrac_2.pack_forget()
            vysledky_2.pack_forget()
        if i == 2:
            Okno_hrac_3.pack_forget()
            vysledky_3.pack_forget()
        if i == 3:
            Okno_hrac_4.pack_forget()
            vysledky_4.pack_forget()
        if i == 4:
            Okno_hrac_5.pack_forget()
            vysledky_5.pack_forget()

    Dealerovo_okno.pack_forget()
    Okno_hracu.pack_forget()

    for hrac in Hraci:
        if hrac.rozpocet<100:
            zkrachovale_existence.append(hrac)

    for hrac in zkrachovale_existence:
        Hraci.remove(hrac)
    
    Pocet_hracu-=len(zkrachovale_existence)

    if len(zkrachovale_existence)!=0:
        ukaz_zkrachovale()

    if Pocet_hracu!=0:
        Spustit_novou_hru.pack()
        Spustit_novou_hru_napis.pack()
        Fakt_spustit_novou_hru.pack(side="left")
        Nespustit_novou_hru.pack(side="right") 
    else:
        Konec()  

# Vyyskakovací okno informujíce o krachu. V závislosti na počtu krachujících se mění text.

def ukaz_zkrachovale():

    oznameni = tk.Toplevel(Okno)
    oznameni.title("Oznámení o krachu hráče")
    oznameni.iconphoto(True, ikona)
    oznameni.geometry("300x150")
    
    Zkrachovani_hraci=" a ".join(map(lambda x: x.jmeno, zkrachovale_existence))

    if Pocet_hracu==0:
        napis = tk.Label(oznameni, text=Zkrachovani_hraci+" končí, což znamená, že již zkrachovali všichni hráči. :-(")        
    elif len(zkrachovale_existence)==1:
        napis = tk.Label(oznameni, text=Zkrachovani_hraci+" krachuje, takže končí hru. :-(")
    else:
        napis = tk.Label(oznameni, text=Zkrachovani_hraci+" krachují, takže končí hru. :-(")
    
    napis.pack(pady=20)
    
    zavrit_oznameni = tk.Button(oznameni, text="Zavřít", command=oznameni.destroy)
    zavrit_oznameni.pack()

def Konec():
    if Pocet_hracu!=0:
        Spustit_novou_hru.pack_forget()
        Spustit_novou_hru_napis.pack_forget()
        Fakt_spustit_novou_hru.pack_forget()
        Nespustit_novou_hru.pack_forget()
    Nadpis.pack_forget()
    Konecne_pozadi.pack()
    Okno.after(5000,sys.exit)

#Základní a nezbytné proměnné a množina jmen pro boty.

Pocet_hracu=0
Pocet_balicku=0
Rozpocet=0
Hraci_balicek=Balicek()
Hraci=[]

Jmena={"Adam", "Alexandr", "Anna", "Augustýn", "Barbora", "Bernard", "Bertrúda", "Bohuslava", "Bonifác", "Bořivoj",
      "Chrudoš", "Celestýna", "Daniel", "David", "Denis", "Eliška", "Esmeralda" "Filip", "František", "Horymír",
      "Jana", "Jan", "Jiří", "Jiřina", "Josefína", "Karel", "Karolína", "Kazimír", "Klára", "Kryštof", "Kunhuta",
      "Ladislav", "Lukáš", "Luboš", "Marek", "Mirek", "Norbert", "Ondřej", "Oliver", "Otakar", "Pankrác",
      "Petr", "Prokop", "Přemysl", "Roman", "Řehoř", "Sebastián", "Servác", "Soňa", "Spytihněv", "Šimon", 
      "Štěpán", "Tadeáš", "Thea", "Theodor", "Tomáš", "Vavřinec", "Věnceslav", "Vojta", "Zuzana", "Žaneta"} 

# Vytvoření hlavního okna, včetně ikony a titulu.

Okno = tk.Tk()
ikona=tk.PhotoImage(file="Ikona.png")
Okno.title("BlackJack")
Okno.iconphoto(True, ikona)
Okno.geometry("1020x560")

Urovne=["Manuální ovládání","Opilec","Začátečník","Pokročilý","Profesionál"]

#Widgety z prvního obrazu. Label nadpis zůstává po celou dobu hry. Dochází rovnou i k otevření widgetů.

Nadpis=tk.Label(Okno,text="BLACKJACK",font=("Arial",40,"bold"),fg="#c94024",bg="black",relief="raised",bd=10)
Nadpis.pack()

Text_ZadejtePocetHracu = tk.Label(Okno, text="Počet hráčů",font=("Arial",15))
Text_ZadejtePocetHracu.pack()

Posuvnik_ZadejtePocetHracu = tk.Scale(Okno, from_=1, to=5, orient="horizontal", length=200, sliderlength=20, showvalue=True)
Posuvnik_ZadejtePocetHracu.pack()

Text_ZadejtePocetBalicku = tk.Label(Okno, text="Počet balíčků",font=("Arial",15))
Text_ZadejtePocetBalicku.pack()

Posuvnik_ZadejtePocetBalicku = tk.Scale(Okno, from_=1, to=8, orient="horizontal", length=200, sliderlength=20, showvalue=True)
Posuvnik_ZadejtePocetBalicku.pack()

Text_ZadejteRozpocet = tk.Label(Okno, text="Počáteční rozpočet",font=("Arial",15))
Text_ZadejteRozpocet.pack()

#Kontrolka na rozpočet, která kontroluje zda není zadáván příliš vysoký rozpočet.

Kontrolka = Okno.register(Kontrala_rozpoctu)
Nastaveni_rozpoctu = tk.Entry(Okno, validate="key", validatecommand=(Kontrolka, "%P"), width=8, justify="center")
Nastaveni_rozpoctu.pack()

Potvrdit_zakladni_vstup = tk.Button(Okno, text="Pokračovat", command=Potvrdit_zaklad, font=("Arial",10))
Potvrdit_zakladni_vstup.place(relx=1.0, rely=1.0, anchor="se",x=-10, y=-10)

Spatny_Rozpocet = tk.Label(Okno, text="Rozpočet musí být minimálně 100", font=("Arial",12),fg="red")

Zadavani_urovne_nadpis = tk.Label(Okno, text="Nastavte úroveň hráčů", font=("Arial",15),fg="#085c25", pady="15")

# Vytvoření framu, ve kterých uživatel vybírá úroveň hráčů. Včetně labelů do kterých se hodnota přenáší pomocí funkce stringvar()

Frame_na_urovne=tk.Frame(Okno)
Frame_urovne_1=tk.Frame(Frame_na_urovne)
Frame_urovne_2=tk.Frame(Frame_na_urovne)
Frame_urovne_3=tk.Frame(Frame_na_urovne)
Frame_urovne_4=tk.Frame(Frame_na_urovne)
Frame_urovne_5=tk.Frame(Frame_na_urovne)

Uroven_prvniho_hrace_nadpis = tk.Label(Frame_urovne_1, text="HRÁČ 1", font=("Arial",10))
Uroven_druheho_hrace_nadpis = tk.Label(Frame_urovne_2, text="HRÁČ 2", font=("Arial",10))
Uroven_tretiho_hrace_nadpis = tk.Label(Frame_urovne_3, text="HRÁČ 3", font=("Arial",10))
Uroven_ctvrteho_hrace_nadpis = tk.Label(Frame_urovne_4, text="HRÁČ 4", font=("Arial",10))
Uroven_pateho_hrace_nadpis = tk.Label(Frame_urovne_5, text="HRÁČ 5", font=("Arial",10))

Uroven_prvniho_hrace_vyber = tk.Listbox(Frame_urovne_1,selectmode=tk.SINGLE)
Uroven_druheho_hrace_vyber = tk.Listbox(Frame_urovne_2,selectmode=tk.SINGLE)
Uroven_tretiho_hrace_vyber = tk.Listbox(Frame_urovne_3,selectmode=tk.SINGLE)
Uroven_ctvrteho_hrace_vyber = tk.Listbox(Frame_urovne_4,selectmode=tk.SINGLE)
Uroven_pateho_hrace_vyber = tk.Listbox(Frame_urovne_5,selectmode=tk.SINGLE)

Spatne_urovne = tk.Label(Okno, text="MUSÍTE NASTAVIT ÚROVEŇ U VŠECH HRÁČŮ!", font=("Arial",12),fg="red")

Uroven_pro_1 = tk.StringVar()
Uroven_pro_2 = tk.StringVar()
Uroven_pro_3 = tk.StringVar()
Uroven_pro_4 = tk.StringVar()
Uroven_pro_5 = tk.StringVar()

Vyber_prvni_urovne = tk.Label(Frame_urovne_1, textvariable=Uroven_pro_1)
Vyber_druhe_urovne = tk.Label(Frame_urovne_2, textvariable=Uroven_pro_2)
Vyber_treti_urovne = tk.Label(Frame_urovne_3, textvariable=Uroven_pro_3)
Vyber_ctvrte_urovne = tk.Label(Frame_urovne_4, textvariable=Uroven_pro_4)
Vyber_pate_urovne = tk.Label(Frame_urovne_5, textvariable=Uroven_pro_5)

Uroven_prvniho_hrace_vyber.bind("<<ListboxSelect>>", Vypsani_urovne_1)
Vypsani_urovne_1(None)
Uroven_druheho_hrace_vyber.bind("<<ListboxSelect>>", Vypsani_urovne_2)
Vypsani_urovne_2(None)
Uroven_tretiho_hrace_vyber.bind("<<ListboxSelect>>", Vypsani_urovne_3)
Vypsani_urovne_3(None)
Uroven_ctvrteho_hrace_vyber.bind("<<ListboxSelect>>", Vypsani_urovne_4)
Vypsani_urovne_4(None)
Uroven_pateho_hrace_vyber.bind("<<ListboxSelect>>", Vypsani_urovne_5)
Vypsani_urovne_5(None)

Zadani_jmena_1 = tk.Entry(Frame_urovne_1,justify="center")
Zadani_jmena_2 = tk.Entry(Frame_urovne_2,justify="center")
Zadani_jmena_3 = tk.Entry(Frame_urovne_3,justify="center")
Zadani_jmena_4 = tk.Entry(Frame_urovne_4,justify="center")
Zadani_jmena_5 = tk.Entry(Frame_urovne_5,justify="center")

Uroven_prvniho_hrace_vyber.config(height=Uroven_prvniho_hrace_vyber.size())
Uroven_druheho_hrace_vyber.config(height=Uroven_druheho_hrace_vyber.size())
Uroven_tretiho_hrace_vyber.config(height=Uroven_tretiho_hrace_vyber.size())
Uroven_ctvrteho_hrace_vyber.config(height=Uroven_ctvrteho_hrace_vyber.size())
Uroven_pateho_hrace_vyber.config(height=Uroven_pateho_hrace_vyber.size())

# Inicializace některých widgetů, primárně tlačítek na pokračování.

Potvrzeni_urovni = tk.Button(Okno, text="Pokračovat", command=Kontrola_urovni, font=("Arial",10))

Rozdavani_karet_napis = tk.Label(Okno, text="Rozdávání karet", font=("Arial",20,),fg="red")

Ukazatel_BlackJacku = tk.Label(Okno, text="BLACKJACK!", font=("Arial", 30, "bold"), fg="#0fdb1d",)

hrat = tk.Button(Okno, text="Pokračovat na tah prvního hráče", command=hra_1, font=("Arial",10))
Zacit_tah_2 = tk.Button(Okno, text="Pokračovat na tah druhého hráče", font=("Arial",10), command=hra_2)
Zacit_tah_3 = tk.Button(Okno, text="Pokračovat na tah třetho hráče", font=("Arial",10), command=hra_3)
Zacit_tah_4 = tk.Button(Okno, text="Pokračovat na tah čtvrtého hráče", font=("Arial",10), command=hra_4)
Zacit_tah_5 = tk.Button(Okno, text="Pokračovat na tah pátého hráče", font=("Arial",10), command=hra_5)
Zacit_dealeruv_tah = tk.Button(Okno, text="Pokračovat na dealerův tah", font=("Arial",10), command=Dealeruv_tah)

Spustit_vyhodnocovani = tk.Button(Okno, text="Pokračovat", font=("Arial",10), command=ukazka_vyhodnoceni)

Spustit_zaverecku = tk.Button(Okno, text="Pokračovat", font=("Arial",10), command=zaverecka)

Spustit_novou_hru = tk.Frame(Okno)
Spustit_novou_hru_napis = tk.Label(Spustit_novou_hru, text="Chceš dát další kolo?", font=("Arial",20))
Fakt_spustit_novou_hru = tk.Button(Spustit_novou_hru, text="ANO", command=Zacatek_kola)
Nespustit_novou_hru = tk.Button(Spustit_novou_hru, text="NE", command=Konec)

Frame_na_prvni_akci = tk.Frame(Okno, bg="#f2acc3")
Prvni_tah_napis = tk.Label(Frame_na_prvni_akci, text="Zvolte první tah!", font=("Arial",12), bg="#f2acc3")

Frame_na_akci = tk.Frame(Okno, bg="#f2acc3")
Tah_napis = tk.Label(Frame_na_akci, text="Zahrajte tah!", font=("Arial",12), bg="#f2acc3")

Frame_na_prvni_split_akce = tk.Frame(Okno, bg="#f2acc3")
Prvni_split_napis = tk.Label(Frame_na_prvni_split_akce, bg="#f2acc3", text="Hraješ s první várkou.", font=("Arial",12))

Frame_na_druhy_split_akce = tk.Frame(Okno, bg="#f2acc3")
Druhy_split_napis = tk.Label(Frame_na_druhy_split_akce, bg="#f2acc3", text="Hraješ s druhou várkou.", font=("Arial",12))

HS_otevreno = False

Pozadi_konec = tk.PhotoImage(file="konec.png")

Konecne_pozadi = tk.Label(Okno, image=Pozadi_konec)

# Přidání položek do listboxů, ve kterých uživatel vybírá úroveň.

for i in range(5):
    Uroven_prvniho_hrace_vyber.insert(i+1,Urovne[i])
    Uroven_druheho_hrace_vyber.insert(i+1,Urovne[i])
    Uroven_tretiho_hrace_vyber.insert(i+1,Urovne[i])
    Uroven_ctvrteho_hrace_vyber.insert(i+1,Urovne[i])
    Uroven_pateho_hrace_vyber.insert(i+1,Urovne[i])

Okno.mainloop()       