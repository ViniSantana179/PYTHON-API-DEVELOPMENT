from fastapi import FastAPI
from fastapi.params import Body


app = FastAPI()

@app.get("/get_user")
def get_user():
    return {"message": "welcome to my API"}

@app.get("/get_posts")
def get_posts():
    # Simulating fetching posts from a database
    return [
        {"id": 1, "title": "Post 1", "content": "This is post 1"},
        {"id": 2, "title": "Post 2", "content": "This is post 2"},
        {"id": 3, "title": "Post 3", "content": "This is post 3"},
    ]

@app.post("/create_post")
def create_post(post: dict = Body(...)):
    # Simulating creating a new post in a database
    return {"message": "Post created successfully", "post": post}