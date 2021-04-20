The Moksha morphology and tools
==========================================

This repository contains finite state source files for the Moksha language,
for building morphological analysers, proofing tools
and dictionaries. The data and implementation are licenced under GNU GPL
licence, also detailed in the
[LICENCE](https://github.com/giellalt/lang-mdf/blob/develop/LICENCE). The
authors named in the AUTHORS file are available to grant other licencing
choices.

[![GitHub issues](https://img.shields.io/github/issues-raw/giellalt/lang-mdf)](https://github.com/giellalt/lang-mdf/issues)
[![Build Status](https://github.com/giellalt/lang-mdf/workflows/Speller%20CI+CD/badge.svg)](https://github.com/giellalt/lang-mdf/actions)
[![License](https://img.shields.io/github/license/giellalt/lang-mdf)](https://raw.githubusercontent.com/giellalt/lang-mdf/develop/LICENSE)

Install proofing tools and [keyboards](https://github.com/giellalt/keyboard-mdf)
for the Moksha language by using the [Divvun Installer](http://divvun.no)
(some languages are only available via the nightly channel).

Cite
------

Rueter, J., Hämäläinen, M., & Partanen, N. (2020). [Open-Source Morphology for Endangered Mordvinic Languages](https://www.aclweb.org/anthology/2020.nlposs-1.13/). In Proceedings of Second Workshop for NLP Open Source Software (NLP-OSS) (pp. 94–100). The Association for Computational Linguistics.

Documentation
-------------

Documentation can be found at:

-   <https://giellalt.uit.no/lang/mdf/MokshaDocumentation.html>
-   <https://giellalt.uit.no/index.html>

Core dependencies
-----------------

In order to compile and use Moksha language morphology and
dictionaries, you need:

- an FST compiler: [HFST](https://github.com/hfst/hfst), [Foma](https://github.com/mhulden/foma) or [Xerox Xfst](https://web.stanford.edu/~laurik/fsmbook/home.html)
- [VislCG3](https://visl.sdu.dk/svn/visl/tools/vislcg3/trunk) Constraint Grammar tools

To install VislCG3 and HFST, just copy/paste this into your Terminal on **Mac OS X**:

```
curl https://apertium.projectjj.com/osx/install-nightly.sh | sudo bash
```

or terminal on **Ubuntu, Debian or Windows Subsystem for Linux**:

```
wget https://apertium.projectjj.com/apt/install-nightly.sh -O - | sudo bash
sudo apt-get install cg3 hfst
```

or terminal on **RedHat, Fedora, CentOS or Windows Subsystem for Linux**:

```
wget https://apertium.projectjj.com/rpm/install-nightly.sh -O - | sudo bash
sudo dnf install cg3 hfst
```

Alternatively, the Apertium wiki has good instructions on how to [install the dependencies for Mac
OS X](https://wiki.apertium.org/wiki/Apertium_on_Mac_OS_X) and how to [install
the dependencies on
linux](https://wiki.apertium.org/wiki/Installation_of_grammar_libraries)

Further details and dependencies are described on the GiellaLT [Getting Started](https://giellalt.uit.no/infra/GettingStarted.html) pages.

Downloading
-----------

Using Git:
```
git clone https://github.com/giellalt/lang-mdf
```

Using Subversion:
```
svn checkout https://github.com/giellalt/lang-mdf.git/trunk lang-mdf
```

Building and installation
-------------------------

[INSTALL](https://github.com/giellalt/lang-mdf/blob/develop/INSTALL)
describes the GNU build system in detail, but for most users it is the usual:

```sh
./autogen.sh # This will automatically clone or check out other GiellaLT dependencies
./configure
make
(as root) make install
```
