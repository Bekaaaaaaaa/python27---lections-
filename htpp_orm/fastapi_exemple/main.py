from fastapi import FastAPI

app = FastAPI()


@app.get("/")

def hello():
    return {"message": "hello world"}

@app.post("/create")
def create():
    return {"massage": "created"}

@app.delete("/delete")
def delete():
    return {"massage": "create"}