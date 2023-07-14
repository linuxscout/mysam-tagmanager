#/usr/bin/sh
# Build mysam-tagmanager

default: all
# Clean build files
clean:
	
backup: 
	
#create all files 
all: 

install:
	sudo python setup.py install
install3:
	sudo python3 setup.py install
# Publish to github
publish:
	git push origin master 

md2rst:
	pandoc -s -r markdown -w rst README.md -o README.rst
md2html:
	pandoc -s -r markdown -w html README.md -o README.html
	
wheel:
	sudo python3 setup.py bdist_wheel
wheel3:
	sudo python3 setup.py bdist_wheel
sdist:
	sudo python3 setup.py sdist
upload:
	echo "use twine upload dist/mysam-tagmanager-0.1.tar.gz"
	
test:
	cd tests; python3 test_maker.py
test_unit:
	cd tests; python3 -m pytest test_unit_tagcoder.py
tagsetdoc:
	mv doc/tagset.md doc/tagset.md.bak
	python3 tests/makedoc.py > doc/tagset.md
doc:
	epydoc -v --config epydoc.conf
