# Generated by Django 2.2.4 on 2022-12-26 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newusers', '0002_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
