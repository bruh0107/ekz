# Generated by Django 4.2.17 on 2024-12-24 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ekz', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.FileField(blank=True, null=True, upload_to='product_photo/'),
        ),
    ]