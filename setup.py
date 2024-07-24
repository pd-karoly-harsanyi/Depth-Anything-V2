from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="metric_depth",
    version="0.0.1",
    packages=find_packages(exclude=["assets", "depth_anything_v2"]),
    python_requires=">=3.9",
    install_requires=requirements,
    include_package_data=True,
    zip_safe=False,
)
