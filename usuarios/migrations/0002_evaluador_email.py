# Generated by Django 2.2.1 on 2019-05-28 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluador',
            name='email',
            field=models.EmailField(default='malo', max_length=200),
            preserve_default=False,
        ),
    ]
