# Generated by Django 4.1.5 on 2023-01-28 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AndresMogollonApp', '0002_educacion_experiencia'),
    ]

    operations = [
        migrations.DeleteModel(
            name='experiencia',
        ),
        migrations.AddField(
            model_name='educacion',
            name='calidad',
            field=models.CharField(choices=[('Educacion', 'Educacion'), ('Experiencia', 'Experiencia')], default='Educacion', max_length=11),
        ),
    ]
