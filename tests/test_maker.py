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


import tagmaker
import tagcoder


def main(args):
    
    taglists = [[u'اسم', u'هاء', u'مجرور',],
                u'تعريف::مرفوع:متحرك:ينون:::'.split(":"),
                u'المضارع المعلوم:هو:::n:'.split(":"),
                u':مضاف:مجرور:متحرك:ينون:::'.split(':'),
                ]
    tag_maker = tagmaker.tagMaker()                
    for taglist in taglists:
        #~ tag_maker = tagmaker.tagMaker("tag.config")
        tag_maker.reset()
        tag_maker._encode(taglist)
        print(u":".join(taglist))
        tagstr = str(tag_maker)
        print(tagstr)
        # decode a unifed tag string
        print(tag_maker._decode())
    print("****TagCoder****")
    tag_coder = tagcoder.tagCoder()
    for taglist in taglists:
        tagstr = tag_coder.encode(taglist)
        print(u":".join(taglist))
        print(tagstr)
        # decode a unifed tag string
        taglist_decoded = tag_coder.decode(tagstr)
        print(taglist_decoded)
        taglist_decoded = [y for (x,y) in taglist_decoded ]
        print(taglist_decoded)
        # test if error
        tagstr2 = tag_coder.encode(taglist_decoded)
        if tagstr2!= tagstr:
            print("error on decoding\n%s\n%s"%(tagstr, tagstr2))
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
