from setuptools import setup

# Package details
setup(
    name="kumparanian",
    version="1.0.2",
    entry_points={
        "console_scripts": ["kumparanian = kumparanian.cli:main"]
    },
    author="Bayu Aldi Yansyah, raden panji maharjo",
    author_email="bayualdiyansyah@gmail.com, radenmaharjo@gmail.com",
    url="https://github.com/kumparan/kumparanian",
    description="Kumparanian CLI",
    long_description=open("README.rst", "r").read(),
    license="BSD 3-Clause License",
    packages=[
        "kumparanian",
        "kumparanian.ds",
        "kumparanian.de",
    ],
    install_requires=[
        "click==8.1.7",
        "colorama==0.4.6",
        "dill==0.3.8",
        "numpy==1.26.4"
    ],
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.10",
    ]
)
