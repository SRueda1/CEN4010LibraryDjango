# Generated by Django 4.1.2 on 2022-10-16 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Book'),
        ),
    ]
