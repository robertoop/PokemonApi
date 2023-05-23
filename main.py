from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def index():
	return "Hola a todos, quieres saber de pokemon"

@app.get("/Pokemon")
def pokemon():
	return "Este es otro mensaje"
