import sys
import json


def to_const(string):
    out_const = ''
    is_first = True
    for s in string:
        if s.isupper():
            if not is_first:
                out_const += '_'
        elif s is ' ':
            out_const += '_'
        out_const += s.upper()
        is_first = False
    return out_const


def un_const(string):
    chars = [c for c in string]

    out = ''
    next_to_underline = False
    for idx, char in enumerate(chars):
        if char is '_':
            next_to_underline = True
        else:
            if next_to_underline:
                out += char.upper()
                next_to_underline = False
            else:
                out += char.lower()

    return out


def to_camel(string):
    out_camel = ''
    is_upper = False
    for s in string:
        if s == '_':
            is_upper = True
        else:
            if is_upper:
                out_camel += s.upper()
                is_upper = False
            else:
                out_camel += s.lower()
    return out_camel


def to_mid_line(string):
    out_mid = ''
    is_first = True
    for s in string:
        if s.isupper():
            if not is_first:
                out_mid += '-'
            s = s.lower()
        out_mid += s
        is_first = False
    return out_mid


def un_mid_line(string):
    out = ''
    is_upper = False
    is_first = True
    for s in string:
        if s is '-':
            if not is_first:
                is_upper = True
                continue
        if is_upper:
            s = s.upper()
            is_upper = False
        out += s
        is_first = False
    return out


def un_camel(string):
    out = ''
    is_first = True
    for s in string:
        if s.isupper():
            if not is_first:
                out += '_'
            s = s.lower()
        out += s
        is_first = False
    return out


def un_camel_2(string):
    out = ''
    is_first = True
    for s in string:
        if s.isupper():
            if not is_first:
                out += ' '
            s = s.lower()
        out += s
        is_first = False
    return out


if __name__ == '__main__':
    if len(sys.argv) > 1 and len(sys.argv[1].strip()):
        query = sys.argv[1]
    else:
        query = sys.stdin.read()

    camel = to_camel(query)
    const = to_const(query)
    un_const = un_const(query)
    mid = to_mid_line(query)
    upper = query.upper()
    lower = query.lower()
    capitalize = query.capitalize()
    un_capitalize = query[0].lower() + query[1:]
    no_space = query.replace(' ', '')
    upper_no_space = upper.replace(' ', '_')
    re_mid = un_mid_line(query)
    re_camel = un_camel(query)
    re_camel_2 = un_camel_2(query)

    items = []
    for txt in [
        camel,
        const,
        un_const,
        mid,
        upper,
        lower,
        capitalize,
        un_capitalize,
        no_space,
        upper_no_space,
        re_mid,
        re_camel,
        re_camel_2
    ]:
        items.append({'title': txt, 'arg': txt})
    result = {'items': items}
    json.dump(result, sys.stdout)
    sys.stdout.flush()
