# Generated by Django 3.2.16 on 2023-01-05 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20221229_1210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='emails',
            new_name='email',
        ),
    ]