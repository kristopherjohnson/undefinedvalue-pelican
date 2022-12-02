help:
	@echo 'Usage:                                                                    '
	@echo '   make newpost                        make a new post                    '
	@echo '   make html                           (re)generate the web site          '
	@echo '   make clean                          remove the generated files         '
	@echo '   make regenerate                     regenerate files upon modification '
	@echo '   make publish                        generate using production settings '
	@echo '   make serve [PORT=8000]              serve site at http://localhost:8000'
	@echo '   make serve-global [SERVER=0.0.0.0]  serve (as root) to $(SERVER):80    '
	@echo '   make devserver [PORT=8000]          start/restart develop_server.sh    '
	@echo '   make stopserver                     stop local server                  '
	@echo '   make github                         upload the web site via gh-pages   '
	@echo '   make pip-install                    install required pip packages      '
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo
	@echo 'Run "source venv-pelican/bin/activate" before executing any commands.     '
	@echo '                                                                          '

newpost:
	./bin/newpost.py
.PHONY: newpost

# Run these commands to recreate the virtual environment:
#
#   rm -rf venv-pelican
#   python3 -m venv venv-pelican
#   source venv-pelican/bin/activate
#   make pip-install
#
# Alternatively, to create an Anaconda environment:
#
#   conda create --name undefinedvalue pip
#   conda activate undefinedvalue
#   make pip-install
#
pip-install:
	pip install -r pip-requirements.txt
.PHONY: pip-install

venv-pelican:
	python3 -m venv venv-pelican
	source venv-pelican/bin/activate && $(MAKE) pip-install

# For any unknown target, pass it down to undefinedvalue/Makefile
%::
	$(MAKE) -C undefinedvalue $@

