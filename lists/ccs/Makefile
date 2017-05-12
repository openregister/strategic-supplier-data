URL=https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/612347/Crown_Reps_and_Strategic_Suppliers_May2017.docx

.PHONY: init test all clean data

list.tsv: data.tsv map.py
	python3 map.py < data.tsv > $@

data.tsv:	data.docx data.py
	python3 data.py data.docx > $@

data.docx:
	curl -Ls $(URL) > $@

flake8:
	flake8 bin

clean:
	find . -name "*.pyc" | xargs rm -f
	find . -name "__pycache__" | xargs rm -rf
	rm -rf cache

init:
	pip3 install --upgrade -r requirements.txt
