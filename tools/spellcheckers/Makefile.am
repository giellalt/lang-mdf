## Process this file with automake to produce Makefile.in
## Copyright: Sámediggi/Divvun/UiT
## Licence: GPL v3+

# The current dir must be built first.
SUBDIRS = filters . fstbased

#########################################
# BEGIN: Local processing
#
# Target template:
#
# analyser-speller-gt-norm.%: analyser-speller-gt-norm.tmp.%
#	build rules

generator-speller-gt-norm.%: analyser-speller-gt-norm.tmp.% \
				$(top_builddir)/src/filters/remove-hard-sign-in-first-syllable.%   
	$(AM_V_XFST_TOOL)$(PRINTF) "read regex                                    \
			@\"$<\"                                                          \
		.o. @\"$(top_builddir)/src/filters/remove-hard-sign-in-first-syllable.$*\"   \
			;\n\
		 $(INVERT_XFST)$(INVERT_FOMA)\
		save stack $@\n\
		quit\n" | $(XFST_TOOL)

analyser-speller-gt-norm.%: analyser-speller-gt-norm.tmp.% \
				$(top_builddir)/src/filters/remove-hard-sign-in-first-syllable.%   
	$(AM_V_XFST_TOOL)$(PRINTF) "read regex                                    \
			@\"$<\"                                                          \
		.o. @\"$(top_builddir)/src/filters/remove-hard-sign-in-first-syllable.$*\"   \
			;\n\
		$(INVERT_HFST)\
		save stack $@\n\
		quit\n" | $(XFST_TOOL)


# END: Local processing
#########################################

include $(top_srcdir)/am-shared/tools-spellcheckers-dir-include.am
