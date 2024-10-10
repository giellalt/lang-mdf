
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
* **+Relat**:  relator nouns, mainly meronyms 
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
* **+Recip**:  reciprocal
* **+Refl**:  reflexive
* **+Rel**:  relative
personal pronouns use additional tags:
```
 +Sg1 +Sg2 +Sg3 +Pl1 +Pl2 +Pl3 
```
Adverbs:
* ** +Adv-Ideoph 	: These are ideophonic descriptors used to modify the verb**: 
*вырк ливтясь*  "**flit** and it flew off"
* ; +Deg 	     : This is degree, depricate + AdA
* ** +Manner     **:  with reference to type of adverb
* ** +Spat 	     **:  spatial
* ** +Temp 	     **:  temporal
* ** +Emphatic   **:  used with negation particles афи, 
* **+EvidNfh**:  кле

Interjections:
* ** +Formulaic  **:  greetings,
The Usage extents are marked using following tags:
* ** +Err/Orth    **:  substandard / outside the written norm
* +Err/Orth-lowered-final-e-2-ja final е lowered to я with Е2Я trigger
* +Err/Orth-soft-loss $тиендсазь €тиендьсазь
* +Err/Orth-soft-kept шяярьня
* +Err/Orth-colloq Евсеич
* +Err/Orth-old1 * old1 like озимь, морковь 1930–1940
* +Err/Orth-pre1978 * orthography preceding 1978
* +Err/Orth-pre2012 * previous orthography

* _+Use/Marg_ * Marginal
* _+Use/-Spell_ * Exclude from speller
* _+Use/SpellNoSugg_ * recognized but not suggested in speller
* _+Use/Circ_ * Circular path
* _+Use/CircN_ * Circular number path
* _+Use/-Ped_ * Remove from pedagogical speller
* _+Use/NG_ * Do not generate, for isme-ped.fst and apertium

* _+Err/Dial_ * The form is non-standard although it may well be central dialect, e.g. стякшемс
* _+Err/Lex_ * The lemma is not a Moksha word

* +URL * For tagging URLs

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
* ** +Cmpos		**:  compositional numeral 14, 24, 34, 44 нилие, 
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

# Tags for originating language

The following tags are used to guide conversion to IPA: loan words
and foreign names are usually pronounced (approximately) as in the
originating (majority) language. Instead of trying to identify the
correct pronunciation based on phonotactics (orthotactics actually),
we tag all words that can't be correctly transcribed using the SME
transcriber with source language codes. Once tagged, it is possible
to split the lexical transducer in smaller ones according to langu-
age, and apply different IPA conversion to each of them.
The principle of tagging is that we only tag to the extent needed,
and following a priority:
1. any untagged word is pronounced with SME orthographic conventions
1. NNO and NOB have identical pronunciation, NNO is only used if
different in spelling from NOB
1. SWE has mostly the same pronunciation as NOB, and is only used
if different in spelling from NOB
1. Occasionally even SME (the default) may be tagged, to block other
languages from being specified, mainly during semi-automatic
language tagging sessions
All in all, we want to get as much correctly transcribed to IPA
with as little work as possible. On the other hand, if more words
are tagged than strictly needed, this should pose no problem as
long as the IPA conversion is correct - at least some words will
get the same pronunciation whether read as SME or NOB/NNO/SWE.

* **+OLang/CHV** = Chuvash
* **+OLang/MDF** = Moksha
* **+OLang/MYV** = Erzya
* **+OLang/RUS** = Russian
* **+OLang/TAT** = Tatar

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
%^ЬKEEP		 retains soft sign, breaks pattern for removal шяярьня
%^Ъ2PED		 brings out hard sign, which is otherwise automatically removed
%^Е2О		 Change stem-final vowel сембе:сембось
%^Е2А		 Change stem-final vowel мельге:мельганза
%^Я2А		 Change stem-final vowel рьвя:рьванц
%^А2Е		 Change stem-final vowel мокша:мокшесь
%^Е2Я		 Change word-final vowel for dialect тувотне > тувотня
%^Devoice	 for devoicing изь:исть
%^PXSG1		 кядне, ярмаконе не vs %{ЕОØ%}не
%^CnsSt		 улемс:уль%^CnsSt%>%{АЕØ%}	

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

* **+Use/TTS** – **only** retained in the HFST Text-To-Speech disambiguation tokeniser
* **+Use/-TTS** – **never** retained in the HFST Text-To-Speech disambiguation tokeniser

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

| Flag diacritic | Explanation
| :------------- |:-----------
| @U.number.one@ | Flag used to give arabic numerals in smj different cases ;
| @U.number.two@ | Flag used to give arabic numerals in smj different cases ;
| @U.number.three@ | Flag used to give arabic numerals in smj different cases ;
| @U.number.four@ | Flag used to give arabic numerals in smj different cases ;
| @U.number.five@ | Flag used to give arabic numerals in smj different cases ;
| @U.number.six@ | Flag used to give arabic numerals in smj different cases ;
| @U.number.seven@ | Flag used to give arabic numerals in smj different cases ;
| @U.number.eight@ | Flag used to give arabic numerals in smj different cases ;
| @U.number.nine@ | Flag used to give arabic numerals in smj different cases ;
| @U.number.zero@ | Flag used to give arabic numerals in smj different cases ;

The word forms in Moksha language start from the lexeme roots of basic
word classes, or optionally from prefixes:
These have been slightly modified from kpv and myv

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/root.lexc](https://github.com/giellalt/lang-mdf/blob/main/src/fst/morphology/root.lexc)</small>
