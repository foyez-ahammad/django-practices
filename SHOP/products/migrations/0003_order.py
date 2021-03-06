# Generated by Django 4.0.5 on 2022-07-01 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_offer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=200)),
                ('product_name', models.CharField(max_length=2000)),
                ('product_items', models.CharField(max_length=10)),
                ('details', models.TextField()),
            ],
        ),
    ]
