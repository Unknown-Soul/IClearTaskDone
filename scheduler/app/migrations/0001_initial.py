# Generated by Django 3.2.8 on 2021-10-24 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('user_identification', models.CharField(editable=False, max_length=6, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='Email')),
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('dateOfBirth', models.DateField(verbose_name='Date Of Birth')),
                ('image', models.FileField(blank=True, default='NO_CONTRACT_UPLOADED', null=True, upload_to='images/')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IP',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('ip', models.CharField(max_length=100)),
                ('hour', models.CharField(max_length=2)),
                ('minute', models.CharField(max_length=2)),
                ('second', models.CharField(max_length=2)),
            ],
        ),
    ]
