import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# modelo para los blogs
class post(models.Model):
    titulo = models.CharField(max_length=160, help_text='Titulo del post')
    contenido = models.CharField(max_length=250, help_text='Contenido del post')
    imagen = models.ImageField(upload_to = 'blog', null = True, blank = True, help_text='Imagen del post')
    link = models.URLField(max_length=200, null=True, blank=True, help_text='Link de una publicacion externa sobre el post')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
    
    def __str__(self):
        return self.titulo
    
class proyectos(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to = 'proyecto')
    git = models.URLField(max_length=230, null=True, blank=True)
    host = models.URLField(max_length=230, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
    
    def __str__(self):
        return self.nombre
      
class educacion_experiencias(models.Model):
    TIPO = (
        ("Educacion", "Educacion"),
        ("Experiencia", "Experiencia")
    )
    
    tipo = models.CharField(max_length=11, choices=TIPO)
    nombre = models.CharField(help_text='Nombre de la educacion ó experiencia', max_length=250)
    institucion = models.CharField(help_text='Institucion que otorga la educacion ó experiencia', max_length=250)
    descripcion = models.CharField(help_text='Descripcion de la educacion ó experiencia', max_length=250)
    inicio = models.IntegerField(help_text='Año de inicio de la educacion ó experiencia')
    fin = models.IntegerField(help_text='Año de finalizacion de la educacion ó experiencia', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'educacion ó experiencia'
        verbose_name_plural = 'educaciones ó experiencias'
    
    def __str__(self):
        return self.tipo + ' - ' + self.nombre
    
class foto(models.Model):
    TIPO = (
        ('Perfil', 'Perfil'),
        ('Portada', 'Portada')
    )
    imagen = models.ImageField(upload_to = 'foto')
    tipo = models.CharField(max_length=7, choices=TIPO, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'foto'
        verbose_name_plural = 'fotos'
    
    def __str__(self):
        return self.tipo
    
class documentos(models.Model):
    documento = models.FileField(upload_to = 'documento')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'documento'
        verbose_name_plural = 'documentos'
    
    def __str__(self):
        return 'Hoja de vida'