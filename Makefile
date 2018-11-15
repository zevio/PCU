install:
	pip install -r requirements.txt
	python -m spacy download en
	python -m spacy download fr

test:
	python3 -m unittest
