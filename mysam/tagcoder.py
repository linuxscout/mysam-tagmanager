#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tag_const.py
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
from __future__ import (
    absolute_import,
    print_function,
    unicode_literals,
    division,
    )
import os
# ~ if __name__ == "__main__":
    
try:
    import tag_const 
    import tagconfig
    import tagmaker    
except:
    from . import tag_const 
    from . import tagconfig
    from . import tagmaker    

    
class tagCoder(tagmaker.tagMaker):
    """
    Manage code, decode a tag
    """

    def __init__(self, configfile = None):
        """Init tha class"""
        tagmaker.tagMaker.__init__(self, configfile)
        self.reset()

    def encode(self, taglist = []):
        """Encode  a tag list into string tag.
        
        Example:
            >>> import mysam.tagmaker as tagmaker
            >>> tag_maker = tagmaker.tagMaker()
            >>> taglist = [u'اسم', u'مضير متصل', u'مجرور']
            >>> tag_maker.encode(taglist)
            >>> tagstr = str(tag_maker)
            >>> print(tagstr)
            N--;--I-;----;----
        
        @param taglist: an given tag list to be coded
        @type taglist: string list
        @return: a string
        @rtype: string
        """

        if not taglist:
            return u""
        self.reset()            
        for tag in taglist:
            self.add(tag)
        
        return self.__str__()
    def decode(self, tagstring):
        """Decode a string tag to get all tags
        Example:
            >>> import mysam.tagcoder as tagcoder
            >>> tag_coder = tagcoder.tagCoder()
            >>> tagcode = 'N--;--I-;----;---'
            >>> print(tag_coder.decode(tagcode)))
            [(u'نوع الكلمة', u'اسم'), (u'جنس', u'لاشيء'), (u'عدد', u'لاشيء'), (u'إعراب', u'مجرور'), (u'علامة', u'لاشيء'), (u'عطف', u'لاشيء'), (u'جر', u'لاشيء'), (u'تعريف', u'نكرة'), (u'ضمير متصل', u'لاشيء'), (u'استقبال', u'لاشيء'), (u'بناء', u'لاشيء'), (u'زمن', u'لاشي
        
        @param tagstring: a string tag to be decoded, if not given, return null
        @type tagstring: string
        @return: tag list
        @rtype: stringlist
        """
        if not tagstring:
            return ""
        else:
            return self._decode(tagstring)
        return tags

            
if __name__ == "__main__":
    taglists = [[u'اسم', u'هاء', u'مجرور',"مصدر"],
                u'تعريف::مرفوع:متحرك:ينون:::'.split(":"),
                u'المضارع المعلوم:هو:::n:'.split(":"),
                u':مضاف:مجرور:متحرك:ينون:::'.split(':'),
                ]
    tag_maker = tagMaker("config/tag.config")

    for taglist in taglists:
        tag_maker.reset()
        tag_maker.encode(taglist)
        print(u"+".join(taglist))
        tagstr = str(tag_maker)
        print(tagstr)
        # decode a unifed tag string
        print(tag_maker.repr(tag_maker.decode()))
    
    
    
