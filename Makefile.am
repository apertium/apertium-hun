RELEASE=0.0
VERSION=0.0.0
LANG=hun
BASENAME=apertium-$(LANG)

TARGETS_COMMON = $(LANG).automorf.bin $(LANG).autogen.bin \
        $(LANG).rlx.bin

# Use this goal for creating .deps, otherwise make -j2 will give problems:
.deps/.d:
	if [ ! -d .deps ]; then mkdir .deps; fi
	touch $@

# Prevent the .d file from being removed automatically:
.PRECIOUS: .deps/.d

$(LANG).autogen.bin: $(BASENAME).$(LANG).dix .deps/.d
	apertium-validate-dictionary $<
	lt-comp rl $< $@ $(BASENAME).$(LANG).acx

$(LANG).automorf.bin: $(BASENAME).$(LANG).dix .deps/.d
	apertium-validate-dictionary $<
	lt-comp lr $< $@ $(BASENAME).$(LANG).acx

$(LANG).autogen.att.gz: $(LANG).autogen.bin
	lt-print $< | gzip -9 -c > $@

$(LANG).automorf.att.gz: $(LANG).automorf.bin
	lt-print $< | gzip -9 -c > $@


$(LANG).rlx.bin: $(BASENAME).$(LANG).rlx
	cg-comp $< $@

EXTRA_DIST=$(BASENAME).$(LANG).dix \
	   $(BASENAME).post-$(LANG).dix \
	   $(BASENAME).$(LANG).acx \
	   $(BASENAME).$(LANG).rlx \
	   $(LANG).prob \
	   spellrelax.xsl \
	   modes.xml

apertium_hundir=$(prefix)/lib/apertium/$(BASENAME)/
apertium_hun_srcdir=$(prefix)/share/apertium/$(BASENAME)/

apertium_hun_DATA=$(TARGETS_COMMON)

pkgconfigdir = $(libdir)/pkgconfig
pkgconfig_DATA = $(BASENAME).pc

# Modes are not installed since they're all just "debug modes". All
# modes are created by this goal.
modes/$(LANG)-morph.mode: modes.xml
	apertium-validate-modes modes.xml
	apertium-gen-modes modes.xml

noinst_DATA=modes/$(LANG)-morph.mode

install-data-local:
	test -d $(DESTDIR)$(apertium_hun_srcdir) || mkdir -p $(DESTDIR)$(apertium_fin_srcdir)
	$(INSTALL_DATA) $(BASENAME).$(LANG).dix $(DESTDIR)$(apertium_hun_srcdir)
	$(INSTALL_DATA) $(BASENAME).$(LANG).rlx $(DESTDIR)$(apertium_hun_srcdir)

CLEANFILES = $(TARGETS_COMMON)
clean-local:
	-rm -rf .deps modes

