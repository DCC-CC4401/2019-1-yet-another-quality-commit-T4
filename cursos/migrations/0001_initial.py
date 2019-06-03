# Generated by Django 2.2 on 2019-06-03 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.BigIntegerField()),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('estudiantes', models.ManyToManyField(to='cursos.Estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('codigo', models.CharField(max_length=200)),
                ('sex_number', models.IntegerField()),
                ('anno', models.IntegerField()),
                ('semester', models.IntegerField(choices=[(1, 'Otoño'), (2, 'Primavera'), (3, 'Verano')], default='2')),
                ('equipos', models.ManyToManyField(to='cursos.Equipo')),
                ('evaluadores', models.ManyToManyField(to='usuarios.Evaluador')),
            ],
            options={
                'unique_together': {('codigo', 'sex_number', 'anno', 'semester')},
            },
        ),
    ]
