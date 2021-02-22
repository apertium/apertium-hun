#!/usr/bin/env python3

import sys

print('Config:')
print('  hfst:')
print('    Gen: hun.autogen.hfst')
print('    Morph: hun.automorf.hfst')
print()
print('Tests:')

headerline = True
lemmas = 0
tokens = 0
piperrors = 0
transitiverrors = 0
subjerrors = 0
otherfails = 0
for line in sys.stdin:
    if not line or line.strip() == '':
        print()
        headerline = True
        continue
    # gravitáció      gravitáción     N;ON+ESS;SG
    fields = line.strip().split('\t')
    tokens += 1
    if len(fields) != 3:
        print('Datoissa virhe!', fields)
        sys.exit(1)
    elif fields[0] == '----' and fields[1] == '----' and fields[2] == '----':
        # this is the kind bs that unimorph is full of
        otherfails += 1
        continue
    lemma = fields[0]
    surf = fields[1]
    unimorphs = fields[2]
    if headerline:
        lemmas += 1
        print('  ', fields[0], ' unimorph paradigm :', sep='')
        headerline = False
    if 'intransitive verb' in surf:
        transitiverrors += 1
    elif 'subjunctive forms' in surf:
        subjerrors += 1
    elif '|' in surf:
        piperrors += 1
    apes = list()
    for unimorph in unimorphs.split(';'):
        if unimorph == 'N':
            apes += ['<n>']
        elif unimorph == 'V':
            apes += ['<vblex>']
        elif unimorph == 'ON+ESS':
            apes += ['<ses>']
        elif unimorph == 'FRML':
            apes += ['<ess1>']
        elif unimorph == 'IN+ESS':
            apes += ['<ine>']
        elif unimorph == 'NOM':
            apes += ['<nom>']
        elif unimorph == 'ON+ALL':
            apes += ['<sub>']
        elif unimorph == 'AT+ALL':
            apes += ['<all>']
        elif unimorph == 'PRP':
            apes += ['<cau>']
        elif unimorph == 'INST':
            apes += ['<ins>']
        elif unimorph == 'TRANS':
            apes += ['<tra>']
        elif unimorph == 'TERM':
            apes += ['<term>']
        elif unimorph == 'ON+ABL':
            apes += ['<dela>']
        elif unimorph == 'IN+ABL':
            apes += ['<ela>']
        elif unimorph == 'IN+ALL':
            apes += ['<ill>']
        elif unimorph == 'DAT':
            apes += ['<dat>']
        elif unimorph == 'ACC':
            apes += ['<acc>']
        elif unimorph == 'AT+ESS':
            apes += ['<ade>']
        elif unimorph == 'AT+ABL':
            apes += ['<abl>']
        elif unimorph == 'SG':
            apes += ['<sg>']
        elif unimorph == 'PL':
            apes += ['<pl>']
        elif unimorph == 'IND':
            if 'PRS' in unimorphs:
                apes += ['<pri>']
            elif 'PST' in unimorphs:
                apes += ['<past>']
            else:
                print('IND without PRS or PST ??')
                sys.exit(1)
        elif unimorph == '1':
            apes += ['<p1>']
        elif unimorph == '2':
            apes += ['<p2>']
        elif unimorph == '3':
            apes += ['<p3>']
        elif unimorph == 'INDF':
            pass  # unmarked in apes
        elif unimorph == 'DEF':
            apes += ['<def>']
        elif unimorph == 'V.PTCP':
            apes += ['<vblex>']
            if 'PRS' in unimorphs:
                apes += ['<pprs>']
            elif 'PST' in unimorphs:
                apes += ['<pp>']
            elif 'FUT' in unimorphs:
                apes += ['<foo>']
            else:
                print('V.PTCP without PRS or PST or FUT??')
                sys.exit(1)
        elif unimorph == 'NFIN':
            apes += '<inf>'
        elif unimorph == 'COND':
            apes += ['<cond>']
        elif unimorph == 'SBJV':
            apes += ['<subj>']
        elif unimorph == 'V.CVB':
            apes += ['<vblex>']
            apes += ['<adv>']
        elif unimorph in ['PRS', 'PST', 'FUT']:
            pass  # handeld elsewhere in combos
        else:
            print('missing unimorph mapping for:', unimorph)
            sys.exit(2)
    reorg = list()
    for ape in apes:
        if ape in ['<n>', '<vblex>']:
            reorg += [ape]
    if reorg == ['<n>']:
        for ape in apes:
            if ape in ['<sg>', '<pl>']:
                reorg += [ape]
        for ape in apes:
            if ape not in reorg:
                reorg += [ape]
    elif reorg == ['<vblex>']:
        for ape in apes:
            if ape not in reorg:
                reorg += [ape]
    else:
        print(reorg)
        sys.exit(1)
    apes = reorg
    print('    ', lemma, ''.join(apes), ': ', surf, sep='')

print()
print('# tokens\tlemmas\tpipe\ttrans\tsubj\tother fails')
print('# ', tokens, '\t', lemmas, '\t', piperrors, '\t', transitiverrors,
      '\t', subjerrors, '\t', otherfails, sep='')
print('# ', tokens / tokens * 100, '\t',
      lemmas / tokens * 100, '\t',
      piperrors / tokens * 100, '\t',
      transitiverrors / tokens * 100, '\t',
      subjerrors / tokens * 100, '\t',
      otherfails / tokens * 100, sep='')
