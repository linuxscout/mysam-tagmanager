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
tag_coder = mysam.tagcoder.tagCoder()
tags = ['اسم', 'مجرور', 'مذكر', "مفرد", "واو"]
tagcode = tag_coder.encode(tags)
print(tagcode)
tag_search = u"مجرور"
print(tag_coder.has_tag(tag_search, tagcode))
tag_search = u"فعل"
print(tag_coder.has_tag(tag_search, tagcode))

# ~ import mysam.tagmaker
# ~ tag_maker = mysam.tagmaker.tagMaker()
# ~ tagcode = 'N--;--I----;---'
# ~ tag_search = u"مجرور"
# ~ print(tag_maker.has_tag(tag_search, tagcode))

