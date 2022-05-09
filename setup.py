""" ToDo Application Setup """

from glob import glob
from os.path import basename, splitext

from setuptools import find_packages, setup

setup(
    name="todo-api",
    version="0.1.0",
    description="ToDo API",

    classifiers=[
        "Programming Language :: Python :: 3.7"
    ],

    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
    install_requires=["flask-restx==0.1.1", "pymongo==3.10.1"]
)
