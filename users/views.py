from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from .forms import UserRegisterForm,UsuarioEditForm



# Create your views here.
def login_request(request):
     msg_login = ""
     if request.method == "POST":
          form = AuthenticationForm(request, data = request.POST)
          #print(form)
          if form.is_valid():
               usuario = form.cleaned_data.get("username")
               contraseña = form.cleaned_data.get("password")

               user = authenticate(username=usuario , password=contraseña)
               
               if user is not None:
                    login (request , user)
                    return render (request, "AppSanta/index.html" , {"mensaje":f"Has iniciado sesión. Bienvenido {usuario}"})
               #else:
                    #form = AuthenticationForm()
                    #return render (request, "user/login.html" , {"mensaje": f"Error, datos incorrectos", "form": form})
               
          msg_login = "Usuario o contraseña incorrectos"
          #else: 
               #return render(request, "AppSanta/index.html", {"mensaje": "Error, formulario inválido"})
     
     form = AuthenticationForm()                                                               
     return render(request, "user/login.html", {"form": form, "msg_login": msg_login})

def register(request):
     msg_register = ""
     if request.method == "POST":

          form = UserRegisterForm(request.POST)
          if form.is_valid():
               form.save()
               return render(request,"AppSanta/index.html")
          msg_register = "Error en los datos ingresados"
     
     form = UserRegisterForm()
     return render(request,"user/registro.html" , {"form": form, "msg_register": msg_register})

#@login_required
def editar_usuario(request):
     usuario = request.user
     if request.method == "POST":
          miFormulario = UsuarioEditForm(request.POST, request.FILES, instance=usuario)
          if miFormulario.is_valid():
               if miFormulario.cleaned_data.get('imagen'):
                    if Imagen.objectsfilter(user=usuario).exists():
                         usuario.imagen.imagen =miFormulario.cleaned_data.get('imagen')
                         usuario.imagen.save()

                    else:
                         avatar =Imagen(user=usuario, imagen=miFormulario.cleaned_data.get('imagen'))
                         avatar.save()
               miFormulario.save()

               return render(request, "AppSanta/index.html")

     else:
          miFormulario = UsuarioEditForm(instance=usuario)
     return render(request, "users/editar_usuario.html", {"mi_form": miFormulario, "usuario": usuario})                        









