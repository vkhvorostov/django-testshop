# Generated by Django 5.0.3 on 2024-04-02 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='imageUrl',
            field=models.ImageField(upload_to='shop_images/'),
        ),
    ]
