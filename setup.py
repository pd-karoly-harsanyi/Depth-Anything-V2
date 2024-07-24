import setuptools
import os

local_path = os.path.dirname(os.path.abspath(__file__))

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="metric_depth",
    version="0.0.1",
    packages=setuptools.find_packages(),
    install_requires=requirements
)
