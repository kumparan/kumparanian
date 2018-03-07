from setuptools import setup

# Package details
setup(
    name="kumparanian",
    version="0.0.5",
    entry_points={
        "console_scripts": ["kumparanian = kumparanian.cli:main"]
    },
    author="Bayu Aldi Yansyah",
    author_email="bayualdiyansyah@gmail.com",
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
        "click==6.7",
        "colorama==0.3.9",
        "dill==0.2.7.1",
        "numpy==1.14.1"
    ],
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5"
    ]
)
