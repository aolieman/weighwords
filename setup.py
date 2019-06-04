from setuptools import setup

setup(
    name = "wayward",
    version = "0.2",
    author = "Lars Buitinck",
    author_email = "L.J.Buitinck@uva.nl",
    description = "Python library for creating word weights/word clouds from text",
    keywords = "word cloud nlp language model",
    license = "LGPL",
    package_data = {"wayward": ["py.typed"]},
    packages = ["wayward"],
    install_requires = ["numpy>=1.15.0"],
    tests_require = ["pytest"],
    classifiers = [
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Programming Language :: Python :: 3.7",
        "Topic :: Text Processing",
    ]
)
