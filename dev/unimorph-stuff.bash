#!/bin/bash

python3 dev/unimorph2apesyaml.py < dev/hun/hun > dev/unimorph-test.yaml
split -l 32768 dev/unimorph-test.yaml
for f in xa? ; do
    # FIXME: chops some lines that are at the boundaries
    gawk 'BEGIN {OK=-1;} /^  [^ ]/ {OK=1;} OK==1 {print;}' < "$f" |\
        cat dev/unimorph-test.yaml.head - |\
        # unimorph Hungarian specific cleanup I hope...
        sed -e 's/|or|//' | tr -d '|' |\
        sed -e 's/<inf><p\([123]\)><\(pl\|sg\)>/<inf><px\1\2>/' > "$f.yaml"
    rm -v "$f"
done
make
lt-print --hfst hun.automorf.bin | hfst-txt2fst -f olw -o hun.automorf.hfst
lt-print --hfst hun.autogen.bin | hfst-txt2fst -f olw -o hun.autogen.hfst
for f in xa?.yaml ; do
    echo "$f"
    python3 dev/morph-test.py --colour --hide-passes "$f" | fgrep -v '<adj>'
done
