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
import mysam.tagconfig
def main(args):
    import pandas as pd
    configuer = mysam.tagconfig.tagConfig()
    configuer.load_config()
    md = configuer.markdown_cat()
    print(md.encode('utf8'))
    mdc = configuer.markdown()
    print(mdc.encode('utf8'))  
    mdm = configuer.markdown_map()
    print(mdm.encode('utf8'))  

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
