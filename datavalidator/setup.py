from setuptools import setup, find_packages

setup(
    name="datavalidator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["pandas"],
    author="Your Name",
    description="Validate data schemas for CSVs/JSONs",
)
