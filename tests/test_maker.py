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

import sys
sys.path.append('../')

import mysam.tagmaker as tagmaker


def main(args):
    
    taglists = [[u'اسم', u'هاء', u'مجرور',],
                u'تعريف::مرفوع:متحرك:ينون:::'.split(":"),
                u'المضارع المعلوم:هو:::n:'.split(":"),
                u':مضاف:مجرور:متحرك:ينون:::'.split(':'),
                ]
    for taglist in taglists:
        tag_maker = tagmaker.tagMaker()
        tag_maker.encode(taglist)
        print(u"+".join(taglist).encode('utf8'))
        tagstr = str(tag_maker)
        print(tagstr.encode('utf8'))
        # decode a unifed tag string
        print(tag_maker.repr(tag_maker.decode()).encode('utf8'))


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
