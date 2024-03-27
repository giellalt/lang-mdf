#!/usr/bin/perl -w
#
# urj-mns-conversion.pl
# Convert names in the URJ propernoun lexicon to mns.

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
	s/ PROP_KIT_FEM/ N_VCH/g ;
	s/ PROP_LAK_MAL/ N_VCH/g ;
	s/ PropNameMaleDer-Y-0Evich/ N_VCS/g ;
	s/ PROP_OSH_SUR/ N_VCH/g ;
	s/ Deriv-RUS-AN_SURMAL/ N_VCH/g ;
	s/ CYRL-L_SUR/ N_VCH/g ;
	s/ Deriv-RUS-IJ_SURMAL/ий N_VCS/g ;
	s/ Deriv-RUS-YJ_SURMAL/ый N_VCS/g ;
	s/ Deriv-RUS-KIJ_SURMAL/ий N_VCS/g ;
	s/ Deriv-RUS-OJ_SURMAL/ой N_VCS/g ;
	s/ CYRL-K_SUR/ N_VCH/g ;
	s/ CYRL-SIBILANT_SUR/ N_VCH/g ;
	s/ Deriv-RUS-IN_SURMAL/ N_VCH/g ;
	s/ Deriv-RUS-V_SURMAL/ N_VCH/g ;
	s/ CYRL-T_SUR/ N_VCH/g ;
	s/ CYRL-CONS_SUR/ N_VCH/g ;
	s/(ы|и) CYRL-VOW_SUR/$1 N_VI/g ;#ordering 1
	s/ CYRL-VOW_SUR/ N_VO/g ;
	s/ CYRL-A_SUR/ N_VO/g ;
	s/ PROP_OSH_MAL/ N_VCH/g ;
	s/ PROP_KIT_MAL/ N_VCH/g ;
	s/ PROP_KUDO_PATRFEM/ N_VO/g ;
	s/ PROP-PLC_KEL1/ N_VCS/g ;
	s/ PROP-PLC_VELE/ N_VO/g ;
	s/ PROP_VELE/ N_VO/g ;
	s/ PROP_KUDO_MAL/ N_VO/g ;
	s/ PropNameMaleDer-Ovich/ N_VCS/g ;
	s/ PROP_OSH_PATRMAL/ N_VCH/g ;
	s/ PropNameMaleDer-IJ-Y0Evich/ий N_VCS/g ;
	s/ PropNameMaleDer-J-0Evich/й N_VCS/g ;
	s/ PropNameMaleDer-IJ-I0Evich/ий N_VCS/g ;
	s/ PropNameMaleDer-I-YEvich/и N_VI/g ;
	s/(ь|й) PROP_KAL_MAL/$1 N_VCS/g ;
	s/ PROP_KAL_MAL/ N_VCH/g ;
	s/(ь|й) PROP_KAL_FEM/$1 N_VCS/g ;
	s/ PROP_KAL_FEM/ N_VCH/g ;
	s/ PROP_OSH_FEM/ N_VCH/g ;
	s/ PROP_KUDO_FEM/ N_VO/g ;
	s/ PROP-PLC_KIT/ N_VCH/g ;
	s/(ь|й) PROP-PLC_KAL/$1 N_VCS/g ;
	s/ PROP-PLC_KAL/ N_VCH/g ;
	s/ PROP-PLC_KUDO/ N_VO/g ;
	s/ PROP_KIT_SUR/ N_VCH/g ;
	
# loanwords with compound border over identical vowels
	s/Hjarteelva/Hjarte-elva/g ;
	

# names with Inari Saami inflection
	s/^Aanaar\+/!Aanaar+/g ;

# sme special symbols
	s/b9/b/g ;

	my $line = $_;

	print $line;
}

