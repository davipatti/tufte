from setuptools import setup

setup(
    name="tufte",
    version="0.1.0",
    description="Tufte in python.",
    packages=["tufte"],
    include_package_data=True,
    install_requires=[
        "matplotlib",
        "numpy",
        "pandas",
        "future"
    ])
