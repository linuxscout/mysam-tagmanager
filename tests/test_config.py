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
sys.path.append('.')
import os
import mysam.tag_const as tag_const
import mysam.tagconfig as tagconfig

import os
def main(args):
    import pandas as pd
    configuer = tagconfig.tagConfig()
    file_conf = os.path.join( os.path.dirname(__file__), "tag.config")
    configuer.load_config(file_conf, debug=True)
    # display
    df = pd.DataFrame(tag_const.TAGSDICT)
    print('****tagdict ****')
    print(df)
    df2 = pd.DataFrame(tag_const.INVERSE_TAGSDICT)
    print('****inverse tagdict ****')
    print(df2)
    df3 = pd.DataFrame(tag_const.ATTR_TAGSDICT)
    print('****attr tagdict ****')
    print(df3)
    #~ df4 = pd.DataFrame(tag_const.TAGSMAP)
    print('****Tags MAP ****')
    #~ print(df4)
    for k in tag_const.TAGSMAP:
        line = u"#MAP:%s=%s"%(k, u';'.join(tag_const.TAGSMAP[k]))
        print(line.encode('utf8'))
    print('**** Structure ****')
    print(tag_const.TAG_PARTS_SIZES)
    print(configuer.tag_parts_sizes)
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
