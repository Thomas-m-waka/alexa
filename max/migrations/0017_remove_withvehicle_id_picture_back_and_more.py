# Generated by Django 4.2.2 on 2023-07-07 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('max', '0016_alter_withoutvehicle_id_picture_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='withvehicle',
            name='id_picture_back',
        ),
        migrations.RemoveField(
            model_name='withvehicle',
            name='id_picture_front',
        ),
    ]
