# https://mangum.io/adapter/

from fastapi import FastAPI
from mangum import Mangum
from okdata.aws.logging import add_fastapi_logging, log_add

app = FastAPI()

add_fastapi_logging(app)


@app.get("/")
def read_root():
    log_add(hello="world")
    return {"hello": "world"}


@app.get("/error")
def read_error():
    log_add(hello="error")
    raise Exception("This is wrong!")


handler = Mangum(app)
