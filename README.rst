Mysam: Arabic tags manager, ميسم: إدارة الوسوم العربية
======================================================

تسيير وسوم الكلمات العربية في مجال المعالجة الآلية للغة، ترميز وتفكيك
هذه المكتبة توفر سكريبتا خاصا بترميز وسوم الكلمات (الخصائص الصرفية
والنحوية والدلالية) في عبارة وسم مختصرة على شكل سلسلة حروف قصيرة مرمّزة
نسميها سلسلة الوسوم. يمكن التحويل بين قائمة الوسوم وسلسة الوسوم المختص
يمكن الاستفادة من هذه المكتبة من أجل ترميز الوسوم وفك ترميزها، سنستعملها
في :

-  التحليل الصرفي (`مكتبة
   قلصادي <https://github.com/linuxscout/qalsadi>`__ )
-  التحليل النحوي ( `مكتبة
   ثعلب <https://github.com/linuxscout/thaalab-aranasyn>`__ )
-  التشكيل ( برنامج مشكال\ `برنامج
   مشكال <https://github.com/linuxscout/mishkal>`__ `برنامج
   مشكال <http://tahadz.com/mishkal>`__ )
-  التدقيق اللغوي النحوي (LanguageTool).


كما تقدّم خدمة متميزة في الإعراب بالطريقة القديمة 




-  قائمة الوسوم : Noun, جامد, مضاف, مجرور, متحرك, ينون
-  سلسلة الوسوم المختصرة [N--;--I-;---H;----]
-  جملة الإعراب {اسم مجرور وهو مضاف، والضمير المتصل مبني في محل جر مضاف
   إليه}

\*\* هذه ليست مكتبة للتوسيم، بل لإدارة الوسوم في معالجة اللغة\*\*

Manage arabic words tags, encode, decode This library provides a script
to encode POS tags (Words features : morphology, syntax, semantic), as a
brief tag string called tag string. We can convert between tag list <==>
coded tag string. We plan to use it in:

-  Morphology analysis (`Qalsadi
   library <https://github.com/linuxscout/qalsadi>`__ )
-  Syntactic analysis ( `Thaalab
   Library <https://github.com/linuxscout/thaalab-aranasyn>`__ )
-  Tashkeel ( `Mishkal <https://github.com/linuxscout/mishkal>`__
   `Mishkal-site <http://tahadz.com/mishkal>`__ )
-  LanguageTool - Style and Grammar Checker
   `LanguageTool <https://languagetool.org/>`__.

It provides a special feature, make **traditional Inflection**.

The conversion can be do like:

-  Tags list: Noun, جامد, مضاف, مجرور, متحرك, ينون
-  Encoded tag string [N--;--I-;---H;----]
-  Inflection phrase {اسم مجرور وهو مضاف، والضمير المتصل مبني في محل جر
   مضاف إليه}

\*\* This not a Tagger library, but, a tags mangger for NLP \*\*

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
| Release       | 0.2          |
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

يمكن التجربة على `موقع مشكال <http://tahadz.com/mishkal>`__ ، اختر
تشكيل، ثم مرّر الفأرة على الكلمة لرؤية التلميح

You can test it on `Mishkal Site <http://tahadz.com/mishkal>`__, choose:
Tashkeel, and move mouse over word to get hint.




Installation
============
```
pip install mysam-tagmanager
```    


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

You can load a specific config file by passing parameter to load\_conf.
If the file doesn't exist or failed to be open, the default config is
loaded.

.. code:: python

    configuer = tagconfig.tagConfig()
    configuer.load_config("tag.config")

If you want to know if the input file is opened, fix 'debug' parameter
to 'True'

If you want to know if the input file is open, fix 'debug' parameter to
'True'

.. code:: python

    configuer = tagconfig.tagConfig()
    configuer.load_config("tag.config", debug=True)

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
