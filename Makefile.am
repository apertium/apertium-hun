RELEASE=0.0
VERSION=0.0.0
LANG1=hun
BASENAME=apertium-$(LANG1)

TARGETS_COMMON = $(LANG1).automorf.bin $(LANG1).autogen.bin \
        $(LANG1).rlx.bin


# This include defines goals for install-modes, .deps/.d and .mode files:
@ap_include@

###############################################################################
## Transducers, disambiguation rules, transfer
###############################################################################


$(LANG1).autogen.bin: $(BASENAME).$(LANG1).dix
	apertium-validate-dictionary $<
	lt-comp rl $< $@ $(BASENAME).$(LANG1).acx

$(LANG1).automorf.bin: $(BASENAME).$(LANG1).dix
	apertium-validate-dictionary $<
	lt-comp lr $< $@ $(BASENAME).$(LANG1).acx

$(LANG1).autogen.att.gz: $(LANG1).autogen.bin
	lt-print $< | gzip -9 -c -n > $@

$(LANG1).automorf.att.gz: $(LANG1).automorf.bin
	lt-print $< | gzip -9 -c -n > $@


$(LANG1).rlx.bin: $(BASENAME).$(LANG1).rlx
	cg-comp $< $@

###############################################################################
## Distribution
###############################################################################

EXTRA_DIST=$(BASENAME).$(LANG1).dix \
	   $(BASENAME).post-$(LANG1).dix \
	   $(BASENAME).$(LANG1).acx \
	   $(BASENAME).$(LANG1).rlx \
	   $(LANG1).prob \
	   spellrelax.xsl \
	   modes.xml

###############################################################################
## Installation
###############################################################################

apertium_hundir=$(prefix)/share/apertium/$(BASENAME)/
apertium_hun_srcdir=$(prefix)/share/apertium/$(BASENAME)/

apertium_hun_DATA=$(TARGETS_COMMON)

pkgconfigdir = $(prefix)/share/pkgconfig
pkgconfig_DATA = $(BASENAME).pc

noinst_DATA=modes/$(LANG1)-morph.mode

install-data-local: install-modes
	test -d $(DESTDIR)$(apertium_hun_srcdir) || mkdir -p $(DESTDIR)$(apertium_fin_srcdir)
	$(INSTALL_DATA) $(BASENAME).$(LANG1).dix $(DESTDIR)$(apertium_hun_srcdir)
	$(INSTALL_DATA) $(BASENAME).$(LANG1).rlx $(DESTDIR)$(apertium_hun_srcdir)

###############################################################################
## Cleanup
###############################################################################

CLEANFILES = $(TARGETS_COMMON)
clean-local:
	-rm -rf .deps modes


test: all
	apertium-regtest test
