# Moksha documentation

[![Maturity](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fgiellalt%2Flang-mdf%2Fgh-pages%2Fmaturity.json)](https://giellalt.github.io/MaturityClassification.html)
![Lemma count](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fgiellalt%2Flang-mdf%2Fgh-pages%2Flemmacount.json)
[![License](https://img.shields.io/github/license/giellalt/lang-mdf)](https://github.com/giellalt/lang-mdf/blob/main/LICENSE)
[![Issues](https://img.shields.io/github/issues/giellalt/lang-mdf)](https://github.com/giellalt/lang-mdf/issues)
[![Build Status](https://divvun-tc.giellalt.org/api/github/v1/repository/giellalt/lang-mdf/main/badge.svg)](https://github.com/giellalt/lang-mdf/actions)

This page documents the work on the [Moksha language model](http://github.com/giellalt/lang-mdf).

The lexicon is full-sized (60000 entries), and the analyser 
is in use in a morphologically enriched Moksha Mordvin dictionary. 

* Generation of: [paradigms](http://giellatekno.uit.no/cgi/p-mdf.fi.html)

# Project documentation

* Add links to project specific documentation here as needed. Keep the documentation in the `docs/` directory.

# In-source documentation

Below is an autogenerated list of documentation pages built from structured comments in the source code. All pages are also concatenated and can be read as one long text [here](mdf.md).

* `src/`
    * `cg3/`
        * [disambiguator.cg3](src-cg3-disambiguator.cg3.html) ([src](https://github.com/giellalt/lang-mdf/blob/main/src/cg3/disambiguator.cg3))
        * [functions.cg3](src-cg3-functions.cg3.html) ([src](https://github.com/giellalt/lang-mdf/blob/main/src/cg3/functions.cg3))
    * `fst/`
        * `morphology/`
            * `affixes/`
                * [adjectives.lexc](src-fst-morphology-affixes-adjectives.lexc.html) ([src](https://github.com/giellalt/lang-mdf/blob/main/src/fst/morphology/affixes/adjectives.lexc))
                * [adpositions.lexc](src-fst-morphology-affixes-adpositions.lexc.html) ([src](https://github.com/giellalt/lang-mdf/blob/main/src/fst/morphology/affixes/adpositions.lexc))
                * [adverbs.lexc](src-fst-morphology-affixes-adverbs.lexc.html) ([src](https://github.com/giellalt/lang-mdf/blob/main/src/fst/morphology/affixes/adverbs.lexc))
                * [clitics.lexc](src-fst-morphology-affixes-clitics.lexc.html) ([src](https://github.com/giellalt/lang-mdf/blob/main/src/fst/morphology/affixes/clitics.lexc))
                * [conjunctors.lexc](src-fst-morphology-affixes-conjunctors.lexc.html) ([src](https://github.com/giellalt/lang-mdf/blob/main/src/fst/morphology/affixes/conjunctors.lexc))
                * [interjections.lexc](src-fst-morphology-affixes-interjections.lexc.html) ([src](https://github.com/giellalt/lang-mdf/blob/main/src/fst/morphology/affixes/interjections.lexc))
                * [nouns.lexc](src-fst-morphology-affixes-nouns.lexc.html) ([src](https://github.com/giellalt/lang-mdf/blob/main/src/fst/morphology/affixes/nouns.lexc))
                * [numbers.lexc](src-fst-morphology-affixes-numbers.lexc.html) ([src](https://github.com/giellalt/lang-mdf/blob/main/src/fst/morphology/affixes/numbers.lexc))
                * [particles.lexc](src-fst-morphology-affixes-particles.lexc.html) ([src](https://github.com/giellalt/lang-mdf/blob/main/src/fst/morphology/affixes/particles.lexc))
                * [pronouns.lexc](src-fst-morphology-affixes-pronouns.lexc.html) ([src](https://github.com/giellalt/lang-mdf/blob/main/src/fst/morphology/affixes/pronouns.lexc))
                * [propernouns.lexc](src-fst-morphology-affixes-propernouns.lexc.html) ([src](https://github.com/giellalt/lang-mdf/blob/main/src/fst/morphology/affixes/propernouns.lexc))
                * [symbols.lexc](src-fst-morphology-affixes-symbols.lexc.html) ([src](https://github.com/giellalt/lang-mdf/blob/main/src/fst/morphology/affixes/symbols.lexc))
                * [verbs.lexc](src-fst-morphology-affixes-verbs.lexc.html) ([src](https://github.com/giellalt/lang-mdf/blob/main/src/fst/morphology/affixes/verbs.lexc))
            * [phonology.twolc](src-fst-morphology-phonology.twolc.html) ([src](https://github.com/giellalt/lang-mdf/blob/main/src/fst/morphology/phonology.twolc))
            * [root.lexc](src-fst-morphology-root.lexc.html) ([src](https://github.com/giellalt/lang-mdf/blob/main/src/fst/morphology/root.lexc))
            * `stems/`
                * [adjectives-russian-like_newwords.lexc](src-fst-morphology-stems-adjectives-russian-like_newwords.lexc.html) ([src](https://github.com/giellalt/lang-mdf/blob/main/src/fst/morphology/stems/adjectives-russian-like_newwords.lexc))
                * [adjectives_newwords.lexc](src-fst-morphology-stems-adjectives_newwords.lexc.html) ([src](https://github.com/giellalt/lang-mdf/blob/main/src/fst/morphology/stems/adjectives_newwords.lexc))
                * [exceptions.lexc](src-fst-morphology-stems-exceptions.lexc.html) ([src](https://github.com/giellalt/lang-mdf/blob/main/src/fst/morphology/stems/exceptions.lexc))
                * [nouns_newwords.lexc](src-fst-morphology-stems-nouns_newwords.lexc.html) ([src](https://github.com/giellalt/lang-mdf/blob/main/src/fst/morphology/stems/nouns_newwords.lexc))
                * [propernouns_newwords.lexc](src-fst-morphology-stems-propernouns_newwords.lexc.html) ([src](https://github.com/giellalt/lang-mdf/blob/main/src/fst/morphology/stems/propernouns_newwords.lexc))
                * [verbs_newwords.lexc](src-fst-morphology-stems-verbs_newwords.lexc.html) ([src](https://github.com/giellalt/lang-mdf/blob/main/src/fst/morphology/stems/verbs_newwords.lexc))
        * `phonetics/`
            * [txt2ipa.xfscript](src-fst-phonetics-txt2ipa.xfscript.html) ([src](https://github.com/giellalt/lang-mdf/blob/main/src/fst/phonetics/txt2ipa.xfscript))
        * `transcriptions/`
            * [transcriptor-abbrevs2text.lexc](src-fst-transcriptions-transcriptor-abbrevs2text.lexc.html) ([src](https://github.com/giellalt/lang-mdf/blob/main/src/fst/transcriptions/transcriptor-abbrevs2text.lexc))
* `tools/`
    * `grammarcheckers/`
        * [grammarchecker.cg3](tools-grammarcheckers-grammarchecker.cg3.html) ([src](https://github.com/giellalt/lang-mdf/blob/main/tools/grammarcheckers/grammarchecker.cg3))
    * `tokenisers/`
        * [tokeniser-disamb-gt-desc.pmscript](tools-tokenisers-tokeniser-disamb-gt-desc.pmscript.html) ([src](https://github.com/giellalt/lang-mdf/blob/main/tools/tokenisers/tokeniser-disamb-gt-desc.pmscript))
        * [tokeniser-gramcheck-gt-desc.pmscript](tools-tokenisers-tokeniser-gramcheck-gt-desc.pmscript.html) ([src](https://github.com/giellalt/lang-mdf/blob/main/tools/tokenisers/tokeniser-gramcheck-gt-desc.pmscript))
        * [tokeniser-tts-cggt-desc.pmscript](tools-tokenisers-tokeniser-tts-cggt-desc.pmscript.html) ([src](https://github.com/giellalt/lang-mdf/blob/main/tools/tokenisers/tokeniser-tts-cggt-desc.pmscript))