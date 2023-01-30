from django.contrib import admin

from AndresMogollonApp.models import *

class educacion_experiencia_admin(admin.ModelAdmin):
    readonly_fields = ("created","updated")
class proyectos_admin(admin.ModelAdmin):
    readonly_fields = ("created","updated")
class post_admin(admin.ModelAdmin):
    readonly_fields = ("created","updated")
class fotos_admin(admin.ModelAdmin):
    readonly_fields = ("created","updated")
class documentos_admin(admin.ModelAdmin):
    readonly_fields = ("created","updated")
        
admin.site.register(educacion_experiencias, educacion_experiencia_admin)
admin.site.register(proyectos, proyectos_admin)
admin.site.register(post, post_admin)
admin.site.register(foto, fotos_admin)
admin.site.register(documentos, documentos_admin)