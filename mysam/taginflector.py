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
from . import tag_const_inflect
    
class tagInflector(tagmaker.tagMaker):
    """
    Manage code, decode a tag
    """

    def __init__(self, configfile = None):
        """Init tha class"""
        tagmaker.tagMaker.__init__(self, configfile)
        self.reset()
        # print("INVERSE_TAGSMAP", self.inverse_tagsmap)
        self.tag_tense_pronoun_inflection = tag_const_inflect.TABLE_TENSE_PRONOUN_INFLECTION
    def _get_pronoun(self, person,  gender, number):
        """
        Get pronoun accoriding to person, number, gender
        """
        key = u"-".join([person, gender, number])
        return self.inverse_tagsmap.get(key, "")

    def _get_verb_mark(self, tagstring ):
        """
        get verb mark based on tagstring
        """
        tense = self.get_value('زمن', tagstring)
        voice = self.get_value(u'بناء', tagstring)
        person = self.get_value(u'شخص', tagstring)
        number = self.get_value(u'عدد', tagstring)
        gender = self.get_value(u'جنس', tagstring)
        # get the pronoun name
        pronoun = self._get_pronoun(person, gender, number)
        mood = self.get_value(u'إعراب', tagstring)
        # get the tense original name

        if tense == "مضارع":
            tense_key = "-".join([tense, voice, mood])
        else:
            tense_key = "-".join([tense,voice])
        tense_key = self.inverse_tagsmap.get(tense_key,"")
        # extract inflect_dict
        inflect_dict =  self.tag_tense_pronoun_inflection.get(tense_key, {}).get(pronoun, {})

        # return " ".join([tense_key, pronoun, " ".join(inflect_dict.values())])
        # format the inflection string
        inflect_list = [inflect_dict.get("description",""),
                 inflect_dict.get("case",""),
                 inflect_dict.get("cause",""),
                 inflect_dict.get("subject",""),
                 inflect_dict.get("extra",""),
                  ]
        # remove empty strings
        inflect_list = [x for x in inflect_list if x]
        inflect_string = " ".join(inflect_list)
        return inflect_string

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
        get inflection for a noun
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
            # tense:
            inflect_conj = self._get_verb_mark(tagstring)
            if inflect_conj:
                inflct.append(inflect_conj)

            # tense = self.get_inflect(u'زمن', tagstring)
            # voice = self.get_inflect(u'بناء', tagstring)
            # inflct.append(u"فعل")
            # inflct.append(tense)
            # inflct.append(voice)
            # # case
            # case = self.get_inflect(u'إعراب', tagstring)
            # #~ print((u"###%s####"%case), tagstring)
            # if case:
            #     case_part = case
            #     inflct.append(case_part)
            #
            #     # inflect Mark
            #     mark =self.get_inflect(u'علامة', tagstring)
            #     mark_value = self.get_value(u'علامة', tagstring)
            #     if mark:
            #         #علامة الإعراب
            #         # وعلامة رفعه الضمة
            #         mark_part =""
            #         # علة علامة الإعراب
            #         # وعلامة رفعه الألف لأنه مثنى
            #         cause_part =""
            #         if case == u"مبني":
            #             mark_part = u"على %s"%mark
            #         else:
            #             # استخراج الحالة
            #             #~ مرفوع => رفعه
            #             #~ منصوب => نصبه
            #             #~ مجرور => جره
            #             case_mark = ""
            #             if case == u"مرفوع":
            #                 case_mark = u"رفعه"
            #             elif case == u"منصوب":
            #                 case_mark = u"نصبه"
            #             elif case == u"مجزوم":
            #                 case_mark = u"جزمه"
            #
            #             mark_part = u"وعلامة %s %s"%(case_mark, mark)
            #
            #             # mark cause
            #
            #             condition_5verbs = (self.has_tag(u"مثنى", tagstring)
            #             or (self.has_tag(u'مذكر', tagstring) and self.has_tag(u"جمع", tagstring))
            #             or (self.has_tag(u'مؤنث', tagstring) and self.has_tag(u"مخاطب", tagstring) and self.has_tag(u"مفرد", tagstring))
            #             )
            #             if condition_5verbs:
            #                 cause_part = u"لأنه من الأفعال الخمسة"
            #         inflct.append(mark_part)
            #         inflct.append(cause_part)
                #attached pronoun

                add_p = self.get_inflect(u'ضمير متصل', tagstring)
                #~ print((u"H###%s####"%add_p))
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
            >>> print(tag_maker.inflect(tagcode))
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
    
    
    
