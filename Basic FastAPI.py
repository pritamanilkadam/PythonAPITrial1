from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "I have made changes to code"}


@app.get("/Message2")
def read_root():
    return {"message": "This is new message 2."}