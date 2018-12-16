#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return FTChinese

class FTChinese-weekly(BaseFeedBook):
    title                 = u'FT中文网·一周排行'
    description           = u'英国《金融时报》集团旗下唯一的中文商业财经网站。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_ftchinese.gif"
    coverfile             = "cv_ftchinese.jpg"
    oldest_article        = 1
    keep_image = True
    feeds = [
            (u'FT中文网·一周排行', 'https://feedx.net/rss/ftweekly.xml', True)
           ]
 