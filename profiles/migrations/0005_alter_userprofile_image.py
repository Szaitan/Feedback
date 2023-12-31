# Generated by Django 4.2.7 on 2023-11-17 12:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.FileField(upload_to='images', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'pdf'])]),
        ),
    ]
