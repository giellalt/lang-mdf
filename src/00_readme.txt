## Thanks to the people at Giellatekno In Tromsø for their work 
# and continued assistance, especially Børre, Ciprian, Sjur and Trond
# Since 2004
## Thanks to Kone Säätiö (The Kone Foundation in Helsinki) funding 
# Since 2012
#
## This project is based on several elements of Moksha research:
# xfst twolc and lexc of Moksha by © Jack Rueter OPEN-SOURCE
# The Moksha-Finnish dictionary (Мокшень-финнонь валкс, mokšalais-suomalainen sanakirja 1998, 2000)
# The Moksha-Russian Dictionary 1997
# Wordlists by Jorma Luutonen 2007
 

##(1)##
# The spellchecker, and the hfst analyser
In This directory:

make lexfiles
make -f Makefile.hfst

# Test with
echo "кал" |hfst-lookup ../bin/mdf.hfstol 


##(2)##
# The Apertium dictionary

##(3)##
# The xerox analyser, in this directory:

make lexfiles
make
