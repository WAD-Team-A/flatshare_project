# Generated by Django 2.2.3 on 2020-03-19 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flatshare', '0015_auto_20200319_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='User_addFlat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128, unique=True)),
                ('password_addFlat', models.CharField(max_length=128)),
                ('email_addflat', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_findFlat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128, unique=True)),
                ('password_findflat', models.CharField(max_length=128)),
                ('email_findflat', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile_addFlat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=128)),
                ('LastName', models.CharField(max_length=128)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('phone_no', models.IntegerField(default=888, unique=True)),
                ('age', models.IntegerField(default=18)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flatshare.User_addFlat')),
            ],
        ),
        migrations.CreateModel(
            name='Flat_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='flat_images')),
                ('iamge_flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flatshare.Flat')),
            ],
        ),
        migrations.AddField(
            model_name='flat',
            name='addflat_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flatshare.User_addFlat'),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=128)),
                ('house_no', models.CharField(max_length=50)),
                ('postCode', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=128)),
                ('flat', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flatshare.Flat')),
            ],
        ),
    ]