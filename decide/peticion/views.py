from django.shortcuts import render, redirect
from .forms import FormularioPeticion
from django.core.mail import EmailMessage

# Create your views here.
def contacto(request):
    formulario_Peticion = FormularioPeticion()

    if request.method == "POST":
        formulario_Peticion = FormularioPeticion(data=request.POST)
        if formulario_Peticion.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
            email2 = EmailMessage("Peticion de censo","El usuario con nombre {} y correo {} solicita:\n\n{}"
                                  .format(nombre, email, contenido),"",["nanomotors33@gmail.com"],reply_to=[email])
            try:
                email2.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")

    return render(request, "contacto/contacto.html", {"miFormulario":formulario_Peticion})

