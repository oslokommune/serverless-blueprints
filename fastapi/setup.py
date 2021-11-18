from setuptools import setup

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="fastapi-blueprint",
    version="0.1.0",
    author="Origo Dataplattform",
    author_email="dataplattform@oslo.kommune.no",
    description="Serverless FastAPI demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.oslo.kommune.no/origo-dataplatform/serverless-blueprints",
    py_modules=["app"],
    install_requires=[
        "aws-xray-sdk",
        "fastapi",
        "mangum",
        "okdata-aws>=1.0.0",
        "uvicorn",
    ],
)
