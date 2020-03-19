# Generated by Django 2.2.3 on 2020-03-19 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatshare', '0012_address_flat_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='flat',
        ),
        migrations.RemoveField(
            model_name='flat_images',
            name='iamge_flat',
        ),
        migrations.RemoveField(
            model_name='profile_addflat',
            name='user',
        ),
        migrations.DeleteModel(
            name='User_findFlat',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Flat',
        ),
        migrations.DeleteModel(
            name='Flat_images',
        ),
        migrations.DeleteModel(
            name='Profile_addFlat',
        ),
        migrations.DeleteModel(
            name='User_addFlat',
        ),
    ]
