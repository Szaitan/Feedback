# Generated by Django 4.2.7 on 2023-11-17 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_alter_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.FileField(upload_to='images'),
        ),
    ]