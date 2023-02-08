
from django.shortcuts import render, redirect
from AndresMogollonApp.forms import FormularioContacto
from AndresMogollonApp.models import *
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime
from django.contrib import messages

def home(request):       
    if(request.method == "POST"): #post de boton correo
        formulario = FormularioContacto(data = request.POST) # validar datos del formulario
        if (formulario.is_valid()): # si los datos son validos
            # obtener datos del formulario
            nombre = request.POST.get('nombre')
            correo = request.POST.get('correo')
            asunto = request.POST.get('asunto')
            contenido = request.POST.get('contenido')
            # ejecutar funcion de envio de correo
            email = EmailMessage(asunto, 
            'Hola soy {}, mi correo es {} me comunico para decirte que: \n\n{}'.format(nombre,correo,contenido), 
            '', [settings.EMAIL_HOST_USER], ['andresmogollob@gmail.com'])
            # redireccionar segun resultado
            try:
                email.send()
                return redirect('/?exito')
            except:
                return redirect('/?error')   
        else:
            messages.error(request,'Por favor revise los campos')  
    else:    
        formulario = FormularioContacto() #inicialziar el formulario
    posts = post.objects.all()
    birthDate =  datetime(2000, 11, 19) 
    today = datetime.today()
    age = today.year - birthDate.year - ((today.month, today.day) <
         (birthDate.month, birthDate.day))
    proyectoss = proyectos.objects.all()
    educaciones = educacion_experiencias.objects.filter(tipo = 'Educacion')
    experiencias = educacion_experiencias.objects.filter(tipo = 'Experiencia') 
    perfil = foto.objects.filter(tipo = 'Perfil').first()
    portada = foto.objects.filter(tipo = 'Portada').first()
    documento_url = documentos.objects.first()
    documento = documento_url.documento.url.replace('v1', 'fl_attachment')
    # https://res.cloudinary.com/dc1hb2uev/image/upload/fl_attachment/{}/personal/yo/CV_Andres_Mogollon.pdf
    # https://res.cloudinary.com/dc1hb2uev/image/upload/v1/AndresMogollon/documento/carta_saldo_a_grado_Qot4CRv_kmpezr
    return render(request, 'base.html', {'formulario':formulario, 
                                         'posts':posts, 
                                         'anio':age,
                                         'proyectos':proyectoss,
                                         'educaciones':educaciones,
                                         'experiencias':experiencias,
                                         'perfil':perfil,
                                         'portada':portada,
                                         'documento':documento}) 

# Create your views here.





# vista para manejar el error 404
def pag_404_not_found(request, exception):
    return render(request, 'Errores/404.html')
#vista para manejar el error 500
def pag_500_error_server(request):
    return render(request, 'Errores/500.html')