# Generated by Django 4.1.5 on 2023-01-28 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AndresMogollonApp', '0008_alter_educacion_experiencias_fin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educacion_experiencias',
            name='fin',
            field=models.IntegerField(blank=True, help_text=2023, max_length=2023, null=True),
        ),
    ]
