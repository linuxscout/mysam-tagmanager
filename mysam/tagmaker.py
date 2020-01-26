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
if __name__ == "__main__":
    import tag_const 
    import tagconfig
else:
    from . import tag_const 
    from . import tagconfig

    
class tagMaker:
    """
    Manage tags, create, code, decode a tag
    """

    def __init__(self, configfile = None):
        """Init tha class"""
        # read config first
        #~ self.load_config()
        if configfile:
            #~ print("Load a config file")
            configuer = tagconfig.tagConfig()
            configuer.load_config(configfile)
            # load on Global variables
            self.tagsdict = configuer.tagsdict 
            self.inverse_tagsdict =configuer.inverse_tagsdict 
            self.attr_tagsdict =configuer.attr_tagsdict
            # if structure not defined, the default structure is used.
            if configuer.tag_parts_sizes:
                self.tag_parts_sizes = configuer.tag_parts_sizes
            else:
                self.tag_parts_sizes = []
            if configuer.tagsmap:
                self.tagsmap = configuer.tagsmap
            else:
                self.tagsmap = configuer.tagsmap
            self.tag_parts_sep = tag_const.TAG_PARTS_SEP
                
        else:
            # load on Global variables
            self.tagsdict = tag_const.TAGSDICT  
            self.inverse_tagsdict  = tag_const.INVERSE_TAGSDICT 
            self.attr_tagsdict = tag_const.ATTR_TAGSDICT 
            # if structure not defined, the default structure is used.
            self.tag_parts_sizes = tag_const.TAG_PARTS_SIZES
            self.tag_parts_sep = tag_const.TAG_PARTS_SEP
            self.tagsmap = tag_const.TAGSMAP
        # prepare the tag maker
        self.reset()

    
    def set_config(self,configfile):
        """ set a config to encode tags"""
        configueur = tagconfig.tagConfig()
        configueur.load_config(configfile)
               
    def reset(self,):
        """ reset the taglist to make a new"""
        # init taglist
        self.taglist = []
        for i in range(len(self.tag_parts_sizes)):
            self.taglist.append(['-']*self.tag_parts_sizes[i])

    def __str__(self,):
        """ prepare list to be printed
        @return: a string
        @rtype: string
        """
        # join sub lists without separater, 
        # the join parts by separator
        return  self.tag_parts_sep.join([u"".join(x) for x in self.taglist])
    @staticmethod
    def repr(obj):
        """ prepare list to be printed
        @return: a string
        @rtype: string
        """
        if type(obj) is dict:
            return  repr(obj).replace("},","},\n")
        else:
            return  repr(obj)             
 
    def add(self, tag):
        """ add a new tag to the taglist
        Example:
            >>> tag_maker = tagmaker.tagMaker()
            >>> tagcode = 'N--;--I-;----;---'
            >>> tag_new = u"تعريف"
            >>> tag_maker.add(tag_new)
            >>> tag_new = u"اسم"
            >>> tag_maker.add(tag_new)
            >>> print(str(tag_maker).encode('utf8'))
            N--;----;--L-;----
        
        @param tag: a tag 
        @type tag: unicode
        """
        debug = False
        # if tag names are differents, it can contain many tags
        taglist =[]
        if not tag in self.tagsdict:
            taglist = self.tagsmap.get(tag,[])
            if debug: print("***",u";;".join(taglist).encode('utf8'))
        else:
            taglist =[tag,]
        # if the tag exist in tagsdict configuration
        # choose value and add it to a position
        for tg in taglist:
            if tg in self.tagsdict:
                if debug: print("***//",tg.encode('utf8'))
                part = self.tagsdict[tg]['part'] -1
                pos = self.tagsdict[tg]['pos']-1
                code = self.tagsdict[tg]['code']
                self.taglist[part][pos] = code


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
        for tag in taglist:
            self.add(tag)
        return self.__str__()
        
    def decode(self, tagstring = False):
        """Decode a string tag to get all tags
        Example:
            >>> import mysam.tagmaker as tagmaker
            >>> tag_maker = tagmaker.tagMaker()
            >>> tagcode = 'N--;--I-;----;---'
            >>> print(tag_maker.decode(tagcode)))
            [(u'نوع الكلمة', u'اسم'), (u'جنس', u'لاشيء'), (u'عدد', u'لاشيء'), (u'إعراب', u'مجرور'), (u'علامة', u'لاشيء'), (u'عطف', u'لاشيء'), (u'جر', u'لاشيء'), (u'تعريف', u'نكرة'), (u'ضمير متصل', u'لاشيء'), (u'استقبال', u'لاشيء'), (u'بناء', u'لاشيء'), (u'زمن', u'لاشي
        
        @param tagstring: a string tag to be decoded, if not given the internal tag string is decoded.
        @type tagstring: string
        @return: tag list
        @rtype: stringlist
        """
        if not tagstring:
            tagstring = self.__str__()
        parts = tagstring.split(self.tag_parts_sep)
        
        tags = []
        # read codes
        for ip, part in enumerate(parts):
            for i in range(len(part)):
                code = part[i]
                key = u":".join([str(ip+1), str(i+1), code])
                #~ print key
                tag = self.inverse_tagsdict.get(key,{}).get('ar_value',"")
                attr = self.inverse_tagsdict.get(key,{}).get('ar_attr',"")
                if tag:
                    tags.append((attr, tag))
                
        return tags
        
    def inflect_noun(self, tagstring=False):
        """
        get inflection for a noun
        @param tagstring: a string tag to be decoded, if not given the internal tag string is decoded.
        @type tagstring: string
        @return: string
        @rtype: string
        """
        if not tagstring:
            tagstring = self.__str__()
        inflct = []
        if self.has_tag(u"اسم", tagstring):
             # inflect = Syntaxtic classe
             # مفعول به منصوب وعلامة نصبه الفتحة
             #نعت منصوب وعلامةنصبه الياء لأنه مثنى
             #مبتدأ مرفوع وعلامة رفعه الواو لأنه جمع مذكر سالم
            # case
            case = self.get_inflect(u'إعراب', tagstring)
            if case:
                case_part = u"اسم %s"%case
                inflct.append(case_part)
                # Jar
                if self.has_tag(u"مجرور", tagstring):
                    jar = self.get_inflect(u'جر', tagstring)
                    if jar:
                        jar_part = jar
                        inflct.append(jar_part)
                # inflect Mark
                mark =self.get_inflect(u'علامة', tagstring)
                mark_value =self.get_value(u'علامة', tagstring)
                if mark:
                    #علامة الإعراب
                    # وعلامة رفعه الضمة
                    mark_part =""
                    # علة علامة الإعراب
                    # وعلامة رفعه الألف لأنه مثنى
                    cause_part =""
                    if case == u"مبني":
                        mark_part = u"على %s"%mark
                    else:
                        # استخراج الحالة
                        #~ مرفوع => رفعه
                        #~ منصوب => نصبه
                        #~ مجرور => جره
                        case_mark = ""
                        if case == u"مرفوع":
                            case_mark = u"رفعه"
                        elif case == u"منصوب":
                            case_mark = u"نصبه"
                        elif case == u"مجرور":
                            case_mark = u"جرّه"
                        
                        mark_part = u"وعلامة %s %s"%(case_mark, mark)
                        
                        # mark cause
                        
                        if self.has_tag(u"مثنى", tagstring):
                            cause_part = u"لأنه مثنى"
                        elif self.has_tag(u'مؤنث', tagstring) and self.has_tag(u"جمع", tagstring):
                            cause_part = u"لأنه جمع مؤنث سالم"                            
                        elif self.has_tag(u'مذكر', tagstring) and self.has_tag(u"جمع", tagstring):
                            cause_part = u"لأنه جمع مذكر سالم"                           
                        elif self.has_tag(u'مجرور', tagstring) and self.has_tag(u"ممنوع من الصرف", tagstring):
                            cause_part = u"لأنه ممنوع من الصرف"                           
                    inflct.append(mark_part)
                    inflct.append(cause_part)
                #attached pronoun
                add_p = self.get_inflect(u'ضمير متصل', tagstring)
                if add_p:
                    add_part = u"وهو مضاف، %s في محل جر مضاف إليه"%add_p
                    inflct.append(add_part)
            else: # no case
                word_type = self.get_value(u'نوع الكلمة', tagstring)
                if word_type:
                    inflct.append(word_type)  
        return u" ".join(inflct)
    def inflect_verb(self, tagstring):
        """
        get inflectionfor a noun
        @param tagstring: a string tag to be decoded, if not given the internal tag string is decoded.
        @type tagstring: string
        @return: string
        @rtype: string
        """
        if not tagstring:
            tagstring = self.__str__()
        inflct = []
        if self.has_tag(u"فعل", tagstring):
             # inflect = Syntaxtic classe
             # مفعول به منصوب وعلامة نصبه الفتحة
             #نعت منصوب وعلامةنصبه الياء لأنه مثنى
             #مبتدأ مرفوع وعلامة رفعه الواو لأنه جمع مذكر سالم
            # case
            case = self.get_inflect(u'إعراب', tagstring)
            #~ print((u"###%s####"%case).encode('utf8'), tagstring)
            if case:
                case_part = u"فعل %s"%case
                inflct.append(case_part)

                # inflect Mark
                mark =self.get_inflect(u'علامة', tagstring)
                mark_value =self.get_value(u'علامة', tagstring)
                if mark:
                    #علامة الإعراب
                    # وعلامة رفعه الضمة
                    mark_part =""
                    # علة علامة الإعراب
                    # وعلامة رفعه الألف لأنه مثنى
                    cause_part =""
                    if case == u"مبني":
                        mark_part = u"على %s"%mark
                    else:
                        # استخراج الحالة
                        #~ مرفوع => رفعه
                        #~ منصوب => نصبه
                        #~ مجرور => جره
                        case_mark = ""
                        if case == u"مرفوع":
                            case_mark = u"رفعه"
                        elif case == u"منصوب":
                            case_mark = u"نصبه"
                        elif case == u"مجزوم":
                            case_mark = u"جزمه"
                        
                        mark_part = u"وعلامة %s %s"%(case_mark, mark)
                        
                        # mark cause
                        
                        condition_5verbs = (self.has_tag(u"مثنى", tagstring)
                        or (self.has_tag(u'مذكر', tagstring) and self.has_tag(u"جمع", tagstring))
                        or (self.has_tag(u'مؤنث', tagstring) and self.has_tag(u"مخاطب", tagstring) and self.has_tag(u"مفرد", tagstring))
                        )
                        if condition_5verbs:
                            cause_part = u"لأنه من الأفعال الخمسة"                            
                    inflct.append(mark_part)
                    inflct.append(cause_part)
                #attached pronoun
                add_p = self.get_inflect(u'ضمير متصل', tagstring)
                #~ print((u"H###%s####"%add_p).encode('utf8'))
                if add_p:
                    add_part = u"%s في محل نصب مفعول به"%add_p
                    inflct.append(add_part)
            else: # no case
                word_type = self.get_value(u'نوع الكلمة', tagstring)
                if word_type:
                    inflct.append(word_type)  
        return u" ".join(inflct)
    def inflect_tool(self, tagstring = False):
        """
        """
        return u""
    def inflect(self, tagstring = False):
        """
        Display inlfection in traditional way
        عرض إعراب الكلمة حسب التقاليد
        
        Example:
            >>> tag_maker = tagmaker.tagMaker()
            >>> tagcode = 'N--;--I-;----;---'
            >>> print(tag_maker.inflect(tagcode).encode('utf8'))
            اسم مجرور وعلامة جرّه الياء لأنه جمع مذكر سالم وهو مضاف، والضمير المتصل مبني في محل جر مضاف إليه
        
        @param tagstring: a string tag to be decoded, if not given the internal tag string is decoded.
        @type tagstring: string
        @return: string
        @rtype: string        
        """
        if not tagstring:
            tagstring = self.__str__()
        inflct = []
        if self.has_tag(u"اسم", tagstring):
            return self.inflect_noun(tagstring)
        elif self.has_tag(u"فعل", tagstring):
            return self.inflect_verb(tagstring)
        elif self.has_tag(u"أداة", tagstring):
            return self.inflect_tool(tagstring)
        else:
            word_type = self.get_value(u'نوع الكلمة', tagstring)
            if word_type:
                inflct.append(word_type)            
        return u" ".join(inflct)

    def has_tag(self, tag, tagstring = False):
        """
        Look up if the tag exists in a string tag
        Example:
            >>> tag_maker = tagmaker.tagMaker()
            >>> tagcode = 'N--;--I-;----;---'
            >>> tag_new = u"تعريف"
            >>> tag_maker.add(tag_new)
            >>> tag_new = u"اسم"
            >>> tag_maker.add(tag_new)
            >>> print(str(tag_maker).encode('utf8'))
            N--;----;--L-;----
        
        @param tagstring: a string tag to be decoded, if not given the internal tag string is decoded.
        @type tagstring: string
        @return: boolean
        @rtype: boolean      
        """
        if not tagstring:
            tagstring = self.__str__()
        parts = tagstring.split(self.tag_parts_sep)
        if tag not in self.tagsdict:
            return False
        else:
            part = self.tagsdict[tag]['part']
            pos = self.tagsdict[tag]['pos']
            code = self.tagsdict[tag]['code']
            if parts[part-1][pos-1] == code:
                return True
            else:
                return False
        return False

    def exists_attr(self, attr, tagstring = False):
        """
        test if attribute is enabled, for example, جر is ok, if tag code is B, K, L, is not if code is '-'
        @param attr: attribute to lookup
        @type attr: string
        @param tagstring: a string tag to be decoded, if not given the internal tag string is decoded.
        @type tagstring: string
        @return: boolean
        @rtype: boolean
        """
        deco = self.decode_attr(attr, tagstring)
        return bool(deco) 

    def get_value(self, attr, tagstring=False):
        """
        Return the value of attribute
        @param attr: attribute to lookup
        @type attr: string
        @param tagstring: a string tag to be decoded, if not given the internal tag string is decoded.
        @type tagstring: string
        @return: the value
        @rtype: string
        """
        deco = self.decode_attr(attr, tagstring)
        if deco: 
            return deco.get('ar_value','')
        return ''

    def get_inflect(self, attr, tagstring=False):
        """
        Return the inflect text of attribute
        @param attr: attribute to lookup
        @type attr: string
        @param tagstring: a string tag to be decoded, if not given the internal tag string is decoded.
        @type tagstring: string
        @return: the inflection
        @rtype: string        
        """
        deco = self.decode_attr(attr, tagstring)
        if deco: 
            return deco.get('inflect','')
        return ''
            
            
    def decode_attr(self, attr, tagstring = False):
        """
        Decode an attribute
        @param attr: attribute to lookup
        @type attr: string
        @param tagstring: a string tag to be decoded, if not given the internal tag string is decoded.
        @type tagstring: string
        @return: the attribute dict
        @rtype: dict of string
        """
        if not tagstring:
            tagstring = self.__str__()
        parts = tagstring.split(self.tag_parts_sep)
        if attr not in self.attr_tagsdict:
            return {}
        else:
            part = self.attr_tagsdict[attr]['part']
            pos = self.attr_tagsdict[attr]['pos']
            code = parts[part-1][pos-1]
            if code == '-':
                return {}
            else:
                key = u":".join([str(part), str(pos), code])
                return self.inverse_tagsdict.get(key,{})
        return {}


            
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
        print(u"+".join(taglist).encode('utf8'))
        tagstr = str(tag_maker)
        print(tagstr.encode('utf8'))
        # decode a unifed tag string
        print(tag_maker.repr(tag_maker.decode()).encode('utf8'))
    
    
    
