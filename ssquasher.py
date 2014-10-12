#! /usr/bin/python2
# coding=utf8
import shlex
import sys
import os.path

if len(sys.argv) < 2:
    try:
        inp = raw_input('Enter template: ')
        arg = False
    except KeyboardInterrupt:
        print 'Interrupted by user'
        exit(1)
    parts = shlex.split(inp)
    if len(parts) != 2:
        print 'Wild error with template processing appeared. ' + \
              'Try to surround mask by quotes.'
        exit(2)
    mask, p = parts
else:
    print sys.argv
    arg = True
    mask, p = sys.argv[1], ''.join(sys.argv[2:])

sep, pt = ';,' # excel ready

print 'Check input:\nMask:   \t' + mask + '\nPattern:\t' + p
print 'If you see an error here, try to surround mask by quotes.'
if arg:
    print 'If you passed template as console argument and see something \n ' + \
        'weird there, it may be OK, but don\'t forget to say big ' + \
        '\Thanks\'\n to Windows developers.'
prompt = raw_input('Continue? (0 = no, <Enter> = yes, c = change separators): ')
if prompt == '0':
    print 'Ok, now exit'
    exit(1)
elif prompt == 'c':
    while True:
        print 'Separators settings. Now in use:\n' + \
            '   \'' + sep + '\'+\'' + pt + '\' as row separator + decimal point\n' + \
            '   \';\'+\',\' is Excel ready. \',\'+\'.\' is default CSV'
        if raw_input('Want to change them? (1 = yes, <Enter> = no): ') == '1':
            sep, pt = raw_input('Be careful! Two first symbols will be taken,\n' + \
                'first as column separator, second as decimal point: ')[0:2]
        else: break

def parse_pattern(pattern, group_sep=',', range_sep=':'):
    result = []
    groups = pattern.strip().replace(' ','').split(group_sep)
    for group in groups:
        if ':' in group:
            parts = map(int, group.split(range_sep))
            res = list(range(parts[0], parts[2] + 1, parts[1]))
            [result.append(str(r)) for r in res]
        else:
            result.append(group)
    return result

pattern = parse_pattern(p)
if not arg: mask = mask.decode(sys.stdin.encoding)
fnames = [mask.format(x) for x in pattern]

data = []
for fn in fnames:
    if os.path.exists(fn):
        print fn + ' exists. Fetching data...'
        data.append(open(fn).readlines())
    else:
        print fn + ' doesn\'t exist. Simulating...'
        data.append([' ' + sep])

maxl = max(map(len, data))

new_data = []
for stack in data:
    l = len(stack)
    while l < maxl:
        stack.append(' ' + sep)
        l += 1
    new_data.append(stack)

dataT = map(list, zip(*new_data))

out = open('result.csv', 'w')
out.write(sep.join(['WLex{0}{1}{0}'.format(wl, sep) for wl in pattern]) + '\n')
for line in dataT:
    for thing in line:
        out.write(sep.join(thing.strip().replace('.',pt).split(' ')) + sep)
    out.write('\n')
out.close()
print 'Compiled data is in \'results.csv\''
