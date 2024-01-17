## Process this file with automake to produce Makefile.in
## Copyright: Sámediggi/Divvun/UiT
## Licence: GPL v3+

SUBDIRS = fst cg3

#################################################
#### Add language-specific build rules here: ####

# We need to add processing of language-specific tags in the analyser:
analyser-gt-desc.hfst\
analyser-gt-desc.foma\
analyser-gt-desc.xfst: \
analyser-gt-desc.%: analyser-gt-desc.tmp.% \
					filters/remove-derivation-position-tags.% \
					filters/remove-norm-comp-tags.%             \
					filters/remove-hard-sign-in-first-syllable.%
	$(AM_V_XFST_TOOL)$(PRINTF) "read regex \
			    @\"filters/remove-derivation-position-tags.$*\" \
			.o. @\"filters/remove-norm-comp-tags.$*\"           \
			.o. @\"$<\"                                         \
			.o. @\"filters/remove-hard-sign-in-first-syllable.$*\" \
			;\n\
		 $(INVERT_HFST)\
		 save stack $@\n\
		 quit\n" | $(XFST_TOOL)

# And also for the normative analyser (foma and hfst):
analyser-gt-norm.hfst\
analyser-gt-norm.foma:\
analyser-gt-norm.%: analyser-gt-norm.tmp.% \
					filters/remove-illegal-derivation-strings-flagbased.% \
					filters/insert-default-compounding-tags.% \
					filters/insert-default_left_compounding-tags.% \
					filters/block-illegal_compound-strings.%  \
					filters/split-CmpN-tags.% \
					filters/convert_to_flags-CmpNP-tags.% \
					filters/split-CmpNP-tags.% \
					filters/remove-hard-sign-in-first-syllable.%
	$(AM_V_XFST_TOOL)$(PRINTF) "read regex \
				@\"filters/block-illegal_compound-strings.$*\"          \
			.o. @\"filters/split-CmpN-tags.$*\"                         \
			.o. @\"filters/insert-default_left_compounding-tags.$*\"    \
			.o. @\"filters/insert-default-compounding-tags.$*\"         \
			.o. @\"filters/remove-illegal-derivation-strings-flagbased.$*\" \
			.o. @\"filters/convert_to_flags-CmpNP-tags.$*\"            \
			.o. @\"filters/split-CmpNP-tags.$*\"                       \
			.o. @\"$<\"                                                \
			.o. @\"filters/remove-hard-sign-in-first-syllable.$*\"                \
			;\n\
		 twosided flag-diacritics\n\
		 $(INVERT_HFST)\
		 save stack $@\n\
		 quit\n" | $(XFST_TOOL)

# The operation 'twosided flag-diacritics" crashes Xerox badly, so we do with
# a simpler, less restrictive normative fst when building with Xerox:
analyser-gt-norm.xfst: analyser-gt-norm.tmp.xfst \
					filters/remove-norm-comp-tags.xfst                \
					filters/remove-derivation-position-tags.xfst      \
					filters/remove-illegal-derivation-strings.xfst    \
					filters/remove-hard-sign-in-first-syllable.xfst
	$(AM_V_XFST)$(PRINTF) "read regex \
				@\"filters/remove-norm-comp-tags.xfst\"                \
			.o. @\"filters/remove-derivation-position-tags.xfst\"      \
			.o. @\"filters/remove-illegal-derivation-strings.xfst\"    \
			.o. @\"$<\"                                                \
			.o. @\"filters/remove-hard-sign-in-first-syllable.xfst\"              \
			;\n\
		 save stack $@\n\
		 quit\n" | $(XFST) $(VERBOSITY)


# We need special treatment of the disamb fst going to further pmatch processing
# mainly due to the target pattern, thus listed here. The rule body and the
# dependencies should be the same as the regular disamb analysers below:
analyser-pmatchdisamb-gt-desc.hfst: analyser-pmatchdisamb-gt-desc.tmp.hfst \
				filters/remove-norm-comp-tags.hfst             \
				filters/remove-derivation-position-tags.hfst   \
				filters/remove-orig_lang-tags.hfst             \
				filters/remove-hard-sign-in-first-syllable.hfst  \
				filters/rename-POS_before_Der-tags.hfst        
	$(AM_V_HXFST)$(PRINTF) "read regex \
		    @\"filters/remove-derivation-position-tags.hfst\" \
		.o. @\"filters/remove-norm-comp-tags.hfst\"           \
		.o. @\"filters/remove-orig_lang-tags.hfst\"           \
		.o. @\"filters/rename-POS_before_Der-tags.hfst\"      \
		.o. @\"$<\"                                           \
		.o. @\"filters/remove-hard-sign-in-first-syllable.hfst\"              \
		;\n\
	invert net\n\
	save stack $@\n\
	quit\n" | $(HFST_XFST) -p $(MORE_VERBOSITY)


# Special case for the disamb analyser, since it follows the same filename
# pattern as the raw fst:
analyser-disamb-gt-desc.hfst\
analyser-disamb-gt-desc.foma\
analyser-disamb-gt-desc.xfst: \
analyser-disamb-gt-desc.%: analyser-disamb-gt-desc.tmp.%           \
					filters/remove-derivation-position-tags.%      \
					filters/remove-norm-comp-tags.%                \
					filters/remove-orig_lang-tags.%                \
					filters/remove-dialect-tags.%                  \
					filters/remove-homonymy-tags.%                 \
					filters/remove-hard-sign-in-first-syllable.%              \
					filters/rename-POS_before_Der-tags.%
	$(AM_V_XFST_TOOL)$(PRINTF) "read regex \
				@\"filters/remove-derivation-position-tags.$*\"      \
			.o. @\"filters/remove-orig_lang-tags.$*\"                \
			.o. @\"filters/remove-dialect-tags.$*\"                  \
			.o. @\"filters/remove-homonymy-tags.$*\"                 \
			.o. @\"filters/remove-norm-comp-tags.$*\"                \
			.o. @\"filters/rename-POS_before_Der-tags.$*\"           \
			.o. @\"$<\"                                              \
			.o. @\"filters/remove-hard-sign-in-first-syllable.$*\"              \
			;\n\
		 $(INVERT_HFST)\
		 save stack $@\n\
		 quit\n" | $(XFST_TOOL)

# We need to add processing of language-specific tags in the generator:
define giella_generators
generator-gt-%.$(1): generator-gt-%.tmp.$(1) \
					 filters/remove-derivation-position-tags.$(1)      \
					 filters/remove-norm-comp-tags.$(1)                \
					 filters/remove-hard-sign-in-first-syllable.$(1)
	$$(AM_V_XFST_TOOL)$$(PRINTF) "read regex \
				@\"filters/remove-derivation-position-tags.$(1)\"      \
			.o. @\"filters/remove-norm-comp-tags.$(1)\"                \
			.o. @\"$$<\"                                               \
			.o. @\"filters/remove-hard-sign-in-first-syllable.$(1)\"              \
			;\n\
		 $$(INVERT_XFST)$$(INVERT_FOMA)\
		 save stack $$@\n\
		 quit\n" | $$(XFST_TOOL)
endef
$(foreach fst,hfst xfst foma,$(eval $(call giella_generators,$(fst))))

# Do NOT apply the accent removal filters to the normative
# dictionary generator:
generator-dict-gt-norm.hfst\
generator-dict-gt-norm.foma\
generator-dict-gt-norm.xfst: \
generator-dict-gt-norm.%: generator-dict-gt-norm.tmp.% \
					filters/remove-derivation-position-tags.% \
					filters/remove-norm-comp-tags.%
	$(AM_V_XFST_TOOL)$(PRINTF) "read regex \
				@\"filters/remove-derivation-position-tags.$*\" \
			.o. @\"filters/remove-norm-comp-tags.$*\"           \
			.o. @\"$<\"                                         \
			;\n\
		 $(INVERT_XFST)$(INVERT_FOMA)\
		 save stack $@\n\
		 quit\n" | $(XFST_TOOL)




##################################################################
#### END: Add local processing instructions ABOVE this line ######
##################################################################

include $(top_srcdir)/../giella-core/am-shared/src-dir-include.am
