RENDERER_TESTS = tests/test_PixelArray.py tests/test_Color.py tests/test_Clipper.py tests/test_Screen.py tests/test_Renderer.py
MATH_TESTS = tests/test_CoordinateTools.py tests/test_MatrixTools.py tests/test_Vector.py
GAME_TESTS = tests/test_GameObject.py tests/test_Input.py tests/test_Input_mock.py
test-dry: 
	export MC_Live_Connection=0; \
	python -m unittest -v $(RENDERER_TESTS) $(MATH_TESTS) $(GAME_TESTS)	

test: 
	export MC_Live_Connection=1; \
	python -m unittest -v $(RENDERER_TESTS) $(MATH_TESTS) $(GAME_TESTS)

install:
	pip install numpy
	pip install mcpi
	cd mcpi_block_structure; git checkout main; git pull


default: install