# Moksha description 

All documents in one file



# DELIMITERS 

# TAGS AND SETS

## Sets containing lists of tags

Upper and lower case

* Sets for parts of speech

* Sets for POS sub-categories

* Sets for Semantic tags

* Sets for Morphosyntactic properties

* Sets for Derivation

Subjective adverbs, which are often set off by commas 

this is an adjective in nominative singular, adnominal attribute
this is an adjective in nominative singular,

this is a list of adverbs that modify adjectives

N ABBR not ABBR

IS there a @CVP

* * *
<small>This (part of) documentation was generated from [src/cg3/disambiguator.cg3](https://github.com/giellalt/lang-mdf/blob/main/src/cg3/disambiguator.cg3)</small>

* Sets for POS sub-categories

* Sets for Semantic tags

* Sets for Morphosyntactic properties

negation marker for 
fits between negation and conneg

* @>ADVL : Modifier of an adverbial to the right.
** vaikko: doppe leat vaikko man ollu studeanttat.
* @ADVL< : Complement of adverbial.
** vahkus: Son málesta guktii vahkus. таргозонзо: Ломанесь пиди-пани кавксть таргозонзо.
* @<ADVL : Adverbial after the main verb.
** dás: Eanet dieđuid gávnnat dás. тестэ: Седе ламо содамочи муят тестэ.
* @ADVL> : Adverbial to the left of the main verb
** viimmat: Dál de viimmat asttan lohkat reivve. окойники: Ней окойники кенеринь ловномо сёрманть.

MOOD-V

макссь чарькодемс, Deal with DATAUX separately; they also take MS

* @+FAUXV : finite auxiliary verbs

* @-FAUXV : non-finite auxiliary verbs

* @+FMAINV : finite main verbs
* @-FMAINV : non-finite main verb

* * *
<small>This (part of) documentation was generated from [src/cg3/functions.cg3](https://github.com/giellalt/lang-mdf/blob/main/src/cg3/functions.cg3)</small>

Adjective inflection

The MOKSHA language adjectives compare.

ADJECTIVES 

-нь

ош:ош

кяль:кяль

келу:келу

келу:келу

* * *

<small>This (part of) documentation was generated from [src/fst/affixes/adjectives.lexc](https://github.com/giellalt/lang-mdf/blob/main/src/fst/affixes/adjectives.lexc)</small>

---

Pronoun inflection

Adpostions in the Moksha language might also inflect in the same cases as regular
nouns, but ...

ADPOSITIONS

Checking 2018-11-10

Checking 2018-11-10

* LEXICON PO-PRL_MEL1GE  мельге:мельг%{АЕ%}

* * *

<small>This (part of) documentation was generated from [src/fst/affixes/adpositions.lexc](https://github.com/giellalt/lang-mdf/blob/main/src/fst/affixes/adpositions.lexc)</small>

---

Adverbs

The MOKSHA language adverbs

ADVERBS 

LEXICON ADV-DEG_ 	 пяк

LEXICON ADV_ 	 
LEXICON ADV-MOD_ 	 
LEXICON ADV-MANNER_ 	 

мзярксть

LEXICON ADV-TEMP_ 	 

ашель:ашель

* * *

<small>This (part of) documentation was generated from [src/fst/affixes/adverbs.lexc](https://github.com/giellalt/lang-mdf/blob/main/src/fst/affixes/adverbs.lexc)</small>

---

Clitics

The MOKSHA language clitics

CLITICS

This is for vowel final Nominatives
This is for PxPl1 and PxPl2 

This is for Consonant-final words

This is for Consonant-final words

* * *

<small>This (part of) documentation was generated from [src/fst/affixes/clitics.lexc](https://github.com/giellalt/lang-mdf/blob/main/src/fst/affixes/clitics.lexc)</small>

---

Conjunctions

The MOKSHA language conjunctions

CONJUNCTIONS

* * *

<small>This (part of) documentation was generated from [src/fst/affixes/conjunctors.lexc](https://github.com/giellalt/lang-mdf/blob/main/src/fst/affixes/conjunctors.lexc)</small>

---

Interjections

The MOKSHA language interjections

INTERJECTIONS 

Contrastive

LEXICON VOCATIVE_  should these really be interjections? 2018-11-10

* * *

<small>This (part of) documentation was generated from [src/fst/affixes/interjections.lexc](https://github.com/giellalt/lang-mdf/blob/main/src/fst/affixes/interjections.lexc)</small>

---

# Noun inflection

Moksha language nouns inflect in cases.

NOUNS 

ава:ава

вальмя:вальмя

вальмя:вальмя

пакся:пакся

пакся:пакся

* LEXICON N_ANDY  анды:анды

анды:анды

анды:анды

LEXICON N_OFTA  

LEXICON N_OFTA-PL 

LEXICON N_PANGA 

LEXICON N_PINGE 
Indef with vowel: Nom Sg, Gen, Dat, Cmpr, Prl, Tra

Floating

Without vowel

LEXICON N_KECHE 
Indef with vowel: Nom Sg, Gen, Dat, Cmpr, Prl, Tra

Floating

Without vowel

тише:тише

тише:тише

LEXICON N_PULA  

LEXICON N_KARIUC1KE 

LEXICON N_SEL1ME 

LEXICON N_OSH 

LEXICON N_SARAZ 

LEXICON N_VAJ 

LEXICON N_KAL 

LEXICON N_KIAL1 

LEXICON N_PINE 

LEXICON N_KELU 

NMN

LEXICON NMN_OFTA-PL 

Indefinite
Definite Sg
Possessor Indices

Indefinite
Definite Pl

Possessor Indices

Indefinite
Definite Sg
Definite Sg
Possessor Indices

Indefinite
Definite Pl

Possessor Indices

Indefinite
Definite Sg

Indefinite
Definite Pl

Indefinite
Definite Sg

Indefinite
Definite Pl

Possessor Indices

Indefinite
Definite Sg

Indefinite
Definite Pl

Indefinite
Definite Sg

Indefinite
Definite Pl

SG-NOM-INDEF ;
SG-DAT/GEN/NOM-DEF ;
PXSG1-Sg ;

Indefinite
Definite Pl

SG-NOM-INDEF ;
SG-DAT/GEN/NOM-DEF ;
PXSG1-Sg ;

PL-NOM-INDEF ;
PL-DAT/GEN/NOM-DEF ;

MUTUAL NOMINAL

Definite Sg
Possessor Indices

Definite Pl
Possessor Indices

Possessor Indices

PXSG1-Pl ;

* *кядь%^PXSG1%>не*
* *кяд00%>не*
* *ярмак%^PXSG1%>%{ЕОØ%}не*
* *ярмак0%>оне*

Ананьина К.И. 2000 53

сельме+N+SP+Gen+Indef
* *сельм%{ЕО%}%>%{ЕОØ%}нь*
* *сельмо%>0нь*

* *киза%^А2О%>%{Х%}т%{ЬØ%}*
* *кизо0%>0т0*

* * *

<small>This (part of) documentation was generated from [src/fst/affixes/nouns.lexc](https://github.com/giellalt/lang-mdf/blob/main/src/fst/affixes/nouns.lexc)</small>

---

Quantifier inflection

Numerals in the MOKSHA language inflect in the same cases as regular
nouns.

NUMERALS

NUMBERS 

омбонцт:омбонц

* **LEXICON ARABICCASE**  adds +Arab

* **LEXICON ARABICCASE0**  adds +Arab

* **LEXICON ARABICCOMPOUNDS**  ! 1-osainen

* * *

<small>This (part of) documentation was generated from [src/fst/affixes/numbers.lexc](https://github.com/giellalt/lang-mdf/blob/main/src/fst/affixes/numbers.lexc)</small>

---

Particles

The MOKSHA language particles ...

PARTICLES 

* * *

<small>This (part of) documentation was generated from [src/fst/affixes/particles.lexc](https://github.com/giellalt/lang-mdf/blob/main/src/fst/affixes/particles.lexc)</small>

---

Pronoun inflection

The Moksha language pronouns inflect in the same cases as regular
nouns, but ...

PRONOUNS 

* **эсь+A+Sg+Nom+Indef:эсь ENDLEX "oma" ;** seen in grammars as a pronoun base, but this does not occur as a pronoun.

* **LEXICON PERS** 
* **мон+Pron+Pers+Sg1:мон PERS-SG1 ;** ...

PERSONAL PRONOUNS

### DEMONSTRATIVE PRONOUNS

INTERROGATIVE PRONOUNS

INDEFINITE PRONOUNS

* LEXICON PRON-PERIF-MOD_СЬКАМОНЗА  ськамонза:ськам

### REFLEXIVE PRONOUNS
### NON-STRESSED REFLEXIVE DATIVES

* * *

<small>This (part of) documentation was generated from [src/fst/affixes/pronouns.lexc](https://github.com/giellalt/lang-mdf/blob/main/src/fst/affixes/pronouns.lexc)</small>

---

Proper noun inflection

The MOKSHA language proper nouns inflect in the same cases as regular
nouns, but with a colon (':') as separator.

Male given name for deriving patronyms 

Вили:Вил

Russian type Surnames 
Абдеев:Абдеев

Багрий:Багр

Аморский:Аморск

PLACE NAMES FROM TEMPLATES 
* **LEXICON PROP-PLC_KAL** ending in other consonant

* **LEXICON PROP-PLC_KIT** ending in t

* **LEXICON PROP-PLC_KUDO** ending in vowel

PROPER NOUNS 
* **LEXICON PROP-PLC_AVA** ending in vowel
* **LEXICON PROP-PLC_VAJ** ending in vowel

* **LEXICON PROP_AVA** ending in vowel

* **LEXICON PROP_VAJ** ending in vowel

* **LEXICON PROP_KELU** ending in u

* **LEXICON PROP_ANDY** ending in i

* * *

<small>This (part of) documentation was generated from [src/fst/affixes/propernouns.lexc](https://github.com/giellalt/lang-mdf/blob/main/src/fst/affixes/propernouns.lexc)</small>

---


# Symbol affixes

* * *

<small>This (part of) documentation was generated from [src/fst/affixes/symbols.lexc](https://github.com/giellalt/lang-mdf/blob/main/src/fst/affixes/symbols.lexc)</small>

---

# Verb inflection

The Moksha language verbs inflect in persons.

## VERBS 

* LEXICON V-AUX-NEG-CONJ_AFOLJ  аф:афоль

тумс:ту

BOTH IV and TV

OBJECT and SUBJECT VERBS 

пачкодемс:пачкодь

SUBJECT ONLY VERBS 

андомс:анд

пачкодемс:пачкодь

андовомс:андов

няемс:ня

* MUMS examples:*
* *мумс:* `мумс+V+Inf`
* *муйхтень:* `мумс+V+Ind+Prt1+ScSg1+OcSg2`
* *музе:* `мумс+V+Ind+Prt1+ScSg3+OcSg3`
* *мусь:* `мумс+V+Ind+Prt1+ScSg3`
* *мулезе:* `мумс+V+Conj+ScSg3+OcSg3`
@U.CONJ-MX.IND@@U.CONJ-TX.NONPAST@+Ind+Prs:@U.CONJ-MX.IND@@U.CONJ-TX.NONPAST@й VERB-ZERO-SC-REMAINDER ;  This is done here to leave the same ending open for COND-ALL
@U.CONJ-MX.IND@@U.CONJ-TX.NONPAST@+Ind+Prs:@U.CONJ-MX.IND@@U.CONJ-TX.NONPAST@ VERB-ZERO-SC-40/50 ;  This is done here to leave the same ending open for COND-ALL
@R.CONJ.ObjAll@@U.CONJ-MX.IND@@U.CONJ-TX.NONPAST@+Use/NG+Ind+Prs:@R.CONJ.ObjAll@@U.CONJ-MX.IND@@U.CONJ-TX.NONPAST@й VERB-ZERO-OC2 ;  This is done here to leave the same ending open for COND-ALL
@R.CONJ.ObjAll@@U.CONJ-MX.IND@@U.CONJ-TX.NONPAST@+Ind+Prs:@R.CONJ.ObjAll@@U.CONJ-MX.IND@@U.CONJ-TX.NONPAST@ VERB-ZERO-OC13 ;  This is done here to leave the same ending open for COND-ALL
+Use/NG:й	 IND-PRT1-SC3 ;  This is a difference from ТИЕМС
:	 IND-PRT1-SC3 ;  

COND-ALL
+Cond:й%>%{ЕОØ%}ндяря COND-4CONJ-ALL ;  
COND-ALL
+NegCnd:й%>%{ЕОØ%}фтяря COND-4CONJ-ALL ;  

@U.CONJ-MX.IND@@U.CONJ-TX.NONPAST@+Ind+Prs:@U.CONJ-MX.IND@@U.CONJ-TX.NONPAST@й VERB-ZERO-SC ;  This is done here to leave the same ending open for COND-ALL
@R.CONJ.ObjAll@@U.CONJ-MX.IND@@U.CONJ-TX.NONPAST@+Ind+Prs:@R.CONJ.ObjAll@@U.CONJ-MX.IND@@U.CONJ-TX.NONPAST@й VERB-ZERO-OC2 ;  This is done here to leave the same ending open for COND-ALL
@R.CONJ.ObjAll@@U.CONJ-MX.IND@@U.CONJ-TX.NONPAST@+Ind+Prs:@R.CONJ.ObjAll@@U.CONJ-MX.IND@@U.CONJ-TX.NONPAST@ VERB-ZERO-OC13 ;  This is done here to leave the same ending open for COND-ALL
COND-ALL
+Cond:й%>%{ЕОØ%}ндяря COND-4CONJ-ALL ;  
COND-ALL
+NegCnd:й%>%{ЕОØ%}фтяря COND-4CONJ-ALL ;  

LEXICON V0_NJAJEMS   няемс:ня
@U.CONJ-MX.IND@@U.CONJ-TX.NONPAST@+Ind+Prs:@U.CONJ-MX.IND@@U.CONJ-TX.NONPAST@й VERB-ZERO-SC ;  This is done here to leave the same ending open for COND-ALL
@R.CONJ.ObjAll@@U.CONJ-MX.IND@@U.CONJ-TX.NONPAST@+Ind+Prs:@R.CONJ.ObjAll@@U.CONJ-MX.IND@@U.CONJ-TX.NONPAST@й VERB-ZERO-OC2 ;  This is done here to leave the same ending open for COND-ALL
@R.CONJ.ObjAll@@U.CONJ-MX.IND@@U.CONJ-TX.NONPAST@+Ind+Prs:@R.CONJ.ObjAll@@U.CONJ-MX.IND@@U.CONJ-TX.NONPAST@й VERB-ZERO-OC13 ;  This is done here to leave the same ending open for COND-ALL
:й	 IND-PRT1-SC3 ;  This is a difference from ТИЕМС
COND-ALL
+Cond:й%>%{ЕОØ%}ндяря COND-4CONJ-ALL ;  
COND-ALL
+NegCnd:й%>%{ЕОØ%}фтяря COND-4CONJ-ALL ;  

### AUXILIARY VERBS
LEXICON V-AUX-NEG-PRT1_ASHEZJ  ашезь:аш

LEXICON V-AUX-NEG-PRT1_IZJ  изь:изь

FROM MYV

@U.CONJ-MX.IND@@U.CONJ-TX.NONPAST@+Ind+Prs:@U.CONJ-MX.IND@@U.CONJ-TX.NONPAST@ VERB-ZERO-ALL ;  This is done here to leave the same ending open for COND-ALL
COND-ALL
+Cond:%>%{ЕОØ%}ндяря COND-4CONJ-ALL ;  
COND-ALL
+NegCnd:%>%{ЕОØ%}фтяря COND-4CONJ-ALL ;  

ашень, тят, афоль
кирдемс+V+ConNeg **tolerate/kestää** ашень кирде
* *кирдь%>%{АЕØ%}*
* *кирд0%>е*
* *ван%>%{АЕØ%}*
* *ван%>а*
апак Homonymy +Imprt+ScSg2
ваномс+V+ConNegII
* *ван%>%{Х%}%{КТ%}%{ЬØ%}*
* *ват%>0т0*
* *кирдь%>%{Х%}%{КТ%}%{ЬØ%}*
* *кирт0%>%{Х%}ть*
### INDICATIVE PRESENT and CONDITIONAL (non-past) POINTERS

### INDICATIVE PRETERITE 1 POINTERS

### INDICATIVE PRETERITE 2 POINTERS

### CONJUNCTIVE

### CONDITIONAL and subsequent CONJUNCTIVE

## INDICATIVE TAGS

### INDICATIVE NONPAST TAGS and CONDITIONAL TAGS

### INDICATIVE PRETERITE 1 TAGS

## INDICATIVE PRETERITE 2 TAGS

## DESIDERATIVE (desiderative tag)

## CONJUNCTIVE TAGS
redo conj 2012-11-07 begin

## cond-conj
## CONDITIONAL-CONJUNCTIVE TAGS

## IMPERATIVE 

## IMPERATIVE		(imperative tags)

## PRECATIVE 

end of MYV BORROWING

NON-FINITES 

GERUNDS 

PARTICIPLES 

* * *

<small>This (part of) documentation was generated from [src/fst/affixes/verbs.lexc](https://github.com/giellalt/lang-mdf/blob/main/src/fst/affixes/verbs.lexc)</small>

---

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
мумс+V+Ind+Prt1+ScSg1+OcSg2: **find/löytää**
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
вий+N+Sg+Gen+PxSg3: **strength/voima**
* *вий>{ЕОØ}нц*
* *вий>0нц*

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
кодама+A+Pl+Nom+Indef:
* *кодам{АОØ}^RmVow>{Х}т{ЬØ}*
* *кодап00>0т0*
тяфтама+A+Pl+Nom+Indef: **this kind of/tällainen**
* ★*тяфтам{АОØ}>{Х}т{ЬØ}* (is not standard language)
* ★*тяфтапо>0т0* (is not standard language)

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
* *тий>{ЕОØ}за*
* *ти0>еза*
седи+N+Pl+Nom+Indef **heart/sydän**
* *седий%>%{Х%}т%{ЬØ%}*
* *седи0%>хть*
корхнемс+V+NomAg+Pl+Nom+Def: **visit, talk/jutella**
* *корхне%>%{ИЫЙ%}й%>%{Х%}тне*
* *корхн0%>и0%>х0не*
озондомс+V+NomAg+Pl+Nom+Def: **pray/rukoilla**
* *озонд%>%{ИЫЙ%}й%>%{Х%}тне*
* *озонд%>ы0%>х0не*
* *тонафт>{ИЫЙ}й>{ЕОØ}нь*
* *тонафт>ы0>ень*
* ★*тонафт>{ИЫЙ}й>{ЕОØ}нь* (is not standard language)
* ★*тонафт>ый>ень* (is not standard language)

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
ям+N+Pl+Nom+Indef: **stew/keitto**
* *ям%>%{Х%}т%{ЬØ%}*
* *яп%>0т0*
тяфтама+A+Pl+Nom+Indef
* *тяфтам{АОØ}>{Х}т{ЬØ}*
* *тяфтап0>0т0*
* ★*тяфтам{АОØ}>{Х}т{ЬØ}* (is not standard language)
* ★*тяфтапо>0т0* (is not standard language)

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
кельгомс+V+ConNegII:
* *кельг>%{Х%}%{КТ%}%{ЬØ%}*
* *кельк%>000*

**%{ЬØ%}:ь**  

* *пань%>%{КТ%}%{ЬØ%}*
* *пан0%>ть*
симомс+V+Imprt+ScSg2
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
* *ингольдень>не*
* *ингольден0>не*

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
* ★*куд>{ЕОØ}нз{АО}>{ЕОØ}н>нг{АЕ}* (is not standard language)
* ★*куд>онзо>0н>нга* (is not standard language)

**Disallow -кс: нетькскс**

**Disallow -гя only after a few**

**Disallow special imperative in K after vowel stems**

**Disallow final е lowering to я tag elsewhere**

**Disallow onset vowel after voiced cons**

* * *

<small>This (part of) documentation was generated from [src/fst/phonology.twolc](https://github.com/giellalt/lang-mdf/blob/main/src/fst/phonology.twolc)</small>

---


# Morphology
INTRODUCTION TO MORPHOLOGICAL ANALYSER OF THE Moksha LANGUAGE.

The morphological analyses of wordforms of the Moksha language are presented
in this system in terms of following symbols.
(It is highly suggested to follow existing standards when adding new tags).
+TYÄ 	 Underdeveloped.

The parts-of-speech tags are:

* **+A**:  adjective
* **+Adv**:  adverb
* **+CS**:  subordinating conjunction
* **+CC**:  coordinating conjunction
* **+Det**:  Determiner
* **+Interj**:  interjection
* **+N**:  noun
* **+Pcle**:  particle
* **+Po**:  postposition
* **+Pron**:  pronoun
* **+Qnt**:  Quantifier
* **+V**:  verb

* **+Descr**:  descriptive

The parts of speech are further split up into:
**Nouns:**
* **+Prop**:  proper
* **+CollN**:  used with paired nouns **collective nouns**
* **+Relator**:  relator nouns, mainly meronyms 
**Pronouns:**
* **+Dem**:  demonstrative
* **+Indef**:  indefinite
* **+Dep**:  dependent word requiring the presence of another, e.g. **мень**
* **+Exclusive**:  ськамонза
* **+Intensive**:  intensive pronoun
* **+Interr**:  interrogative
* **+PerifMod**:  periferal modifier ськамонза, кавонест
* **+Pers**:  personal
* **+Recipr**:  reciprocal
* **+Refl**:  reflexive
* **+Recip**:  reflexive
* **+Rel**:  relative
personal pronouns use additional tags:
```
 +Sg1 +Sg2 +Sg3 +Pl1 +Pl2 +Pl3 
```
Adverbs:
* ** +Adv-Ideoph 	: These are ideophonic descriptors used to modify the verb**: 
*вырк ливтясь*  "**flit** and it flew off"
* ; +Deg 	     : This is degree, depricate + AdA
* ** +Manner 		**:  with reference to type of adverb
* ** +Spat 			**:  spatial
* ** +Temp 			**:  temporal
* ** +Emphatic		**:  used with negation particles афи, 

Interjections:
* ** +Formulaic  **:  greetings,
The Usage extents are marked using following tags:
* ** +Err/Orth    **:  substandard / outside the written norm
* +Err/Orth-lowered-final-e-2-ja final е lowered to я with Е2Я trigger
* +Err/Orth-colloq Евсеич

* _+Use/Marg_ * Marginal
* _+Use/-Spell_ * Exclude from speller
* _+Use/SpellNoSugg_ * recognized but not suggested in speller
* _+Use/Circ_ * Circular path
* _+Use/CircN_ * Circular number path
* _+Use/-Ped_ * Remove from pedagogical speller
* _+Use/NG_ * Do not generate, for isme-ped.fst and apertium

* _+Err/Dial_ * The form is non-standard although it may well be central dialect, e.g. стякшемс
* _+Err/Lex_ * The lemma is not a Moksha word

# Dialect tags
* +Dial * No specification
Specific to some dialects
* +Dial/-C * Not central standard

The nominals are inflected in the following Case and Number
* ** +Sg 		**:  singular
* ** +Pl 		**:  plural
* ** +SP 		**:  both singular and plural
* ** +Abe 		**:  abessive
* ** +Abl 		**:  ablative
* ** +Acc 		**:  accusative Not really necessary
* ** +Cau 		**:  causatative
* ** +Com 		**:  comitative -нек
* ** +Cmpr 		**:  comparative -шка
* ** +Dat 		**:  dative
* ** +Ela 		**:  elative
* ** +Gen 		**:  genitive
* ** +Ill 		**:  illative
* ** +Ine 		**:  inessive
* ** +Lat 		**:  lative
* ** +Loc 		**:  locative
* ** +Nom 		**:  nominative
* ** +Prl 		**:  prolative
* ** +Tra 		**:  translative
* ** +Voc 		**:  Vocative

The possession is marked as such:
* ** +PxSg1 	**:  first person singular
* ** +PxSg2 	**:  second person singular
* ** +PxSg3 	**:  third person singular
* ** +PxPl1 	**:  first person plural
* ** +PxPl2 	**:  second person plural
* ** +PxPl3 	**:  third person plural

* ** +Def 	**:  Definite
The comparative forms are:
* ** +Comp 		**:  comparative as opposed to superlative
* ** +Superl 	**:  superlative

Particles
* **+Epist		**:  epistemic
Quantifiers and Numerals are classified under:
* ** +Num 		**:  numeral
* ** +Arab	**:  arabic numeral
* **+Appr 		**:  Approximative numeral кафта-колма, колмошка "two or three"
* ** +AssocColl **:  -ne- ; avide-; -месть
* ** +Coll 		**:  Collective
* ** +Card 		**:  cardinal
* ** +Distr 	**:  Distributive
* _+Iter_ Iterative This will be replaced by +Mult
* _+Mult_ Multiplicative form expressing number of times; myv: `кавксть`, kpv: `кыкысь`
* ** +Ord 		**:  ordinal
* ** +Attr 		**:  attribute, premodifier

Verb voice:
* ** +Act 	**:  active
* ** +Pss 	**:  passive
Verb moods are:
* ** +Cond 	**:  conditional ндяря- protasis
* ** +NegCnd **:  negative conditional Офтяря- negative protasis
* ** +NegCndSub **:  negative conditional Офтяряль negative protasis
* ** +Conj 	**:  conjunctional "Оль"
* ** +Des 	**:  desiderative ксоль "was about to; wanted to"
* ** +Ind 	**:  indicative
* ** +Imprt **:  imperative
* ** +Opt 	**:  optative
* ** +Prec  **:  Precative mood is a directive mood that signals that the utterance is a request. imperative + additional vowel and cons -ака forms equal Precative

Verb tenses are
 +Prs 	 present and future ! nominal	conjugation as well
 +Prt1 	 preterite I ! only finite verbal
 +Prt2 	 preterite II ! nominal conjugation as well

Verb personal forms are:

 +ScSg1 	 subject conjugation first person singular
 +ScSg2 	 subject conjugation second person singular
 +ScSg3 	 subject conjugation third person singular
 +ScPl1 	 subject conjugation first person plural
 +ScPl2 	 subject conjugation second person plural
 +ScPl3 	 subject conjugation third person plural

 +OcSg1 	 objject conjugation first person singular
 +OcSg2 	 objject conjugation second person singular
 +OcSg3 	 objject conjugation third person singular
 +OcPl1 	 objject conjugation first person plural
 +OcPl2 	 objject conjugation second person plural
 +OcPl3 	 objject conjugation third person plural

Other verb forms are
  +ConNeg 	 connegative, main verb complement to Neg, vowel-stem
  +ConNegII 	 connegative, main verb complement to Neg, cons-stem
  +Ger 	 gerund This is used with Der/Озь and VAbl
  +Inf    	 infinitive
  +Neg    	 verb of negation эзь, аволь, иля
  +Aux		 auxiliary verb
+Prc 	 participle
  +VGen   	 Verb Genitive, genitive form participle
  +VAbl   	 Verb Ablative "озадо"

 +ABBR 	 Abbreviation
* +Symbol = independent symbols in the text stream, like £, €, ©
 +ACR  	 Acronym

Special symbols are classified with:

The verbs are syntactically split according to transitivity:
 +TV 	 transitive verb
 +IV 	 intransitive verb
Special multiword units are analysed with:
Non-dictionary words can be recognised with:

* +Dig1 
* +Dig2 
* +Dig3 
* +Dig4 
* +Rom Roman numerals

Compounding
* +Cmp Dynamic compound - this tag should always be part of a dynamic compound.
It is important for Apertium, and useful in other cases as well.
* +Cmp/Hyph with nouns
* +Cmp/Hyph-Coll with nouns
* +Cmp/Hyph-Redup with verbs
* +Cmp/Hyph-Synonym with verbs
* +Cmp/Hyph-Serial with verbs
* +Cmp/Hyph-tejems with verbs

Question and Focus particles:
* +Clt/Cop This marks all instances of enclitic copula inflection
* +Clt/Aram Used with preceding dative тейне-арам 'in my opinion'
* +Clt/Add 
* +Clt/AddGA 
* +Clt/AddVok 
* +Clt/AddNgA 

### Tags distinguishing different versions of the same lemma (before POS)
* +v1
* +v2
* +v3
* +v4
* +v5
* +v6
* +v7
* +v8
* +v9
* +v10
* +v11
* +v12
* +v13
* +v14
* +v15
* +v16
* +v17
* +v18
* +v19
* +v20
* +v21
* +v22
* +v23
* +v24

* **+Sem/Act** Activity
* **+Sem/Amount** Amount
* **+Sem/Ani** Animate
* **+Sem/Aniprod** Animal Product
* **+Sem/Body** Bodypart
* **+Sem/Body-abstr** siellu, vuoig?a, jierbmi
* **+Sem/Build** Building
* **+Sem/Build-part** Part of Bulding, like the closet
* **+Sem/Cat** Category
* **+Sem/Clth** Clothes
* **+Sem/Clth-jewl** Jewelery
* **+Sem/Clth-part** part of clothes, boallu, sávdnji...
* **+Sem/Ctain** Container
* **+Sem/Ctain-abstr** Abstract container like bank account
* **+Sem/Ctain-clth**
* **+Sem/Curr** Currency like dollár, Not Money
* **+Sem/Dance** Dance
* **+Sem/Dir** Direction like GPS-kursa
* **+Sem/Domain** Domain like politics, reindeerherding (a system of actions)
* **+Sem/Drink** Drink
* **+Sem/Dummytag** Dummytag
* **+Sem/Edu** Educational event
* **+Sem/Event** Event
* **+Sem/Feat** Feature, like Árvu
* **+Sem/Feat-phys** Physiological feature, ivdni, fárda
* **+Sem/Feat-psych** Psychological feauture
* **+Sem/Feat-measr** Psychological feauture
* **+Sem/Fem** Female name
* **+Sem/Fem-Patr** Female name
* **+Sem/Fem-Sur** Female name
* **+Sem/Food** Food
* **+Sem/Food-med** Medicine
* **+Sem/Furn** Furniture
* **+Sem/Game** Game
* **+Sem/Geom** Geometrical object
* **+Sem/Group** Animal or Human Group
* **+Sem/Hum** Human
* **+Sem/Hum-abstr** Human abstract
* **+Sem/Ideol** Ideology
* **+Sem/Lang** Language
* **+Sem/Mal** Male name
* **+Sem/Mal-Patr** Male name
* **+Sem/Mal-Sur** Male name
* **+Sem/Mat** Material for producing things
* **+Sem/Measr** Measure
* **+Sem/Money** Has to do with money, like wages, not Curr(ency)
* **+Sem/Obj** Object
* **+Sem/Obj-clo** Cloth
* **+Sem/Obj-cogn** Cloth
* **+Sem/Obj-el** (Electrical) machine or apparatus
* **+Sem/Obj-ling** Object with something written on it
* **+Sem/Obj-rope** flexible ropelike object
* **+Sem/Obj-surfc** Surface object
* **+Sem/Org** Organisation
* **+Sem/Part** Feature, oassi, bealli
* **+Sem/Perc-cogn** Cognative perception
* **+Sem/Perc-emo** Emotional perception
* **+Sem/Perc-phys** Physical perception
* **+Sem/Perc-psych** Physical perception
* **+Sem/Plant** Plant
* **+Sem/Plant-part** Plant part
* **+Sem/Plc** Place
* **+Sem/Plc-abstr** Abstract place
* **+Sem/Plc-elevate** Place
* **+Sem/Plc-line** Place
* **+Sem/Plc-water** Place
* **+Sem/Pos** Position (as in social position job)
* **+Sem/Process** Process
* **+Sem/Prod** Product
* **+Sem/Prod-audio** Audio product
* **+Sem/Prod-cogn** Cognition product
* **+Sem/Prod-ling** Linguistic product
* **+Sem/Prod-vis** Visual product
* **+Sem/Rel** Relation
* **+Sem/Route** Name of a Route
* **+Sem/Rule** Rule or convention
* **+Sem/Semcon** Semantic concept
* **+Sem/Sign** Sign (e.g. numbers, punctuation) 
* **+Sem/Sport** Sport
* **+Sem/State** 
* **+Sem/State-sick** Illness
* **+Sem/Substnc** Substance, like Air and Water
* **+Sem/Sur** Surname
* **+Sem/Symbol** Symbol
* **+Sem/Time** Time
* **+Sem/Tool** Prototypical tool for repairing things
* **+Sem/Tool-catch** Tool used for catching (e.g. fish)
* **+Sem/Tool-clean** Tool used for cleaning
* **+Sem/Tool-it** Tool used in IT
* **+Sem/Tool-measr** Tool used for measuring
* **+Sem/Tool-music** Music instrument
* **+Sem/Tool-write** Writing tool
* **+Sem/Txt** Text (girji, lávlla...)
* **+Sem/Veh** Vehicle
* **+Sem/Wpn** Weapon
* **+Sem/Wthr** The Weather or the state of ground

Semantics are classified with
* **+Sem/Kin** Kin term

Derivations are classified under the morphophonetic form of the suffix, the
source and target part-of-speech.

## Der begin
*  **+Der**  In front of every derivation to make it
possible to target derivations as a class e.g. in regular expressions etc
*  **+Der/Poss**  possessive noun ава » аванне
*  **+Der/Ord**  
*  **+Der/Iter**  весть, кафксть, колмоксть...
*  **+Der/Wife**  Added to male names, surnames, patronymics

## DECLARING DEVERBAL DERIVATIONS OF VERBS
* +Der/kshnO  verb2verb derivation
* +Der/OkshnOms  verb2verb derivation
* +Der/OvOms  verb2verb derivation
* +Der/Ozevems  verb2verb derivation
* +Der/OvkshnOms  verb2verb derivation
* +Der/OvtOms  verb2verb derivation

 +Der/Dimin	 diminutive markers in ня and кя seem to be subject of complementary distribution
* +Der/NJ Онь
* +Der/Bachk * бачк

Morphophonology
To represent phonologic variations in word forms we use the following
symbols in the lexicon files:
 %{ИЫЙ%}	 phasing out Ы2, eg кундамс:кундай
 %{ЕОØ%}	 morphemes requiring a preceding vowel; also пинге
 %{ЕО%} 	 сельме
 %{ЕØ%}	 кече
 %{АЯ%} 	 А2 in кундамс:кундан
 %{ВИУ%}         lative
 %{Х%}		 This usually precedes the plural marker
 %{КТ%}		 used in imperative and connegative
 %{ЬØ%}	 after imperative Sg2
 %{DIM%}	 This will be for diminutive initial consonant

2016-03-12
%^А2О		 used with final а in пула 

 А2 	 А2:а А2:я
 %{вгк%} 	 %{вгк%}:г %{вгк%}:в %{вгк%}:к
 %{гк%}	 clitic in ``` %{гк%} %{АЕ%} ```
 К1 	 К1:к К1:т
%{АЕØ%}	  ConNeg with ашень, тят, афоль
%{АО%}	  пула stem
%{АОØ%}	  офта stem
%{АЕ%}	 prolative
 Х1 	 Х1:х Х1:0
 Ь2 	 Ь2:ь Ь2:0
%{ъØ%}         This will represent schwa in first syllable

in ped realized as hard sign

And following triggers to control variation
* %^RmVow 	 for removing vowels
%^Ь2ZERO	 removes soft sign before vowel or other combination
%^Ъ2PED		 brings out hard sign, which is otherwise automatically removed
%^Е2О		 Change stem-final vowel сембе:сембось
%^Е2А		 Change stem-final vowel мельге:мельганза
%^Я2А		 Change stem-final vowel рьвя:рьванц
%^А2Е		 Change stem-final vowel мокша:мокшесь
%^Е2Я		 Change word-final vowel for dialect тувотне > тувотня
%^Devoice	 for devoicing изь:исть
%^PXSG1		 кядне, ярмаконе не vs %{ЕОØ%}не

## Flag diacritics
We have manually optimised the structure of our lexicon using following
flag diacritics to restrict morhpological combinatorics - only allow compounds
with verbs if the verb is further derived into a noun again:
|  @P.NeedNoun.ON@ | (Dis)allow compounds with verbs unless nominalised
|  @D.NeedNoun.ON@ | (Dis)allow compounds with verbs unless nominalised
|  @C.NeedNoun@ | (Dis)allow compounds with verbs unless nominalised

For languages that allow compounding, the following flag diacritics are needed
to control position-based compounding restrictions for nominals. Their use is
handled automatically if combined with +CmpN/xxx tags. If not used, they will
do no harm.
|  @P.CmpFrst.FALSE@ | Require that words tagged as such only appear first
|  @D.CmpPref.TRUE@ | Block such words from entering ENDLEX
|  @P.CmpPref.FALSE@ | Block these words from making further compounds
|  @D.CmpLast.TRUE@ | Block such words from entering R
|  @D.CmpNone.TRUE@ | Combines with the next tag to prohibit compounding
|  @U.CmpNone.FALSE@ | Combines with the prev tag to prohibit compounding
|  @P.CmpOnly.TRUE@ | Sets a flag to indicate that the word has passed R
|  @D.CmpOnly.FALSE@ | Disallow words coming directly from root.

Use the following flag diacritics to control downcasing of derived proper
nouns (e.g. Finnish Pariisi -> pariisilainen). See e.g. North Sámi for how to use
these flags. There exists a ready-made regex that will do the actual down-casing
given the proper use of these flags.
|  @U.Cap.Obl@ | Allowing downcasing of derived names: deatnulasj.
|  @U.Cap.Opt@ | Allowing downcasing of derived names: deatnulasj.

@D.CONJ-MX.IND@ 	 2012-11-04 should this be **D** or **N**

# FLAGS USED WITH MODIFIERS WITHOUT NOUNS

# FLAGS USED WITH COLLECTIVE NOUNS
## number
* @U.DECL-NX.SG@
* @U.DECL-NX.SP@
* @U.DECL-NX.PL@
* @R.DECL-NX.SG@
* @R.DECL-NX.SP@
* @R.DECL-NX.PL@

* @U.CX.ABE@ 
* @U.CX.ABL@ 
* @U.CX.CAU@ 
* @U.CX.CMP@ 
* @U.CX.COM@ 
* @U.CX.DAT@ 
* @U.CX.ELA@ 
* @U.CX.GEN@ 
* @U.CX.ILL@ 
* @U.CX.INE@ 
* @U.CX.LAT@ 
* @U.CX.LOC@ 
* @U.CX.NOM@ 
* @U.CX.PRL@ 
* @U.CX.TRA@ 
* @U.CX.PRL@ 
* @U.CX.TEMP@ 

* @U.DECL-DX.DEF@ 
* @U.DECL-DX.INDEF@ 
* @U.DECL-DX.PXSG1@ 
* @U.DECL-DX.PXSG2@ 
* @U.DECL-DX.PXSG3@ 
* @U.DECL-DX.PXPL1@ 
* @U.DECL-DX.PXPL2@ 
* @U.DECL-DX.PXPL3@ 

The word forms in Moksha language start from the lexeme roots of basic
word classes, or optionally from prefixes:
These have been slightly modified from kpv and myv

* * *

<small>This (part of) documentation was generated from [src/fst/root.lexc](https://github.com/giellalt/lang-mdf/blob/main/src/fst/root.lexc)</small>

---

This is where new words are added as lexc entries before they are 
added to the xml source files.
од:од A_KAL "(eng) /(fin)/(rus) " ;

ADD ADJECTIVES BELOW

Adding more 2016-05-22

Adding more 2020-03-08

* * *

<small>This (part of) documentation was generated from [src/fst/stems/adjectives-russian-like_newwords.lexc](https://github.com/giellalt/lang-mdf/blob/main/src/fst/stems/adjectives-russian-like_newwords.lexc)</small>

---

This is where new words are added as lexc entries before they are 
added to the xml source files.
духовнай:духовнай A_VAJ "(eng) /(fin) /(rus) " ;

ADD NOUNS BELOW

* * *

<small>This (part of) documentation was generated from [src/fst/stems/adjectives_newwords.lexc](https://github.com/giellalt/lang-mdf/blob/main/src/fst/stems/adjectives_newwords.lexc)</small>

---

Exceptions are quite strange word-forms. the ones that do not fit anywhere 
else. This file contains all enumerated word forms that cannot reasonably be
created from lexical data by regular inflection. Usually there should be next
to none exceptions, it's always better to have a paradigm that covers only
one or few words than an exception since these will not work nicely with e.g.
compounding scheme or possibly many end applications.

MISSING ADV

MISSING CS

MISSING Pcle

IRREGULAR diminutives

MISSING V

VOCATIVES

TOPONYMY

PROPER NAMES

Wife NAMES

QUESTIONABLE FORMS

FOREIGN WORDS
A

PCLE

NOUNS

PROP

MISSING VALENCY

more words for Mormula

* * *

<small>This (part of) documentation was generated from [src/fst/stems/exceptions.lexc](https://github.com/giellalt/lang-mdf/blob/main/src/fst/stems/exceptions.lexc)</small>

---

This is where new words are added as lexc entries before they are 
added to the xml source files.
автор:автор N_KAL ;

ADD NOUNS BELOW

* * *

<small>This (part of) documentation was generated from [src/fst/stems/nouns-russian-homographs_newwords.lexc](https://github.com/giellalt/lang-mdf/blob/main/src/fst/stems/nouns-russian-homographs_newwords.lexc)</small>

---

This is where new words are added as lexc entries before they are 
added to the xml source files.
автор:автор N_KAL "(eng) /(fin) /(rus) " ;

ADD NOUNS BELOW

* * *

<small>This (part of) documentation was generated from [src/fst/stems/nouns_newwords.lexc](https://github.com/giellalt/lang-mdf/blob/main/src/fst/stems/nouns_newwords.lexc)</small>

---

This is where new words are added as lexc entries before they are 
added to the xml source files.
автор:автор PROP_KAL "(eng) /(fin) /(rus) " ;

ADD PROPER NOUNS BELOW

MOKSHA PROPER NAMES

* * *

<small>This (part of) documentation was generated from [src/fst/stems/propernouns_newwords.lexc](https://github.com/giellalt/lang-mdf/blob/main/src/fst/stems/propernouns_newwords.lexc)</small>

---

This is where new words are added as lexc entries before they are 
added to the xml source files.
автор:автор N_KAL "(eng) /(fin) /(rus) " ;

ADD VERBS BELOW

* * *

<small>This (part of) documentation was generated from [src/fst/stems/verbs_newwords.lexc](https://github.com/giellalt/lang-mdf/blob/main/src/fst/stems/verbs_newwords.lexc)</small>

---



retroflex plosive, voiceless			t`  ʈ	    0288, 648 (` = ASCII 096)
retroflex plosive, voiced			d`	ɖ		0256, 598
labiodental nasal					F 	ɱ		0271, 625
retroflex nasal						n` 	ɳ		0273, 627
palatal nasal						J 	ɲ		0272, 626
velar nasal							N 	ŋ		014B, 331
uvular nasal							N\	ɴ		0274, 628
	
bilabial trill						B\ 	ʙ		0299, 665
uvular trill							R\ 	ʀ		0280, 640
alveolar tap							4	ɾ		027E, 638
retroflex flap						r` 	ɽ		027D, 637
bilabial fricative, voiceless		p\ 	ɸ		0278, 632
bilabial fricative, voiced			B 	β		03B2, 946
dental fricative, voiceless			T 	θ		03B8, 952
dental fricative, voiced				D 	ð		00F0, 240
postalveolar fricative, voiceless	S	ʃ		0283, 643
postalveolar fricative, voiced		Z 	ʒ		0292, 658
retroflex fricative, voiceless		s` 	ʂ		0282, 642
retroflex fricative, voiced			z` 	ʐ		0290, 656
palatal fricative, voiceless			C 	ç		00E7, 231
palatal fricative, voiced			j\ 	ʝ		029D, 669
velar fricative, voiced	        	G 	ɣ		0263, 611
uvular fricative, voiceless			X	χ		03C7, 967
uvular fricative, voiced				R 	ʁ		0281, 641
pharyngeal fricative, voiceless		X\ 	ħ		0127, 295
pharyngeal fricative, voiced			?\ 	ʕ		0295, 661
glottal fricative, voiced			h\	ɦ		0266, 614

alveolar lateral fricative, vl.		K 
alveolar lateral fricative, vd.		K\

labiodental approximant				P (or v\) 
alveolar approximant					r\ 
retroflex approximant				r\` 
velar approximant					M\

retroflex lateral approximant		l` 
palatal lateral approximant			L 
velar lateral approximant			L\
Clicks

bilabial								O\	(O = capital letter) 
dental								|\
(post)alveolar						!\ 
palatoalveolar						=\ 
alveolar lateral						|\|\
Ejectives, implosives

ejective								_>	e.g. ejective p		p_>
implosive							_<	e.g. implosive b	b_<
Vowels

close back unrounded					M
close central unrounded 				1 
close central rounded				} 
lax i								I 
lax y								Y 
lax u								U

close-mid front rounded				2 
close-mid central unrounded			@\ 
close-mid central rounded			8 
close-mid back unrounded				7

schwa	ə							@

open-mid front unrounded				E 
open-mid front rounded				9
open-mid central unrounded			3 
open-mid central rounded				3\ 
open-mid back unrounded				V 
open-mid back rounded				O

ash (ae digraph)						{ 
open schwa (turned a)				6

open front rounded					& 
open back unrounded	        		A 
open back rounded					Q
Other symbols

voiceless labial-velar fricative		W 
voiced labial-palatal approx.		H 
voiceless epiglottal fricative		H\ 
voiced epiglottal fricative			<\ 
epiglottal plosive					>\

alveolo-palatal fricative, vl. 		s\ 
alveolo-palatal fricative, voiced	z\ 
alveolar lateral flap				l\ 
simultaneous S and x					x\ 
tie bar								_
Suprasegmentals

primary stress						" 
secondary stress						% 
long									: 
half-long							:\ 
extra-short							_X 
linking mark							-\
Tones and word accents

level extra high						_T 
level high							_H
level mid							_M 
level low							_L 
level extra low						_B
downstep								! 
upstep								^	(caret, circumflex)

contour, rising						 
contour, falling						_F 
contour, high rising					_H_T 
contour, low rising					_B_L 

contour, rising-falling				_R_F 
(NB Instead of being written as diacritics with _, all prosodic 
marks can alternatively be placed in a separate tier, set off 
by < >, as recommended for the next two symbols.)
global rise						<R> 
global fall						<F>
Diacritics						
									
voiceless						_0	(0 = figure), e.g. n_0
voiced							_v 
aspirated						_h 
more rounded						_O	(O = letter) 
less rounded						_c 
advanced							_+
retracted						_-
centralized						_" 
syllabic							=	(or _=) e.g. n= (or n_=) 
non-syllabic						_^ 
rhoticity						`
									
breathy voiced					_t 
creaky voiced					_k
linguolabial						_N 
labialized						_w 
palatalized						'	(or _j) e.g. t' (or t_j) 
velarized						_G 
pharyngealized					_?\
									
dental							_d 
apical							_a 
laminal							_m
nasalized						~	(or _~) e.g. A~ (or A_~) 
nasal release					_n
lateral release					_l 
no audible release				_}

velarized or pharyngealized		_e 
velarized l, alternatively		5 
raised							_r 
lowered							_o 
advanced tongue root				_A 
retracted tongue root			_q

* * *

<small>This (part of) documentation was generated from [src/phonetics/txt2ipa.xfscript](https://github.com/giellalt/lang-mdf/blob/main/src/phonetics/txt2ipa.xfscript)</small>

---



We describe here how abbreviations are in Moksha are read out, e.g.
for text-to-speech systems.

For example:

* s.:syntynyt # ;  
* os.:omaa% sukua # ;  
* v.:vuosi # ;  
* v.:vuonna # ;  
* esim.:esimerkki # ; 
* esim.:esimerkiksi # ; 

* * *

<small>This (part of) documentation was generated from [src/transcriptions/transcriptor-abbrevs2text.lexc](https://github.com/giellalt/lang-mdf/blob/main/src/transcriptions/transcriptor-abbrevs2text.lexc)</small>

---


[ L A N G U A G E ]  G R A M M A R   C H E C K E R

# DELIMITERS

# TAGS AND SETS

## Tags

This section lists all the tags inherited from the fst, and used as tags
in the syntactic analysis. The next section, **Sets**, contains sets defined
on the basis of the tags listed here, those set names are not visible in the output.

### Beginning and end of sentence
BOS
EOS

### Parts of speech tags

N
A
Adv
V
Pron
CS
CC
CC-CS
Po
Pr
Pcle
Num
Interj
ABBR
ACR
CLB
LEFT
RIGHT
WEB
PPUNCT
PUNCT

COMMA
¶

### Tags for POS sub-categories

Pers
Dem
Interr
Indef
Recipr
Refl
Rel
Coll
NomAg
Prop
Allegro
Arab
Romertall

### Tags for morphosyntactic properties

Nom
Acc
Gen
Ill
Loc
Com
Ess
Ess
Sg
Du
Pl
Cmp/SplitR
Cmp/SgNom Cmp/SgGen
Cmp/SgGen
PxSg1
PxSg2
PxSg3
PxDu1
PxDu2
PxDu3
PxPl1
PxPl2
PxPl3
Px

Comp
Superl
Attr
Ord
Qst
IV
TV
Prt
Prs
Ind
Pot
Cond
Imprt
ImprtII
Sg1
Sg2
Sg3
Du1
Du2
Du3
Pl1
Pl2
Pl3
Inf
ConNeg
Neg
PrfPrc
VGen
PrsPrc
Ger
Sup
Actio
VAbess

Err/Orth

### Semantic tags

Sem/Act
Sem/Ani
Sem/Atr
Sem/Body
Sem/Clth
Sem/Domain
Sem/Feat-phys
Sem/Fem
Sem/Group
Sem/Lang
Sem/Mal
Sem/Measr
Sem/Money
Sem/Obj
Sem/Obj-el
Sem/Org
Sem/Perc-emo
Sem/Plc
Sem/Sign
Sem/State-sick
Sem/Sur
Sem/Time
Sem/Txt

HUMAN

PROP-ATTR
PROP-SUR

TIME-N-SET

###  Syntactic tags

@+FAUXV
@+FMAINV
@-FAUXV
@-FMAINV
@-FSUBJ>
@-F<OBJ
@-FOBJ>
@-FSPRED<OBJ
@-F<ADVL
@-FADVL>
@-F<SPRED
@-F<OPRED
@-FSPRED>
@-FOPRED>
@>ADVL
@ADVL<
@<ADVL
@ADVL>
@ADVL
@HAB>
@<HAB
@>N
@Interj
@N<
@>A
@P<
@>P
@HNOUN
@INTERJ
@>Num
@Pron<
@>Pron
@Num<
@OBJ
@<OBJ
@OBJ>
@OPRED
@<OPRED
@OPRED>
@PCLE
@COMP-CS<
@SPRED
@<SPRED
@SPRED>
@SUBJ
@<SUBJ
@SUBJ>
SUBJ
SPRED
OPRED
@PPRED
@APP
@APP-N<
@APP-Pron<
@APP>Pron
@APP-Num<
@APP-ADVL<
@VOC
@CVP
@CNP
OBJ
<OBJ
OBJ>
<OBJ-OTHERS
OBJ>-OTHERS
SYN-V
@X

## Sets containing sets of lists and tags

This part of the file lists a large number of sets based partly upon the tags defined above, and
partly upon lexemes drawn from the lexicon.
See the sourcefile itself to inspect the sets, what follows here is an overview of the set types.

### Sets for Single-word sets

INITIAL

### Sets for word or not

WORD
NOT-COMMA

### Case sets

ADLVCASE

CASE-AGREEMENT
CASE

NOT-NOM
NOT-GEN
NOT-ACC

### Verb sets

NOT-V

### Sets for finiteness and mood

REAL-NEG

MOOD-V

NOT-PRFPRC

### Sets for person

SG1-V
SG2-V
SG3-V
DU1-V
DU2-V
DU3-V
PL1-V
PL2-V
PL3-V

### Pronoun sets

### Adjectival sets and their complements

### Adverbial sets and their complements

### Sets of elements with common syntactic behaviour

### NP sets defined according to their morphosyntactic features

### The PRE-NP-HEAD family of sets

These sets model noun phrases (NPs). The idea is to first define whatever can
occur in front of the head of the NP, and thereafter negate that with the
expression **WORD - premodifiers**.

### Border sets and their complements

### Grammarchecker sets

* * *
<small>This (part of) documentation was generated from [tools/grammarcheckers/grammarchecker.cg3](https://github.com/giellalt/lang-mdf/blob/main/tools/grammarcheckers/grammarchecker.cg3)</small># Tokeniser for mdf

Usage:
```
$ make
$ echo "ja, ja" | hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
$ echo "Juos gorreválggain lea (dárbbašlaš) deavdit gáibádusa boasttu olmmoš, man mielde lahtuid." | hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
$ echo "(gáfe) 'ja' ja 3. ja? ц jaja ukjend \"ukjend\"" | hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
$ echo "márffibiillagáffe" | hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
```

Pmatch documentation:
<https://github.com/hfst/hfst/wiki/HfstPmatch>

Characters which have analyses in the lexicon, but can appear without spaces
before/after, that is, with no context conditions, and adjacent to words:
* Punct contains ASCII punctuation marks
* The symbol after m-dash is soft-hyphen `U+00AD`
* The symbol following {•} is byte-order-mark / zero-width no-break space
`U+FEFF`.

Whitespace contains ASCII white space and
the List contains some unicode white space characters
* En Quad U+2000 to Zero-Width Joiner U+200d'
* Narrow No-Break Space U+202F
* Medium Mathematical Space U+205F
* Word joiner U+2060

Apart from what's in our morphology, there are
1. unknown word-like forms, and
2. unmatched strings
We want to give 1) a match, but let 2) be treated specially by
`hfst-tokenise -a`
Unknowns are made of:
* lower-case ASCII
* upper-case ASCII
* select extended latin symbols
* mdf specific characters
ASCII digits
* select symbols
* Combining diacritics as individual symbols,
* various symbols from Private area (probably Microsoft),
so far:
* U+F0B7 for "x in box"

## Unknown handling
Unknowns are tagged ?? and treated specially with `hfst-tokenise`
hfst-tokenise --giella-cg will treat such empty analyses as unknowns, and
remove empty analyses from other readings. Empty readings are also
legal in CG, they get a default baseform equal to the wordform, but
no tag to check, so it's safer to let hfst-tokenise handle them.

Finally we mark as a token any sequence making up a:
* known word in context
* unknown (OOV) token in context
* sequence of word and punctuation
* URL in context

* * *

<small>This (part of) documentation was generated from [tools/tokenisers/tokeniser-disamb-gt-desc.pmscript](https://github.com/giellalt/lang-mdf/blob/main/tools/tokenisers/tokeniser-disamb-gt-desc.pmscript)</small>

---

# Grammar checker tokenisation for mdf

Requires a recent version of HFST (3.10.0 / git revision>=3aecdbc)
Then just:
```
$ make
$ echo "ja, ja" | hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
```

More usage examples:
```
$ echo "Juos gorreválggain lea (dárbbašlaš) deavdit gáibádusa boasttu olmmoš, man mielde lahtuid." | hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
$ echo "(gáfe) 'ja' ja 3. ja? ц jaja ukjend \"ukjend\"" | hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
$ echo "márffibiillagáffe" | hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
```

Pmatch documentation:
<https://github.com/hfst/hfst/wiki/HfstPmatch>

Characters which have analyses in the lexicon, but can appear without spaces
before/after, that is, with no context conditions, and adjacent to words:
* Punct contains ASCII punctuation marks
* The symbol after m-dash is soft-hyphen `U+00AD`
* The symbol following {•} is byte-order-mark / zero-width no-break space
`U+FEFF`.

Whitespace contains ASCII white space and
the List contains some unicode white space characters
* En Quad U+2000 to Zero-Width Joiner U+200d'
* Narrow No-Break Space U+202F
* Medium Mathematical Space U+205F
* Word joiner U+2060

Apart from what's in our morphology, there are
1) unknown word-like forms, and
2) unmatched strings
We want to give 1) a match, but let 2) be treated specially by hfst-tokenise -a
* select extended latin symbols
* select symbols
* various symbols from Private area (probably Microsoft),
so far:
* U+F0B7 for "x in box"

TODO: Could use something like this, but built-in's don't include šžđčŋ:

Simply give an empty reading when something is unknown:
hfst-tokenise --giella-cg will treat such empty analyses as unknowns, and
remove empty analyses from other readings. Empty readings are also
legal in CG, they get a default baseform equal to the wordform, but
no tag to check, so it's safer to let hfst-tokenise handle them.

Finally we mark as a token any sequence making up a:
* known word in context
* unknown (OOV) token in context
* sequence of word and punctuation
* URL in context

* * *

<small>This (part of) documentation was generated from [tools/tokenisers/tokeniser-gramcheck-gt-desc.pmscript](https://github.com/giellalt/lang-mdf/blob/main/tools/tokenisers/tokeniser-gramcheck-gt-desc.pmscript)</small>

---

