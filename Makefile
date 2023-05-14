DOCKER:=docker

DOCKER_NAME:=oldmankris/pelican
DOCKER_TAG:=latest
DOCKER_BUILD_PLATFORM:=linux/arm/v7,linux/arm64/v8,linux/amd64

DOCKER_BUILD_FLAGS:=--squash --no-cache

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

# Run "make github" using a Docker image
github-with-docker:
	$(DOCKER) run -it --rm -v $(pwd):/app -v ~/.ssh:/root.ssh $(DOCKER_NAME):$(DOCKER_TAG) "cd /app && make github"
.PHONY: run-docker

# Build the Docker image needed by `github-with-docker`
build-docker:
	$(DOCKER) build $(DOCKER_BUILD_FLAGS) -t $(DOCKER_NAME):$(DOCKER_TAG) .
.PHONY: build-docker

# Build and push multi-architecture image needed by `github-with-docker` up to registry.
push-docker:
	$(DOCKER) buildx build --push --platform $(DOCKER_BUILD_PLATFORM) --tag $(DOCKER_NAME):$(DOCKER_TAG) .
.PHONY: push-docker

# For any unknown target, pass it down to undefinedvalue/Makefile
%::
	$(MAKE) -C undefinedvalue $@

