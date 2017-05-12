#
#  target register data
#
REGISTER=data/strategic-supplier/strategic-supplier.tsv

FIXUPS=\
	fixup/name.tsv

#
#  source CCS list
#
SOURCE=lists/ccs/list.tsv

all: $(REGISTER)

$(REGISTER):	$(SOURCE) $(FIXUPS)
	mkdir -p data/strategic-supplier
	bin/strategic-supplier.py < $(SOURCE) > $@

# remove targets
clobber:
	rm -f $(REGISTER) $(DATA) $(MAPS)

clean::
	-find . -name "*.pyc" | xargs rm -f
	-find . -name "__pycache__" | xargs rm -rf
