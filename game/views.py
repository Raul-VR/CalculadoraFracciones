from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt #extensar
#Esto sirve para convertir strings a jsons y jsons a strings
from json import loads, dumps

class Fraccion:
    def __init__(self, num, den):
        self.num = num
        self.den = den
    def toJSON(self):
        return dumps(self, default=lambda o:o.__dict__, sort_keys=False, indent=4)

# Create your views here.
def index(request):
    # return HttpResponse('<h1> Bienvenidos a la sesión del jueves </h1>')
    return render(request, 'index.html')

def proceso(request):
    nombre = request.POST['nombre']
    nombre = nombre.upper()
    # render construye un http response, mientras que con HttpResponse ya lo estamos haciendo directamente
    # return render(request, 'proceso.html',{'name':nombre})
    return HttpResponse('Hola ' +  nombre)

def bienvenida(request):
    letrero = "Bienvenida"
    return HttpResponse(letrero)

def multiplicacion(request):
    p = request.GET['p']
    q = request.GET['q']
    r = int(p)*int(q)
    return HttpResponse("La multiplicacion de " +p+ "x" +q+ "=" + str(r))

# Lo que hace esto es que la funcion inmediatamente posterior hace expempcion del token de seguridad
# csrf quiere hacer seguro que ya estas logeado, y con este exemptor lo que hacemos es que no lo tome en cuenta
@csrf_exempt #extensar
def suma(request):
    # el body va a venir en formato unicode, para que no haya errores de conversion con eñes
    body_unicode = request.body.decode('utf-8')
    # Aqui usamos el loads para convertir json a python
    # loads es un deserealización, porque para transportarse en la red se necesita de serealizacion a un diccionario en python
    body = loads(body_unicode)
    numerador1 = body['numerador1']
    denominador1 = body['denominador1']
    numerador2 = body['numerador2']
    denominador2 = body['denominador2']
    if (denominador1 == denominador2):
        resultado = Fraccion( (numerador1+numerador2) , denominador1 )
    else:
        resultado = Fraccion( (numerador1*denominador2)+(denominador1*numerador2) , denominador1*denominador2 )

    #El \ es para decir que la linea continua
    json_resultado = resultado.toJSON()
    return HttpResponse(json_resultado, \
        content_type = "text/json-comment-filtered")

@csrf_exempt #extensar
def resta(request):
    # el body va a venir en formato unicode, para que no haya errores de conversion con eñes
    body_unicode = request.body.decode('utf-8')
    # Aqui usamos el loads para convertir json a python
    # loads es un deserealización, porque para transportarse en la red se necesita de serealizacion a un diccionario en python
    body = loads(body_unicode)
    numerador1 = body['numerador1']
    denominador1 = body['denominador1']
    
    numerador2 = body['numerador2']
    denominador2 = body['denominador2']

    if (denominador1 == denominador2):
        resultado = Fraccion( (numerador1-numerador2) , denominador1 )
    else:
        resultado = Fraccion( (numerador1*denominador2)-(denominador1*numerador2) , denominador1*denominador2 )

    #El \ es para decir que la linea continua
    json_resultado = resultado.toJSON()
    return HttpResponse(json_resultado, \
        content_type = "text/json-comment-filtered")

@csrf_exempt #extensar
def multiplicacion(request):
    # el body va a venir en formato unicode, para que no haya errores de conversion con eñes
    body_unicode = request.body.decode('utf-8')
    # Aqui usamos el loads para convertir json a python
    # loads es un deserealización, porque para transportarse en la red se necesita de serealizacion a un diccionario en python
    body = loads(body_unicode)
    numerador1 = body['numerador1']
    denominador1 = body['denominador1']
    numerador2 = body['numerador2']
    denominador2 = body['denominador2']
    resultado = Fraccion(numerador1*numerador2,denominador1*denominador2)
    #El \ es para decir que la linea continua
    json_resultado = resultado.toJSON()
    return HttpResponse(json_resultado, \
        content_type = "text/json-comment-filtered")

@csrf_exempt #extensar
def division(request):
    # el body va a venir en formato unicode, para que no haya errores de conversion con eñes
    body_unicode = request.body.decode('utf-8')
    # Aqui usamos el loads para convertir json a python
    # loads es un deserealización, porque para transportarse en la red se necesita de serealizacion a un diccionario en python
    body = loads(body_unicode)
    numerador1 = body['numerador1']
    denominador1 = body['denominador1']
    numerador2 = body['numerador2']
    denominador2 = body['denominador2']
    resultado = Fraccion(numerador1*denominador2,denominador1*numerador2)
    #El \ es para decir que la linea continua
    json_resultado = resultado.toJSON()
    return HttpResponse(json_resultado, \
        content_type = "text/json-comment-filtered")