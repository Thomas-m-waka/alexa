# Generated by Django 4.1.5 on 2023-07-11 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('max', '0027_rename_id_picture_front2_withvehicle_vehice_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='withvehicle',
            old_name='vehice_photo',
            new_name='id_picture_front2',
        ),
    ]
