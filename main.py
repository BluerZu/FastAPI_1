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

@app.get("/factorial/{numero}")
def factorial(numero: int):
    if numero < 0:
        return {"Número": numero, "Factorial": "No tiene"}
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return {"Número": numero, "Factorial": resultado}

@app.get("/suma/{a}/{b}")
def suma(a: int, b: int):
    resultado = a + b
    return {"Suma": resultado}

@app.get("/par-impar/{numero}")
def par_impar(numero: int):
    if numero % 2 == 0:
        resultado = "par"
    else:
        resultado = "impar"
    return {"Número": numero, "Resultado": resultado}