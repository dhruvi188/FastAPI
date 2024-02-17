from typing import Union

from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

class Blog(BaseModel):
    title: str
    body: str
    description: str | None = None

@app.post('/blog')
def create_blog(request: Blog):
    title = request.title
    return {'data': f'{request.title}'}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/blog/unpublished")
def unpublished():
    return {'data': 'unpublished'}

@app.get("/blog/{id}")
def blogs(id: int):
    return {'data': id}
