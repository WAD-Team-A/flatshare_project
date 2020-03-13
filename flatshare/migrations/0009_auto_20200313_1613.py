# Generated by Django 2.2.3 on 2020-03-13 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flatshare', '0008_flat_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='address',
        ),
        migrations.AddField(
            model_name='flat',
            name='city',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flat',
            name='house_no',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flat',
            name='postCode',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flat',
            name='street',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]
