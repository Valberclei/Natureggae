# Generated by Django 3.2.16 on 2022-12-29 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newusers', '0003_auto_20221226_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]