# Generated by Django 2.1.5 on 2019-05-20 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rubrica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True)),
                ('durationMin', models.IntegerField(default=0)),
                ('durationMax', models.IntegerField()),
            ],
        ),
    ]