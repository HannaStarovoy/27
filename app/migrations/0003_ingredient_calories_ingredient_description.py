# Generated by Django 5.0.2 on 2024-02-20 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='calories',
            field=models.FloatField(default=0, verbose_name='Калорийность'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='description',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
    ]
