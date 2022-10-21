test: 
	python -m unittest -v tests/test_PixelArray.py tests/test_Color.py

install:
	pip install numpy
	pip install mcpi


default: install