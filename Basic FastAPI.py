from fastapi import FastAPI

app = FastAPI()

@app.get("/Message1")
def read_root():
    return {"message": "I have made changes to code. My main branch has been updated. Something more"}


@app.get("/Message2")
def read_root():
    return {"message": "This is new message 2."}
