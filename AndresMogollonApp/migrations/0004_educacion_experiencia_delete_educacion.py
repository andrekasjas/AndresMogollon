# Generated by Django 4.1.5 on 2023-01-28 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AndresMogollonApp', '0003_delete_experiencia_educacion_calidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='educacion_experiencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Educacion', 'Educacion'), ('Experiencia', 'Experiencia')], max_length=11)),
                ('nombre', models.CharField(help_text='Nombre de la educacion ó experiencia', max_length=250)),
                ('institucion', models.CharField(help_text='Institucion que otorga la educacion ó experiencia', max_length=250)),
                ('descripcion', models.CharField(help_text='Descripcion de la educacion ó experiencia', max_length=250)),
                ('inicio', models.DateField(help_text='Fecha de inicio de la educacion ó experiencia')),
                ('fin', models.DateField(help_text='Fecha de finalizacion de la educacion ó experiencia')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'educacion ó experiencia',
                'verbose_name_plural': 'educaciones ó experiencias',
            },
        ),
        migrations.DeleteModel(
            name='educacion',
        ),
    ]
