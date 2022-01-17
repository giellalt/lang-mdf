
# Morphology
INTRODUCTION TO MORPHOLOGICAL ANALYSER OF THE Moksha LANGUAGE.


The morphological analyses of wordforms of the Moksha language are presented
in this system in terms of following symbols.
(It is highly suggested to follow existing standards when adding new tags).
 +TYÄ 	 Underdeveloped.



The parts-of-speech tags are:

* **+Aadjective**:  adjective
* **+Advadverb**:  adverb
* **+CSconjunction**:  subordinating conjunction
* **+CCconjunction**:  coordinating conjunction
* **+DetDeterminer**:  Determiner
* **+Interjinterjection**:  interjection
* **+Nnoun**:  noun
* **+Pcleparticle**:  particle
* **+Popostposition**:  postposition
* **+Pronpronoun**:  pronoun
* **+QntQuantifier**:  Quantifier
* **+Vverb**:  verb

* **+Descrdescriptive**:  descriptive

The parts of speech are further split up into:
**Nouns:**
* **+Propproper**:  proper
* **+CollNnouns****:  used with paired nouns **collective nouns**
* **+Relator**:  relator nouns, mainly meronyms 
**Pronouns:**
* **+Demdemonstrative**:  demonstrative
* **+Indefindefinite**:  indefinite
* **+Dep**мень****:  dependent word requiring the presence of another, e.g. **мень**
* **+Exclusiveськамонза**:  ськамонза
* **+Intensivepronoun**:  intensive pronoun
* **+Interrinterrogative**:  interrogative
* **+PerifModкавонест**:  periferal modifier ськамонза, кавонест
* **+Perspersonal**:  personal
* **+Reciprreciprocal**:  reciprocal
* **+Reflreflexive**:  reflexive
* **+Recipreflexive**:  reflexive
* **+Relrelative**:  relative
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
* +Err/Orth-lowered-final-e-2-jatrigger final е lowered to я with Е2Я trigger

* _+Use/MargMarginal_ * Marginal
* _+Use/-Spellspeller_ * Exclude from speller
* _+Use/SpellNoSuggspeller_ * recognized but not suggested in speller
* _+Use/Circpath_ * Circular path
* _+Use/CircNpath_ * Circular number path
* _+Use/-Pedspeller_ * Remove from pedagogical speller
* _+Use/NGapertium_ * Do not generate, for isme-ped.fst and apertium

* _+Err/Dialстякшемс_ * The form is non-standard although it may well be central dialect, e.g. стякшемс
* _+Err/Lexword_ * The lemma is not a Moksha word

# Dialect tags
* +Dialspecification * No specification
Specific to some dialects
* +Dial/-Cstandard * Not central standard


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
* _+Iter+Mult_ Iterative This will be replaced by +Mult
* _+Mult`кыкысь`_ Multiplicative form expressing number of times; myv: `кавксть`, kpv: `кыкысь`
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
* +Symbol© = independent symbols in the text stream, like £, €, ©
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
* +Romnumerals Roman numerals

Compounding
* +Cmpcompound. Dynamic compound - this tag should always be part of a dynamic compound.
It is important for Apertium, and useful in other cases as well.
* +Cmp/Hyphnouns with nouns
* +Cmp/Hyph-Collnouns with nouns
* +Cmp/Hyph-Redupverbs with verbs
* +Cmp/Hyph-Synonymverbs with verbs
* +Cmp/Hyph-Serialverbs with verbs
* +Cmp/Hyph-tejemsverbs with verbs

Question and Focus particles:
* +Clt/Copinflection This marks all instances of enclitic copula inflection
* +Clt/Aramopinion' Used with preceding dative тейне-арам 'in my opinion'
* +Clt/Add 
* +Clt/AddGA 
* +Clt/AddVok 
* +Clt/AddNgA 




### Tags distinguishing different versions of the same lemma (before POS)
* +v1@CODE@
* +v2@CODE@
* +v3@CODE@
* +v4@CODE@
* +v5@CODE@
* +v6@CODE@
* +v7@CODE@
* +v8@CODE@
* +v9@CODE@
* +v10@CODE@
* +v11@CODE@
* +v12@CODE@
* +v13@CODE@
* +v14@CODE@
* +v15@CODE@
* +v16@CODE@
* +v17@CODE@
* +v18@CODE@
* +v19@CODE@
* +v20@CODE@
* +v21@CODE@
* +v22@CODE@
* +v23@CODE@
* +v24@CODE@

* **+Sem/ActActivity** Activity
* **+Sem/AmountAmount** Amount
* **+Sem/AniAnimate** Animate
* **+Sem/AniprodProduct** Animal Product
* **+Sem/BodyBodypart** Bodypart
* **+Sem/Body-abstrjierbmi** siellu, vuoig?a, jierbmi
* **+Sem/BuildBuilding** Building
* **+Sem/Build-partcloset** Part of Bulding, like the closet
* **+Sem/CatCategory** Category
* **+Sem/ClthClothes** Clothes
* **+Sem/Clth-jewlJewelery** Jewelery
* **+Sem/Clth-partsávdnji...** part of clothes, boallu, sávdnji...
* **+Sem/CtainContainer** Container
* **+Sem/Ctain-abstraccount** Abstract container like bank account
* **+Sem/Ctain-clth**@CODE@****
* **+Sem/CurrMoney** Currency like dollár, Not Money
* **+Sem/DanceDance** Dance
* **+Sem/DirGPS-kursa** Direction like GPS-kursa
* **+Sem/Domainactions)** Domain like politics, reindeerherding (a system of actions)
* **+Sem/DrinkDrink** Drink
* **+Sem/DummytagDummytag** Dummytag
* **+Sem/Eduevent** Educational event
* **+Sem/EventEvent** Event
* **+Sem/FeatÁrvu** Feature, like Árvu
* **+Sem/Feat-physfárda** Physiological feature, ivdni, fárda
* **+Sem/Feat-psychfeauture** Psychological feauture
* **+Sem/Feat-measrfeauture** Psychological feauture
* **+Sem/Femname** Female name
* **+Sem/Fem-Patrname** Female name
* **+Sem/Fem-Surname** Female name
* **+Sem/FoodFood** Food
* **+Sem/Food-medMedicine** Medicine
* **+Sem/FurnFurniture** Furniture
* **+Sem/GameGame** Game
* **+Sem/Geomobject** Geometrical object
* **+Sem/GroupGroup** Animal or Human Group
* **+Sem/HumHuman** Human
* **+Sem/Hum-abstrabstract** Human abstract
* **+Sem/IdeolIdeology** Ideology
* **+Sem/LangLanguage** Language
* **+Sem/Malname** Male name
* **+Sem/Mal-Patrname** Male name
* **+Sem/Mal-Surname** Male name
* **+Sem/Matthings** Material for producing things
* **+Sem/MeasrMeasure** Measure
* **+Sem/MoneyCurr(ency)** Has to do with money, like wages, not Curr(ency)
* **+Sem/ObjObject** Object
* **+Sem/Obj-cloCloth** Cloth
* **+Sem/Obj-cognCloth** Cloth
* **+Sem/Obj-elapparatus** (Electrical) machine or apparatus
* **+Sem/Obj-lingit** Object with something written on it
* **+Sem/Obj-ropeobject** flexible ropelike object
* **+Sem/Obj-surfcobject** Surface object
* **+Sem/OrgOrganisation** Organisation
* **+Sem/Partbealli** Feature, oassi, bealli
* **+Sem/Perc-cognperception** Cognative perception
* **+Sem/Perc-emoperception** Emotional perception
* **+Sem/Perc-physperception** Physical perception
* **+Sem/Perc-psychperception** Physical perception
* **+Sem/PlantPlant** Plant
* **+Sem/Plant-partpart** Plant part
* **+Sem/PlcPlace** Place
* **+Sem/Plc-abstrplace** Abstract place
* **+Sem/Plc-elevatePlace** Place
* **+Sem/Plc-linePlace** Place
* **+Sem/Plc-waterPlace** Place
* **+Sem/Posjob)** Position (as in social position job)
* **+Sem/ProcessProcess** Process
* **+Sem/ProdProduct** Product
* **+Sem/Prod-audioproduct** Audio product
* **+Sem/Prod-cognproduct** Cognition product
* **+Sem/Prod-lingproduct** Linguistic product
* **+Sem/Prod-visproduct** Visual product
* **+Sem/RelRelation** Relation
* **+Sem/RouteRoute** Name of a Route
* **+Sem/Ruleconvention** Rule or convention
* **+Sem/Semconconcept** Semantic concept
* **+Sem/Sign** Sign (e.g. numbers, punctuation) 
* **+Sem/SportSport** Sport
* **+Sem/State** 
* **+Sem/State-sickIllness** Illness
* **+Sem/SubstncWater** Substance, like Air and Water
* **+Sem/SurSurname** Surname
* **+Sem/SymbolSymbol** Symbol
* **+Sem/TimeTime** Time
* **+Sem/Toolthings** Prototypical tool for repairing things
* **+Sem/Tool-catchfish)** Tool used for catching (e.g. fish)
* **+Sem/Tool-cleancleaning** Tool used for cleaning
* **+Sem/Tool-itIT** Tool used in IT
* **+Sem/Tool-measrmeasuring** Tool used for measuring
* **+Sem/Tool-musicinstrument** Music instrument
* **+Sem/Tool-writetool** Writing tool
* **+Sem/Txtlávlla...)** Text (girji, lávlla...)
* **+Sem/VehVehicle** Vehicle
* **+Sem/WpnWeapon** Weapon
* **+Sem/Wthrground** The Weather or the state of ground





Semantics are classified with
* **+Sem/Kinterm** Kin term



Derivations are classified under the morphophonetic form of the suffix, the
source and target part-of-speech.


## Der begin
*  **+Derit**  In front of every derivation to make it
possible to target derivations as a class e.g. in regular expressions etc
*  **+Der/Possаванне**  possessive noun ава » аванне
*  **+Der/Ord**  
*  **+Der/Iterколмоксть...**  весть, кафксть, колмоксть...
*  **+Der/Wifepatronymics**  Added to male names, surnames, patronymics

## DECLARING DEVERBAL DERIVATIONS OF VERBS
* +Der/kshnOderivation  verb2verb derivation
* +Der/OkshnOmsderivation  verb2verb derivation
* +Der/OvOmsderivation  verb2verb derivation
* +Der/OvkshnOmsderivation  verb2verb derivation
* +Der/OvtOmsderivation  verb2verb derivation

  +Der/Dimin	 diminutive markers in ня and кя seem to be subject of complementary distribution
* +Der/NJОнь Онь
* +Der/Bachkбачк * бачк

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
|  @P.NeedNoun.ON@nominalised | (Dis)allow compounds with verbs unless nominalised
|  @D.NeedNoun.ON@nominalised | (Dis)allow compounds with verbs unless nominalised
|  @C.NeedNoun@nominalised | (Dis)allow compounds with verbs unless nominalised

For languages that allow compounding, the following flag diacritics are needed
to control position-based compounding restrictions for nominals. Their use is
handled automatically if combined with +CmpN/xxx tags. If not used, they will
do no harm.
|  @P.CmpFrst.FALSE@first | Require that words tagged as such only appear first
|  @D.CmpPref.TRUE@ENDLEX | Block such words from entering ENDLEX
|  @P.CmpPref.FALSE@compounds | Block these words from making further compounds
|  @D.CmpLast.TRUE@R | Block such words from entering R
|  @D.CmpNone.TRUE@compounding | Combines with the next tag to prohibit compounding
|  @U.CmpNone.FALSE@compounding | Combines with the prev tag to prohibit compounding
|  @P.CmpOnly.TRUE@R | Sets a flag to indicate that the word has passed R
|  @D.CmpOnly.FALSE@root. | Disallow words coming directly from root.

Use the following flag diacritics to control downcasing of derived proper
nouns (e.g. Finnish Pariisi -> pariisilainen). See e.g. North Sámi for how to use
these flags. There exists a ready-made regex that will do the actual down-casing
given the proper use of these flags.
|  @U.Cap.Obl@deatnulasj. | Allowing downcasing of derived names: deatnulasj.
|  @U.Cap.Opt@deatnulasj. | Allowing downcasing of derived names: deatnulasj.






 @D.CONJ-MX.IND@ 	 2012-11-04 should this be **D** or **N**











# FLAGS USED WITH MODIFIERS WITHOUT NOUNS

# FLAGS USED WITH COLLECTIVE NOUNS
## number
* @U.DECL-NX.SG@@CODE@
* @U.DECL-NX.SP@@CODE@
* @U.DECL-NX.PL@@CODE@
* @R.DECL-NX.SG@@CODE@
* @R.DECL-NX.SP@@CODE@
* @R.DECL-NX.PL@@CODE@

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
<small>This (part of) documentation was generated from [../src/fst/root.lexc](http://github.com/giellalt/lang-mdf/blob/main/../src/fst/root.lexc)</small>