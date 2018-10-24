from setuptools import setup

setup(
    name="tufte",
    version="0.1.0",
    description="Tufte in python.",
    author="David Pattinson",
    author_email="davipatti10@gmail.com",
    packages=["tufte"],
    include_package_data=True,
    install_requires=[
        "matplotlib>=3.0.0"
    ])
