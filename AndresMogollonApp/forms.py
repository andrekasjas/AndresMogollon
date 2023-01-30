from django import forms
from captcha.fields import CaptchaField
# formulario de contacto
class FormularioContacto(forms.Form):
    nombre = forms.CharField(label=False, max_length=100,required=True, widget=forms.TextInput(attrs={'placeholder':'Tu nombre', 'class':'inputs'}))
    correo = forms.EmailField(label=False, required=True, widget=forms.EmailInput(attrs={'placeholder':'Tu correo', 'class':'inputs'}))
    asunto = forms.CharField(label=False, max_length=100,required=True, widget=forms.TextInput(attrs={'placeholder':'Asunto','class':'inputs'}))
    contenido = forms.CharField(label=False, required=True, widget=forms.Textarea(attrs={'placeholder':'Contenido','class':'inputs'}))
    captcha = CaptchaField()