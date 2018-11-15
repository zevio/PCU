install:
	pip install -r requirements.txt
	python3 -m spacy download en
	python3 -m spacy download fr

test:
	python3 -m unittest
