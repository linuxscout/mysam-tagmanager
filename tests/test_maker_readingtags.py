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

import mysam.tagmaker as tagmaker
import mysam.tag_const as tag_const


def main(args):
    import pandas as pd
    # test all existing tags 
    tag_maker = tagmaker.tagMaker()
    tagstr = str(tag_maker)
    print("----")
    for tag in tag_const.TAGSDICT:
        tagstr = str(tag_maker)
        tag_maker.add(tag)
        tagstr_new = str(tag_maker)
        if tagstr == tagstr_new:
            print(u" ".join(["error:old\t",  tagstr, tag, "\n     new:\t",  tagstr_new]).encode('utf8'))
        else:
            print(u" ".join([tag, tagstr_new]).encode('utf8')) 
        decode_tags = tag_maker.decode()
        df = pd.DataFrame(decode_tags)
        print(df)
        tag_maker.add(u"اسم")
        print("******Inflect", tag_maker.inflect().encode('utf8'))
        tag_maker.add(u"فعل")
        print("***Verb***Inflect", tag_maker.inflect().encode('utf8'))
    
    


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
