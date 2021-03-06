# Generated by Django 2.1.7 on 2019-06-02 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_classificacao_prefixo'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='bairro',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='cep',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='cidade',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='cpf',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='endereco',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='estado',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='nascimento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='observacoes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='sexo',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
