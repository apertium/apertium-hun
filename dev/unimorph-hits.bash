#!/bin/bash
UNIMORPH=dev/hun/hun
if ! test -f $UNIMORPH ; then
    echo missing $UNIMORPH, do:
    echo git clone git@github.com/unimorph/hun dev/hun
    exit 2
fi
case $1 in
    word*) cut -f 2 $UNIMORPH | lt-proc hun.automorph.bin | grep -F '*';;
    lemma*) cut -f 1 $UNIMORPH | lt-proc hun.automorph.bin | uniq | grep -F '*';;
    *) lt-proc hun.automorph.bin < $UNIMORPH | grep -F '*';;
esac
