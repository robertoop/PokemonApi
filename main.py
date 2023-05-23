from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def index():
	return "Hola a todos, quieres saber de pokemon"

@app.get("/Pokemon/{num}")
def pokemon(num):
	pokemons={
	"1":"Bulbasaur",
	"2":"Ivysaur",
	"3": "Venasaur",
	"4": "Charmander"
		
	}
	return pokemons{num}

@app.get("/Conversor_CaF/{C}")
def conversorCaF(C):
	try:
		C=float(C)
		TF=C*(9/5) + 32
		return f"La temperatura es de {TF} grados Farenheit"
	except:
		return "Entrada invalida"
