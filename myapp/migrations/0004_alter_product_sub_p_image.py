# Generated by Django 4.2.1 on 2023-05-16 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_p_iamge_product_sub_p_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_sub',
            name='P_image',
            field=models.FileField(default='product', upload_to='product_photo'),
        ),
    ]
