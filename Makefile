help:
	$(MAKE) -C undefinedvalue help

# For any unknown target, pass it down to undefinedvalue/Makefile
%::
	$(MAKE) -C undefinedvalue $@

