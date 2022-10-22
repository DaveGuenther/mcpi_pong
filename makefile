test: 
	python -m unittest discover -v tests/

install:
	pip install numpy
	pip install mcpi


default: install