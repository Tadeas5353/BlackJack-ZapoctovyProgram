# BlackJack-ZapoctovyProgram
Zápočtový program z předmětu Programování 2 na MFF UK Praha. Autor: Tadeáš Janků. Hru s rozhraním je doporučeno hrát v nezvětšeném okně.

## Začátek hry
Jedná se o klasický BlackJack, který můžete znát z casin. Nicméně nehraje se o skutečné peníze.
Hra je určena pro jednoho až pět hráčů. Cílem hry je mít větší skóre než dealer. Zároveň však nepřesáhnout hodnotu 21.
Na začátku hry mají všichni hráči stejný startovní rozpočet, který musí být minimálně 100 korun. Následně si každý z nich určí,
kolik korun chce vsadit. Nejmenší povolená sázka je jedna koruna. Maximální pak 40% rozpočtu (aby hráč měl dostatek peněz na pojištění nebo 
zdvojení sázky). Následně každý hráčů dostane dvě karty. Dvě karty dostane i dealer a hráčům ukáže první z nich. Druhou nechává schovanou.

## První Tah
Hráč, který začíná má po obdržení prvních dvou karet čtyři možnosti, jak může pokračovat. Buď může zahrát STAND. Což znamená, že již nechce další kartu.
Následně hra pokračuje tahem dalšího hráče. Další možný tah je HIT, kdy si hráč lízne další kartu a její hodnota se přičte ke skóre prvních dvou. Třetím tahem je DOUBLE,
kdy si hráč stejně jako u hitu llízne kartu, zároveň však zdvojnásobuje svou sázku. 

Posledním tahem je SPLIT. Ten je možné zahrát jen v případě, že hráč má dvě karty stejné hodboty.
V tomto případě si hráč lízne dvě karty a postupně vytvoří dvojice s jednou kartou z ruky. Následně hraje s dvěmi várkami karet. Zároveň zdvojnásobuje svou sázku, protože na každou z várek
sází automaticky původní vsazenou částku.

## Další tahy
Pokud hráč zahrál hit, tak se po líznutí karty může rozhodnout, zda si chce další kartu, či nikoliv. Tedy zda chce zahrát znovu HIT nebo STAND. Tah končí buď ve chvíli,
kdy hráč zahraje STAND nebo když hodnota jeho karet přesáhne 21. V případě, že hráč zahrál split, postupuje obdobně, nicméně hraje postupně s první a po té s druhou várkou karet.

## Dealerův tah
Až všichni hráči provedou své tahy, přichází na řadu dealer. Ten si stejně jako hráči líže karty z balíčku, má však výrazně omezené možnosti. Pokud má skóre menší než 17, musí si líznout kartu.
Pokud má skóre větší než 17, musí zahrát STAND.

## Vyhodnocení
Až skončí dealerův tah, hráči postupně porovnávají své skóre s dealerovým skóre. Ovšem jen v případě, že hráčovo skóre je nejvýše 21. Pokud je vyšší, hráč automaticky prohrává. 
(A to i v případě, že Dealer též přesáhnul 21). Pokud hráč má skóre nejvýše 21 a dealer naopak více než 21, pak automaticky vyhrává hráč. Pokud mají hráč i dealer pod 21, vyhrává ten, kdo 
má vyšší skóre. Pokud mají stejně, je to remíza. Hráč, který zahrál split porovnává s dealerem skóre z obou várek nezávisle na sobě. 

Pokud vyhraje dealer, hráči propadá sázka. Pokud vyhraje hráč, 
dostává zpátky vsazenou částku a navíc ještě jednou tolik. Pokud hra skončí remízou, hráč dostává zpátky sázku, ale nic navíc. V případě, že hráč zahrál DOUBLE, myslí se sázkou zdvojnásobená hodnota původní sázky. Výjimku ve vyhodnocování tvoří situace, kdy hráč nebo dealer má BlackJack.

## Hodnoty karet a BlackJack
Pokud je karta číslem, pak její hodnota je rovna tomuto číslo (takže třeba hodnota listové trojky je tři). Hodnota karet J,Q,K je 10. Hodnota esa je buď 1 nebo 11, podle toho, co je zrovna pro držitele této
karty výhodnější. V případě, že hráč v prvních dvou kartách má eso a kartu s hodnotou deset (10,J,Q,K), má tzv. BlackJack (hodnota karet je rovnou 21). V tomto případě hráč automaticky končí svůj tah. Při vyhodnocování pak automaticky vyhrává a získává zpět vsazenou částku a 150% vsazených peněz navíc.

Pokud dealer má BlackJack, tak naopak automaticky poráží všechny hráče. Pokud dealer i hráč mají BlackJack, je to remíza a hráči se vrací vsazená částka. BlackJack je silnější než 21 bodů nasbíraných pomocí tří 
a více karet.

## Pojištění
Pokud kartou, kterou na začátku hry dealer ukáže hráčům je eso, dostává každý z hráčů možnost se pojistit proti dealerově BlackJacku a to zaplacením poloviny své sazené částky. Pokud dealer bude mít na konci
kola BlackJack, hráč dostává zpátky svou sázku. Pokud ho mít nebude, pojistka propadá.

## Krach
V případě, že rozpočet některého hráče klesne pod 100 korun, tak tento hráč krachuje a hra dále pokračuje bez něj. V případě, že zkrachují všichni hráči, hra končí.

## Ovládání hry
Hra se ovládá myší, jednoduchým klikáním na tlačítka. Na první stránce hráč nastav počet hráčů, počet hracích balíčků a počáteční rozpočet. Až vše potvrdí, tak může nastavit úrovně botů (viz další odstavec), případně zvolit manuální ovládání některého z hráčů. Pokud tak učiní, tak pro něj nastaví i jméno. Pro boty se jméno vybírá náhodně. 

Hráči ovládání manuálně si po té nastaví vsazenou částku na první hru a rozdávají se karty. Pokud má dealer eso, dostanou hráči možnost se pojistit. Po té se obejví vyskakovací okénko s informacemi o pojištění.
Tah začíná první hráč. Pokud se jedná o bota, tah proběhne na pozadí a na obrazovce se zobrazí stav po konci jeho tahu. Pokud se jedná o hráče, tak tah probíhá klikáním na tlačítka: STAND, HIT, DOUBLE a SPLIT. V
seznamu hráčů na levé straně obrazovky je vždy barevně vyznačeno, kdo je zrovna na tahu. 

Až skončí tah hráče, tak je nutno kliknout na tlačítko, kterým se hra přesune buď na tah dalšího hráče nebo na tah Dealera. Až odeahraje Dealer svůj tah, objeví se tabulka s vyhodnocením, kde bude vidět, kolik který hráč získává peněz. Tady mějte na paměti, že sázka se odečetla hned na začátku kola, tudíž pokud hráč získává nula korun, znamená to, že vlastně ztrácí vsazenou částku. Pokud některý hráč zkrachuje, objeví se vyskakovací okno s touto inforamcí.

Po konci každého kola dostanete na výběr zda chcete dát další kolo, či zda chcete hru ukončit.

## Úrovně botů

Ve hře je možné si nastavit čtyři úrovně botů (+ manuální ovládání). Úroveň bota ovlivňuje zda se bot pojistí, či nikoliv a hlavně jaké bude hrát tahy. Výše sázky a jméno jsou na úrovni bota nezávislé.

### Profesionál
Hráč, který vždy zahraje nejlepší možný tah. Vychází z výpočtu pravděpodobnosti na hru BlackJack.

### Pokročilý 
Hráč, který má se hrou už nějaké zkušenosti a umí hrát dobře. Nicméně ne vždy zvolí nejlepší možnou variantu.

### Začátečník 
Hráč, který se hrou začíná. Nemá ji příliš ozkoušenou, nicméně dokáže nad ní přemýšlet.

### Opilec 
Hráč, který se ke stolu přiklopítal těžce omámen a nedokáže pořádně posoudit, co vůbec dělá. Jeho tahy jsou čistě náhodné.

## Hra v konzoli

Hru si je možné zahrát i v konzolové verzi psaním příkazů. Z herního pohledu hra funguje úplně stejně jako hra s digitálním rozhraním. Rozdíl je v tom, že všechny vstupu musí hráč napsat na klávesnici. Dostává 
upozornění, v případě, že některý vstup napíše špatně. V této verzi je též vidět, jak postupně probíhají tahy botů. Při psaní vstupu není nutné rozlišovat velká a malá písmena. Úroveň hráče se vybírá napsaním příslušného čísla.
