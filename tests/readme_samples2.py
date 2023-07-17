#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  readme_samples1.py
#  
#  Copyright 2023 zerrouki <zerrouki@majd4>
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
sys.path.append("../")


import mysam.tagcoder
   
taglists = [[u'اسم', u'هاء', u'مجرور',],
        u'تعريف::مرفوع:متحرك:ينون:::'.split(":"),
        ]
tgcoder = mysam.tagcoder.tagCoder()
for taglist in taglists:
    # encode
    tagcode = tgcoder.encode(taglist)
    print("tags list:", u";".join(taglist))
    print("tagcode:", tagcode)
    # decode a unifed tag string
    print("decode:", tgcoder.decode(tagcode))

