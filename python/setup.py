from setuptools import find_packages, setup

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="python-blueprint",
    version="0.1.0",
    author="Oslo Origo",
    author_email="dataspeilet@oslo.kommune.no",
    description="Serverless application blueprint",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oslokommune/serverless-blueprints",
    packages=find_packages(),
    install_requires=[
        "aws-xray-sdk",
        "okdata-aws>=2,<3",
    ],
    python_requires=">=3.11",
)
