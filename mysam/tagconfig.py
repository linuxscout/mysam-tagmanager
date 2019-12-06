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
        self.tagsdict ={}
        self.inverse_tagsdict ={}
        self.attr_tagsdict= {}
        self.tagsmap ={}
        #parameters
        self.tag_parts_sizes =[]

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
        @type debug: boolean
        """
        # if given file, try to use it, else load
        if config_file:
            try:
                with codecs.open(config_file, 'r', encoding='utf-8') as infile:
                    self.lines = infile.readlines()
                #~ print("load configfile with success")

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
            if not line.startswith('#') and not line.startswith('$') and line:
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
            elif line.startswith('$PARAM:'):
                alist = line[7:].split("=")
                if len(alist) >= 2:
                    field_name = alist[0]
                    values = alist[1].split(";")
                    if field_name == "TAG_PARTS_SIZES":
                        self.tag_parts_sizes = [self.str2int(v) for v in values]
            elif line.startswith('$MAP:'):
                alist = line[5:].split("=")
                if len(alist) >= 2:
                    tag = alist[0]
                    values = alist[1].split(";")
                    self.tagsmap[tag] = values
                
        #~ # load on Global variables
        #~ tag_const.TAGSDICT = self.tagsdict 
        #~ tag_const.INVERSE_TAGSDICT =self.inverse_tagsdict 
        #~ tag_const.ATTR_TAGSDICT =self.attr_tagsdict
        #~ # if structure not defined, the default structure is used.
        #~ if self.tag_parts_sizes:
            #~ tag_const.TAG_PARTS_SIZES = self.tag_parts_sizes
        #~ if self.tagsmap:
            #~ tag_const.TAGSMAP = self.tagsmap

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
            if line and not line.startswith('$'):
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
        textlines.append("## Structure")
        textlines.append("\tTAG_PARTS_SIZES=[%s]"%tag_const.TAG_PARTS_SIZES)
        textlines.append("\tTAG_PARTS_SEP  ='%s'"%tag_const.TAG_PARTS_SEP)
        structure = []
        for i in range(len(tag_const.TAG_PARTS_SIZES)):
            structure.append('-'*tag_const.TAG_PARTS_SIZES[i])
        structure = tag_const.TAG_PARTS_SEP.join(structure)
        textlines.append("\tStructure  =[%s]"%structure)
        textlines.append("## Parts")

        for line in self.lines[1:]:
            line = line.strip('\n')
            if line and not line.startswith('$'):
                if line.startswith('##'):
                    # is a sub class 
                    textlines.append(u'\t\t%s'%line[2:])
                    # to do makr it
                elif line.startswith('#'):
                    textlines.append(u"\t%s"%line[1:])
        textlines.append("## Detailled")
        for line in self.lines[1:]:
            line = line.strip('\n')
            if line and not line.startswith('$'):
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
    def markdown_map(self,):
        """ Dispaly MAP tags and tags in markdown style as categories.
        read lines from load config, the create a Markdown text to document out tag ste system
        @return: text.
        @rtype: unicode text
        """
        textlines =[]
        ## prepare the Mapping
        textlines.append("\n# TAGS MAP")
        textlines.append("Feature|maps")
        textlines.append("-------|----")

        for k in tag_const.TAGSMAP:
            textlines.append("%s|%s"%(k, u', '.join(tag_const.TAGSMAP[k])))
        
        return u"\n".join(textlines)
                    
if __name__ == "__main__":
    import pandas as pd
    # set encoding
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    
    configuer = tagConfig()
    configuer.load_config("config/tag.config", debug=True)
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
