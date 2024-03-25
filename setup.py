from setuptools import setup, find_packages

setup(
    name="DataPrepKit",
    version="0.1.0",
    author="Mohammad Mrayyan",
    author_email="mohammad.t.mrayyan@gmail.com",
    description="A series of functions that assist in reading data from a variety of file formats, summarizing datasets, managing missing values, and encoding categorical data.",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
