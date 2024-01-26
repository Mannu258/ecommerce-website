# Generated by Django 5.0.1 on 2024-01-26 17:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('messege', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('category', models.CharField(default='', max_length=50)),
                ('subcategory', models.CharField(default='', max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=300)),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(blank=True, max_length=60, null=True)),
                ('name', models.CharField(max_length=30, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('number', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('number', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('address1', models.CharField(max_length=500)),
                ('address2', models.CharField(default='', max_length=500)),
                ('country', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=60)),
                ('zip', models.IntegerField()),
                ('payment', models.CharField(max_length=30)),
                ('user', models.ForeignKey(default='root', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
    ]
