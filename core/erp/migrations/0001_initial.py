# Generated by Django 4.0.5 on 2022-07-09 13:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('dni', models.CharField(max_length=10, unique=True, verbose_name='Dni')),
                ('date_joined', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de registro')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('age', models.PositiveIntegerField(default=0, verbose_name='Edad')),
                ('salary', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Salario')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar/%Y/%m/%d', verbose_name='Imagen')),
                ('cvitae', models.FileField(blank=True, null=True, upload_to='cvitae/%Y/%m/%d', verbose_name='Curriculum')),
                ('categ', models.ManyToManyField(to='erp.category')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.type')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'empleado',
                'ordering': ['id'],
            },
        ),
    ]