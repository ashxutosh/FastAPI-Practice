from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Hello, World!"}

@app.get("/about")
def about():
    return {"messsage": "I'm Ashutosh Rout, the developer of this API."}