# Generated by Django 3.2.13 on 2022-11-23 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='product',
            name='thumbnails',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]