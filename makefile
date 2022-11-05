RENDERER_TESTS = tests/test_PixelArray.py tests/test_Color.py tests/test_Clipper.py tests/test_Screen.py tests/test_Painter.py

test: 
	python -m unittest -v $(RENDERER_TESTS)

install:
	pip install numpy
	pip install mcpi


default: install