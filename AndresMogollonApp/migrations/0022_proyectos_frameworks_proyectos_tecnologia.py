# Generated by Django 4.1.5 on 2023-02-05 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AndresMogollonApp', '0021_alter_foto_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyectos',
            name='frameworks',
            field=models.CharField(default='sin', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proyectos',
            name='tecnologia',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
