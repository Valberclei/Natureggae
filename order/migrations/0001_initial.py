# Generated by Django 3.2.13 on 2022-12-03 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0004_rename_thumbnails_product_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('emails', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('zipcode', models.CharField(max_length=255)),
                ('place', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('paid', models.BooleanField(default=False)),
                ('paid_amount', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('ordered', 'ordered'), ('shipped', 'shipped')], default='ordered', max_length=20)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='product.product')),
            ],
        ),
    ]
