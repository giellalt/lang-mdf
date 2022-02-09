# The Moksha morphophonological/twolc rules file 

This file documents the [phonology.twolc file](http://github.com/giellalt/lang-mdf/blob/main/src/fst/phonology.twolc) 

```
а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я 
А Б В Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я 
```

This will represent schwa in first syllable

2016-03-12
%^А2О:0		 used with final а in пула 

 %{ЬØ%}:0	 after imperative Sg2
 %{ЬØ%}:ь	 after imperative Sg2
 %{ВИУ%}:в        lative

 %{АЯ%}:я  А2 in панемс:панян
 %{ИЫЙ%}:й	 phasing out Ы2, eg кундамс:кундай
 %{ИЫЙ%}:ы	 phasing out Ы2, eg кандомс:канды
 %{ИЫЙ%}:и	 phasing out Ы2, eg панемс:пани

 %{ЕОØ%}:е	 morpheme onset linking vowel from %^О1
 %{ЕОØ%}:о	 morpheme onset linking vowel from %^О1
 %{ЕОØ%}:0	 morpheme onset linking vowel from %^О1 also пинге

%{АЕØ%}:а	  ConNeg with ашень, тят, афоль

%{АО%}:а	  пула stem
%{АО%}:о	  пула stem
%{АОØ%}:а	  офта stem
%{АОØ%}:о	  офта stem
%{АОØ%}:0	  офта stem

 %{ЕО%}:е	 сельме
 %{ЕО%}:о	 

 %{ЕØ%}:е	 кече
 %{ЕØ%}:0	 

%{АЕ%}:а	 prolative

 %{Х%}:0	 This usually precedes the plural marker

%{DIM%}:н		 This will be for diminutive initial consonant

%{КТ%}:т	 used in imperative and connegative
* *пань%>%{Х%}%{КТ%}%{ЬØ%}*
* *пат0%>0тье0*

in ped realized as hard sign

## TRIGGERS
* %^RmVow:0  for removing vowels 
%^Ь2ZERO:0	 removes soft sign before vowel or other combination
%^Ъ2PED:0	 brings out hard sign, which is
otherwise automatically removed %{ъØ%} 
%^Е2О:0		 Change stem-final vowel сембе:сембось
%^Е2А:0		 Change stem-final vowel мельге:мельганза
%^Я2А:0		 Change stem-final vowel рьвя:рьванц
%^А2Е:0		 Change stem-final vowel мокша:мокшесь
%^Е2Я:0		 Change word-final vowel for dialect тувотне > тувотня

%^Devoice:0	 for devoicing изь:исть
%^PXSG1:0		 кядне, ярмаконе не vs %{ЕОØ%}не

* ` %- ` – Hyphen with constructions like "-bdi"
* ` %> ` – conjugation/declension morpheme boundary suffix
* ` »  ` – derivation morpheme boundary suffix
* ` #  ` – word boundary 

## The Sets

```
Vows = а о у ы э я ё ю и е ;                                            
verbStemVows = а о э я ё е ;                                            
verbStemVowStrong = а о э я ё е ;                                       
noGlideVow = а о у ы э ;                                                
glideVow = я ё ю и е ;                                                  
BTV = а о у я ё ю ;                                 ! Back Trigger Vowels
FTV = ы и е э ;                                    ! Front Trigger Vowels

Cns = б в г д ж з й к л м н п р с т ф х ц ч ш щ ;                       
CnsAndSoft = б в г д ж з й к л м н п р с т ф х ц ч ш щ ь ;                       
NPC = б в г д ж з к л м н п р с т ф х ц ч ш щ ; ! Nonpalatal Consonants 
CnsVoiced = б в г д ж з й л м н р ;                                     
CnsVoicedDent = д з л н р ;                                             
CnsVoicedNonDent = б в г ж й м ;                                        
CnsVoiceless = к п с т ф х ц ч ш щ ;                                    
CnsVoicelessDent = с т ц ;                                              
CnsVoicelessNonDent = к п ф х ч ш щ ;                                   
CnsNonDent = б в г ж к м п ф х ч ш щ ;                                  
CnsDent = д з л н р с т ц  ;                                            
CnsDentNoL = д з н р с т ц  ;                                           

Letters = Vows Cns ь ъ ;                                                
```

## The Definitions

## The Rules

**verbStemVowStrong:0**  
* *цёра%>%{АЯ%}н*
* *цёр0%>ан*

**у:0**

тумс+V+Ind+Prs+ScSg1
* ★*#ту%>%{АЯ%}н* (is not standard language)
* ★*#т0%>ан* (is not standard language)
* *#ту%>%{АЯ%}н*
* *#ту%>ян*

**о:0**  

**A1:o**  

**%{ИЫЙ%}:j**  
* *стя%>%{ИЫЙ%}%>сь*
* *стя%>й%>сь*
мумс+V+TV+Ind+Prt1+ScSg1+OcSg2: **find/löytää**
* *му%>%{ИЫЙ%}хтень*
* *му%>йхтень*

**%{ИЫЙ%}:ы**

**%{ИЫЙ%}:и**

**%{ИЫЙ%}:0**  
араламс+V+Der/NomAg+Sg+Nom+PxSg3: **protect/puolustaa**
* *арала%>%{ИЫЙ%}й%>%{ЕОØ%}ц*
* *арала%>0й%>ец*

**%{ЕОØ%}:о**
район+N+SP+Gen+Indef:
* *район%>%{ЕОØ%}нь*
* *район%>онь*
ялга+N+Pl+Nom+Indef+Clt/Cop+Prt2+ScPl3
* *ялга>{Х}т{ЬØ}>{ЕОØ}льхть*
* *ялга>0т0>ольхть*

**%{ЕОØ%}:е LEFT**
* *пинг%{ЕОØ%}#*
* *пинге#*
* *эрьхк%{ЕО0%}#*
* *эрьхке0*
* *тий%>%{ЕОØ%}за*
* *ти0%>еза*
кой+N+SP+Ill+PxSg1+Clt/Add:
* *кой%>%{ЕОØ%}з%>%{ЕОØ%}н%>%{гк%}%{АЕ%}*
* *ко0%>ез%>он%>га*
* ★*кой%>%{ЕОØ%}з%>%{ЕОØ%}н%>%{гк%}%{АЕ%}* (is not standard language)
* ★*ко0%>0з%>он%>га* (is not standard language)

**%{ЕОØ%}:е RIGHT**
* *тий%>%{ЕОØ%}за*
* *ти0%>еза*
* *пинг%{ЕОØ%}#*
* *пинге#*
* *эрьхк%{ЕО0%}#*
* *эрьхке0*
вай+N+Sg+Nom+PxSg1 **oil,butter/voi**
* *вай%>%{ЕОØ%}зе*
* *ва0%>езе*

**%{ЕОØ%}:0 LEFT**
зепе+N+Pl+Nom+Indef: **pocket/tasku**
* *зеп%{ЕОØ%}%^RmVow%>%{Х%}т%{ЬØ%}*
* *зеп00%>0т0*

**%{ЕОØ%}:0 RIGHT**
вай+N+Sg+Nom+PxSg1 **oil,butter/voi**
* *вай%>%{ЕОØ%}зе*
* *вай%>0зе*
* ★*вай%>%{ЕОØ%}нь* (is not standard language)
* ★*ва0%>0нь* (is not standard language)

**%{АОØ%}:о**

**%{АОØ%}:а**
* *панг%{АОØ%}#*
* *панга#*
* *тий%>%{ЕОØ%}за*
* *ти0%>еза*

**%{АОØ%}:0**
офта+N+Sg+Nom+Def **bear/ohto, karhu**
* *офт%{АОØ%}%^RmVow%>сь*
* *офт00%>сь*
кодама+Pron+Interr+Pl+Nom+Indef:
* *кодам%{АОØ%}%^RmVow%>%{Х%}т%{ЬØ%}*
* *кодап00%>0т0*

**%{АО%}:о**
пула+N+Sg+Nom+Def: **tail**
* *пул%{АО%}%>сь*
* *пуло%>сь*
* *пул%{АО%}%>%{ЕОØ%}нз%{АО%}*
* *пуло%>0нза*
* *пул%{АО%}%>%{Х%}т%{ЬØ%}*
* *пуло%>0т0*

**%{АО%}:а**
* *пул%{АО%}#*
* *пула#*

**Vx:0 %{АО%}:0**
пря+N+SP+Ine+Der/Cop+Prs+ScSg1 **top, head/pää**
* *пря%>с%{АО%}%>%{АЯ%}н*
* *пря%>с0%>ан*

**%{ЕО%}:е**
* *сельм%{ЕО%}#*
* *сельме#*

**%{ЕО%}:о**
* *сельм%{ЕО%}%>%{ЕОØ%}нь*
* *сельмо%>0нь*
сельме+N+Pl+Nom+PxSg1: __my eyes/silmäni
* *сельм%{ЕО%}%^PXSG1%>не*
* *сельмо0%>не*
байдек+N+Der+Der/Dimin+N+Sg+Nom+Indef: **staff/sauva**
* *байдек%>%{ЕО%}%{DIM%}я*
* *байдек%>оня*

**%{ЕØ%}:е**

**%{ЕØ%}:0**
тяште+N+Pl+Nom+Def **star/tähti**
* *тяшть%{ЕØ%}%^RmVow%>%{Х%}т%{ЬØ%}*
* *тяшт000%>0ть*

**0:j**  

**е:0**
веле+N+SP+Lat+Indef
* *веле%>%{ВИУ%}*
* *вел0%>и*

**е:о**

**е:а**

**е:я**

≈ * Rules final е lowered to я
* *тув%{АО%}%>%{Х%}тне%^Е2Я*
* *туво%>0тня0*

**%{АЕ%}:я**

**%{ЕОØ%}:я**

**%{ЕО%}:я**

**%{ЕØ%}:я**

**а:е**

**а:о**

**я:а**
* *рьвя%^Я2А%>%{ЕОØ%}нц*
* *рьва0%>0нц*
* *ърьвя%^Я2А%>%{Х%}т%{ЬØ%}*
* *ърьва0%>0т0*
* *ава%>з%>%{ЕОØ%}нт*
* *ава0з0онт*
вальмя+N+Pl+Nom+Indef: **window/ikkuna**
* *вальмя%^Я2А%>%{Х%}т%{ЬØ%}*
* *вальма0%>0т0*

**%{АЕØ%}:а Always**  

**%{АЕØ%}:а Sometimes**  

**%{АЕØ%}:е Always**  
**%{АЕØ%}:е Sometimes**  
мокша+N+Sg+Nom+Def: **Moksha**
* *мокш%{АЕØ%}%>сь*
* *мокше%>сь*

**%{АЕØ%}:0 Always**  

**%{АЕØ%}:0 Sometimes**  

**%{АЕ%}:a**  
вал+Hom1+N+Sg+Nom+Indef+Clt/Add: **word/sana**
* *вал%>%{гк%}%{АЕ%}#*
* *вал%>га#*
мельге+Pron+Prl+PxSg3: **after**
* *мельг%{АЕ%}%>%{ЕОØ%}нз%{АО%}*
* *мельга%>0нза*
* ★*мельг%{АЕ%}%>%{ЕОØ%}нз%{АО%}* (is not standard language)
* ★*мельге%>0нза* (is not standard language)
вальмя+N+SP+Prl+Indef: **window/ikkuna**
* *вальмя%^Я2А%>%{вгк%}%{АЕ%}*
* *вальма0%>ва*

**%{АЕ%}:е**  
менель+N+SP+Prl+Indef **sky/taivas**
* *менель%>%{вгк%}%{АЕ%}*
* *менель%>ге*
* *шяй%>%{вгк%}%{АЕ%}*
* *шяй%>ге*
аля+N+Sg+Dat+PxSg1+Foc **father/isä**
* *аля%>%{ЕОØ%}з%>ти%>%{гк%}%{АЕ%}*
* *аля%>0з%>ти%>ге*

**%{АЯ%}:ya**
* *пань>%{АЯ%}н*
* *пан00ян*
тумс+V+Ind+Prs+ScSg1 **leave/lähteä**
* *ту>%{АЯ%}н*
* *ту>ян*

* *пань>%{Х%}т%{АЯ%}ма*
* *пан000тяма*
мярьгомс+V+Ind+Prs+ScPl1: **say/sanoa**
* *мярьг%>%{Х%}т%{АЯ%}ма*
* *мярьк%>0тяма*
* *сим%>%{Х%}%{КТ%}%{АЯ%}*
* *сип%>0тя*
симомс+V+Ind+Prs+ScPl1: **say/sanoa**
* *сим%>%{Х%}т%{АЯ%}ма*
* *сип%>0тяма*

**%{АЯ%}:a**  

* *канд>%{АЯ%}н*
* *канд0ан*
* *аще%>%{АЯ%}н*
* *ащ0%>ан*

**j:0 LEFT**  
* *тий%>%{ЕОØ%}за*
* *ти00еза*
седи+N+Pl+Nom+Indef **heart/sydän**
* *седий%>%{Х%}т%{ЬØ%}*
* *седи0%>хть*
корхнемс+V+IV+NomAg+Pl+Nom+Def: **visit, talk/jutella**
* *корхне%>%{ИЫЙ%}й%>%{Х%}тне*
* *корхн0%>и0%>х0не*
озондомс+V+IV+NomAg+Pl+Nom+Def: **pray/rukoilla**
* *озонд%>%{ИЫЙ%}й%>%{Х%}тне*
* *озонд%>ы0%>х0не*

**j:0 RIGHT**  
* *тий%>%{ЕОØ%}за*
* *ти00еза*

седи+N+Pl+Nom+Indef **heart/sydän**
* *седий%>%{Х%}т%{ЬØ%}*
* *седи0%>хть*
араламс+V+Der/NomAg+Sg+Nom+PxSg3: **protect/puolustaa**
* *арала%>%{ИЫЙ%}й%>%{ЕОØ%}ц*
* *арала%>00%>ец*

**j:0 RIGHT**

**ye:e always**  

**ye:e sometimes**  

**a:ya**  

**о:а**  
удомс+V+Ind+ConNeg
* *удо%>%{АЕØ%}#*
* *уда%>0#*

### CONSONANT CHANGES
** %{Х%}:0 after vowel**  
валда+N+Pl+Nom+Def **light/valo**
* *валд%{АОØ%}%^RmVow%>%{Х%}т%{ЬØ%}*
* *валт00%>0т0*
* *пул%{АО%}%>%{Х%}т%{ЬØ%}*
* *пуло%>0т0*

** %{Х%}:х after some consonants**  
ваны+N+Pl+Nom+Def **watcher/katsoja**
* *ваный%>%{Х%}тне*
* *ваны0%>х0не*

**м:п ям**  
* *ям%>%{Х%}т%{ЬØ%}*
* *яп%>0т0*

**в:ф кев**  
* *кев%>%{Х%}т%{ЬØ%}*
* *кеф%>0т0*

**б:п сруб**  
* *сруб%>%{Х%}т%{ЬØ%}*
* *сруп%>0т0*

**н:т сан**  
сан+N+Pl+Nom+Indef: **sinew/suoni**
* *сан%>%{Х%}т{ЬØ}*
* *сат%>0т0*
ваномс+V+Imprt+ScSg2: **look/katsoa**
* *ван%>%{Х%}%{КТ%}{ЬØ}*
* *ват%>0т0*
панемс+V+Imprt+ScSg2: **put/laittaa**
* *пань%>%{Х%}%{КТ%}{ЬØ}*
* *пат0%>0ть*

**d:t**  
кулхцондомс+V+Imprt+ScSg2: **listen**
* *кулхцонд>{Х}{КТ}{ЬØ}*
* *кулхцонт>0т0*
офта+N+SP+Abl+Indef
* *офт%{АОØ%}%^RmVow%>д%{АО%}*
* *офт00%>та*
* ★*офт%{АОØ%}%^RmVow%>д%{АО%}* (is not standard language)
* ★*офт00%>да* (is not standard language)
кядь+N+SP+Abl+Indef: __hand;arm/käsi
* *кядь%>д%{АО%}*
* *кядь%>та*
* ★*кядь%>д%{АО%}* (is not standard language)
* ★*кять%>та* (is not standard language)
кандомс+V+Ind+Prs+ScSg1+OcSg2
* *канд%>%{Х%}тя*
* *кант%>0тя*
* *канд>%{Х%}%{КТ%}%{ЬØ%}*
* *кант%>0т0*
* *лемдь%>%^Devoice%>ф*
* *лемть%>0%>ф*
* *пильг%{ЕОØ%}%^RmVow%>д%{АО%}*
* *пильг00%>та*

**З:С**
изь+V+Aux+Neg+Ind+Prt1+ScPl3:	**they did not**
* *изь%^Devoice%^Ь2ZERO%>ть*
* *ис000%>ть*

* *келазь%>%{DIM%}я*

**Ж:Ш**

**ж:ч панчсь**
* *панж%>сь*
* *панч%>сь*

**г:к**
* *мярьг%>%{Х%}т%{АЯ%}ма*
* *мярьк%>0тяма*

**с:ц ломань:ломанць**  

**G1:0**  

**G1:g**  
вал+Hom1+N+Sg+Nom+Indef+Foc **word/sana**
* *вал%>%{гк%}%{АЕ%}*
* *вал%>га*
аля+N+Sg+Dat+PxSg2+Foc **father/isä**
* *аля%>цти%>%{гк%}%{АЕ%}*
* *аля%>цти%>ге*

**G1:k**  
вал+Hom1+N+SP+Ill+Indef+Foc **word/sana**
* *вал%>с%>%{гк%}%{АЕ%}*
* *вал%>с%>ка*
офто+N+SP+Abl+PxPl2+Foc
* *офт%{АОØ%}%>д%{АО%}%>%{ЕОØ%}нт%>%{гк%}%{АЕ%}*
* *офто%>до%>0нт%>ка*
ава+N+SP+Ela+PxPl2+Foc
* *тядя%>ст%{АО%}%>%{ЕОØ%}нт%>%{гк%}%{АЕ%}*
* *тядя%>сто%>0нт%>ка*

**%{ВИУ%}:v**

**%{ВИУ%}:i**
учительскай+N+SP+Lat+Indef: **teachers' lounge/opettajain huone**
* *учительскай%>%{ВИУ%}*
* *учительска0%>и*
пирьф+N+SP+Lat+Indef: **garden/tarha**
* *пирьф%>%{ВИУ%}*
* *пирьф%>и*

**%{ВИУ%}:u**
уша+N+SP+Lat+Indef: **outdoors**
* *уш%{АЕØ%}%>%{ВИУ%}*
* *уше%>у*
* *Крым%>%{ВИУ%}*
* *Крым%>у*

**G2:g**  

вальмя+N+SP+Prl+Indef
* *вальмя%^Я2А%>%{вгк%}%{АЕ%}*
* *вальма0%>ва*

**G2:k**  

**G4:0**  

**G4:k**  

**m:0**  

### imperative suffix
**К1 %{КТ%}:t left**  
* *пань%>%{КТ%}%{ЬØ%}*
* *пан0%>ть*

**К1 %{КТ%}:t right**  
* *канд>%{Х%}%{КТ%}%{ЬØ%}*
* *кант>00т0*
* *пань%>%{КТ%}%{ЬØ%}*
* *пан0%>ть*

**К1 %{КТ%}:к left**  
* *кунда>%{Х%}%{КТ%}%{ЬØ%}*
* *кунда00к0*

**К1 %{КТ%}:к right**  
* *кунда>%{Х%}%{КТ%}%{ЬØ%}*
* *кунда00к0*

**К1 %{КТ%}:0 **
кельгомс+V+TV+ConNegII:
* *кельг>%{Х%}%{КТ%}%{ЬØ%}*
* *кельк%>000*

**%{ЬØ%}:ь**  

* *пань%>%{КТ%}%{ЬØ%}*
* *пан0%>ть*
симомс+V+IV+Imprt+ScSg2
* *сим%>%{Х%}%{КТ%}%{ЬØ%}*
* *сип%>0ть*
* ★*сим%>%{Х%}%{КТ%}%{ЬØ%}* (is not standard language)
* ★*сип%>0т0* (is not standard language)

**%{ЬØ%}:0**  
зепе+N+Pl+Nom+Indef: **pocket/tasku**
* *зеп%{ЕОØ%}%^RmVow%>%{Х%}т%{ЬØ%}*
* *зеп00%>0т0*

ши+N+Pl+Nom+Indef: **day/päivä**
* *ши%>%{Х%}т%{ЬØ%}*
* *ши%>0т0*
* *пань%>%{КТ%}%{ЬØ%}*
* *пан0%>ть*
вальмя+N+Pl+Nom+Indef: **window/ikkuna**
* *вальмя%^Я2А%>%{Х%}т%{ЬØ%}*
* *вальма0%>0т0*

Plural before definite plural following a consonant
**t:0**  
Ананьина К.И. 2000: 55
* *ава%>%{Х%}тне*
* *ава%>0тне*
* *шуфт%>%{Х%}тне*
* *шуфт%>0тне*
* *нармот0%>0тне*
* *лав%>%{Х%}тне*
* *лаф%>00не*
* ★*лав%>%{Х%}тне* (is not standard language)
* ★*лаф%>0тне* (is not standard language)

**s:0**  

* *класс%>SLossс*
* *клас000с*

**y:0**  
plural
* *пань%>%{КТ%}%{ЬØ%}*
* *пан0%>ть*
ведь+N+Der+Der/Dimin+N+Sg+Nom+Indef: **a little water**
* *ведь%>%{DIM%}я*
* *вед0%>ня*
* *мяль%>%{ЕОØ%}зе*
* *мял0%>езе*
мирде+N+Sg+Nom: **husband/aviomies**
* *мирдь%{ЕØ%}#*
* *мирд0е#*
кядь+N+Pl+Nom+PxSg1: **hand; arm**
* *кядь%^PXSG1%>не*
* *кяд00%>не*

учемс+V+Ind+Prt1+ScSg3
* *учь%>сь*
* *уч0%>сь*

нярь+N+Sg+Gen+PxSg2: **hand; arm**
* *нярь%>це*
* *няр0%>це*

* *афоль%>ине*
* *афол0%>ине*

изь+V+Aux+Neg+Ind+Prt1+ScPl3: **they did not**
* *изь%^Devoice%^Ь2ZERO%>ть*
* *ис000%>ть*
ломань+N+SP+Abl+Indef:
* ★*ломань%>д%{АО%}* (is not standard language)
* ★*ломань%>да* (is not standard language)

### DIMINUTIVES
**%{DIM%}:н**
* *ши%>%{DIM%}я*
* *ши%>ня*
* *ара%>%{ИЫЙ%}%>%{DIM%}я*
* *ара%>й%>ня*

**%{DIM%}:к**
* *пикс>%{DIM%}я*
* *пикс0кя*

**%{ъØ%}:ъ**

## Disallow

**Disallow TLoss after non-t**  

**Disallow KLoss after non-k**  

**Disallow SLoss after non-s**  

**Disallow овок**

**Disallow Онга**

**Disallow -кс: нетькскс**

**Disallow -гя only after a few**

**Disallow special imperative in K after vowel stems**

**Disallow final е lowering to я tag elsewhere**

**Disallow onset vowel after voiced cons**

* * *

<small>This (part of) documentation was generated from [src/fst/phonology.twolc](https://github.com/giellalt/lang-mdf/blob/main/src/fst/phonology.twolc)</small>

---

