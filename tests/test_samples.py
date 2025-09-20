#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  makedoc.py
#  
#  Copyright 2018 zerrouki <zerrouki@majd4>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

def main(args):
    # exmpale for encode
    import mysam.tagmaker as tagmaker
    tag_maker = tagmaker.tagMaker()
    taglist = [u'اسم', u'مضير متصل', u'مجرور']
    tag_maker.encode(taglist)
    tagstr = str(tag_maker)
    print(tagstr.encode('utf8'))
    

    # exmaple for decode
    print("***exmaple for decode***")
    tag_maker = tagmaker.tagMaker()
    tagcode = 'N--;--I-;----;---'
    print(tag_maker.repr(tag_maker.decode(tagcode)).encode('utf8'))

    print("***exmaple for inflect***")
    tag_maker = tagmaker.tagMaker()
    tagcode = 'N--;M3IY;---H;---'
    print(tag_maker.inflect(tagcode).encode('utf8'))

    print("***exmaple for add tag***")
    tag_maker = tagmaker.tagMaker()
    tagcode = 'N--;--I-;----;---'
    tag_new = u"تعريف"
    tag_maker.add(tag_new)
    tag_new = u"اسم"
    tag_maker.add(tag_new)
    print(str(tag_maker).encode('utf8'))

    print("***exmaple for has tag***")
    tag_maker = tagmaker.tagMaker()
    tagcode = 'N--;--I-;----;---'
    tag_search = u"مجرور"
    print(tag_maker.has_tag(tag_search, tagcode))


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
