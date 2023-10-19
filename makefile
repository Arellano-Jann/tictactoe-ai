1:
	python3 .tictac_test_1.py
2:
	python3 .tictac_test_2.py
3:
	python3 .tictac_test_3.py
4:
	python3 .tictac_test_4.py
5:
	python3 .tictac_test_5.py
6:
	python3 .tictac_test_6.py
7:
	python3 .tictac_test_7.py

c:
	make 2 4

c2:
	make 1 3 5 6

c1:
	make 1 2 3 4 5 6

all:
	python3 .tictac_test_1.py
	python3 .tictac_test_2.py
	python3 .tictac_test_3.py
	python3 .tictac_test_4.py
	python3 .tictac_test_5.py
	python3 .tictac_test_6.py
	python3 .tictac_test_7.py