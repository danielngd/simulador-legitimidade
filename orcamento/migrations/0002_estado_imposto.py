# Generated by Django 3.2.7 on 2021-09-04 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orcamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('sigla', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Imposto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('valor', models.FloatField()),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orcamento.estado')),
            ],
        ),
    ]
