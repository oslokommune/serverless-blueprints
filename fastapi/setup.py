from setuptools import setup

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="fastapi-blueprint",
    version="0.1.0",
    author="Oslo Origo",
    author_email="dataspeilet@oslo.kommune.no",
    description="Serverless FastAPI demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oslokommune/serverless-blueprints",
    py_modules=["app"],
    install_requires=[
        "aws-xray-sdk",
        "fastapi>=0.109.2",
        "mangum",
        "okdata-aws>=4.1,<5",
        "uvicorn",
    ],
    python_requires=">=3.11",
)
