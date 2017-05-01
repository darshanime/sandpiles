# flake8: noqa
from distutils.core import setup

setup(
    name = "sandpiles",
    packages = ["sandpiles"],
    version = "0.4",
    description = "Generalized sandpiles for eyegasm",
    author = "Darshan Chaudhary",
    author_email = "deathbullet@gmail.com",
    url = "https://github.com/darshanime/sandpiles",
    download_url = "https://github.com/darshanime/sandpiles/archive/0.4.tar.gz",
    keywords = ["sandpiles", "visualization"],
    license = "LICENSE.txt",
    classifiers = [],
    install_requires=[
        "matplotlib==2.0.0", "numpy==1.12.0", "imageio==2.1.2"
    ]
)
