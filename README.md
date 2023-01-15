# Cloud-Data-Engineering-W1
## Advanced Testing Techniques
This is a submodule for advanced testing


### Setup
1. Create and source Venv
```bash
virtualenv ~/.advanced-testing
source ~/.advanced-testing/bin/activate
```

2. Create scaffold
```bash
touch Makefile
touch hello.py test_hello.py 
touch requirements.txt
```

3. Populate `Makefile`
```bash
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=hello --cov=hellocli test_hello.py

lint:
	pylint --disable=R,C hello.py hellocli.py

all: install lint test
```

### How to debug
* print
* pdb
* testing


#### Learning about gist
Hey I added a gist [check it out](https://gist.github.com/cs-uche/a302ff477d285f957f135aaa959e9136)
