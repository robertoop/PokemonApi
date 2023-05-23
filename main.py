from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def index():
	return "Hola a todos, quieres saber de pokemon"

@app.get("/Pokemon/{num}")
def pokemon(num):
	return num

@app.get("/Conversor_CaF/{C}")
def conversorCaF(C):
	TF=C*(9/5) + 32
	return f"La temperatura es de {TF} grados Farenheit"
