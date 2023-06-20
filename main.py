from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{"Data":"Test"}

@app.get("/about")
def about():
    return{"Data":"About"}

#Utilzando un slash
@app.get("/invertir/{cadena}")
def invertir(cadena: str):
    cadena_invertida = cadena[::-1]
    return{"Cadena":cadena, "Cadena Invertida": cadena_invertida}

#Utilizando un signo de interrogación
@app.get("/invertir1")
def invertir1(cadena: str):
    cadena_invertida = cadena[::-1]
    return{"Cadena":cadena, "Cadena Invertida": cadena_invertida}
