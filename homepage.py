__author__ = 'yuzt'
#coding: utf-8

from xpinyin import Pinyin
import codecs

def people(filename):
    space = u"&nbsp;&nbsp;&nbsp;&nbsp;"
    with codecs.open(filename, encoding="utf-8") as infile:
        names = [line.strip() for line in infile]
    td_format = u"<td width=\"172\">{0}（<a href=\"javascript:toto('{1}')\"><img src=\"img/email.gif\" /></a>）</td>"
    for index, name in enumerate(names):
        p = Pinyin()
        pinyin = p.get_pinyin(name," ").split()
        if len(name) == 2:
            pinyin_abbrev = pinyin[0] + pinyin[1][0]
            name = name[0] + space + name[1]
        elif len(name) >= 3:
            pinyin_abbrev = pinyin[0] + "".join(item[0] for item in pinyin[1:])
        td = td_format.format(name, pinyin_abbrev)
        print td
        if (index+1) % 3 == 0 and index < len(names)-1:
            print
            print "<td width=\"98\">&nbsp;</td>"

if __name__ == '__main__':
    people("data/postgraduates2015.txt")

