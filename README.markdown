# Apertium Hungarian: `apertium-hun`

This is an Apertium monolingual language package for Hungarian. What you can
use this language package for:

* Morphological analysis of Hungarian
* Morphological generation of Hungarian
* Part-of-speech tagging of Hungarian

## Requirements

You will need the following software installed:

* lttoolbox (>= 3.3.0)
* apertium (>= 3.3.0)
* vislcg3 (>= 0.9.9.10297)

If this does not make any sense, we recommend you look at:
<https://wiki.apertium.org>.

## Compiling

Given the requirements being installed, you should be able to just run:

```
    $ ./configure
    $ make
```

You can use `./autogen.sh` instead of `./configure` if you're compiling
from source.

If you're doing development, you don't have to install the data, you
can use it directly from this directory.

If you are installing this language package as a prerequisite for an
Apertium translation pair, then do (typically as root / with sudo):

```
    # make install
```

You can give a `--prefix` to `./configure` to install as a non-root user,
but make sure to use the same prefix when installing the translation
pair and any other language packages.

## Testing

If you are in the source directory after running make, the following
commands should work:

    $  echo "rossz idő van" | apertium -d . hun-morph
    TODO: test analysis result

    $ echo "rossz idő van" | apertium -d . hun-tagger
    TODO: test tagger result

## Files and data

* `apertium-hun.hun.dix`            - Monolingual dictionary
* `hun.prob`                        - Tagger model
* `apertium-hun.hun.rlx`            - Constraint Grammar disambiguation rules
* `apertium-hun.post-hun.dix`       - Post-generator
* `modes.xml`                       - Translation modes

## For more information

* <http://wiki.apertium.org/wiki/Installation>
* <http://wiki.apertium.org/wiki/apertium-hun>
* <http://wiki.apertium.org/wiki/Using_an_lttoolbox_dictionary>

## Help and support

If you need help using this language pair or data, you can contact:

* Mailing list: <apertium-stuff@lists.sourceforge.net>
* IRC: `#apertium` on `irc.freenode.net`

See also the file AUTHORS included in this distribution.

## Development notes

The lexicon has been converted with some sedding from:

* hunspell
* <http://mokk.bme.hu/resources/morphdb-hu/>
* <https://github.com/dlt-rilmta/emMorph>
* <https://github.com/unimorph/hun/>

### TODO

I (Flammie) made this conversion but I am not native speaker and also
some of the source material has **a lot** of problems, e.g. unimorph,
so these are in the lexicon too.

The nouns and adjectives were generally easy to sed into right
paradigms by longest suffix match from singular nominative. Verbs have
a bit more problems. The verbs that don't have definite forms may have definite
forms since I didn't bother creating double paradigms.
