from setuptools import find_packages, setup

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="python-blueprint",
    version="0.1.0",
    author="Origo Dataplattform",
    author_email="dataplattform@oslo.kommune.no",
    description="Serverless application blueprint",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.oslo.kommune.no/origo-dataplatform/serverless-blueprints",
    packages=find_packages(),
    install_requires=[
        "aws-xray-sdk",
        "okdata-aws",
    ],
)
