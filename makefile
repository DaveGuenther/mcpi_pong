test: 
	python -m unittest -v tests/test_PixelArray.py tests/test_Color.py tests/test_Clipper.py tests/test_Screen.py tests/test_Painter.py

install:
	pip install numpy
	pip install mcpi


default: install