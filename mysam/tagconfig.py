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
try:
    from . import tag_const 
except:
    import tag_const
    
import re
import codecs
class tagConfig:
    """ Load config from given configuration """
    tagsdict ={}
    inverse_tagsdict = {}
    attr_tagsdict = {}
    
    def __init__(self,):
        # read config fist
        pass;
        #~ self.load_config()
        self.lines =[]
    @staticmethod
    def str2int(nb):
        """ Safe str 2 int conversion """
        try:
            return int(nb)
        except ValueError:
            return 0       
    def load_config(self, config_file = False, debug=False):
        """ Load config rules  from a file, or use default config file
        You can find a tag.config like in doc directory
        @param config_file: file to load
        @type config_file: string
        @param debug: it exist when file is not found
        @typedebug: boolean
        """
        # if given file, try to use it, else load
        if config_file:
            try:
                with codecs.open(config_file, 'r', encoding='utf-8') as infile:
                    self.lines = infile.readlines()

            except:
                if debug:
                    import sys
                    print("can't Open file", config_file)
                    sys.exit()
                self.lines = tag_const.TAGS_CONFIG.split("\n")
        else:
            self.lines = tag_const.TAGS_CONFIG.split("\n")

        for line in self.lines:
            line = line.strip("\n")
            if not line.startswith('#') and line:
                alist = line.split(";")
                alist = [x.strip() for x in alist]
                # prepare keys
                ar_key = alist[6].strip()
                en_key = alist[5].strip()
                part_key = self.str2int(alist[0])
                pos_key = self.str2int(alist[1])
                code = alist[4]
                attr = alist[2]
                attr_ar = alist[3]
                key = u":".join([str(part_key), str(pos_key), code])
                # extract fields
                adict = {
                'part': part_key,
                'pos': pos_key,
                'attr': alist[2],
                'ar_attr': alist[3],
                'code': code ,
                'value': alist[5],
                'ar_value': alist[6],
                'inflect': alist[7],
                }
                # value based index
                self.tagsdict[ar_key] = adict
                self.tagsdict[en_key] = adict
                # code based index
                self.inverse_tagsdict[key] = adict
                #attrib based index
                self.attr_tagsdict[attr] = adict
                self.attr_tagsdict[attr_ar] = adict
        # load on Global variables
        tag_const.TAGSDICT = self.tagsdict 
        tag_const.INVERSE_TAGSDICT =self.inverse_tagsdict 
        tag_const.ATTR_TAGSDICT =self.attr_tagsdict

    def markdown(self,):
        """ Dispaly rules and tags in markdown style.
        read lines from load config, the create a Markdown text to document out tag ste system
        @return: text.
        @rtype: unicode text
        """
        textlines =[]        
        textlines.append("# Table of configuration")
        #~ lines = tag_const.TAGS_CONFIG.split("\n")
        # make headers + table seprator
        headers = self.lines[0].strip('\n').replace(';','|')
        textlines.append("## Columns description")
        textlines.append("* " + self.lines[0].replace(';','\n* '))
        headers += "\n" +re.sub('[^|]','-', headers)
        # avoid the first line
        for line in self.lines[1:]:
            line = line.strip('\n')
            if line:
                if line.startswith('##'):
                    # is a sub class 
                    pass;
                    # to do makr it
                elif line.startswith('#'):
                    textlines.append('\n')
                    textlines.append(u"#"+line)
                    textlines.append('\n')
                    textlines.append(headers)
                else:
                    textlines.append(line.replace(';','|'))
        return u"\n".join(textlines)
                    
    def markdown_cat(self,):
        """ Dispaly rules and tags in markdown style as categories.
        read lines from load config, the create a Markdown text to document out tag ste system
        @return: text.
        @rtype: unicode text
        """
        #~ lines = tag_const.TAGS_CONFIG.split("\n")
        textlines =[]
        textlines.append("# Description")
        textlines.append("## Parts")

        for line in self.lines[1:]:
            line = line.strip('\n')
            if line:
                if line.startswith('##'):
                    # is a sub class 
                    textlines.append(u'\t\t%s'%line[2:])
                    # to do makr it
                elif line.startswith('#'):
                    textlines.append(u"\t%s"%line[1:])
        textlines.append("## Detailled")
        for line in self.lines[1:]:
            line = line.strip('\n')
            if line:
                if line.startswith('##'):
                    # is a sub class 
                    textlines.append(u'\t%s:'%line[2:])
                    # to do makr it
                elif line.startswith('#'):
                    textlines.append(u"#%s:\n"%line)
                else:
                    # print a sub category
                    alist = line.split(";") 
                    textlines.append("\t\t "+ u"%s: %s"%(alist[4], alist[5]))
        return u"\n".join(textlines)
                    
if __name__ == "__main__":
    import pandas as pd
    # set encoding
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    
    configuer = tagConfig()
    configuer.load_config()
    df = pd.DataFrame(tag_const.TAGSDICT)
    print('****tagdict ****')
    print(df)
    df2 = pd.DataFrame(tag_const.INVERSE_TAGSDICT)
    print('****inverse tagdict ****')
    print(df2)
    df3 = pd.DataFrame(tag_const.INVERSE_TAGSDICT)
    print('****attr tagdict ****')
    print(df3)
    print("************Markdown ******************")
    md = configuer.markdown_cat()
    print(md.encode('utf8'))
    mdc = configuer.markdown()
    print(mdc.encode('utf8'))    
