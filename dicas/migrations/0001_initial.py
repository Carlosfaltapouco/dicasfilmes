# Generated by Django 4.0.1 on 2022-02-16 23:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_da_dica', models.CharField(max_length=200)),
                ('categoria', models.CharField(max_length=200)),
                ('onde', models.CharField(max_length=200)),
                ('comentario', models.TextField()),
                ('date_dica', models.DateTimeField(blank=b'I01\n', default=datetime.datetime.now)),
            ],
        ),
    ]