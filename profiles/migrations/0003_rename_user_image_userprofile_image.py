# Generated by Django 4.2.7 on 2023-11-17 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_userprofile_user_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_image',
            new_name='image',
        ),
    ]
