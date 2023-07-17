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

import os
   
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
            >>> import mysam.tagcoder
            >>> tag_coder = mysam.tagcoder.tagCoder()
            >>> taglist = [u'اسم', u'ضمير متصل', u'مجرور']
            >>> tagstr = tag_coder.encode(taglist)
            >>> print(tagstr)
            N--;------I;--H
        
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
            >>> import mysam.tagcoder
            >>> tag_coder = mysam.tagcoder.tagCoder()
            >>> tagcode = 'N--;--I-;----;--H'
            >>> print(tag_coder.decode(tagcode)))
            [('نوع الكلمة', 'اسم'), ('خاصية', 'لاشيء'), ('جنس', 'لاشيء'), ('عدد', 'لاشيء'), ('شخص', 'متكلم'), ('علامة', 'لاشيء'), ('عطف', 'لاشيء'), ('استقبال', 'لاشيء'), ('ضمير متصل', 'لاشيء')]

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

    def add_tag(self, tag, tagstring):
        """ Add new tag to th tagstring code
        Example:
            >>> import mysam.tagcoder
            >>> tag_coder = mysam.tagcoder.tagCoder()
            >>> tagcode = 'V-0;M1H-faU;W--'
            >>> tag = "ضمير متصل"
            >>> print(tag_coder.add_tag(tag, tagcode))
            V-0;M1H-faU;W-H


        @param tagstring: a string tag to be decoded, if not given, return null
        @type tagstring: string
        @return: tag list
        @rtype: stringlist
        """
        if not tagstring:
            return ""
        else:
            # decode the string
            decoded_taglist = self._decode(tagstring)
            # extract values
            tag_values = [v for (k,v) in decoded_taglist]
            # add tag to tag_values
            if tag in tag_values:
                return tagstring
            else:
                tag_values.append(tag)
                # encode
                return self.encode(tag_values)

    def remove_tag(self, tag, tagstring):
        """ remove a tag from tagstring code
        Example:
            >>> import mysam.tagcoder
            >>> tag_coder = mysam.tagcoder.tagCoder()
            >>> tagcode = 'V-0;M1H-faU;W-H'
            >>> tag = "ضمير متصل"
            >>> print(tag_coder.remove_tag(tag, tagcode))
            V-0;M1H-faU;W--


        @param tagstring: a string tag to be decoded, if not given, return null
        @type tagstring: string
        @return: tag list
        @rtype: stringlist
        """
        if not tagstring:
            return ""
        else:
            # decode the string
            decoded_taglist = self._decode(tagstring)
            # extract values
            tag_values = [v for (k,v) in decoded_taglist]
            # add tag to tag_values
            if not tag in tag_values:
                return tagstring
            else:
                tag_values.remove(tag)
                # encode
                return self.encode(tag_values)



if __name__ == "__main__":
    pass
    
    
    
