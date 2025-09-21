#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_unit_coder.py
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
import unittest
import mysam.tagcoder
import mysam.taginflector



from fixtures import tagcode_dataset


class tagCoderTestCase(unittest.TestCase):
    """Tests for `Lemmatizer`."""

    def setUp(self):
        """
        initial lemmatizer
        """
        self.word_lemma_list= tagcode_dataset.Lemmas_DataSet
        self.limit = 1000
        self.mytagcoder = mysam.tagcoder.tagCoder()
        self.inflector = mysam.taginflector.tagInflector()


    def test_word_cases(self, ):
        """ test word case"""
        # ~ word = "وفي"
        # ~ expected_tagcode = 'V-1;F1Y-i--;---'
        # ~ tagscode_list = self._check_word_tags(word)
        # ~ print(tagscode_list)
        # ~ self.assertIn(expected_tagcode, tagscode_list)
        
        # ~ word = "بالمدرستين"
        # ~ expected_tagcode = 'NA-;F2----I;-BL'
        # ~ tagscode_list = self._check_word_tags(word)
        # ~ print(tagscode_list)
        # ~ self.assertIn(expected_tagcode, tagscode_list)
        
        word = "واحتاج"
        expected_tagcode = 'V-0;M1H-paB;W--'
        expected_inflect = "فعل ماض مبني على الفتح الظاهر على آخره"
        tags = ['الماضي المعلوم', 'هو', 'n',"مبني", 'Verb', "معطوف بالواو"]        
        # ~ expected_tagcode = ''
        tagscode = self.mytagcoder.encode(tags)
        inflect  = self.inflector.inflect(tagscode)
        print(word, tagscode, inflect)
        
        self.assertEqual(expected_tagcode, tagscode, "Error on tagscode")
        self.assertEqual(expected_inflect, inflect, "Error on Inflection")

    def test_get_mark_cases(self, ):
        """ test word case"""

        tagscode = 'V-0;M1H-paB;W--'
        expected_inflect = "فعل ماض مبني على الفتح الظاهر على آخره"
        tags = ['الماضي المعلوم', 'هو', 'n',"مبني", 'Verb', "معطوف بالواو"]
        # ~ expected_tagcode = ''
        inflect  = self.inflector._get_verb_mark(tagscode)
        self.assertEqual(expected_inflect, inflect, "Error on Inflection")


    def test_word_inflect(self, ):
        """ test word case"""
        word = "ويحتاج"
        tagscode = 'V-0;M1H-faU;W--'
        expected_inflect = "فعل مضارع   مرفوع وعلامة رفعه الضمة الظاهرة على آخره"
        inflect  = self.inflector.inflect(tagscode)
        self.assertEqual(expected_inflect, inflect, "Error on Inflection")

        word = "ويحتاجه"
        tagscode = 'V-0;M1H-faU;W-H'
        expected_inflect = "فعل مضارع   مرفوع وعلامة رفعه الضمة الظاهرة على آخره والضمير المتصل مبني في محل نصب مفعول به"
        inflect  = self.inflector.inflect(tagscode)
        self.assertEqual(expected_inflect, inflect, "Error on Inflection")

        word = "ويحتاجانها"
        tagscode = 'V-0;M2H-faU;W-H'
        expected_inflect = "فعل مضارع   مرفوع وعلامة رفعه ثبوت النون لأنه من الأفعال الخمسة وألف الاثنين: ضمير متصل مبني في محل رفع فاعل والضمير المتصل مبني في محل نصب مفعول به"
        inflect  = self.inflector.inflect(tagscode)
        self.assertEqual(expected_inflect, inflect, "Error on Inflection")

    def test_word_addtag(self, ):
        """ test word case"""
        word = "ويحتاج"
        tagscode = 'V-0;M1H-faU;W--'
        expected_tagscode = 'V-0;M1H-faU;W-H'
        new_tagscode  = self.mytagcoder.add_tag("ضمير متصل", tagscode)
        self.assertEqual(expected_tagscode, new_tagscode, "Error on adding tag")

        tagscode = 'V-0;M1H-faU;W-H'
        expected_tagscode = 'V-0;M1H-faU;W--'
        new_tagscode  = self.mytagcoder.remove_tag("ضمير متصل", tagscode)
        self.assertEqual(expected_tagscode, new_tagscode, "Error on adding tag")


if __name__ == '__main__':
    unittest.main()
