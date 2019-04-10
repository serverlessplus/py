all:
	rm -rf build dist serverlessplus.egg-info
	python3 setup.py sdist bdist_wheel
	python3 -m twine check dist/*
	python3 -m twine upload dist/*
