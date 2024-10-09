#!/usr/bin/perl -w
#
# urj-mdf-conversion.pl
# Convert names in the URJ propernoun lexicon to mdf.

use strict;
use utf8;
use feature 'unicode_strings';
BEGIN {
       $| = 1;
       binmode(STDIN, ':encoding(UTF-8)');
       binmode(STDOUT, ':encoding(UTF-8)');
}
use open qw( :encoding(UTF-8) :std );

while(<>) {
	# Continuation lexicon substitutions:
#	s/ C-FI-NEN/nen LONDON/g ;
	s/ PROP_KAL_PLC/ PROP_KAL/g ;
	s/ PROP_KUDO_PLC/ PROP_AVA/g ;
	s/ PROP_OSH_PLC/ PROP_OSH/g ;
	s/ PROP-PLC_KEL1/ PROP_KIAL1/g ;
	s/ PROP-PLC_VELE/ PROP_TISHE/g ;
	s/ PROP_VELE/ PROP_TISHE/g ;
	s/ PROP-PLC_KUDO/ PROP_AVA/g ;
	s/ PROP_KUDO/ PROP_AVA/g ;
	s/ PROP_RUS_JA/ PROP_AVA/g ;

	
# loanwords with compound border over identical vowels
	s/Hjarteelva/Hjarte-elva/g ;
	

# names with Inari Saami inflection
	s/^Aanaar\+/!Aanaar+/g ;

# sme special symbols
	s/b9/b/g ;

	my $line = $_;

	print $line;
}

