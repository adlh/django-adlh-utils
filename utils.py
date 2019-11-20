# -*- coding: utf-8 -*-

import codecs
import unicodedata
import re
import os

_latin_dict = {
    ord(u"¡"): u"|", ord(u"¢"): u"c", ord(u"£"): u"L", ord(u"¤"): u"o", 
    ord(u"¥"): u"Y", ord(u"¦"): u"|", ord(u"§"): u"S", ord(u"¨"): u"`", 
    ord(u"©"): u"c", ord(u"ª"): u"a", ord(u"«"): u"<<", ord(u"¬"): u"-",
    ord(u"­"): u"-", ord(u"®"): u"R", ord(u"¯"): u"-", ord(u"°"): u"o",
    ord(u"±"): u"+-", ord(u"²"): u"2", ord(u"³"): u"3", ord(u"´"): u"'",
    ord(u"µ"): u"u", ord(u"¶"): u"P", ord(u"·"): u".", ord(u"¸"): u",",
    ord(u"¹"): u"1", ord(u"º"): u"o", ord(u"»"): u">>", ord(u"¼"): u"1/4",
    ord(u"½"): u"1/2", ord(u"¾"): u"3/4", ord(u"¿"): u"?", ord(u"À"): u"A",
    ord(u"Á"): u"A", ord(u"Â"): u"A", ord(u"Ã"): u"A", ord(u"Ä"): u"A",
    ord(u"Å"): u"A", ord(u"Æ"): u"Ae", ord(u"Ç"): u"C", ord(u"È"): u"E",
    ord(u"É"): u"E", ord(u"Ê"): u"E", ord(u"Ë"): u"E", ord(u"Ì"): u"I",
    ord(u"Í"): u"I", ord(u"Î"): u"I", ord(u"Ï"): u"I", ord(u"Ð"): u"D",
    ord(u"Ñ"): u"N", ord(u"Ò"): u"O", ord(u"Ó"): u"O", ord(u"Ô"): u"O",
    ord(u"Õ"): u"O", ord(u"Ö"): u"O", ord(u"×"): u"*", ord(u"Ø"): u"O",
    ord(u"Ù"): u"U", ord(u"Ú"): u"U", ord(u"Û"): u"U", ord(u"Ü"): u"U",
    ord(u"Ý"): u"Y", ord(u"Þ"): u"p", ord(u"ß"): u"ss", ord(u"à"): u"a",
    ord(u"á"): u"a", ord(u"â"): u"a", ord(u"ã"): u"a", ord(u"ä"): u"a",
    ord(u"å"): u"a", ord(u"æ"): u"ae", ord(u"ç"): u"c", ord(u"è"): u"e",
    ord(u"é"): u"e", ord(u"ê"): u"e", ord(u"ë"): u"e", ord(u"ì"): u"i",
    ord(u"í"): u"i", ord(u"î"): u"i", ord(u"ï"): u"i", ord(u"ð"): u"d",
    ord(u"ñ"): u"~", ord(u"ò"): u"o", ord(u"ó"): u"o", ord(u"ô"): u"o",
    ord(u"õ"): u"o", ord(u"ö"): u"o", ord(u"÷"): u"/", ord(u"ø"): u"o",
    ord(u"ù"): u"u", ord(u"ú"): u"u", ord(u"û"): u"u", ord(u"ü"): u"u",
    ord(u"ý"): u"y", ord(u"þ"): u"p", ord(u"ÿ"): u"y", ord(u"’"): u"'" }

def _asciify_enc(error):
    return _latin_dict.get(ord(error.object[error.start]), u''), error.end
codecs.register_error('asciify_enc', _asciify_enc)

_specials_dict = { 
    ord(u'’'): u"'", 
    ord(u"€"): u"EUR",
    ord(u"$"): u"S",
    ord(u","): u"_",
    ord(u"&"): u"and",
    ord(u"+"): u"plus",
    ord(u"%"): u"perc",
    ord(u"ß"): u"ss", 
    ord(u"ñ"): u"nn", 
    ord(u"Ñ"): u"NN", 
}


def _replace_special_chars(text):
    ret = []
    for letter in text:
        code = ord(letter)
        if code in _specials_dict.keys():
            ret.append(_specials_dict[code])
        else:
            ret.append(letter)
    return ''.join(ret)


def slugify(text, delim=u'-'):
    """Generates an ASCII-only slug, Trying to convert some common chars to
    asci-only equivalents.

    Example:
    >>> str = u'Wikipédia, le projet d’encyclopédie, aß, niño? Äbub 100€ %10!!!'
    >>> slugify(str)
    u'wikipadia-le-projet-daencyclopadie-aa-niao-abub-100a-perc10'
    
    """
    # first replace special chars to safe ascii
    text = _replace_special_chars(text)

    result = []
    _punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.:]+')
    for word in _punct_re.split(text.lower()):
        word = unicodedata.normalize('NFKD', word).encode('ascii', 'asciify_enc')
        if word:
            result.append(word)
    return unicode(delim.join(result))


def slugify_filename(filename):
    """Slugify the base-name of a file (ignoring the extension part).

    Usage:
    >>> filename = u'Ähm a bad name!.png'
    >>> slugify_filename(filename)
    u'ahm-a-bad-name.png'

    """
    parts = os.path.splitext(filename)
    return ''.join([slugify(parts[0]), parts[1]])

if __name__ == '__main__':
    print_all()

