# Generated by Django 3.0 on 2019-12-14 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20191214_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='\\media\\default.jpg', upload_to='profile_pics'),
        ),
    ]
