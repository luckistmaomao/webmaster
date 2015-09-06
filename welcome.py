__author__ = 'yuzt'
#coding: utf-8

from xpinyin import Pinyin
from optparse import OptionParser
import sys
import codecs
from itertools import izip

reload(sys)
sys.setdefaultencoding("utf-8")

def parse_options():
    usage = "Automatically generate welcome email."
    optionparser = OptionParser(usage)
    optionparser.add_option("-n","--name", dest="name", type=str, help="specify the student chinese name")
    optionparser.add_option("-f","--file", dest="file", type=str, help="specify the student name list" )
    options, args = optionparser.parse_args()
    return options

def welcome():
    options = parse_options()
    p = Pinyin()
    if options.name:
        username = options.name
        username = unicode(username)
        second_name = username[1:]
        pinyin = p.get_pinyin(username, " ").split()
        pinyin_abbrev = pinyin[0] + "".join(item[0] for item in pinyin[1:])
        message_format = u"{0}同学好，大家好，\n最近我们组迎来了{0}同学，欢迎他们加入我们温暖的大家庭！\n{1}同学的组内邮箱为： {2}@nlp.nju.edu.cn\n大家多联系，多关照。\n如果有任何问题，请联系管理员程善伯chengsb@nlp.nju.edu.cn或郁振庭zhucf@nlp.nju.edu.cn。\n另：组内为每位同学分配了一定资源，附件中为组内资源介绍。\n\n祝好！\n\n谢谢\n振庭"
        message = message_format.format(username, second_name, pinyin_abbrev)
        print message
    elif options.file:
        message_format = "大家好，\n最近我们组迎来了：\n{0}等{1}位同学同学。\n欢迎他们加入我们温暖的大家庭！\n大家多联系，多关照。\n如果有任何问题，请联系管理员\n另：组内为每位同学分配了一定资源，附件中为组内资源介绍以及组内编程规范，\n请仔细阅读。\n\n祝好！\n\n谢谢\n振庭"
        with codecs.open(options.file, encoding="utf-8") as infile:
            names = [line.strip() for line in infile]
        num_students = len(names)
        pinyins = [p.get_pinyin(name, " ").split() for name in names]
        pinyin_abbrevs = [pinyin[0] + "".join(item[0] for item in pinyin[1:]) for pinyin in pinyins]
        email_format = u"{0}({1}@nlp.nju.edu.cn)"
        emails = [email_format.format(name, pinyin_abbrev) for name, pinyin_abbrev in izip(names, pinyin_abbrevs)]
        message = message_format.format("\n".join(emails), num_students)
        print message
    else:
        print >> sys.stderr, "Please check your options"


if __name__ == '__main__':
    welcome()
