import logging

import uvicorn
from fastapi import FastAPI, Request

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


app = FastAPI()


# middleware
@app.middleware("http")
async def log_request(request: Request, call_next):
    logging.debug(f"Request Method: {request.method}")
    logging.debug(f"Request Path: {request.url.path}")

    headers = dict(request.headers)
    logging.debug(f"Request Headers: {headers}")

    body = await request.body()
    logging.debug(f"Request Body: {body.decode('utf-8')}")

    response = await call_next(request)
    return response


@app.get("/")
def test_get():
    return {"Hello": "World"}


@app.post("/")
def test_post():
    return {"Hello": "World"}


@app.put("/")
def test_put():
    return {"Hello": "World"}


@app.delete("/")
def test_delete():
    return {"Hello": "World"}


@app.patch("/")
def test_patch():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="debug", reload=True)
    # uvicorn main:app --reload
