from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{"Data":"Test"}

@app.get("/about")
def about():
    return{"Data":"About"}

#Utilzando un slash
#Ejemplo: 127.0.0.1:8000/invertir/123456789
@app.get("/invertir/{cadena}")
def invertir(cadena: str):
    cadena_invertida = cadena[::-1]
    return{"Cadena":cadena, "Cadena Invertida": cadena_invertida}

#Utilizando un signo de interrogación
#Ejemplo: 127.0.0.1:8000/invertir1?cadena=123456789
@app.get("/invertir1")
def invertir1(cadena: str):
    cadena_invertida = cadena[::-1]
    return{"Cadena":cadena, "Cadena Invertida": cadena_invertida}
