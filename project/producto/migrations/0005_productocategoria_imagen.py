# Generated by Django 5.0.4 on 2024-05-19 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0004_alter_producto_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='productocategoria',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagen_categoria'),
        ),
    ]