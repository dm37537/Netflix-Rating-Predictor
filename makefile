all:

Netflix.html: Netflix.py
	pydoc3 -w Netflix

Netflix.log:
	git log > Netflix.log

RunNetflix.tmp: RunNetflix.py RunNetflix.in RunNetflix.out
	RunNetflix.py < RunNetflix.in > RunNetflix.tmp
	diff RunNetflix.tmp RunNetflix.out

TestNetflix.out: TestNetflix.py
	coverage3 run    --branch TestNetflix.py >  TestNetflix.out 2>&1
	coverage3 report -m                      >> TestNetflix.out

clean:
	rm -f .coverage
	rm -f *.pyc
	rm -f RunNetflix.tmp
	rm -f TestNetflix.out
	rm -rf __pycache__
