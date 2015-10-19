# -*- coding: utf-8 -*-

keywords = [
    u"كيماوي",
    u"غاز سام",
    u"كلور",
    u"اختناق",
    u"سام",
    u"غازات سامة",
    u"الكلور",
    u"الكيماوي",
    u"الاختناق",
    u"الغازات السامة",
    u"السام"
]

def call(sentence, keywords=keywords):
    matches = filter(lambda keyword: keyword in sentence.decode("utf-8"), keywords)

    if any(matches):
        print "Match on " + str(matches)
        return matches
    else:
        print "Do nothing. No keyword match."
        return []
