from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
#def index(request):
#    respuesta = "Hola curso"
 #   return HttpResponse(respuesta)

# Create your views here.
def adios(request):
    respuesta = "Adios nos vemos pronto!!!"
    return HttpResponse(respuesta)

# Create your views here.
def saludar(request, name):
    respuesta = "Buenos dias "+ name  
    return HttpResponse(respuesta)

# Create your views here.
def edad(request, name, age):
    edadfict= str(age-5)
    respuesta = f"La edad de {name} es {edadfict} años."
    return HttpResponse(respuesta)


#/ - redirige a la ruta "/blogs" con el método llamado "root"
def root(request):
    return redirect("/blogs")


#/blogs - muestra el string "placeholder para luego mostrar una lista de todos los blogs"
# con un método llamado "index"
def index(request):
    respuesta = "placeholder para luego mostrar una lista de todos los blogs"
    return HttpResponse(respuesta)


#/blogs/new - muestra el string "placeholder para mostrar un nuevo formulario para crear un nuevo blog" 
# con un método llamado "new"
def new(request):
    respuesta = "placeholder para mostrar un nuevo formulario para crear un nuevo blog"
    return HttpResponse(respuesta)



#/blogs/create - redirige a la ruta "/" con un método llamado "create"
def create(request):
    return redirect("/")


#/blogs/< number > - muestra el string "placeholder para mostrar el blog numero: {number}" 
# con un método llamado "show" (ej. localhost:8000/blogs/15 debería mostrar el mensaje:
# 'placeholder para mostrar el blog numero 15')
def show(request, number):
    respuesta= f"placeholder para mostrar el blog numero: {number}"
    return HttpResponse(respuesta)


#/blogs/< number >/edit - muestra el string "placeholder para editar el blog {number}" 
# con un método llamado "edit"
def edit(request, number):
    respuesta = f"placeholder para editar el blog: {number}"
    return HttpResponse(respuesta)


#/blogs/< number >/delete - redirige a la ruta "/blogs" con el método llamado "destroy"
def destroy(request, number):
    return redirect("/blogs")


#(**Bonus**) /blogs/json - regresa una JsonResponse con un titulo y que contenga llaves.
def bonus(request):
    resp=({"nombre":"Italo",
            "apellido":"Alarcon",
            "email" :"italo@gmail.com",
            "direccion":"calle carrera s/n"})
    return JsonResponse(resp)