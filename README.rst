Mysam: Arabic tags manager, ميسم: إدارة الوسوم العربية
======================================================

تسيير وسوم الكلمات العربية، ترميز وتفكيك Manage arabic words tags,
encode, decode

Tagging System description
--------------------------

You can look at tagging descripton on `doc/tagset.md <doc/tagset.md>`__

Developpers: Taha Zerrouki: http://tahadz.com taha dot zerrouki at gmail
dot com

+---------------+--------------+
| Features      | value        |
+===============+==============+
| Authors       | Taha         |
|               | Zerrouki:    |
|               | http://tahad |
|               | z.com,       |
|               | taha dot     |
|               | zerrouki at  |
|               | gmail dot    |
|               | com          |
+---------------+--------------+
| Release       | 0.1          |
+---------------+--------------+
| License       | `GPL <https: |
|               | //github.com |
|               | /linuxscout/ |
|               | mysam-tagman |
|               | ager/master/ |
|               | LICENSE>`__  |
+---------------+--------------+
| Tracker       | `linuxscout/ |
|               | mysam-tagman |
|               | ager/Issues  |
|               | <https://git |
|               | hub.com/linu |
|               | xscout/mysam |
|               | -tagmanager/ |
|               | issues>`__   |
+---------------+--------------+
| Website       | https://pypi |
|               | .python.org/ |
|               | pypi/mysam-t |
|               | agmanager    |
+---------------+--------------+
| Source        | `Github <htt |
|               | p://github.c |
|               | om/linuxscou |
|               | t/mysam-tagm |
|               | anager>`__   |
+---------------+--------------+
| Feedbacks     | `Comments <h |
|               | ttps://githu |
|               | b.com/linuxs |
|               | cout/mysam-t |
|               | agmanager/is |
|               | sues>`__     |
+---------------+--------------+
| Accounts      | [@Twitter](h |
|               | ttps://twitt |
|               | er.com/linux |
|               | scout)       |
|               | [@Sourceforg |
|               | e](http://so |
|               | urceforge.ne |
|               | t/projects/m |
|               | ysam-tagmana |
|               | ger/)        |
+---------------+--------------+

.. raw:: html

   <!--Doc  |[package Documentaion](http://pythonhosted.org/mysam-tagmanager/)-->

.. raw:: html

   <!--Download  |[pypi.python.org](https://pypi.python.org/pypi/mysam-tagmanager)-->

.. raw:: html

   <!--
   ## Citation
   If you would cite it in academic work, can you use this citation
   ```
   T. Zerrouki‏, mysam-tagmanager,  Arabic Word Tagger,
     https://pypi.python.org/pypi/mysam-tagmanager/, 2018
   ```
   or in bibtex format

   ```bibtex
   @misc{zerrouki2012mysam,
     title={mysam-tagmanager : Arabic Word Tagger},
     author={Zerrouki, Taha},
     url={https://pypi.python.org/pypi/mysam-tagmanager,
     year={2010}
   }
   ```
   -->

مزايا
-----

-  ترميز المزايا إلى وسم موحد مختصر
-  تفكيك الوسم إلى خصائصه
-  توليد الإعراب حسب الطريق التقليدية

Features
--------

-  Encode features to an unified tag string
-  Encode unified tag string to a list of features
-  Generate a traditional inflection style

Applications
------------

-  Text summarizing.
-  Sentences identification.
-  Grammar analysis.
-  Morphological analysis.

تطبيقات
-------

-  التنقيب عن المعلومات.
-  التعرف على الجمل.
-  التحليل النحوي.
-  تسريع التحليل الصرفي.

Demo جرّب
---------

مكن التجربة على `موقع مشكال <http://tahadz.com/mishkal>`__ ، اختر تشكيل،
ثم مرّر الفأرة على الكلمة لرؤية التلميح

You can test it on `Mishkal Site <http://tahadz.com/mishkal>`__, choose:
Tashkeel, and move mouse over word to get hint. |mysam-tagmanager Demo|

.. raw:: html

   <!--
   Installation
   =====
   ```
   pip install mysam-tagmanager
   ```    
       -->

Usage
-----

.. code:: python

    import mysam.tagmaker as tagmaker

Example
-------

Test load configuration
~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    import mysam.tagconfig as tagconfig
    import mysam.tag_const as tag_const
    import pandas as pd
    configuer = tagconfig.tagConfig()
    configuer.load_config()
    # display
    df = pd.DataFrame(tag_const.TAGSDICT)
    print('****tagdict ****')
    print(df)
    *****Result *****
    ****tagdict ****
              1st person  2nd person  3rd person          Beh          FEH  \
    ar_attr          شخص         شخص         شخص           جر          عطف   
    ar_value       متكلم       مخاطب        غائب          باء        الفاء   
    attr          person      person      person  preposition  conjonction   
    code               I           Y           H            B            F   
    inflect                                            بالباء                
    part               4           4           4            3            3   
    pos                4           4           4            2            1   
    value     1st person  2nd person  3rd person          Beh          FEH   
    ....
    ....

Test call tagmaker
~~~~~~~~~~~~~~~~~~

.. code:: python

    import mysam.tagmaker as tagmaker
       
    taglists = [[u'اسم', u'هاء', u'مجرور',],
            u'تعريف::مرفوع:متحرك:ينون:::'.split(":"),
            ]
    for taglist in taglists:
    tag_maker = tagmaker.tagMaker()
    # encode
    tag_maker.encode(taglist)
    print(u"+".join(taglist).encode('utf8'))
    tagstr = str(tag_maker)
    print(tagstr)
    # decode a unifed tag string
    print(tag_maker.decode())

    **** result ****

    اسم+هاء+مجرور
    N--;--I-;----;----
    [(u'نوع الكلمة', u'اسم'), (u'جنس', u'لاشيء'), (u'عدد', u'لاشيء'), (u'إعراب', u'مجرور'), (u'علامة', u'لاشيء'), (u'عطف', u'لاشيء'), (u'جر', u'لاشيء'), (u'تعريف', u'نكرة'), (u'ضمير متصل', u'لاشيء'), (u'استقبال', u'لاشيء'), (u'بناء', u'لاشيء'), (u'زمن', u'لاشيء'), (u'شخص', u'لاشيء')]
    تعريف++مرفوع+متحرك+ينون+++
    ---;--U-;--L-;----
    [(u'نوع الكلمة', u'لاشيء'), (u'جنس', u'لاشيء'), (u'عدد', u'لاشيء'), (u'إعراب', u'مرفوع'), (u'علامة', u'لاشيء'), (u'عطف', u'لاشيء'), (u'جر', u'لاشيء'), (u'تعريف', u'معرفة'), (u'ضمير متصل', u'لاشيء'), (u'استقبال', u'لاشيء'), (u'بناء', u'لاشيء'), (u'زمن', u'لاشيء'), (u'شخص', u'لاشيء')]
        

Exmaple for inflect
~~~~~~~~~~~~~~~~~~~

.. code:: python

    >>> tag_maker = tagmaker.tagMaker()
    >>> tagcode = 'N--;--I-;----;---'
    >>> print(tag_maker.inflect(tagcode).encode('utf8'))
    اسم مجرور وعلامة جرّه الياء لأنه جمع مذكر سالم وهو مضاف، والضمير المتصل مبني في محل جر مضاف إليه

Exmaple for add tag
~~~~~~~~~~~~~~~~~~~

.. code:: python

    >>> tag_maker = tagmaker.tagMaker()
    >>> tagcode = 'N--;--I-;----;---'
    >>> tag_new = u"تعريف"
    >>> tag_maker.add(tag_new)
    >>> tag_new = u"اسم"
    >>> tag_maker.add(tag_new)
    >>> print(str(tag_maker).encode('utf8'))
    N--;----;--L-;----

Exmaple for has tag
~~~~~~~~~~~~~~~~~~~

.. code:: python

    >>> tag_maker = tagmaker.tagMaker()
    >>> tagcode = 'N--;--I-;----;---'
    >>> tag_search = u"مجرور"
    >>> print(tag_maker.has_tag(tag_search, tagcode))
    True

.. |mysam-tagmanager Demo| image:: doc/images/mysam_demo.png%20alt=%22mysam-tagmanager
