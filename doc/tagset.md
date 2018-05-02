# Description
## Structure
	TAG_PARTS_SIZES=[[3, 4, 5, 5]]
	TAG_PARTS_SEP  =';'
	Structure  =[---;----;-----;-----]
## Parts
	 Word Type نوع الكلمة
		 Sub Class صنف فرعي
		 transitive
	 Conjugation
		 Gender الجنس
		 Number العدد
		 Inlfection case الحالة الإعرابية
		 Inflection marks
	 Procletics and prefixes
		 Conjuction
		 preposition
		 Definition
		 Enclitics
	 Special Verb
		 Istiqbal
		 Voice البناء
		 tense الزمن
		 person الشخص
	Parameters: must starts by #PARAM:
## Detailled
## Word Type نوع الكلمة:

		 N: Noun
		 V: Verb
		 T: Tool
		 P: Punctuation
		 S: Symbol
		 D: Numeric
		 -: Undef
	 Sub Class صنف فرعي:
		 M: Masdar
	 transitive:
		 0: intransitive
		 1: transitive
		 2: double transitive
		 4: commun
		 تعدي: undef
## Conjugation:

	 Gender الجنس:
		 M: masculine
		 F: Feminine
		 -: none
	 Number العدد:
		 1: single
		 2: dual
		 3: plural
		 4: plural
		 -: none
	 Inlfection case الحالة الإعرابية:
		 U: marfou3
		 0: manjzoum
		 I: majrour
		 A: mansoub
		 B: mabni
		 -: undef
	 Inflection marks:
		 u: damma
		 a: fatha
		 i: kasra
		 0: sukun
		 A: alef
		 W: waw
		 Y: yeh
		 N: noon
		 -: undef
## Procletics and prefixes:

	 Conjuction:
		 W: WAW
		 F: FEH
		 -: undef
	 preposition:
		 B: Beh
		 K: Kaf
		 L: Lam
		 -: undef
	 Definition:
		 L: definited
		 -: indefinite
	 Enclitics:
		 H: Heh
		 -: undef
## Special Verb:

	 Istiqbal:
		 s: istqbal
		 -: undef
	 Voice البناء:
		 a: acive voice
		 p: acive voice
		 -: undef
	 tense الزمن:
		 p: past
		 f: present
		 i: imperative
		 -: undef
	 person الشخص:
		 I: 1st person
		 Y: 2nd person
		 H: 3rd person
		 -: undef
##Parameters: must starts by #PARAM::

# Table of configuration
## Columns description
* #Part
* Pos
* Attribute
* خاصية
* code
* Value
* قيمة
* inflection
* 


## Word Type نوع الكلمة


#Part|Pos|Attribute|خاصية|code|Value|قيمة|inflection|
-----|---|---------|-----|----|-----|----|----------|
1|1|word_type|نوع الكلمة|N|Noun|اسم|اسم|
1|1|word_type|نوع الكلمة|V|Verb|فعل|فعل|
1|1|word_type|نوع الكلمة|T|Tool|أداة|حرف|
1|1|word_type|نوع الكلمة|P|Punctuation|ترقيم|علامة ترقيم|
1|1|word_type|نوع الكلمة|S|Symbol|رمز|رمز|
1|1|word_type|نوع الكلمة|D|Numeric|عدد|عدد|
1|1|word_type|نوع الكلمة|-|Undef|لاشيء||
1|2|subclass|صنف|M|Masdar|مصدر||
1|3|transitive|تعدي|0|intransitive|لازم||
1|3|transitive|تعدي|1|transitive|متعدي||
1|3|transitive|تعدي|2|double transitive|متعدي لمفعولين||
1|3|transitive|تعدي|4|commun|مشترك||
1|3|transitive|-|تعدي|undef|لاشيء||


## Conjugation


#Part|Pos|Attribute|خاصية|code|Value|قيمة|inflection|
-----|---|---------|-----|----|-----|----|----------|
2|1|gender|جنس|M|masculine|مذكر|مذكر
2|1|gender|جنس|F|Feminine|مؤنث|مؤنث|
2|1|gender|جنس|-|none|لاشيء||
2|2|number|عدد|1|single|مفرد|مفرد|
2|2|number|عدد|2|dual|مثنى|مثنى|
2|2|number|عدد|3|plural|جمع|جمع|
2|2|number|عدد|4|plural|جمع تكسير|جمع تكسير|
2|2|number|عدد|-|none|لاشيء||
2|3|case|إعراب|U|marfou3|مرفوع|مرفوع|
2|3|case|إعراب|0|manjzoum| مجزوم|مجزوم|
2|3|case|إعراب|I|majrour|مجرور|مجرور|
2|3|case|إعراب|A|mansoub|منصوب|منصوب|
2|3|case|إعراب|B|mabni|مبني|مبني|
2|3|case|إعراب|-|undef|لاشيء||
2|4|mark|علامة|u|damma|الضمة|الضمة|
2|4|mark|علامة|a|fatha|الفتحة|الفتحة|
2|4|mark|علامة|i|kasra|الكسرة|الكسرة|
2|4|mark|علامة|0|sukun|السكون|السكون|
2|4|mark|علامة|A|alef|الألف|الألف|
2|4|mark|علامة|W|waw|الواو|الواو|
2|4|mark|علامة|Y|yeh|الياء|الياء|
2|4|mark|علامة|N|noon|ثبوت النون|ثبوت النون|
2|4|mark|علامة|-|undef|لاشيء||


## Procletics and prefixes


#Part|Pos|Attribute|خاصية|code|Value|قيمة|inflection|
-----|---|---------|-----|----|-----|----|----------|
3|1|conjonction|عطف|W|WAW|الواو||
3|1|conjonction|عطف|F|FEH|الفاء||
3|1|conjonction|عطف|-|undef|لاشيء||
3|2|preposition|جر|B|Beh|باء|بالباء|
3|2|preposition|جر|K|Kaf|كاف|بالكاف|
3|2|preposition|جر|L|Lam|لام|باللام|
3|2|preposition|جر|-|undef|لاشيء||
3|3|definite|تعريف|L|definited|معرفة||
3|3|definite|تعريف|-|indefinite|نكرة||
3|4|encletic|ضمير متصل|H|Heh|ضمير متصل|والضمير المتصل مبني|
3|4|encletic|ضمير متصل|-|undef|لاشيء||


## Special Verb


#Part|Pos|Attribute|خاصية|code|Value|قيمة|inflection|
-----|---|---------|-----|----|-----|----|----------|
4|1|istqbal|استقبال|s|istqbal|استقبال|استقبال|
4|1|istqbal|استقبال|-|undef|لاشيء||
4|2|voice|بناء|a|acive voice|معلوم|مبني للمعلوم|
4|2|voice|بناء|p|acive voice|مجهول|مبني للمجهول|
4|2|voice|بناء|-|undef|لاشيء||
4|3|tense|زمن|p|past|ماض|ماضي|
4|3|tense|زمن|f|present|مضارع|مضارع|
4|3|tense|زمن|i|imperative|أمر|أمر|
4|3|tense|زمن|-|undef|لاشيء||
4|4|person|شخص|I|1st person|متكلم||
4|4|person|شخص|Y|2nd person|مخاطب||
4|4|person|شخص|H|3rd person|غائب||
4|4|person|شخص|-|undef|لاشيء||


##Parameters: must starts by #PARAM:


# TAGS MAP
Feature|maps
-------|----
الأمر المؤكد|أمر, مؤكذ
الأمر|أمر
المضارع المعلوم|مضارع, معلوم, مرفوع
نحن|متكلم, جمع
المضارع المجهول|مضارع, مجهول, مرفوع
مضاف|ضمير متصل
المضارع المنصوب|مضارع, معلوم, منصوب
أنت|مخاطب, مذكر, مفرد
أنا|متكلم, مفرد
المضارع المؤكد الثقيل|مضارع, معلوم, مؤكد
أنتما|مخاطب, مذكر, مثنى
أنتما مؤ|مخاطب, مؤنث, مثنى
Verb|فعل
تعريف|معرفة
المضارع المجزوم|مضارع, معلوم, مجزوم
Noun|اسم
الماضي المجهول|ماضي, مجهول
هن|غائب, مؤنث, جمع
هم|غائب, مذكر, جمع
هما|غائب, مذكر, مثنى
المضارع المجهول المنصوب|مضارع, مجهول, منصوب
مفعول به|ضمير متصل
هما مؤ|غائب, مؤنث, مثنى
هي|غائب, مؤنث, مفرد
المضارع المؤكد الثقيل المجهول |مضارع, مجهول, مؤكد
هو|غائب, مذكر, مفرد
أنتِ|مخاطب, مؤنث, مفرد
الماضي المعلوم|ماضي, معلوم
n|لازم
المضارع المجهول المجزوم|مضارع, مجهول, مجزوم
أنتم|مخاطب, مذكر, جمع
أنتن|مخاطب, مؤنث, جمع
y|متعدي
