# Dokumentace kódu

Hra běží buďto v konzolové verzi nebo ve verzi s rozhraním. Obě dvě části hry mají stejné hlavní mechaniky. Liší se pouze v zobrazování a posunu na další kroky. Proto technická dokumentace je vysvětlena
primárně na verzi s rozhraním a následně dovysvětlena pro konzolovou variantu. Dokud nebude řečeno jinak bude se dokumentace věnovat výhradně verzi s rozhraním. V této dokumentaci je funkčnost programu rozebrána
jen částečně, zbytek je dovysvětlen poznámkami v samotném kódu.

Hra běží pomocí knihovny Tkinter v okně s názvem "Okno". Hra běží primárně pomocí funkcí, které se volají zmáčknutím tlačítek. Celkově jsou v kódu tři třídy a 38 funkcí (v textové verzi tři třídy a tři funkce). 
Vysoký počet funkcí je primárně z důvodu využívání knihovny Tkinter. Některé funkce si jsou velmi podobné proto jejich funkčnost bude vysvětlena dohromady.

## Třídy

Jak již bylo zmíněno. Kód obsahuje tři třídy. Každá z nich nám definuje některý důležitý aspekt hry. 

### Karta

Objekt třídy karta obsahuje tři parametry. Údaj o barvě, typu a hodnotě. A funkci "nazev", tato funkce slouží k vypsání názvu kartu.

### Balicek

Třída balíček obsahuje pouze parametr self, který odkazuje na seznam. Do tohotu seznamu jsou pomocí několika for cyklů přidány karty (textová verze využívá namísto toho 52 vytvořených objektů, které jsou postupně
přidávány). Toto přídání probíhá pomocí funkce "Vytvor_novy". Tato funkce se odkáže i na funkci "Zamichat", která balíček náhodně zamíchá. Balíček obsahuje ještě funkci "Lizni_kartu", která vezme poslední kartu v
balíčku a provede s ní požadovanou akci.

### Hrac

Třída hráč obsahuje kromě atributu self ještě osmnáct dalších atributů. Ukazující jméno, úroveň, rozpočet, aktuální výšši sázky, karty, údaj o tom, zda hráč má, či nemá, BlackJack, údaj o tom, zda je hráč pojištěn.
Počet jedenáctkových es (vysvětlení níže), aktuální skóre hráčových karet, údaj o tom, zda hráč zahrál split, či nikoliv a atributy sazka, skore, karty, jedenáctková esa pro obě várky při splitu.

Atribut jedenáctkových es slouží k zaznamenávání toho, kolik es v rukou hráče má hra brát s hodnotou 11. Pokud hráči přijde do rukou eso, tento atribut se zvedne o jedna. Pokud hráčovo skóre překročí 21, hra se
koukne zda hráč má nějaké eso s hodnotou jedenáct a pokud ano, tak skóre sníží o deset a počet jedenáctkových es o jedno.

Třída obsahuje ještě dvě funkce. Rozhodovací funkci pro první tah, která slouží u botů k určení prvního tahu (v případě textové verze si v ní i hráč volí svůj tah) a pojišťovací funkci, která slouží u botů (u
textové verze opět i u o hráčem ovládaných hráčů) k rozhodnutí o tom, zda se pojistit, či nikoliv.

## Funkce

Nyní stručně popíšu fungování jednotlivých funkcí v kódu. První tři jsou společné pro digitální i konzolovou podobu. Zbytek se věnuje pouze konzolové verzi. Kromě prvních tří jsou funkce seřazeny tak, jak jsou 
postupně napsány v kódu. Funkce jsou zde většinou napsány v pořadí, ve kterém jsou volány, nicméně to neplatí vždy. Například funkce potvrdit_sazky je volána před funkcí rozdej_karty.

### Rozhodovací funkce

Rozhodovací funkce slouží k rozhodnutí dalšího postupu u botů (v případě textové verze i u hráčem ovládaných postav). Bere v potaz hráčovo skóre a Dealerovu odkrytou kartu.

### Dealerův tah

Během dealerova tahu si dealer líže kartu do chvíle, dokud jeho skóre nedosáhne hodnoty sedmnáct. 

### Vyhodnoceni

Funkce vyhodnocení bere údaje o skóre hráče a dealera, údaje o tom, zda mají BlackJack a o tom, zda hráč byl pojištěn a výšši hráčovi sázky. Z těchto údajů po té určí, zda a případně kolik peněz hráč vyhrál.

### Kontrola rozpočtu

Funkce znemožňujíc uživateli zadat počáteční rozpočet vyšší než jeden milion korun. Příliš vysoký rozpočet by mohl způsobovat problémy při hraní a zobrazování.

### Nastaveni_hracu_zobrazit

Tato funkce otevírá okno s nastavováním úrovní hráčů.

### Potvrdit_zaklad

Funkce zavře okno se základními informacemi (počet hráčů a balíčků a rozpočet) a nastaví tyto hodnoty do patřičných proměnných

### Vypsani_urovne

Pět funkcí, které v případě, že hráč zaškrtne u některého hráče manuální ovládání otevřou kolonku pro zadání jména. Každá funkce pro jednoho hráče u stolu.

### Kontrola_urovni

Funkce kontroluje, zda všem hráčům byla nastavena úroveň

### Potvrdit_urovne

Tato funkce představuje důležitý krok. Vytvoří zde totiž třídy hráčů dle zadaných požadavků uživatele, podle úrovní a jména a přidá je do listu Hraci. Botům je náhodně vybráno jméno z množiny jmen. 
Pokud uživatel nezadá žádné jméno některému hráči s manuálním ovládáním je nastaveno jméno Ignotus Primus/Secundus/Tertius/Quartus/Quintus, dle pořadí hráče u stolu. Jedná se o malý easter egg. 
Slovo ignotus totiž v překladu do češtiny znamená neznámý. Druhá část jména pak označuje řadovou číslovku.

### Konvertor_urovni

Funkce, která převede textové znění úrovně na číselné.

### Zacatek_kola

Funkce nastaví základní rozhraní obrazovky. A umožňuje uživateli zadávat sázky.

### Rozdej_karty

Funkce, která všem hráčům a dealerovy rozdá karty. Jako jednou ze dvou funkcí se spouští se zpožděním pro vytvoření efektu, že probíhá rozdávání.

### Potvrdit_sazky

Funkce, která přiřadí hráčům jejich vsazenou částku. Botům ji stanoví náhodně.

### Pojistovani

Funkce, která otevře rozhraní, ve kterém se hráči můžou pojistit.

### Vyhodnoceni_pojisteni

Funkce, která hráčům nastaví zda jsou pojištěni, či nikoliv. U botů navíc zavolá self.pojistovaci_funkce, která za ně rozhodne, zda se mají pojistit, či nikoliv.

### Konvertor_balicku

Pomocná funkce, která dostane balíček karet v podobě listu karet a převede ho na string názvů karet.

### Hra

Pět funkcí, každá pro jednoho hráče u stolu. Funkce znázorní, který hráč je na tahu a podle toho, zda se jedná o bota zavolá buď tah_bota nebo tah_hrace. Po konci tahu každého hráče se přechází na tah dalšího
hráče nebo v případě posledního hráče na tah dealera.

### Tah_bota

Tato funkce simuluje celý tah bota. Volá rozhodovací funkce a dle jejich výsledků rozhoduje v dalším postupu.

### Tah_hrace 

Tato funkce připraví zákldní rozhraní pro tah uživatelem ovládaného hráče. Následující funkce budou popisovat funkce, na které se tato funkce může zavolat a tedy se netýkají tahu bota.

### Double

Funkce double simuluje zahrání DOUBLE

### Stand

Funkce simuluje zahrání STAND a zároveň ukončuje tah hráče. Je volána tedy vždy, když hráč, ať už umýslně, či neúmyslně končí svůj.

### Hit

Funkce simuluje zahrání HIT, zároveň otevírá frame pro další tah.

### Split

Funkce simuluje zahrání funkce split a otevírá frame pro zahrání tahu s první várkou.

### Split_hit_1

Funkce simuluje zahrání HIT s první várkou splitu.

### Split_stand_1

Funkce simuluje zahrání STAND s první várkou splitu a zároveň ukončuje hraní s první várkou. (Je tedy volána i v případě, že hráč má v první várce BlackJack).

### Split_hit_2

Funkce simuluje zahrání HIT s druhou várkou splitu.

### Split_stand_2

Funkce ukončuje hraní splitu, simuluje zároveň hraní STAND s druhou várkou.

### Ukazka_vyhodnoceni

Během této funkce proběhne vyhodnocení sázek každého hráče a následně k zobrazení výsledků.

### Zaverecka

Funkce kontroluje, zda některý z hráčů nezkrachoval a v případě, že někdo ano, vyřadí ho za hry. Dá uživateli možnost ukončit hru nebo dát nové kolo. Pokud hráč chce nové kolo, zavolá se znovu funkce zacatek_kola a celý proces jede od znovu. Pokud hráč chce skončit, zavolá se funkce konec.

### Ukaz_zkrachovale

V případě, že některý hráč zkrachuje, tato funkce otevře vyskakovací okno, které nás o zkrachování informuje.

### Konec

Pokud hráč chce ukončit hru nebo pokud všichni hráči zkrachují, otevře tato funkce závěrečné pozadí a po pěti vteřinách ukončí program.

## Hlavní část kódu

Většina programu probíhá skrze výše zmíněnné funkce. V hlavní části kódu jsou tak primárně pouze pojmenovány některé objekty, hlavně widgety z Tkinter knihovny.
Dále tu je seznam jmen, inicializace proměmných jako Pocet_hracu nebo Pocet_balicku. Nebo proměnná HS_otevreno, která zaznamenává, zda je otevřený label s tlačítky na Hit a Stand. (Podle čehož se určuje, zda se má otevřít, či nikoliv).

## Textová verze hry

Textová verze hry se od té s rozhraním liší primárně v tom, jak hra porbíhá. Nedochází zde k postupnému volání funkcí. Nejprve dojde k nastavení základnách údajů jako jsou úrovně nebo rozpočet a po té se spustí while loop, který běží do té doby, dokud je proměnná dalsi_hra nastavena na True. Jedne průchod tímto loopem symbolizuje jedno kolo. 

Na začátku kola jsou rozdány karty a dojde k nastavení sázek. Po té přichází na řadu for loop, který pro každého jednoho hráče v seznamu Hraci odehraje hru. Kód v této fázi je velice podobný kódu z funkce tah_bota. Rozdíl je primárně v textových výpisech a v tom, že rozhodovací funkce se nyní volá i na hráče. Po skončení for loopu proběhne dealerův tah a vyhodnocení. Následně uživatel zvolí, zda chce pokračovat. Pokud řekne, že ne, proměnná Dalsi_hra se nastaví na False, čímž skončí while cyklus a hra může skončit.

Pro pocit plynulosti a dobrou čitelnost a hratelnost je program uměle zpomalován funkcí time.sleep().
