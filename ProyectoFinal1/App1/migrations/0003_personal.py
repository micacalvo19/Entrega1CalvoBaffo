# Generated by Django 4.0.5 on 2022-07-13 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0002_rename_formulario_socio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=50)),
            ],
        ),
    ]
